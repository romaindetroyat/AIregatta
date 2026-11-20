# Exemples de code

> Du code court, commenté et prêt à lancer, pour se brancher sur le flux équipes d’AI Regatta. Il illustre le [contrat d’interface](../contrat-interface.md) ; ce n’est pas un logiciel tactique (P12).

| Fichier | Langage | Ce qu’il montre |
|---|---|---|
| [python/abonnement.py](python/abonnement.py) | Python 3.10+, paho-mqtt 2.x | Connexion TLS avec le compte de l’équipe, suivi de `race/current`, état de la flotte avec dédoublonnage par `seq`, **compte à rebours calculé localement**, distance de l’étrave à la prochaine bouée, mesure de l’écart d’horloge avec `sys/time` |
| [python/envoyer_au_comite.py](python/envoyer_au_comite.py) | Python 3.10+, paho-mqtt 2.x | Envoi d’un accusé de réception (`ack`) et d’une réclamation (`protest`) dans `outbox`, attente du `receipt` dans `inbox` |
| [javascript/navigateur.html](javascript/navigateur.html) | Navigateur, mqtt.js 5.10.1 | Connexion par WebSocket, liste des bateaux en direct, compte à rebours |
| [javascript/node-abonnement.mjs](javascript/node-abonnement.mjs) | Node.js 18+, mqtt.js 5.10.1 | Même chose qu’`abonnement.py`, en plus court |
| [nmea/lire-nmea.py](nmea/lire-nmea.py) | Python 3.10+, sans dépendance | Lecture du flux NMEA 0183 sur TCP, décodage des positions AIS (types 18, 21, 24) et du vent |

## Où se brancher

| Cible | MQTT (TLS) | WebSocket | NMEA | Mot de passe |
|---|---|---|---|---|
| **Bac à sable cloud** (dès janvier 2027) | `bac-a-sable.[domaine à définir]:8883` | `wss://bac-a-sable.[domaine à définir]:8884/mqtt` | `bac-a-sable.[domaine à définir]:10110` | Celui du bac à sable |
| **Site, le jour J** | `10.20.0.10:8883` | `wss://10.20.0.10:8884/mqtt` | `10.20.0.10:10110` | Celui du site |
| Simulateur local (si l’organisation le distribue, à confirmer) | `127.0.0.1:1883`, sans TLS (`AIR_TLS=0`) | selon sa configuration | `127.0.0.1:10110` | Selon sa configuration |

Le code est **le même** pour toutes les cibles : seules l’adresse et le mot de passe changent. Ne mettez jamais un mot de passe dans le code ni dans un dépôt Git : les exemples les lisent dans des variables d’environnement.

## Préparer l’environnement

```
# Python
python3 -m venv .venv && . .venv/bin/activate
pip install "paho-mqtt>=2,<3" jsonschema     # jsonschema est facultatif

# Node.js
npm install mqtt@5.10.1
```

Variables communes aux exemples Python et Node.js :

| Variable | Exemple | Rôle |
|---|---|---|
| `AIR_HOST`, `AIR_PORT` | `10.20.0.10`, `8883` | Adresse du broker (Python) |
| `AIR_URL` | `mqtts://10.20.0.10:8883` | Adresse du broker (Node.js) |
| `AIR_TLS` | `1` | `0` pour une connexion sans chiffrement (simulateur local) |
| `AIR_CA` | `./ca-ai-regatta.crt` | Certificat de l’organisation (site) ; vide pour le bac à sable (à confirmer) |
| `AIR_USER` | `equipe-fra07` | Compte de l’équipe |
| `AIR_PASSWORD` | — | Mot de passe, à saisir dans votre terminal, jamais dans un fichier versionné |
| `AIR_BOAT` | `FRA-07` | Votre bateau |
| `AIR_RACE` | `SIM-2027-01-20-M4` | Facultatif : forcer une manche au lieu de suivre `race/current` |

## Lancer chaque exemple

**Abonnement (Python)** — sur le bac à sable :

```
export AIR_HOST=bac-a-sable.[domaine à définir] AIR_PORT=8883
export AIR_USER=equipe-fra07 AIR_BOAT=FRA-07
read -rs AIR_PASSWORD && export AIR_PASSWORD      # saisie masquée
python3 python/abonnement.py
```

Sur le site, remplacez l’adresse par `10.20.0.10` et ajoutez `export AIR_CA=./ca-ai-regatta.crt`. Vous devez voir une ligne par seconde : manche, compte à rebours, vitesse et chemin de votre bateau, distance à la prochaine bouée, écart d’horloge. Si l’écart dépasse 5 ms, réglez chrony avant d’aller plus loin (contrat, §7).

**Envoyer au comité (Python)** — mêmes variables :

```
python3 python/envoyer_au_comite.py --dry-run ack --notice N-0014      # affiche le message sans l'envoyer
python3 python/envoyer_au_comite.py ack --notice N-0014 --race SIM-2027-01-20-M4
python3 python/envoyer_au_comite.py protest --race SIM-2027-01-20-M4 --against FRA-03 \
    --incident 2027-01-20T10:03:02.000Z --rule "[règle à préciser]" \
    --description "Test de réclamation sur le bac à sable"
```

Le script se termine avec le code 0 si le comité (ou le robot comité du bac à sable) a renvoyé un `receipt`, 1 sinon. Sur le bac à sable, n’envoyez des réclamations que sur des manches `SIM-…`.

**Navigateur** — ouvrez `javascript/navigateur.html` (un double-clic suffit), saisissez l’adresse WebSocket, le compte et le mot de passe, puis « Se connecter ». Sur le site, le certificat `ca-ai-regatta.crt` doit d’abord être installé dans le magasin de certificats du système ; sinon le navigateur refuse la connexion sans message clair.

**Node.js** :

```
export AIR_URL=mqtts://bac-a-sable.[domaine à définir]:8883 AIR_USER=equipe-fra07
read -rs AIR_PASSWORD && export AIR_PASSWORD
node javascript/node-abonnement.mjs
```

**NMEA** :

```
python3 nmea/lire-nmea.py bac-a-sable.[domaine à définir] 10110
python3 nmea/lire-nmea.py                      # sur le site : 10.20.0.10:10110
```

## Vérifier un message avec les schémas

Les schémas de [../schemas/](../schemas/) permettent de vérifier automatiquement un message, par exemple dans vos tests :

```python
import json, jsonschema
schema = json.load(open("schemas/position.schema.json", encoding="utf-8"))
jsonschema.validate(message, schema)   # lève une exception si le message n'est pas conforme
```

Les schémas refusent les champs inconnus ; en production, votre logiciel doit au contraire **ignorer** les champs qu’il ne connaît pas (contrat, §9).

## Ce que ces exemples ne font pas

Ils ne gèrent pas l’affichage cartographique, ne calculent aucune tactique et ne parlent pas à votre bateau : tout cela est votre travail. Ils montrent seulement les bonnes pratiques qui évitent les pièges du jour J : session persistante et réabonnement à chaque connexion, dédoublonnage par `seq`, compte à rebours local, horloge synchronisée, accusés de réception.
