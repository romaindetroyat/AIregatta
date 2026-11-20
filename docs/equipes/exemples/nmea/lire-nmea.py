#!/usr/bin/env python3
"""AI Regatta — lire le flux NMEA 0183 du PC course (TCP 10.20.0.10:10110).

Aucune dépendance : bibliothèque standard Python 3.9+ uniquement.

Le flux contient (voir connecteurs.md) :
  !AIVDM type 18   position de chaque bateau (comme un AIS de classe B)
  !AIVDM type 24   nom du bateau (son boat_id) associé à son MMSI
  !AIVDM type 21   position de chaque bouée (comme une aide à la navigation AIS)
  $WIMWD           vent moyen sur le parcours (direction vraie, vitesse)
  $PAIRW           vent mesuré à une bouée (phrase propre à AI Regatta, à confirmer)
  $PAIRS           heure du départ et étape de la procédure (phrase propre à AI Regatta, à confirmer)
  $GPZDA           heure UTC du serveur

Usage :
  python3 lire-nmea.py                     # 10.20.0.10:10110
  python3 lire-nmea.py 127.0.0.1 10110     # simulateur local ou bac à sable

Attention : l'AIS arrondit la position à environ 20 cm et la vitesse à 0,1 nœud.
Pour la tactique fine, préférez le flux MQTT (contrat-interface.md).
"""

import socket
import sys
import time
from functools import reduce

HOST = sys.argv[1] if len(sys.argv) > 1 else "10.20.0.10"
PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 10110


# --- Somme de contrôle NMEA ------------------------------------------------------


def checksum_ok(line: str) -> bool:
    """Vérifie le *hh final : OU exclusif de tous les caractères entre $ (ou !) et *."""
    if len(line) < 4 or line[0] not in "$!" or line[-3] != "*":
        return False
    body, expected = line[1:-3], line[-2:]
    return f"{reduce(lambda acc, c: acc ^ ord(c), body, 0):02X}" == expected.upper()


# --- Décodage AIS (champ « charge utile » des phrases !AIVDM) ----------------------


def payload_to_bits(payload: str, fill_bits: int) -> str:
    """Chaque caractère porte 6 bits (« armure » AIS)."""
    bits = []
    for ch in payload:
        v = ord(ch) - 48
        if v > 40:
            v -= 8
        bits.append(format(v, "06b"))
    joined = "".join(bits)
    return joined[: len(joined) - fill_bits] if fill_bits else joined


def u(bits: str, start: int, length: int) -> int:
    return int(bits[start:start + length], 2)


def s(bits: str, start: int, length: int) -> int:
    v = u(bits, start, length)
    return v - (1 << length) if v & (1 << (length - 1)) else v


def text(bits: str, start: int, nchars: int) -> str:
    out = []
    for k in range(nchars):
        v = u(bits, start + 6 * k, 6)
        out.append(chr(v + 64) if v < 32 else chr(v))
    return "".join(out).rstrip("@ ")


def decode_ais(bits: str) -> dict | None:
    msg_type, mmsi = u(bits, 0, 6), u(bits, 8, 30)
    if msg_type in (1, 2, 3):  # classe A (au cas où)
        return {"type": msg_type, "mmsi": mmsi, "sog_kn": u(bits, 50, 10) / 10,
                "lon": s(bits, 61, 28) / 600000, "lat": s(bits, 89, 27) / 600000,
                "cog": u(bits, 116, 12) / 10, "hdg": u(bits, 128, 9)}
    if msg_type == 18:  # classe B : c'est ce qu'envoie le PC course pour les bateaux
        hdg = u(bits, 124, 9)
        return {"type": 18, "mmsi": mmsi, "sog_kn": u(bits, 46, 10) / 10,
                "lon": s(bits, 57, 28) / 600000, "lat": s(bits, 85, 27) / 600000,
                "cog": u(bits, 112, 12) / 10, "hdg": None if hdg == 511 else hdg}
    if msg_type == 24 and u(bits, 38, 2) == 0:  # partie A : le nom
        return {"type": 24, "mmsi": mmsi, "name": text(bits, 40, 20)}
    if msg_type == 21:  # aide à la navigation : les bouées
        return {"type": 21, "mmsi": mmsi, "name": text(bits, 43, 20),
                "lon": s(bits, 164, 28) / 600000, "lat": s(bits, 192, 27) / 600000}
    return None


# --- Lecture du flux --------------------------------------------------------------


names: dict[int, str] = {}   # MMSI -> boat_id ou mark_id
fragments: dict[str, list[str]] = {}  # messages AIS en plusieurs phrases


def handle(line: str) -> None:
    if not checksum_ok(line):
        print(f"[ignorée] somme de contrôle fausse : {line}", file=sys.stderr)
        return
    fields = line[1:-3].split(",")
    tag = fields[0]

    if tag.endswith("VDM"):
        total, number, seq_id, payload, fill = int(fields[1]), int(fields[2]), fields[3], fields[5], int(fields[6])
        if total > 1:  # réassemblage des messages longs
            parts = fragments.setdefault(seq_id, [])
            parts.append(payload)
            if number < total:
                return
            payload = "".join(fragments.pop(seq_id))
        ais = decode_ais(payload_to_bits(payload, fill))
        if not ais:
            return
        if ais["type"] in (21, 24):
            names[ais["mmsi"]] = ais["name"]
        if "lat" in ais:
            who = names.get(ais["mmsi"], f"MMSI {ais['mmsi']}")
            extra = f" {ais['sog_kn']:.1f} nd, route {ais['cog']:.0f}°" if "sog_kn" in ais else ""
            print(f"{who:>8} : {ais['lat']:.6f} {ais['lon']:.6f}{extra}")
    elif tag == "WIMWD":
        print(f"vent moyen : du {fields[1]}° vrai, {fields[5]} nd")
    elif tag == "PAIRW":
        print(f"vent à {fields[1]} : du {fields[2]}°, {fields[3]} nd, rafale {fields[4]} nd")
    elif tag == "PAIRS":
        print(f"chrono {fields[1]} : étape {fields[2]}, départ à {fields[3]} UTC")
    elif tag.endswith("ZDA"):
        print(f"heure serveur : {fields[1]} UTC")


def main() -> None:
    while True:  # reconnexion automatique (bascule du serveur de secours en quelques secondes)
        try:
            with socket.create_connection((HOST, PORT), timeout=10) as sock:
                print(f"Connecté à {HOST}:{PORT}")
                buffer = b""
                while True:
                    chunk = sock.recv(4096)
                    if not chunk:
                        raise ConnectionError("fermé par le serveur")
                    buffer += chunk
                    *lines, buffer = buffer.split(b"\n")
                    for raw in lines:
                        line = raw.decode("ascii", errors="replace").strip()
                        if line:
                            handle(line)
        except (OSError, ConnectionError) as err:
            print(f"Connexion perdue ({err}), nouvelle tentative dans 2 s…", file=sys.stderr)
            time.sleep(2)
        except KeyboardInterrupt:
            return


if __name__ == "__main__":
    main()
