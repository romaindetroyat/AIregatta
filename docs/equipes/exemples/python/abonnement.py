#!/usr/bin/env python3
"""AI Regatta — exemple d'abonnement au flux équipes (MQTT).

Ce que fait ce script :
  1. se connecte au broker du PC course (ou au bac à sable) en TLS, avec le compte de l'équipe ;
  2. suit la course indiquée par `race/current` et s'abonne à tous ses sujets ;
  3. tient à jour l'état de la flotte (une entrée par bateau), en écartant doublons et messages en retard (`seq`) ;
  4. calcule le compte à rebours LOCALEMENT, à partir de l'heure GPS du départ (message `clock`) ;
  5. affiche chaque seconde la distance de l'étrave de votre bateau à sa prochaine bouée ;
  6. mesure l'écart de votre horloge avec la balise de temps `sys/time`.

Dépendance : paho-mqtt 2.x  (pip install "paho-mqtt>=2,<3")

Configuration par variables d'environnement (aucun secret dans le code) :
  AIR_HOST       adresse du broker            (défaut 10.20.0.10)
  AIR_PORT       port                         (défaut 8883, TLS)
  AIR_TLS        1 = TLS, 0 = sans chiffrement (défaut 1)
  AIR_CA         chemin du certificat de l'autorité de l'organisation (ca-ai-regatta.crt) ;
                 vide = magasin de certificats du système (cas du bac à sable)
  AIR_USER       compte, ex. equipe-fra07     (obligatoire)
  AIR_PASSWORD   mot de passe                 (obligatoire)
  AIR_BOAT       votre bateau, ex. FRA-07     (défaut FRA-07)
  AIR_RACE       forcer une course, ex. 2027-05-15-C3 (facultatif ; sinon race/current)
  AIR_CLIENT_ID  identifiant client MQTT stable (défaut <AIR_USER>-abonnement)

Exemple :
  export AIR_USER=equipe-fra07 AIR_PASSWORD='...' AIR_CA=./ca-ai-regatta.crt
  python3 abonnement.py
"""

import json
import math
import os
import sys
import threading
import time
from collections import deque

import paho.mqtt.client as mqtt

# --- Configuration -----------------------------------------------------------

HOST = os.environ.get("AIR_HOST", "10.20.0.10")
PORT = int(os.environ.get("AIR_PORT", "8883"))
USE_TLS = os.environ.get("AIR_TLS", "1") != "0"
CA_FILE = os.environ.get("AIR_CA") or None
try:
    USER = os.environ["AIR_USER"]
    PASSWORD = os.environ["AIR_PASSWORD"]
except KeyError as missing:
    sys.exit(f"Variable d'environnement manquante : {missing}")
MY_BOAT = os.environ.get("AIR_BOAT", "FRA-07")
FORCED_RACE = os.environ.get("AIR_RACE") or None
CLIENT_ID = os.environ.get("AIR_CLIENT_ID", f"{USER}-abonnement")
TEAM_ID = USER.removeprefix("equipe-")  # equipe-fra07 -> fra07

# --- Temps -------------------------------------------------------------------

GPS_EPOCH_UNIX_MS = 315_964_800_000  # 1980-01-06T00:00:00Z en ms Unix
DEFAULT_GPS_UTC_OFFSET_S = 18        # remplacé par la valeur publiée dans sys/time et clock


def now_gps_ms(gps_utc_offset_s: int) -> int:
    """Heure GPS actuelle selon l'horloge LOCALE (qui doit être synchronisée par chrony)."""
    return time.time_ns() // 1_000_000 - GPS_EPOCH_UNIX_MS + 1000 * gps_utc_offset_s


def fmt_duration(ms: int) -> str:
    sign = "-" if ms < 0 else ""
    ms = abs(ms)
    return f"{sign}{ms // 60000:02d}:{(ms // 1000) % 60:02d}.{(ms // 100) % 10}"


# --- Géométrie ---------------------------------------------------------------

EARTH_RADIUS_M = 6_371_000.0


def distance_m(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Distance en mètres (approximation plane, largement suffisante sur 500 m)."""
    mean_lat = math.radians((lat1 + lat2) / 2)
    dx = math.radians(lon2 - lon1) * math.cos(mean_lat) * EARTH_RADIUS_M
    dy = math.radians(lat2 - lat1) * EARTH_RADIUS_M
    return math.hypot(dx, dy)


# --- État de la course, partagé entre le fil réseau et le fil d'affichage ----


class RaceState:
    def __init__(self) -> None:
        self.lock = threading.Lock()
        self.reset(None)
        self.gps_utc_offset_s = DEFAULT_GPS_UTC_OFFSET_S
        self.clock_samples: deque[int] = deque(maxlen=60)  # écarts mesurés avec sys/time (ms)
        self.contract_version = None

    def reset(self, race_id) -> None:
        self.race_id = race_id
        self.boats: dict[str, dict] = {}     # boat_id -> dernier message de position
        self.last_seq: dict[str, int] = {}   # clé de dédoublonnage -> dernier seq accepté
        self.marks: dict[str, dict] = {}     # mark_id -> dernière mesure
        self.course = None
        self.clock = None
        self.leaderboard = None
        self.seen_notices: set[str] = set()
        self.seen_events: set[str] = set()

    def accept(self, key: str, msg: dict) -> bool:
        """Écarte les doublons et les messages plus anciens que le dernier reçu (règle du §8.3)."""
        seq = msg.get("seq")
        if seq is None:
            return True
        last = self.last_seq.get(key)
        # Un recul important de seq signale une bascule de serveur : on repart de la nouvelle valeur.
        if last is not None and last - 1000 < seq <= last:
            return False
        self.last_seq[key] = seq
        return True


state = RaceState()


def race_topics(race_id: str) -> list[tuple[str, int]]:
    return [(f"race/{race_id}/#", 1)]


# --- Callbacks MQTT (API de rappel version 2 de paho-mqtt 2.x) ----------------


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code.is_failure:
        print(f"[connexion] refusée : {reason_code}", file=sys.stderr)
        return
    print(f"[connexion] établie avec {HOST}:{PORT} (session reprise : {flags.session_present})")
    # Règle du §8.4 : on se réabonne à TOUT à chaque connexion, même si la session est reprise.
    subs = [("race/current", 1), ("sys/time", 0), ("meta/schema", 1), (f"teams/{TEAM_ID}/inbox", 1)]
    with state.lock:
        race_id = FORCED_RACE or state.race_id
    if race_id:
        subs += race_topics(race_id)
    client.subscribe(subs)


def on_disconnect(client, userdata, disconnect_flags, reason_code, properties):
    # paho se reconnecte tout seul (loop_start + reconnect_delay_set) ; le chrono continue localement.
    print(f"[connexion] perdue ({reason_code}), reconnexion automatique…", file=sys.stderr)


def switch_race(client, new_race_id):
    with state.lock:
        old = state.race_id
        if new_race_id == old:
            return
        state.reset(new_race_id)
    if old:
        client.unsubscribe(f"race/{old}/#")
    if new_race_id:
        client.subscribe(race_topics(new_race_id))
    print(f"[course] suivi de {new_race_id}")


def on_message(client, userdata, message):
    try:
        msg = json.loads(message.payload)
    except (ValueError, UnicodeDecodeError):
        print(f"[erreur] message illisible sur {message.topic}", file=sys.stderr)
        return
    parts = message.topic.split("/")

    if message.topic == "race/current":
        if not FORCED_RACE:
            switch_race(client, msg.get("race_id"))
        return

    if message.topic == "sys/time":
        with state.lock:
            state.gps_utc_offset_s = msg["gps_utc_offset_s"]
            # écart = délai réseau + décalage de votre horloge ; on retiendra le minimum sur 60 s
            state.clock_samples.append(now_gps_ms(state.gps_utc_offset_s) - msg["t_gps_ms"])
        return

    if message.topic == "meta/schema":
        with state.lock:
            state.contract_version = msg.get("contract_version")
        print(f"[contrat] version {msg.get('contract_version')} servie par le broker")
        return

    if parts[0] == "teams" and parts[-1] == "inbox":
        print(f"[comité → nous] {msg['type']} : {msg['title']} — {msg['body']}")
        if msg.get("requires_ack"):
            print(f"    ⚠ accusé de réception attendu : envoyer_au_comite.py ack --inbox {msg['msg_id']}")
        return

    if parts[0] != "race" or len(parts) < 3:
        return
    with state.lock:
        if parts[1] != state.race_id:
            return  # message d'une autre course (changement de course en cours)
        kind = parts[2]
        if kind == "boats" and len(parts) == 5 and parts[4] == "pos":
            if state.accept("pos/" + parts[3], msg):
                state.boats[parts[3]] = msg
        elif kind == "marks" and len(parts) == 4:
            if state.accept("mark/" + parts[3], msg):
                state.marks[parts[3]] = msg
        elif kind == "clock":
            if state.accept("clock", msg):
                state.clock = msg
                state.gps_utc_offset_s = msg["gps_utc_offset_s"]
        elif kind == "course":
            if state.accept("course", msg):
                state.course = msg
                print(f"[parcours] version {msg['course_version']} : {msg['name']}")
        elif kind == "leaderboard":
            if state.accept("leaderboard", msg):
                state.leaderboard = msg
        elif kind == "events":
            if msg["event_id"] not in state.seen_events or msg["status"] == "cancelled":
                state.seen_events.add(msg["event_id"])
                print(f"[événement] {msg['type']} ({msg['status']}) : {msg['text_fr']}")
        elif kind == "notices":
            for notice in msg["notices"]:
                if notice["notice_id"] not in state.seen_notices:
                    state.seen_notices.add(notice["notice_id"])
                    ack = " — accusé de réception demandé" if notice["requires_ack"] else ""
                    print(f"[avis {notice['notice_id']}] {notice['title']}{ack}")


# --- Calculs d'affichage -----------------------------------------------------


def next_mark_ids() -> list[str]:
    """Prochaine(s) bouée(s) de notre bateau : d'après le classement, sinon le premier bord."""
    if state.leaderboard:
        for entry in state.leaderboard["entries"]:
            if entry["boat_id"] == MY_BOAT and entry["next_mark_ids"]:
                return entry["next_mark_ids"]
    if state.course and state.course["legs"]:
        return state.course["legs"][0]["mark_ids"]
    return []


def mark_position(mark_id: str):
    """Position mesurée si elle est fraîche, sinon position déclarée dans le parcours."""
    measured = state.marks.get(mark_id)
    if measured and measured["lat"] is not None and not measured["stale"]:
        return measured["lat"], measured["lon"]
    if state.course:
        for mark in state.course["marks"]:
            if mark["mark_id"] == mark_id:
                return mark["lat"], mark["lon"]
    return None


def status_line() -> str:
    with state.lock:
        offset = state.gps_utc_offset_s
        now = now_gps_ms(offset)
        out = [f"course {state.race_id or '—'}"]

        # Compte à rebours calculé localement (§7) : jamais à partir de l'arrivée des messages.
        clock = state.clock
        if clock and clock["start_t_gps_ms"] is not None and clock["step"] not in ("postponed", "general_recall", "abandoned"):
            remaining = clock["start_t_gps_ms"] - now
            out.append(f"départ dans {fmt_duration(remaining)}" if remaining > 0 else f"course +{fmt_duration(-remaining)}")
        elif clock:
            out.append(f"chrono : {clock['step']}")

        me = state.boats.get(MY_BOAT)
        if me and me["lat"] is not None:
            lat = me["bow_lat"] if me["bow_lat"] is not None else me["lat"]
            lon = me["bow_lon"] if me["bow_lon"] is not None else me["lon"]
            age = now - me["t_gps_ms"]
            flag = " PERDU" if me["stale"] else ""
            out.append(f"{MY_BOAT} {me['sog_kn'] or 0:.1f} nd via {me['path']}, âge {age} ms{flag}")
            dists = [(mid, distance_m(lat, lon, *pos)) for mid in next_mark_ids() if (pos := mark_position(mid))]
            if dists:
                mid, d = min(dists, key=lambda x: x[1])  # porte : la plus proche des deux bouées
                out.append(f"→ {mid} à {d:.0f} m")
        else:
            out.append(f"{MY_BOAT} : pas de position")

        out.append(f"flotte {len(state.boats)} bateaux")
        if len(state.clock_samples) >= 5:
            best = min(state.clock_samples)
            alert = "  ⚠ VÉRIFIER CHRONY" if abs(best) > 5 else ""
            out.append(f"écart horloge ≈ {best} ms{alert}")
    return " | ".join(out)


# --- Programme principal -----------------------------------------------------


def main() -> None:
    client = mqtt.Client(
        mqtt.CallbackAPIVersion.VERSION2,
        client_id=CLIENT_ID,
        clean_session=False,  # session persistante (§3.2)
        protocol=mqtt.MQTTv311,
    )
    client.username_pw_set(USER, PASSWORD)
    if USE_TLS:
        client.tls_set(ca_certs=CA_FILE)  # None = certificats du système
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message
    client.reconnect_delay_set(min_delay=1, max_delay=5)

    if FORCED_RACE:
        state.reset(FORCED_RACE)

    # connect_async + loop_start : la connexion (et les reconnexions) se font dans un fil réseau.
    client.connect_async(HOST, PORT, keepalive=10)
    client.loop_start()
    try:
        while True:
            time.sleep(1.0)
            print(status_line())
    except KeyboardInterrupt:
        pass
    finally:
        client.disconnect()
        client.loop_stop()


if __name__ == "__main__":
    main()
