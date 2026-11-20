#!/usr/bin/env python3
"""AI Regatta — envoyer un message au comité (sujet teams/<teamId>/outbox).

Deux exemples de messages :
  ack      accusé de réception d'un avis officiel ou d'un message de l'inbox
  protest  réclamation contre un ou plusieurs bateaux

Le script publie en QoS 1, puis attend dans teams/<teamId>/inbox l'accusé de réception
automatique du PC course (type « receipt » ou « error », avec in_reply_to = notre msg_id).
Tant que ce receipt n'est pas arrivé, considérez le message comme NON parvenu.

Dépendance : paho-mqtt 2.x. Facultatif : jsonschema, pour vérifier le message avant l'envoi.
Mêmes variables d'environnement que abonnement.py (AIR_HOST, AIR_PORT, AIR_TLS, AIR_CA,
AIR_USER, AIR_PASSWORD, AIR_BOAT).

Exemples :
  python3 envoyer_au_comite.py ack --notice N-0014 --race 2027-05-14-M3
  python3 envoyer_au_comite.py ack --inbox C-fra07-0032 --race 2027-05-14-M3
  python3 envoyer_au_comite.py protest --race 2027-05-14-M3 --against FRA-03 \\
      --incident "2027-05-14T13:03:02.000Z" --rule "[règle à préciser]" \\
      --description "Au croisement, FRA-03 bâbord amures n'a pas manœuvré pour éviter FRA-07."
  python3 envoyer_au_comite.py --dry-run ack --notice N-0014      # affiche sans envoyer
"""

import argparse
import datetime as dt
import json
import os
import pathlib
import sys
import threading

import paho.mqtt.client as mqtt

GPS_EPOCH_UNIX_MS = 315_964_800_000
GPS_UTC_OFFSET_S = 18  # valeur publiée dans sys/time ; à relire avant l'épreuve
SCHEMA = pathlib.Path(__file__).resolve().parents[2] / "schemas" / "outbox.schema.json"


def iso_and_gps(when: dt.datetime) -> tuple[str, int]:
    """Renvoie l'horodatage ISO 8601 UTC (ms) et son équivalent t_gps_ms."""
    when = when.astimezone(dt.timezone.utc)
    iso = when.strftime("%Y-%m-%dT%H:%M:%S.") + f"{when.microsecond // 1000:03d}Z"
    unix_ms = int(when.timestamp() * 1000)
    return iso, unix_ms - GPS_EPOCH_UNIX_MS + 1000 * GPS_UTC_OFFSET_S


def parse_iso(text: str) -> dt.datetime:
    return dt.datetime.fromisoformat(text.replace("Z", "+00:00"))


def build_message(args, team_id: str, boat_id: str) -> dict:
    now = dt.datetime.now(dt.timezone.utc)
    t, t_gps_ms = iso_and_gps(now)
    # msg_id unique et lisible : code équipe + date + heure à la milliseconde
    msg_id = f"{team_id}-{now:%Y%m%d}-{now:%H%M%S}{now.microsecond // 1000:03d}"

    if args.type == "ack":
        payload = {"ref_id": args.notice or args.inbox, "ref_kind": "notice" if args.notice else "inbox"}
    else:  # protest
        incident_iso, incident_gps = iso_and_gps(parse_iso(args.incident))
        location = {"lat": args.lat, "lon": args.lon} if args.lat is not None and args.lon is not None else None
        payload = {
            "against": args.against,
            "incident_time": incident_iso,
            "incident_t_gps_ms": incident_gps,
            "rule": args.rule,
            "location": location,
            "description": args.description,
            "witnesses": args.witness or [],
        }
    return {
        "t": t,
        "t_gps_ms": t_gps_ms,
        "msg_id": msg_id,
        "team_id": team_id,
        "boat_id": boat_id,
        "race_id": args.race,
        "type": args.type,
        "payload": payload,
    }


def validate(message: dict) -> None:
    """Vérifie le message avec le schéma JSON s'il est disponible (facultatif)."""
    try:
        import jsonschema
    except ImportError:
        return
    if SCHEMA.exists():
        jsonschema.validate(message, json.loads(SCHEMA.read_text(encoding="utf-8")))


def send(message: dict, team_id: str, timeout_s: float) -> bool:
    host = os.environ.get("AIR_HOST", "10.20.0.10")
    port = int(os.environ.get("AIR_PORT", "8883"))
    user, password = os.environ["AIR_USER"], os.environ["AIR_PASSWORD"]
    inbox, outbox = f"teams/{team_id}/inbox", f"teams/{team_id}/outbox"
    subscribed, receipt = threading.Event(), threading.Event()
    answer: dict = {}

    def on_connect(client, userdata, flags, reason_code, properties):
        if reason_code.is_failure:
            print(f"Connexion refusée : {reason_code}", file=sys.stderr)
            return
        client.subscribe(inbox, qos=1)  # on écoute AVANT de publier, pour ne pas rater le receipt

    def on_subscribe(client, userdata, mid, reason_codes, properties):
        subscribed.set()

    def on_message(client, userdata, msg):
        data = json.loads(msg.payload)
        if data.get("in_reply_to") == message["msg_id"]:
            answer.update(data)
            receipt.set()

    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=f"{user}-envoi", protocol=mqtt.MQTTv311)
    client.username_pw_set(user, password)
    if os.environ.get("AIR_TLS", "1") != "0":
        client.tls_set(ca_certs=os.environ.get("AIR_CA") or None)
    client.on_connect, client.on_subscribe, client.on_message = on_connect, on_subscribe, on_message
    client.connect(host, port, keepalive=10)
    client.loop_start()
    try:
        if not subscribed.wait(timeout_s):
            print("Pas d'abonnement à l'inbox : connexion impossible ?", file=sys.stderr)
            return False
        # QoS 1, jamais retained (interdit sur outbox). Renvoyer le même msg_id ne crée pas de doublon.
        info = client.publish(outbox, json.dumps(message, ensure_ascii=False), qos=1, retain=False)
        info.wait_for_publish(timeout_s)
        print(f"Publié sur {outbox} : {message['msg_id']} ({message['type']})")
        if receipt.wait(timeout_s):
            print(f"Réponse du comité : {answer['type']} — {answer['title']} — {answer['body']}")
            return answer["type"] == "receipt"
        print("Aucun accusé de réception reçu : renvoyez le même message (même msg_id) "
              "ou prévenez le comité.", file=sys.stderr)
        return False
    finally:
        client.disconnect()
        client.loop_stop()


def main() -> None:
    parser = argparse.ArgumentParser(description="Envoyer un message au comité AI Regatta")
    parser.add_argument("--dry-run", action="store_true", help="afficher le message sans l'envoyer")
    parser.add_argument("--timeout", type=float, default=10.0, help="attente maximale en secondes")
    sub = parser.add_subparsers(dest="type", required=True)

    ack = sub.add_parser("ack", help="accusé de réception")
    target = ack.add_mutually_exclusive_group(required=True)
    target.add_argument("--notice", help="notice_id de l'avis, ex. N-0014")
    target.add_argument("--inbox", help="msg_id du message reçu dans l'inbox")
    ack.add_argument("--race", default=None, help="race_id, ex. 2027-05-14-M3")

    protest = sub.add_parser("protest", help="réclamation")
    protest.add_argument("--race", required=True)
    protest.add_argument("--against", nargs="+", required=True, help="bateau(x) réclamé(s), ex. FRA-03")
    protest.add_argument("--incident", required=True, help="instant de l'incident, ISO 8601 UTC")
    protest.add_argument("--rule", required=True)
    protest.add_argument("--description", required=True)
    protest.add_argument("--witness", nargs="*", help="témoins, ex. ITA-05")
    protest.add_argument("--lat", type=float)
    protest.add_argument("--lon", type=float)

    args = parser.parse_args()
    user = os.environ.get("AIR_USER", "equipe-fra07")
    team_id = user.removeprefix("equipe-")
    boat_id = os.environ.get("AIR_BOAT", "FRA-07")

    message = build_message(args, team_id, boat_id)
    validate(message)
    if args.dry_run:
        print(json.dumps(message, ensure_ascii=False, indent=2))
        return
    sys.exit(0 if send(message, team_id, args.timeout) else 1)


if __name__ == "__main__":
    main()
