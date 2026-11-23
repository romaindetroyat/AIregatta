# AI Regatta — Contrat d’interface du flux équipes

> **Version 1.0-draft** (`1.0.0-draft`), 20 novembre 2026. Gel prévu le **15 mars 2027** (version `1.0.0`).
> Ce document décrit précisément ce que le PC course envoie aux équipes, et ce que les équipes peuvent lui envoyer.
> Il complète, sans les remplacer, le [§7 de l’architecture](../architecture-materiel-communications.md#7-formats-de-messages) et la [liaison 6](../liaisons-et-logiciel.md#6-redistribution-à-toutes-les-équipes-flux-essentiel).
> Tout ce qui est marqué **« à confirmer »** peut encore changer avant le gel.

## Sommaire

1. [Le vocabulaire en deux minutes](#1-le-vocabulaire-en-deux-minutes)
2. [Conventions communes](#2-conventions-communes)
3. [Se connecter](#3-se-connecter)
4. [Qualité de service et messages conservés](#4-qualité-de-service-et-messages-conservés)
5. [Arborescence des sujets](#5-arborescence-des-sujets)
6. [Les sujets un par un](#6-les-sujets-un-par-un)
7. [Horloge et compte à rebours](#7-horloge-et-compte-à-rebours)
8. [Cas particuliers et pannes](#8-cas-particuliers-et-pannes)
9. [Versions et politique de changement](#9-versions-et-politique-de-changement)
10. [Points à confirmer](#10-points-à-confirmer)

---

## 1. Le vocabulaire en deux minutes

- **MQTT** : un protocole très simple pour diffuser des messages. Un programme central, le **broker** (ici Mosquitto, au PC course), reçoit des messages et les redistribue à tous ceux qui se sont **abonnés**.
- **Sujet** (*topic* en anglais) : l’adresse d’un message, écrite comme un chemin, par exemple `race/2027-05-14-M3/boats/FRA-07/pos`. On s’abonne à un sujet précis, ou à une famille avec un joker : `+` remplace un niveau, `#` remplace tout ce qui suit (`race/2027-05-14-M3/#` = tout ce qui concerne la manche).
- **QoS** (*quality of service*) : le niveau de garantie de livraison. **QoS 0** : envoyé une fois, sans accusé de réception, perdu si le réseau hoquette (parfait pour une position qui sera remplacée 100 ms plus tard). **QoS 1** : le broker renvoie le message jusqu’à ce qu’il soit acquitté ; il peut arriver en double, jamais perdu tant que la session est conservée.
- **Message conservé** (*retained*) : le broker garde le dernier message d’un sujet et le donne immédiatement à tout nouvel abonné. C’est ce qui permet de connaître l’état de la course dès la connexion, sans attendre.
- **Session persistante** : le broker se souvient de vos abonnements et met de côté les messages QoS 1 pendant une courte déconnexion.
- **JSON** : le format texte des messages, lisible par tous les langages.
- **JSON Schema** : un fichier qui décrit la forme exacte d’un message JSON ; il sert à vérifier automatiquement un message. Les schémas sont dans [schemas/](schemas/).

## 2. Conventions communes

| Sujet | Règle |
|---|---|
| Encodage | JSON en UTF-8, un objet par message, sans saut de ligne imposé. |
| Noms des champs | Anglais, en `snake_case` (minuscules et tirets bas) : `boat_id`, `sog_kn`. Le suffixe indique l’unité quand elle n’est pas évidente. Cette règle remplace les noms des exemples du §7.3 de l’architecture (`boatId`, `hAcc_m` deviennent `boat_id`, `h_acc_m`). |
| Champs présents | **Tous les champs listés sont toujours présents.** Une valeur inconnue vaut `null`, jamais un champ absent. |
| Champs inconnus | Votre logiciel **doit ignorer** les champs qu’il ne connaît pas : de nouveaux champs facultatifs peuvent apparaître (voir §9). |
| Temps | Chaque message porte **deux** horodatages du même instant : `t`, texte ISO 8601 en UTC avec millisecondes (`2027-05-14T13:04:07.200Z`), et `t_gps_ms`, entier (voir ci-dessous). Les autres instants suivent la même règle : un champ texte et son jumeau `…_t_gps_ms`. |
| `t_gps_ms` | Millisecondes écoulées depuis l’époque GPS (6 janvier 1980, 00:00:00 UTC), **dans l’échelle de temps GPS**, qui ne connaît pas les secondes intercalaires. Avantage : c’est un entier qui ne fait que croître, idéal pour calculer des écarts. Conversion : `t_gps_ms = temps_unix_ms − 315 964 800 000 + 1 000 × gps_utc_offset_s`, avec `gps_utc_offset_s` = 18 s aujourd’hui (valeur publiée dans `sys/time` et `clock`, à confirmer pour mai 2027 selon les annonces de l’IERS). |
| Position | Latitude et longitude en degrés décimaux, système **WGS84** (celui du GPS), 7 décimales (≈ 1 cm). |
| Angles | Degrés **vrais** (par rapport au nord géographique, pas magnétique), de 0 (inclus) à 360 (exclu), sens des aiguilles d’une montre. Une direction de vent (`twd`) indique **d’où vient** le vent. |
| Vitesses | En **nœuds**, suffixe `_kn` (1 nœud = 1,852 km/h ≈ 0,514 m/s). Quelques champs de vent sont doublés en m/s, suffixe `_ms`. |
| Distances | En **mètres**, suffixe `_m`. |
| Durées | En millisecondes (`_ms`) ou secondes (`_s`), selon le suffixe. |
| Gîte et tangage | Degrés ; gîte positive = bateau penché sur tribord (à confirmer avec le firmware de la balise), tangage positif = étrave qui monte. |
| Identifiants | Manche `raceId` = date + numéro de manche : `2027-05-14-M3` (préfixe `SIM-` dans le bac à sable). Équipe `teamId` = code en minuscules : `fra07`. Bateau `boatId` = numéro de voile : `FRA-07`. Bouées du parcours n°3 : `B1` et `B2` (porte 1-2, qui sert au départ, au passage et à l’arrivée), `B3` (bouée au vent, à laisser à bâbord), `P1` et `P2` (tour de pénalité). |
| Compteur `seq` | Entier croissant **par sujet** (par bateau pour les positions), attribué par le PC course. Il sert à repérer les doublons et les messages arrivés dans le désordre. |

## 3. Se connecter

### 3.1 Sur le site

- Chaque équipe dispose d’une **prise Ethernet** dans la zone équipes. **Tous les câbles ont la même longueur**, et passent par le même commutateur : personne n’a quelques mètres d’avance.
- Ces prises sont sur un réseau isolé, le **VLAN « équipes »** (un VLAN est un réseau séparé qui partage les mêmes câbles et commutateurs). Il n’atteint que le broker et le serveur de temps, plus un accès Internet à débit garanti pour vos propres liaisons.
- L’adresse est attribuée automatiquement (DHCP) ; une adresse fixe par équipe est possible sur demande (à confirmer).
- **Secours** : une borne Wi-Fi couvre la zone équipes, sur le même VLAN. Elle sert si votre câble ou votre carte réseau lâche ; elle n’est pas plus rapide et n’est pas prévue pour un usage permanent.

| Service | Adresse | Remarque |
|---|---|---|
| MQTT (sans chiffrement) | `mqtt://10.20.0.10:1883` | Réseau local fermé ; identifiant et mot de passe obligatoires |
| MQTT chiffré (TLS) | `mqtts://10.20.0.10:8883` | Recommandé ; certificat signé par l’autorité de certification de l’organisation (fichier `ca-ai-regatta.crt` remis à l’inscription) |
| MQTT sur WebSocket chiffré | `wss://10.20.0.10:8884/mqtt` | Pour les applications dans un navigateur |
| NMEA 0183 sur TCP | `10.20.0.10:10110` | Voir [connecteurs.md](connecteurs.md) |
| Serveur de temps NTP | `10.20.0.1` | Obligatoire, voir §7 |

L’adresse `10.20.0.10` est une **adresse IP virtuelle** : elle est portée par le serveur principal et, s’il tombe, reprise en quelques secondes par le serveur de secours. Vous n’avez rien à reconfigurer ; votre client doit simplement savoir se reconnecter (voir §8.5).

### 3.2 Comptes et droits

Chaque équipe reçoit **un compte** : identifiant `equipe-<code>` (par exemple `equipe-fra07`) et mot de passe, remis à l’inscription. Le même compte sert dans le bac à sable (avec un mot de passe différent) et sur le site.

| Sujet | Droit de l’équipe `fra07` |
|---|---|
| `race/#` | Lecture seule |
| `sys/time`, `meta/schema` | Lecture seule |
| `teams/fra07/inbox` | Lecture seule (messages du comité à votre équipe) |
| `teams/fra07/outbox` | **Écriture seule** (vos messages au comité) |
| `teams/<autre équipe>/#` | Aucun accès |
| `sys/beacons/#` et tout le reste | Aucun accès (réservé à l’organisation) |

Règles de connexion :

- **Identifiant client MQTT** (*client id*) : `equipe-<code>-<suffixe libre>`, par exemple `equipe-fra07-tactique`. Il doit être **stable** d’une connexion à l’autre pour retrouver votre session persistante.
- **Session persistante** : connectez-vous avec `clean_session = false` (MQTT 3.1.1) ou `clean_start = false` et une durée de session d’au moins 300 s (MQTT 5).
- **Keepalive** : 10 s conseillé (le broker détecte ainsi une coupure en 15 s au plus).
- MQTT 3.1.1 et MQTT 5 sont tous deux acceptés. Les exemples utilisent 3.1.1, le plus répandu.

### 3.3 Limites (à confirmer)

| Limite | Valeur proposée | Si elle est dépassée |
|---|---|---|
| Connexions simultanées par compte | 3 | La connexion supplémentaire est refusée |
| Messages publiés sur `outbox` | 1 par seconde en moyenne, pointes de 5 | Messages en trop ignorés, message `error` dans votre `inbox` |
| Taille d’un message publié | 8 Kio | Message refusé |
| Publication sur un sujet non autorisé | — | Ignorée (MQTT 3.1.1) ou refusée avec le code 0x87 « non autorisé » (MQTT 5) |
| Drapeau *retained* sur vos publications | Interdit | Message refusé |

## 4. Qualité de service et messages conservés

Règle générale : **positions et vent en QoS 0** (le suivant arrive vite), **tout ce qui ne doit pas se perdre en QoS 1** (événements, avis, chrono, messages du comité). Les sujets qui décrivent un **état** sont **conservés** : à la connexion, vous recevez tout de suite le parcours, le chrono, l’état, le classement, les pavillons et les avis.

Les deux serveurs reçoivent les mêmes publications du moteur de course : les messages conservés existent aussi sur le serveur de secours (à vérifier lors des tests de bascule).

## 5. Arborescence des sujets

```
race/current                          # manche en cours (ajout au §7.3)
race/{raceId}/state                   # état de la manche
race/{raceId}/clock                   # heure GPS du départ, étape de la procédure
race/{raceId}/course                  # bouées, lignes, bords, limites
race/{raceId}/marks/{markId}          # position mesurée + vent si équipée
race/{raceId}/boats/{boatId}/pos      # position officielle, 10 Hz
race/{raceId}/wind/field              # carte de vent, grille de 20 m, 1 Hz
race/{raceId}/wind/trend              # tendance à 5–15 min
race/{raceId}/events                  # événements de course
race/{raceId}/flags                   # pavillons envoyés (ajout au §7.3)
race/{raceId}/leaderboard             # classement live
race/{raceId}/notices                 # avis officiels à toutes les équipes (ajout au §7.3)
teams/{teamId}/inbox                  # comité → une équipe (ajout au §7.3)
teams/{teamId}/outbox                 # une équipe → comité (ajout au §7.3)
sys/time                              # balise de temps 1 Hz (ajout au §7.3)
meta/schema                           # version du contrat (ajout au §7.3)
```

| Sujet | Sens | Cadence | QoS | Conservé | Schéma |
|---|---|---|---|---|---|
| `race/current` | PC course → équipes | À chaque changement | 1 | Oui | [current](schemas/current.schema.json) |
| `race/{raceId}/state` | PC course → équipes | À chaque changement | 1 | Oui | [state](schemas/state.schema.json) |
| `race/{raceId}/clock` | PC course → équipes | À chaque changement + rappel chaque seconde | 1 | Oui | [clock](schemas/clock.schema.json) |
| `race/{raceId}/course` | PC course → équipes | À chaque changement | 1 | Oui | [course](schemas/course.schema.json) |
| `race/{raceId}/marks/{markId}` | PC course → équipes | 1 Hz | 0 | Oui | [mark](schemas/mark.schema.json) |
| `race/{raceId}/boats/{boatId}/pos` | PC course → équipes | 10 Hz (4G), 2 Hz (radio), 1 Hz (perdu) | 0 | Non | [position](schemas/position.schema.json) |
| `race/{raceId}/wind/field` | PC course → équipes | 1 Hz | 0 | Non | [wind-field](schemas/wind-field.schema.json) |
| `race/{raceId}/wind/trend` | PC course → équipes | Toutes les 10 s (à confirmer) | 0 | Oui | [wind-trend](schemas/wind-trend.schema.json) |
| `race/{raceId}/events` | PC course → équipes | À la volée | 1 | Non | [event](schemas/event.schema.json) |
| `race/{raceId}/flags` | PC course → équipes | À chaque changement | 1 | Oui | [flags](schemas/flags.schema.json) |
| `race/{raceId}/leaderboard` | PC course → équipes | 1 Hz + à chaque changement | 1 | Oui | [leaderboard](schemas/leaderboard.schema.json) |
| `race/{raceId}/notices` | Comité → toutes les équipes | À chaque nouvel avis | 1 | Oui | [notice](schemas/notice.schema.json) |
| `teams/{teamId}/inbox` | Comité → une équipe | À la volée | 1 | Non | [inbox](schemas/inbox.schema.json) |
| `teams/{teamId}/outbox` | Une équipe → comité | À la volée, ≤ 1/s | 1 | Non (interdit) | [outbox](schemas/outbox.schema.json) |
| `sys/time` | PC course → équipes | 1 Hz | 0 | Non | [time](schemas/time.schema.json) |
| `meta/schema` | PC course → équipes | À chaque nouvelle version | 1 | Oui | [meta](schemas/meta.schema.json) |

Débit total reçu par une équipe abonnée à tout : de l’ordre de 6 à 20 ko/s pour 6 bateaux.

## 6. Les sujets un par un

### 6.1 `race/current` — la manche en cours

Indique quelle manche suivre : la manche en cours, ou la prochaine entre deux manches. Abonnez-vous à ce sujet d’abord, puis à `race/{raceId}/#` pour la manche indiquée.

| Champ | Type | Unité | Description |
|---|---|---|---|
| `t`, `t_gps_ms` | texte, entier | — | Instant de publication |
| `race_id` | texte ou null | — | Manche en cours ou prochaine ; `null` quand la journée est finie |
| `day` | texte | date | Jour de course, `AAAA-MM-JJ` |
| `races_today` | liste de textes | — | Manches prévues dans la journée |

```json
{
  "t": "2027-05-14T12:50:00.000Z",
  "t_gps_ms": 1494334218000,
  "race_id": "2027-05-14-M3",
  "day": "2027-05-14",
  "races_today": ["2027-05-14-M1", "2027-05-14-M2", "2027-05-14-M3", "2027-05-14-M4"]
}
```

### 6.2 `race/{raceId}/state` — l’état de la manche

| Champ | Type | Unité | Description |
|---|---|---|---|
| `t`, `t_gps_ms`, `seq` | | | Instant de publication, compteur |
| `race_id` | texte | — | Manche |
| `status` | texte | — | `scheduled` (prévue), `sequence` (procédure de départ en cours), `racing` (en course), `finished` (terminée), `postponed` (retardée), `abandoned` (annulée) |
| `race_number` | entier | — | Numéro de la manche dans la journée |
| `day` | texte | date | Jour de course |
| `entries` | liste de `boat_id` | — | Bateaux inscrits à la manche |
| `course_version` | entier | — | Version du parcours en vigueur ; elle change à chaque modification de `course` |
| `time_limit_s` | entier ou null | s | Temps limite de la manche, fixé par les instructions de course |
| `results_status` | texte | — | `none`, `provisional` (provisoire), `final` (définitif, après réclamations) |
| `message_fr` | texte ou null | — | Courte phrase lisible |

```json
{
  "t": "2027-05-14T12:57:00.010Z",
  "t_gps_ms": 1494334638010,
  "race_id": "2027-05-14-M3",
  "seq": 4,
  "status": "sequence",
  "race_number": 3,
  "day": "2027-05-14",
  "entries": ["FRA-03", "FRA-07", "FRA-12", "ITA-05", "MON-01", "ESP-21"],
  "course_version": 2,
  "time_limit_s": 900,
  "results_status": "none",
  "message_fr": "Procédure de départ lancée"
}
```

### 6.3 `race/{raceId}/clock` — le chrono officiel

Le chrono est piloté par le PC course (P17). La procédure prévue est celle du règlement de l’organisateur : **RCV 26, signaux à −5:00, −4:00, −1:00 et départ** ; par dérogation, **une minute : −1:00, −0:40, −0:20, départ** (l’exemple ci-dessous). **Les durées sont fixées par les instructions de course** et transmises dans le champ `procedure` : votre logiciel ne doit pas les coder en dur.

| Champ | Type | Unité | Description |
|---|---|---|---|
| `t`, `t_gps_ms`, `seq` | | | Instant de publication, compteur |
| `race_id` | texte | — | Manche |
| `step` | texte | — | Dernière étape franchie : `none` (procédure pas encore lancée), `warning` (avertissement), `preparatory` (préparatoire), `one_minute` (−1:00, procédure de 5 minutes), `last_step` (−0:20, procédure d’une minute), `start` (départ donné), `postponed` (retard), `general_recall` (rappel général : un nouveau départ sera publié), `abandoned` (annulation) |
| `start_time`, `start_t_gps_ms` | texte, entier, ou null | — | **Heure GPS exacte du départ.** `null` tant qu’elle n’est pas fixée |
| `procedure` | liste | — | Les étapes prévues : `step`, `offset_s` (décalage par rapport au départ, négatif), `time` et `t_gps_ms` (heure de l’étape), `sound` (`short`, `long`, `none`) |
| `next_signal` | objet ou null | — | Prochaine étape : `step`, `time`, `t_gps_ms` ; `null` après le départ |
| `individual_recall` | liste de `boat_id` | — | Bateaux rappelés individuellement (partis trop tôt), vide sinon |
| `gps_utc_offset_s` | entier | s | Écart GPS − UTC (18 s), pour vos conversions |

```json
{
  "t": "2027-05-14T12:59:30.000Z",
  "t_gps_ms": 1494334788000,
  "race_id": "2027-05-14-M3",
  "seq": 91,
  "step": "preparatory",
  "start_time": "2027-05-14T13:00:00.000Z",
  "start_t_gps_ms": 1494334818000,
  "procedure": [
    {
      "step": "warning",
      "offset_s": -60,
      "time": "2027-05-14T12:59:00.000Z",
      "t_gps_ms": 1494334758000,
      "sound": "short"
    },
    {
      "step": "preparatory",
      "offset_s": -40,
      "time": "2027-05-14T12:59:20.000Z",
      "t_gps_ms": 1494334778000,
      "sound": "short"
    },
    {
      "step": "last_step",
      "offset_s": -20,
      "time": "2027-05-14T12:59:40.000Z",
      "t_gps_ms": 1494334798000,
      "sound": "short"
    },
    {
      "step": "start",
      "offset_s": 0,
      "time": "2027-05-14T13:00:00.000Z",
      "t_gps_ms": 1494334818000,
      "sound": "short"
    }
  ],
  "next_signal": {
    "step": "last_step",
    "time": "2027-05-14T12:59:40.000Z",
    "t_gps_ms": 1494334798000
  },
  "individual_recall": [],
  "gps_utc_offset_s": 18
}
```

**Le compte à rebours se calcule chez vous**, à partir de `start_t_gps_ms` et de votre horloge synchronisée : jamais à partir de l’heure d’arrivée du message (voir §7). Après le départ, le temps de course écoulé se calcule de la même façon.

### 6.4 `race/{raceId}/course` — le parcours

| Champ | Type | Unité | Description |
|---|---|---|---|
| `t`, `t_gps_ms`, `seq` | | | Instant de publication, compteur |
| `race_id` | texte | — | Manche |
| `course_version` | entier | — | Version du parcours (augmente à chaque modification) |
| `name` | texte | — | Nom lisible du parcours |
| `axis_twd` | nombre | degrés vrais | Direction du vent retenue pour orienter le parcours |
| `length_m` | nombre | m | Distance entre la porte 1-2 et la bouée 3, au vent (≈ 200 m, à valider avec l’organisateur) |
| `marks` | liste | — | Bouées : `mark_id`, `role` (`gate` porte 1-2 de départ, de passage et d’arrivée, `windward` bouée au vent, `penalty` bouée du tour de pénalité ; d’autres parcours peuvent utiliser `leeward_gate`, `leeward`, `offset`, `start_committee`, `start_pin`, `finish`), `kind` (`instrumented` avec vent, `simple` position seule), `lat`, `lon` (position déclarée par le comité), `wind_equipped` |
| `start_line` | objet | — | `ends` : les deux extrémités de la ligne de départ (`B1`, `B2`) |
| `finish_line` | objet | — | `ends` : les deux extrémités de la ligne d’arrivée (`B1`, `B2` : sur le parcours n°3, la même porte) |
| `penalty_marks` | liste | — | Bouées du tour de pénalité, dans l’ordre : `P1` puis `P2` ; le tour se fait avant de franchir l’arrivée (règlement, § 7) |
| `legs` | liste | — | Ordre des bords : `leg` (numéro), `to_type` (`mark` bouée à contourner, `line` porte à franchir entre ses deux bouées, `gate` porte où l’on contourne l’une des deux bouées, `finish`), `mark_ids`, `rounding` (côté où laisser la bouée : `port` bâbord, `starboard` tribord ; `null` pour une porte, où l’on choisit l’une des deux bouées, et pour l’arrivée) |
| `boundary` | liste de `{lat, lon}` | degrés | Polygone des limites du parcours, sommets dans l’ordre, non refermé (le dernier sommet rejoint le premier) |
| `reference_point` | texte | — | Point du bateau qui sert à l’arbitrage : `bow` (étrave) |

Les positions de `marks` sont celles **déclarées** ; les positions **mesurées** en temps réel sont dans `marks/{markId}` (les bouées ancrées bougent un peu, et sont déplacées si le vent tourne, P19).

```json
{
  "t": "2027-05-14T12:40:00.000Z",
  "t_gps_ms": 1494333618000,
  "race_id": "2027-05-14-M3",
  "seq": 2,
  "course_version": 2,
  "name": "Parcours n°3 : porte 1-2, bouée 3 à bâbord, 2 tours",
  "axis_twd": 135.0,
  "length_m": 200,
  "marks": [
    {
      "mark_id": "B1",
      "role": "gate",
      "kind": "simple",
      "lat": 43.1077184,
      "lon": 5.9412093,
      "wind_equipped": false
    },
    {
      "mark_id": "B2",
      "role": "gate",
      "kind": "simple",
      "lat": 43.107439,
      "lon": 5.9408265,
      "wind_equipped": false
    },
    {
      "mark_id": "B3",
      "role": "windward",
      "kind": "instrumented",
      "lat": 43.1063083,
      "lon": 5.942758,
      "wind_equipped": true
    },
    {
      "mark_id": "P1",
      "role": "penalty",
      "kind": "simple",
      "lat": 43.10735,
      "lon": 5.9408091,
      "wind_equipped": false
    },
    {
      "mark_id": "P2",
      "role": "penalty",
      "kind": "simple",
      "lat": 43.1074263,
      "lon": 5.9407047,
      "wind_equipped": false
    }
  ],
  "start_line": {
    "ends": [
      "B1",
      "B2"
    ]
  },
  "finish_line": {
    "ends": [
      "B1",
      "B2"
    ]
  },
  "penalty_marks": [
    "P1",
    "P2"
  ],
  "legs": [
    {
      "leg": 1,
      "to_type": "mark",
      "mark_ids": [
        "B3"
      ],
      "rounding": "port"
    },
    {
      "leg": 2,
      "to_type": "line",
      "mark_ids": [
        "B1",
        "B2"
      ],
      "rounding": null
    },
    {
      "leg": 3,
      "to_type": "mark",
      "mark_ids": [
        "B3"
      ],
      "rounding": "port"
    },
    {
      "leg": 4,
      "to_type": "finish",
      "mark_ids": [
        "B1",
        "B2"
      ],
      "rounding": null
    }
  ],
  "boundary": [
    {
      "lat": 43.1083409,
      "lon": 5.9413659
    },
    {
      "lat": 43.1073246,
      "lon": 5.9399738
    },
    {
      "lat": 43.1055461,
      "lon": 5.94241
    },
    {
      "lat": 43.1065624,
      "lon": 5.943802
    }
  ],
  "reference_point": "bow"
}
```

### 6.5 `race/{raceId}/marks/{markId}` — position et vent d’une bouée

La bouée instrumentée (la bouée 3, au vent) porte un anémomètre ; les autres ne donnent que leur position, et `wind` vaut `null`.

| Champ | Type | Unité | Description |
|---|---|---|---|
| `t`, `t_gps_ms`, `seq` | | | Instant de la mesure, compteur |
| `race_id`, `mark_id` | texte | — | Manche, bouée |
| `lat`, `lon` | nombre ou null | degrés | Position mesurée |
| `fix` | texte | — | Qualité de la position : `none`, `3d`, `dgnss`, `rtk_float`, `rtk_fixed` (RTK : correction centimétrique) |
| `h_acc_m` | nombre ou null | m | Précision horizontale estimée |
| `drift_m` | nombre ou null | m | Écart à la position déclarée dans `course` |
| `stale` | booléen | — | `true` si aucune mesure fraîche depuis plus de 3 s (à confirmer) |
| `wind` | objet ou null | — | `tws_kn` et `tws_ms` (vitesse du vent vrai, nœuds et m/s), `twd` (direction d’où vient le vent, degrés vrais), `gust_kn` (rafale max sur la période), `twd_std` (écart-type de la direction, degrés : plus il est grand, plus le vent oscille), `avg_s` (durée de moyenne, s) |

```json
{
  "t": "2027-05-14T13:04:07.000Z",
  "t_gps_ms": 1494335065000,
  "race_id": "2027-05-14-M3",
  "mark_id": "B3",
  "seq": 1447,
  "lat": 43.1063123,
  "lon": 5.9427605,
  "fix": "rtk_fixed",
  "h_acc_m": 0.02,
  "drift_m": 0.5,
  "stale": false,
  "wind": {
    "tws_kn": 9.8,
    "tws_ms": 5.04,
    "twd": 132.5,
    "gust_kn": 12.1,
    "twd_std": 6.2,
    "avg_s": 10
  }
}
```

### 6.6 `race/{raceId}/boats/{boatId}/pos` — position officielle d’un bateau

C’est le flux essentiel : la position donnée par la **balise officielle** (P08), seule source pour le suivi, le classement et l’arbitrage. Vous recevez celle de tous les bateaux, la vôtre comprise, au même instant (P11). Abonnement conseillé : `race/{raceId}/boats/+/pos`.

| Champ | Type | Unité | Description |
|---|---|---|---|
| `t`, `t_gps_ms` | texte, entier | — | **Instant de la mesure** par la balise (et non de l’envoi) |
| `seq` | entier | — | Compteur par bateau, attribué par le PC course |
| `boat_id` | texte | — | Bateau |
| `lat`, `lon` | nombre ou null | degrés | Position de l’antenne de la balise |
| `bow_lat`, `bow_lon` | nombre ou null | degrés | **Position calculée de l’étrave** (le point qui compte pour l’arbitrage) : antenne + distance antenne-étrave mesurée au contrôle, orientée par le cap |
| `bow_src` | texte | — | Base du calcul de l’étrave : `hdg` (cap, normal), `cog` (route fond, moins précis, quand le cap manque), `none` |
| `fix` | texte | — | `none`, `3d`, `dgnss`, `rtk_float`, `rtk_fixed` |
| `h_acc_m` | nombre ou null | m | Précision horizontale estimée |
| `sats` | entier ou null | — | Satellites utilisés (absent par la radio) |
| `sog_kn` | nombre ou null | nœuds | Vitesse fond (par rapport au sol, *speed over ground*) |
| `cog` | nombre ou null | degrés vrais | Route fond (*course over ground*) |
| `hdg` | nombre ou null | degrés vrais | Cap (direction de l’étrave) ; `null` par la radio |
| `heel` | nombre ou null | degrés | Gîte ; `null` par la radio |
| `pitch` | nombre ou null | degrés | Tangage ; `null` par la radio |
| `path` | texte | — | Chemin suivi : `4g` (principal, 10 Hz) ou `radio` (secours 868 MHz, 2 Hz) |
| `stale` | booléen | — | `true` si le PC course n’a plus de données fraîches de ce bateau depuis plus de 1 s |
| `age_ms` | entier | ms | Âge de la donnée à la publication (temps entre la mesure et l’envoi par le PC course) |

Exemple normal (4G, 10 Hz) :

```json
{
  "t": "2027-05-14T13:04:07.200Z",
  "t_gps_ms": 1494335065200,
  "boat_id": "FRA-07",
  "seq": 2472,
  "lat": 43.1069934,
  "lon": 5.9416712,
  "bow_lat": 43.1069936,
  "bow_lon": 5.9416786,
  "bow_src": "hdg",
  "fix": "rtk_fixed",
  "h_acc_m": 0.02,
  "sats": 27,
  "sog_kn": 3.42,
  "cog": 86.4,
  "hdg": 88.0,
  "heel": 14.2,
  "pitch": -1.5,
  "path": "4g",
  "stale": false,
  "age_ms": 38
}
```

Même bateau passé sur la radio de secours (2 Hz, pas de cap ni de gîte, étrave estimée par la route fond) :

```json
{
  "t": "2027-05-14T13:04:09.500Z",
  "t_gps_ms": 1494335067500,
  "boat_id": "FRA-07",
  "seq": 2491,
  "lat": 43.106995,
  "lon": 5.941719,
  "bow_lat": 43.1069952,
  "bow_lon": 5.9417264,
  "bow_src": "cog",
  "fix": "rtk_float",
  "h_acc_m": 0.35,
  "sats": null,
  "sog_kn": 3.3,
  "cog": 87.1,
  "hdg": null,
  "heel": null,
  "pitch": null,
  "path": "radio",
  "stale": false,
  "age_ms": 412
}
```

Bateau perdu (plus aucune donnée depuis 3,1 s : dernière position connue, `stale: true`) :

```json
{
  "t": "2027-05-14T13:05:12.000Z",
  "t_gps_ms": 1494335130000,
  "boat_id": "ITA-05",
  "seq": 2960,
  "lat": 43.107184,
  "lon": 5.941331,
  "bow_lat": 43.107187,
  "bow_lon": 5.941325,
  "bow_src": "hdg",
  "fix": "none",
  "h_acc_m": null,
  "sats": null,
  "sog_kn": null,
  "cog": null,
  "hdg": null,
  "heel": null,
  "pitch": null,
  "path": "radio",
  "stale": true,
  "age_ms": 3100
}
```

Le champ `battery` de la balise et les autres données de santé ne sont **pas** diffusés aux équipes : ils restent sur `sys/beacons/#`, réservé à l’organisation.

### 6.7 `race/{raceId}/wind/field` — la carte de vent

Le moteur vent (S9) fusionne les bouées instrumentées et la station à terre en une **grille de mailles de 20 m** qui couvre le parcours (≈ 240 m × 240 m pour ≈ 200 m de parcours, soit 12 × 12 mailles).

| Champ | Type | Unité | Description |
|---|---|---|---|
| `t`, `t_gps_ms`, `seq` | | | Instant de calcul, compteur |
| `race_id` | texte | — | Manche |
| `grid.origin_lat`, `grid.origin_lon` | nombre | degrés | **Coin sud-ouest** de la grille |
| `grid.cell_m` | nombre | m | Taille d’une maille (20) |
| `grid.nx`, `grid.ny` | entier | — | Nombre de mailles d’ouest en est (`nx`) et du sud au nord (`ny`) |
| `grid.order` | texte | — | `row_major_south_west` : la maille de colonne `i` (0 = ouest) et de ligne `j` (0 = sud) est à l’indice `j × nx + i` ; son centre est à `(i + 0,5) × 20 m` à l’est et `(j + 0,5) × 20 m` au nord de l’origine |
| `tws_kn` | liste de `nx × ny` nombres ou null | nœuds | Vitesse du vent vrai par maille |
| `twd` | liste de `nx × ny` nombres ou null | degrés vrais | Direction d’où vient le vent, par maille |
| `conf` | liste de `nx × ny` nombres ou null | 0 à 1 | Confiance (1 = près d’un capteur, faible = extrapolé) |
| `mean` | objet | nœuds, degrés | Vent moyen sur le parcours : `tws_kn`, `twd` |
| `sources` | liste de textes | — | Capteurs utilisés (`mark:B3`, `met:davis`…) |

La grille est alignée sur le nord ; pour passer de mètres en degrés près du site : 1 m ≈ 0,0000090° de latitude et ≈ 0,0000123° de longitude.

```json
{
  "t": "2027-05-14T13:04:07.000Z",
  "t_gps_ms": 1494335065000,
  "race_id": "2027-05-14-M3",
  "seq": 1447,
  "grid": {
    "origin_lat": 43.1064791,
    "origin_lon": 5.9405557,
    "cell_m": 20,
    "nx": 12,
    "ny": 12,
    "order": "row_major_south_west"
  },
  "tws_kn": [
    9.2, 9.3, 9.4, 9.5, 9.6, 9.8, 9.9, 10.0, 10.1, 10.2, 10.3, 10.4,
    9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 10.0, 10.1, 10.2, 10.3, 10.4, 10.5,
    9.4, 9.5, 9.6, 9.7, 9.8, 9.9, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6,
    9.5, 9.6, 9.7, 9.8, 9.9, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7,
    9.6, 9.7, 9.8, 9.9, 10.0, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8,
    9.7, 9.8, 9.9, 10.0, 10.1, 10.2, 10.4, 10.5, 10.6, 10.7, 10.8, 10.9,
    9.8, 9.9, 10.0, 10.1, 10.2, 10.3, 10.5, 10.6, 10.7, 10.8, 10.9, 11.0,
    9.9, 10.0, 10.1, 10.2, 10.3, 10.4, 10.6, 10.7, 10.8, 10.9, 11.0, 11.1,
    10.0, 10.1, 10.2, 10.3, 10.4, 10.6, 10.7, 10.8, 10.9, 11.0, 11.1, 11.2,
    10.1, 10.2, 10.3, 10.4, 10.5, 10.7, 10.8, 10.9, 11.0, 11.1, 11.2, 11.3,
    10.2, 10.3, 10.4, 10.5, 10.6, 10.8, 10.9, 11.0, 11.1, 11.2, 11.3, 11.4,
    10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 11.0, 11.1, 11.2, 11.3, 11.4, 11.5
  ],
  "twd": [
    130.3, 130.9, 131.5, 132.1, 132.7, 133.3, 133.9, 134.5, 135.1, 135.7, 136.3, 136.9,
    129.9, 130.5, 131.1, 131.7, 132.3, 132.9, 133.5, 134.1, 134.7, 135.3, 135.9, 136.5,
    129.5, 130.1, 130.7, 131.3, 131.9, 132.5, 133.1, 133.7, 134.3, 134.9, 135.5, 136.1,
    129.1, 129.7, 130.3, 130.9, 131.5, 132.1, 132.7, 133.3, 133.9, 134.5, 135.1, 135.7,
    128.7, 129.3, 129.9, 130.5, 131.1, 131.7, 132.3, 132.9, 133.5, 134.1, 134.7, 135.3,
    128.3, 128.9, 129.5, 130.1, 130.7, 131.3, 131.9, 132.5, 133.1, 133.7, 134.3, 134.9,
    127.9, 128.5, 129.1, 129.7, 130.3, 130.9, 131.5, 132.1, 132.7, 133.3, 133.9, 134.5,
    127.5, 128.1, 128.7, 129.3, 129.9, 130.5, 131.1, 131.7, 132.3, 132.9, 133.5, 134.1,
    127.1, 127.7, 128.3, 128.9, 129.5, 130.1, 130.7, 131.3, 131.9, 132.5, 133.1, 133.7,
    126.7, 127.3, 127.9, 128.5, 129.1, 129.7, 130.3, 130.9, 131.5, 132.1, 132.7, 133.3,
    126.3, 126.9, 127.5, 128.1, 128.7, 129.3, 129.9, 130.5, 131.1, 131.7, 132.3, 132.9,
    125.9, 126.5, 127.1, 127.7, 128.3, 128.9, 129.5, 130.1, 130.7, 131.3, 131.9, 132.5
  ],
  "conf": [
    0.49, 0.55, 0.6, 0.65, 0.7, 0.73, 0.76, 0.77, 0.76, 0.73, 0.7, 0.65,
    0.51, 0.57, 0.63, 0.68, 0.73, 0.78, 0.82, 0.83, 0.82, 0.78, 0.73, 0.68,
    0.53, 0.59, 0.64, 0.7, 0.76, 0.82, 0.87, 0.89, 0.87, 0.82, 0.76, 0.7,
    0.53, 0.59, 0.65, 0.71, 0.77, 0.83, 0.89, 0.95, 0.89, 0.83, 0.77, 0.71,
    0.53, 0.59, 0.64, 0.7, 0.76, 0.82, 0.87, 0.89, 0.87, 0.82, 0.76, 0.7,
    0.51, 0.57, 0.63, 0.68, 0.73, 0.78, 0.82, 0.83, 0.82, 0.78, 0.73, 0.68,
    0.49, 0.55, 0.6, 0.65, 0.7, 0.73, 0.76, 0.77, 0.76, 0.73, 0.7, 0.65,
    0.47, 0.52, 0.57, 0.61, 0.65, 0.68, 0.7, 0.71, 0.7, 0.68, 0.65, 0.61,
    0.43, 0.48, 0.53, 0.57, 0.6, 0.63, 0.64, 0.65, 0.64, 0.63, 0.6, 0.57,
    0.4, 0.44, 0.48, 0.52, 0.55, 0.57, 0.59, 0.59, 0.59, 0.57, 0.55, 0.52,
    0.36, 0.4, 0.43, 0.47, 0.49, 0.51, 0.53, 0.53, 0.53, 0.51, 0.49, 0.47,
    0.31, 0.35, 0.38, 0.41, 0.44, 0.46, 0.47, 0.47, 0.47, 0.46, 0.44, 0.41
  ],
  "mean": {
    "tws_kn": 9.9,
    "twd": 131.0
  },
  "sources": ["mark:B3", "met:davis"]
}
```

### 6.8 `race/{raceId}/wind/trend` — la tendance du vent

Prévision simple à 5, 10 et 15 minutes, avec un niveau de confiance (S9). Ce n’est **pas** un conseil tactique (P12) : c’est une donnée, la même pour tous.

| Champ | Type | Unité | Description |
|---|---|---|---|
| `t`, `t_gps_ms`, `seq` | | | Instant de calcul, compteur |
| `now` | objet | nœuds, degrés | Vent moyen actuel : `tws_kn`, `twd` |
| `forecasts` | liste | — | Par horizon : `horizon_min`, `twd`, `twd_shift` (bascule prévue en degrés ; positif = le vent tourne dans le sens des aiguilles d’une montre, à droite), `tws_kn`, `conf` (0 à 1) |
| `side_bias` | objet | — | Différence entre gauche et droite du parcours, vue en remontant au vent : `favoured` (`left`, `right`, `none`), `delta_tws_kn`, `delta_twd` |
| `method` | texte | — | Méthode utilisée, pour information |

```json
{
  "t": "2027-05-14T13:04:07.000Z",
  "t_gps_ms": 1494335065000,
  "race_id": "2027-05-14-M3",
  "seq": 248,
  "now": {
    "tws_kn": 9.9,
    "twd": 131.0
  },
  "forecasts": [
    {
      "horizon_min": 5,
      "twd": 133.0,
      "twd_shift": 2.0,
      "tws_kn": 9.9,
      "conf": 0.7
    },
    {
      "horizon_min": 10,
      "twd": 135.0,
      "twd_shift": 4.0,
      "tws_kn": 10.2,
      "conf": 0.55
    },
    {
      "horizon_min": 15,
      "twd": 136.0,
      "twd_shift": 5.0,
      "tws_kn": 10.4,
      "conf": 0.4
    }
  ],
  "side_bias": {
    "favoured": "right",
    "delta_tws_kn": 0.6,
    "delta_twd": 3.5
  },
  "method": "moyenne glissante 10 min + régression linéaire (v0)"
}
```

### 6.9 `race/{raceId}/events` — les événements de course

Un message par événement. Le logiciel du PC course **signale**, un arbitre **décide** (P15) : un événement détecté automatiquement peut être `provisional`, puis confirmé ou annulé par un nouveau message qui le remplace (`replaces`).

| Champ | Type | Unité | Description |
|---|---|---|---|
| `t`, `t_gps_ms` | | | **Instant de l’événement** (par exemple l’instant exact du passage de bouée), pas de la publication |
| `seq` | entier | — | Compteur des événements de la manche |
| `event_id` | texte | — | Identifiant unique |
| `race_id` | texte | — | Manche |
| `type` | texte | — | Voir la liste ci-dessous |
| `boat_id` | texte ou null | — | Bateau concerné (`null` pour un événement de flotte) |
| `mark_id` | texte ou null | — | Bouée concernée |
| `status` | texte | — | `provisional` (détecté, pas encore validé), `confirmed`, `cancelled` |
| `source` | texte | — | `auto` (moteur de course) ou `committee` (saisi par le comité) |
| `replaces` | texte ou null | — | `event_id` de l’événement que celui-ci corrige |
| `details` | objet | — | Détails propres au type (ci-dessous) |
| `text_fr` | texte | — | Phrase lisible, en français |

| `type` | Signification | `details` |
|---|---|---|
| `warning` | Signal d’avertissement | `start_time`, `start_t_gps_ms` |
| `preparatory` | Signal préparatoire | `start_time`, `start_t_gps_ms` |
| `last_step` | Dernière étape (−0:20) | `start_time`, `start_t_gps_ms` |
| `start` | Départ donné | `start_time`, `start_t_gps_ms` |
| `ocs` | Bateau du mauvais côté de la ligne au départ (*on course side*) | `dist_over_line_m` |
| `individual_recall` | Rappel individuel | `boat_ids` |
| `general_recall` | Rappel général | `new_warning_time` (ou `null`) |
| `mark_rounding` | Passage de bouée ou de porte | `leg_completed`, `rank_at_mark`, `elapsed_ms` |
| `penalty_issued` | Pénalité infligée | `penalty` (`one_turn` : tour par la zone P1-P2, à faire avant l’arrivée ; `dsq`), `rule`, `deadline_s`, `reason_fr` |
| `penalty_done` | Pénalité effectuée | `penalty` |
| `boundary_exit` | Sortie des limites du parcours | `dist_outside_m` |
| `finish` | Arrivée | `rank`, `finish_time`, `finish_t_gps_ms`, `elapsed_ms` |
| `retired` | Abandon | `reason` |
| `postponement` | Retard de la procédure | `new_warning_time` (ou `null`) |
| `abandonment` | Manche annulée | `reason_fr` |
| `course_change` | Changement de parcours (bouée déplacée) | `course_version`, `mark_ids` |
| `shortened_course` | Parcours réduit | `course_version`, `finish_at` |

Le contenu de `details` sera figé au gel du contrat ; d’ici là, il peut s’enrichir (à confirmer avec les règles de course, P14).

```json
{
  "t": "2027-05-14T12:57:00.000Z",
  "t_gps_ms": 1494334638000,
  "event_id": "2027-05-14-M3-E0001",
  "race_id": "2027-05-14-M3",
  "seq": 1,
  "type": "warning",
  "boat_id": null,
  "mark_id": null,
  "status": "confirmed",
  "source": "committee",
  "replaces": null,
  "details": {
    "start_time": "2027-05-14T13:00:00.000Z",
    "start_t_gps_ms": 1494334818000
  },
  "text_fr": "Signal d'avertissement, départ à 15:00:00 heure locale"
}
```

```json
{
  "t": "2027-05-14T13:01:52.300Z",
  "t_gps_ms": 1494334930300,
  "event_id": "2027-05-14-M3-E0009",
  "race_id": "2027-05-14-M3",
  "seq": 9,
  "type": "mark_rounding",
  "boat_id": "FRA-07",
  "mark_id": "B3",
  "status": "confirmed",
  "source": "auto",
  "replaces": null,
  "details": {
    "leg_completed": 1,
    "rank_at_mark": 2,
    "elapsed_ms": 112300
  },
  "text_fr": "FRA-07 passe la bouée au vent en 2e position"
}
```

```json
{
  "t": "2027-05-14T13:00:00.000Z",
  "t_gps_ms": 1494334818000,
  "event_id": "2027-05-14-M3-E0005",
  "race_id": "2027-05-14-M3",
  "seq": 5,
  "type": "ocs",
  "boat_id": "ESP-21",
  "mark_id": null,
  "status": "provisional",
  "source": "auto",
  "replaces": null,
  "details": {
    "dist_over_line_m": 0.8
  },
  "text_fr": "ESP-21 du mauvais côté de la ligne au départ (à confirmer par le comité)"
}
```

```json
{
  "t": "2027-05-14T13:03:10.000Z",
  "t_gps_ms": 1494335008000,
  "event_id": "2027-05-14-M3-E0012",
  "race_id": "2027-05-14-M3",
  "seq": 12,
  "type": "penalty_issued",
  "boat_id": "FRA-03",
  "mark_id": null,
  "status": "confirmed",
  "source": "committee",
  "replaces": null,
  "details": {
    "penalty": "one_turn",
    "rule": "6.1",
    "deadline_s": null,
    "reason_fr": "Contact avec ITA-05 au croisement"
  },
  "text_fr": "Pénalité d'un tour pour FRA-03"
}
```

```json
{
  "t": "2027-05-14T13:09:41.700Z",
  "t_gps_ms": 1494335399700,
  "event_id": "2027-05-14-M3-E0031",
  "race_id": "2027-05-14-M3",
  "seq": 31,
  "type": "finish",
  "boat_id": "FRA-07",
  "mark_id": null,
  "status": "provisional",
  "source": "auto",
  "replaces": null,
  "details": {
    "rank": 1,
    "finish_time": "2027-05-14T13:09:41.700Z",
    "finish_t_gps_ms": 1494335399700,
    "elapsed_ms": 581700
  },
  "text_fr": "FRA-07 franchit la ligne d'arrivée, 1er provisoire"
}
```

### 6.10 `race/{raceId}/flags` — les pavillons envoyés

Les pavillons sont hissés à la main (P18) ; le comité saisit en même temps dans sa console ce qu’il envoie, et ce sujet en donne l’image. **En cas de différence, ce sont les signaux réellement faits par le comité qui font foi** (à confirmer dans les instructions de course).

| Champ | Type | Unité | Description |
|---|---|---|---|
| `t`, `t_gps_ms`, `seq` | | | Instant de publication, compteur |
| `flags` | liste | — | Pavillons actuellement envoyés (liste vide s’il n’y en a aucun) |
| `flags[].flag` | texte | — | `class` (pavillon de classe, avertissement), `P`, `I`, `Z`, `U`, `black` (noir), `AP` (retard), `N` (annulation), `X` (rappel individuel), `first_substitute` (premier substitut, rappel général), `S` (parcours réduit), `C` (changement de parcours), `L` (avis aux concurrents), `Y`, `H`, `orange` (pavillon de la ligne de départ) |
| `flags[].since`, `since_t_gps_ms` | texte, entier | — | Depuis quand il est envoyé |
| `flags[].over` | texte ou null | — | Pavillon envoyé au-dessus de `A` ou `H`, sinon `null` |
| `flags[].meaning_fr` | texte | — | Signification en clair |

```json
{
  "t": "2027-05-14T12:58:30.000Z",
  "t_gps_ms": 1494334728000,
  "race_id": "2027-05-14-M3",
  "seq": 3,
  "flags": [
    {
      "flag": "orange",
      "since": "2027-05-14T12:50:00.000Z",
      "since_t_gps_ms": 1494334218000,
      "over": null,
      "meaning_fr": "Ligne de départ en place"
    },
    {
      "flag": "class",
      "since": "2027-05-14T12:57:00.000Z",
      "since_t_gps_ms": 1494334638000,
      "over": null,
      "meaning_fr": "Signal d'avertissement"
    },
    {
      "flag": "P",
      "since": "2027-05-14T12:58:00.000Z",
      "since_t_gps_ms": 1494334698000,
      "over": null,
      "meaning_fr": "Signal préparatoire"
    }
  ]
}
```

### 6.11 `race/{raceId}/leaderboard` — le classement live

| Champ | Type | Unité | Description |
|---|---|---|---|
| `t`, `t_gps_ms`, `seq` | | | Instant du calcul, compteur |
| `provisional` | booléen | — | `true` tant que le classement n’est pas définitif |
| `entries` | liste | — | Un élément par bateau, dans l’ordre du classement |
| `entries[].rank` | entier ou null | — | Rang ; `null` si non classé |
| `entries[].boat_id` | texte | — | Bateau |
| `entries[].status` | texte | — | `not_started`, `racing`, `finished`, `ocs`, `dns` (pas parti), `dnc` (pas venu), `dnf` (pas fini), `ret` (abandon), `dsq` (disqualifié), `ufd` et `bfd` (départ anticipé sous pavillon U ou noir), `dne` (disqualification non retirable), `rdg` (réparation accordée) |
| `entries[].legs_completed` | entier | — | Bords terminés |
| `entries[].next_leg`, `next_mark_ids` | entier ou null, liste | — | Prochain bord et sa ou ses bouées |
| `entries[].dist_to_next_m` | nombre ou null | m | Distance de l’étrave à la prochaine bouée (la plus proche des deux pour une porte) |
| `entries[].gap_to_leader_s` | nombre ou null | s | Écart estimé avec le premier |
| `entries[].penalties_pending` | entier | — | Pénalités à effectuer |
| `entries[].finish_time`, `finish_t_gps_ms`, `elapsed_ms` | | | Arrivée et temps de course, `null` avant l’arrivée |

```json
{
  "t": "2027-05-14T13:04:07.000Z",
  "t_gps_ms": 1494335065000,
  "race_id": "2027-05-14-M3",
  "seq": 248,
  "provisional": true,
  "entries": [
    {
      "rank": 1,
      "boat_id": "MON-01",
      "status": "racing",
      "legs_completed": 2,
      "next_leg": 3,
      "next_mark_ids": ["B3"],
      "dist_to_next_m": 44.5,
      "gap_to_leader_s": 0.0,
      "penalties_pending": 0,
      "finish_time": null,
      "finish_t_gps_ms": null,
      "elapsed_ms": null
    },
    {
      "rank": 2,
      "boat_id": "FRA-07",
      "status": "racing",
      "legs_completed": 2,
      "next_leg": 3,
      "next_mark_ids": ["B3"],
      "dist_to_next_m": 56.0,
      "gap_to_leader_s": 6.8,
      "penalties_pending": 0,
      "finish_time": null,
      "finish_t_gps_ms": null,
      "elapsed_ms": null
    },
    {
      "rank": 3,
      "boat_id": "ITA-05",
      "status": "racing",
      "legs_completed": 2,
      "next_leg": 3,
      "next_mark_ids": ["B3"],
      "dist_to_next_m": 70.3,
      "gap_to_leader_s": 15.2,
      "penalties_pending": 0,
      "finish_time": null,
      "finish_t_gps_ms": null,
      "elapsed_ms": null
    },
    {
      "rank": 4,
      "boat_id": "FRA-03",
      "status": "racing",
      "legs_completed": 1,
      "next_leg": 2,
      "next_mark_ids": ["B1", "B2"],
      "dist_to_next_m": 12.5,
      "gap_to_leader_s": 31.0,
      "penalties_pending": 1,
      "finish_time": null,
      "finish_t_gps_ms": null,
      "elapsed_ms": null
    },
    {
      "rank": 5,
      "boat_id": "FRA-12",
      "status": "racing",
      "legs_completed": 1,
      "next_leg": 2,
      "next_mark_ids": ["B1", "B2"],
      "dist_to_next_m": 30.2,
      "gap_to_leader_s": 44.9,
      "penalties_pending": 0,
      "finish_time": null,
      "finish_t_gps_ms": null,
      "elapsed_ms": null
    },
    {
      "rank": null,
      "boat_id": "ESP-21",
      "status": "ocs",
      "legs_completed": 0,
      "next_leg": 1,
      "next_mark_ids": ["B3"],
      "dist_to_next_m": null,
      "gap_to_leader_s": null,
      "penalties_pending": 0,
      "finish_time": null,
      "finish_t_gps_ms": null,
      "elapsed_ms": null
    }
  ]
}
```

### 6.12 `race/{raceId}/notices` — les avis officiels

Le tableau officiel en version électronique : le comité publie à **toutes** les équipes. Le message conservé contient **la liste complète** des avis valables pour la manche (y compris ceux de la journée et de l’épreuve) ; un nouvel avis remplace la liste par une liste plus longue.

| Champ | Type | Unité | Description |
|---|---|---|---|
| `t`, `t_gps_ms`, `seq` | | | Instant de publication, compteur |
| `notices[].notice_id` | texte | — | Identifiant, `N-0001`… |
| `notices[].issued`, `issued_t_gps_ms` | | | Instant de publication de l’avis |
| `notices[].scope` | texte | — | Portée : `event` (épreuve), `day` (journée), `race` (manche) |
| `notices[].priority` | texte | — | `info`, `important`, `urgent` |
| `notices[].title`, `body` | texte | — | Titre (120 caractères au plus) et texte |
| `notices[].requires_ack` | booléen | — | `true` si chaque équipe doit en accuser réception (message `ack` dans `outbox`) |
| `notices[].ack_deadline` | texte ou null | — | Heure limite de l’accusé de réception |
| `notices[].supersedes` | texte ou null | — | Avis remplacé par celui-ci |
| `notices[].attachment_url` | texte ou null | — | Lien vers une pièce jointe sur le réseau local, s’il y en a une |

```json
{
  "t": "2027-05-14T12:45:00.000Z",
  "t_gps_ms": 1494333918000,
  "race_id": "2027-05-14-M3",
  "seq": 7,
  "notices": [
    {
      "notice_id": "N-0012",
      "issued": "2027-05-14T08:30:00.000Z",
      "issued_t_gps_ms": 1494318618000,
      "scope": "day",
      "priority": "info",
      "title": "Programme du jour",
      "body": "4 manches prévues. Premier signal d'avertissement à 12:00 heure locale.",
      "requires_ack": false,
      "ack_deadline": null,
      "supersedes": null,
      "attachment_url": null
    },
    {
      "notice_id": "N-0014",
      "issued": "2027-05-14T12:45:00.000Z",
      "issued_t_gps_ms": 1494333918000,
      "scope": "race",
      "priority": "important",
      "title": "Porte 1-2 déplacée",
      "body": "La porte 1-2 a été déplacée de 15 m vers le sud-ouest. Le parcours passe en version 2.",
      "requires_ack": true,
      "ack_deadline": "2027-05-14T12:55:00.000Z",
      "supersedes": null,
      "attachment_url": null
    }
  ]
}
```

### 6.13 `teams/{teamId}/inbox` — messages du comité à votre équipe

Seule votre équipe lit ce sujet. QoS 1, non conservé : gardez une **session persistante** pour ne rien manquer pendant une courte coupure.

| Champ | Type | Unité | Description |
|---|---|---|---|
| `t`, `t_gps_ms` | | | Instant d’envoi |
| `msg_id` | texte | — | Identifiant unique du message |
| `team_id` | texte | — | Votre équipe |
| `race_id` | texte ou null | — | Manche concernée |
| `type` | texte | — | `receipt` (accusé de réception automatique de l’un de vos messages), `message`, `reply` (réponse à une question), `penalty_notice`, `protest_notice` (une réclamation vous vise), `hearing` (convocation à une instruction), `decision` (décision du jury), `safety`, `technical`, `error` (votre message a été refusé) |
| `in_reply_to` | texte ou null | — | `msg_id` de votre message auquel celui-ci répond |
| `priority` | texte | — | `info`, `important`, `urgent` |
| `requires_ack` | booléen | — | `true` : répondez par un `ack` |
| `title`, `body` | texte | — | Titre et texte |
| `data` | objet | — | Données propres au type (numéro de réclamation, heure d’instruction…) |

```json
{
  "t": "2027-05-14T13:05:40.180Z",
  "t_gps_ms": 1494335158180,
  "msg_id": "C-fra07-0031",
  "team_id": "fra07",
  "race_id": "2027-05-14-M3",
  "type": "receipt",
  "in_reply_to": "fra07-20270514-0005",
  "priority": "info",
  "requires_ack": false,
  "title": "Réclamation reçue",
  "body": "Votre réclamation contre FRA-03 est enregistrée sous le n° R-0004.",
  "data": {
    "accepted": true,
    "protest_id": "R-0004"
  }
}
```

```json
{
  "t": "2027-05-14T13:20:00.000Z",
  "t_gps_ms": 1494336018000,
  "msg_id": "C-fra07-0032",
  "team_id": "fra07",
  "race_id": "2027-05-14-M3",
  "type": "hearing",
  "in_reply_to": null,
  "priority": "important",
  "requires_ack": true,
  "title": "Instruction de la réclamation R-0004",
  "body": "Instruction à 16:00 heure locale, tente du jury. Rejeu vidéo et traces disponibles.",
  "data": {
    "protest_id": "R-0004",
    "hearing_time": "2027-05-14T14:00:00.000Z"
  }
}
```

### 6.14 `teams/{teamId}/outbox` — vos messages au comité

Le seul sujet sur lequel vous pouvez écrire. Publiez en **QoS 1**, sans drapeau *retained*. Chaque message reçoit en retour, dans votre `inbox`, un `receipt` (ou un `error`) qui reprend votre `msg_id` dans `in_reply_to` : tant que vous ne l’avez pas reçu, considérez le message comme non parvenu.

Enveloppe commune :

| Champ | Type | Unité | Description |
|---|---|---|---|
| `t`, `t_gps_ms` | | | Instant d’envoi, selon votre horloge synchronisée |
| `msg_id` | texte | — | Identifiant **unique**, choisi par vous, préfixé par votre code : `fra07-20270514-0005`. Renvoyer le même `msg_id` ne crée pas de doublon |
| `team_id`, `boat_id` | texte | — | Votre équipe et votre bateau ; ils doivent correspondre à votre compte |
| `race_id` | texte ou null | — | Manche concernée, `null` si le message n’en concerne aucune |
| `type` | texte | — | `ack`, `protest`, `redress_request`, `retire`, `technical_issue`, `assistance_request`, `question` |
| `payload` | objet | — | Contenu propre au type (tableaux ci-dessous) |

Les règles de fond (délais pour réclamer, forme, recevabilité) relèvent des **règles de course et des instructions de course** (règles 9.3 et 9.5 : réclamation dans les 10 minutes qui suivent l’arrivée du dernier bateau). Ce contrat ne fixe que la forme du message.

#### `ack` — accusé de réception

| Champ de `payload` | Type | Description |
|---|---|---|
| `ref_id` | texte | `notice_id` d’un avis ou `msg_id` d’un message de l’`inbox` |
| `ref_kind` | texte | `notice` ou `inbox` |

```json
{
  "t": "2027-05-14T12:46:12.400Z",
  "t_gps_ms": 1494333990400,
  "msg_id": "fra07-20270514-0003",
  "team_id": "fra07",
  "boat_id": "FRA-07",
  "race_id": "2027-05-14-M3",
  "type": "ack",
  "payload": {
    "ref_id": "N-0014",
    "ref_kind": "notice"
  }
}
```

#### `protest` — réclamation contre un autre bateau

| Champ de `payload` | Type | Description |
|---|---|---|
| `against` | liste de `boat_id` | Bateau(x) réclamé(s) |
| `incident_time`, `incident_t_gps_ms` | texte, entier | Instant de l’incident (le jury retrouvera les traces et la vidéo à partir de là) |
| `rule` | texte | Numéro de la règle invoquée, dans nos règles de course (par exemple `6.1`) |
| `location` | `{lat, lon}` ou null | Lieu de l’incident |
| `description` | texte | Ce qui s’est passé (2 000 caractères au plus) |
| `witnesses` | liste de `boat_id` | Témoins éventuels |

Une réclamation envoyée ici **sert de « héler »** (le cri « Protest ! » des régates habitables) et en garde la trace horodatée. Délai : 10 minutes après l’arrivée du dernier bateau (règle 9.3) ; formulaire complémentaire éventuel dans les instructions de course.

```json
{
  "t": "2027-05-14T13:05:40.120Z",
  "t_gps_ms": 1494335158120,
  "msg_id": "fra07-20270514-0005",
  "team_id": "fra07",
  "boat_id": "FRA-07",
  "race_id": "2027-05-14-M3",
  "type": "protest",
  "payload": {
    "against": ["FRA-03"],
    "incident_time": "2027-05-14T13:03:02.000Z",
    "incident_t_gps_ms": 1494335000000,
    "rule": "6.2",
    "location": {
      "lat": 43.107201,
      "lon": 5.941883
    },
    "description": "Au croisement, FRA-03 bâbord amures n'a pas manœuvré pour éviter FRA-07 tribord amures ; contact au tableau arrière.",
    "witnesses": ["ITA-05"]
  }
}
```

#### `redress_request` — demande de réparation

Une demande de réparation vise une erreur du comité ou de l’organisation (par exemple une donnée officielle fausse), pas un autre bateau.

| Champ de `payload` | Type | Description |
|---|---|---|
| `incident_time`, `incident_t_gps_ms` | texte, entier | Instant du problème |
| `reason` | texte | `committee_error`, `official_system_failure` (panne du système officiel), `assistance_given` (vous avez porté assistance), `damage_by_other`, `other` |
| `description` | texte | Explication |
| `requested_remedy` | texte ou null | Réparation demandée |

```json
{
  "t": "2027-05-14T13:12:00.000Z",
  "t_gps_ms": 1494335538000,
  "msg_id": "fra07-20270514-0006",
  "team_id": "fra07",
  "boat_id": "FRA-07",
  "race_id": "2027-05-14-M3",
  "type": "redress_request",
  "payload": {
    "incident_time": "2027-05-14T13:02:30.000Z",
    "incident_t_gps_ms": 1494334968000,
    "reason": "official_system_failure",
    "description": "La porte 1-2 publiée dans course v2 ne correspondait pas à la position réelle de B2 (écart de 12 m).",
    "requested_remedy": "Moyenne des points sur les autres manches du jour"
  }
}
```

#### `retire` — abandon

| Champ de `payload` | Type | Description |
|---|---|---|
| `reason` | texte | `penalty_accepted` (vous acceptez une pénalité en abandonnant), `damage`, `link_lost`, `safety`, `other` |
| `description` | texte ou null | Précisions |

```json
{
  "t": "2027-05-14T13:06:30.000Z",
  "t_gps_ms": 1494335208000,
  "msg_id": "fra07-20270514-0007",
  "team_id": "fra07",
  "boat_id": "FRA-07",
  "race_id": "2027-05-14-M3",
  "type": "retire",
  "payload": {
    "reason": "damage",
    "description": "Servo de safran bloqué"
  }
}
```

#### `technical_issue` — signalement technique

| Champ de `payload` | Type | Description |
|---|---|---|
| `component` | texte | `team_link` (votre liaison avec le bateau), `boat`, `official_beacon` (balise officielle), `team_network` (votre prise, votre Wi-Fi), `data_feed` (le flux équipes), `other` |
| `severity` | texte | `low`, `medium`, `high` |
| `description` | texte | Ce que vous constatez, avec l’heure UTC |

```json
{
  "t": "2027-05-14T12:20:00.000Z",
  "t_gps_ms": 1494332418000,
  "msg_id": "fra07-20270514-0002",
  "team_id": "fra07",
  "boat_id": "FRA-07",
  "race_id": null,
  "type": "technical_issue",
  "payload": {
    "component": "data_feed",
    "severity": "medium",
    "description": "Positions de MON-01 absentes depuis 12:19:40 UTC sur notre abonnement."
  }
}
```

#### `assistance_request` — demande d’assistance sur l’eau

| Champ de `payload` | Type | Description |
|---|---|---|
| `urgency` | texte | `urgent` ou `normal` |
| `reason` | texte | `capsized` (chaviré), `dismasted` (démâté), `stuck` (pris dans un obstacle), `drifting` (dérive sans contrôle), `link_lost`, `collision`, `other` |
| `description` | texte ou null | Précisions |

Ce message **complète** l’appel direct à l’officier de sécurité, il ne le remplace pas : en cas d’urgence, prévenez aussi de vive voix ou par la radio prévue (à confirmer). La position du bateau est connue par sa balise ; inutile de l’envoyer.

```json
{
  "t": "2027-05-14T13:07:15.000Z",
  "t_gps_ms": 1494335253000,
  "msg_id": "fra07-20270514-0008",
  "team_id": "fra07",
  "boat_id": "FRA-07",
  "race_id": "2027-05-14-M3",
  "type": "assistance_request",
  "payload": {
    "urgency": "urgent",
    "reason": "capsized",
    "description": "FRA-07 chaviré près de la limite est, ne se redresse pas."
  }
}
```

#### `question` — question au comité

| Champ de `payload` | Type | Description |
|---|---|---|
| `about` | texte | `course`, `procedure`, `rules`, `data_feed`, `logistics`, `other` |
| `text` | texte | La question |

La réponse arrive dans votre `inbox` (`type: reply`). Si elle intéresse tout le monde, le comité la publie aussi en avis (`notices`), pour que toutes les équipes aient la même information (P11).

```json
{
  "t": "2027-05-14T12:10:00.000Z",
  "t_gps_ms": 1494331818000,
  "msg_id": "fra07-20270514-0001",
  "team_id": "fra07",
  "boat_id": "FRA-07",
  "race_id": null,
  "type": "question",
  "payload": {
    "about": "course",
    "text": "Au passage de la porte 1-2, peut-on toucher la ligne entre B1 et B2 ?"
  }
}
```

### 6.15 `sys/time` — balise de temps

Publié chaque seconde, au début de la seconde, par le serveur synchronisé sur l’heure GPS de la base RTK, à quelques millisecondes près. Les positions, elles, portent l’heure GPS exacte de leur mesure.

| Champ | Type | Unité | Description |
|---|---|---|---|
| `t`, `t_gps_ms`, `seq` | | | Heure du serveur à l’envoi, compteur |
| `gps_utc_offset_s` | entier | s | Écart GPS − UTC |
| `source` | texte | — | `gnss` (normal : heure tirée des messages GPS de la base), `gnss_pps` (si la carte de la base sort l’impulsion), `ntp_fallback`, `free_running` (le serveur a perdu sa référence : alerte) |
| `server` | texte | — | Serveur qui publie (`srv1` principal, `srv2` secours) |
| `ntp_server` | texte | — | Serveur NTP à utiliser |
| `sync_ok` | booléen | — | `true` si le serveur est calé sur sa référence |
| `est_error_us` | entier | µs | Erreur estimée du serveur par rapport au temps GPS |

```json
{
  "t": "2027-05-14T13:04:07.000Z",
  "t_gps_ms": 1494335065000,
  "seq": 3847,
  "gps_utc_offset_s": 18,
  "source": "gnss",
  "server": "srv1",
  "ntp_server": "10.20.0.1",
  "sync_ok": true,
  "est_error_us": 2000
}
```

### 6.16 `meta/schema` — version du contrat

| Champ | Type | Unité | Description |
|---|---|---|---|
| `t`, `t_gps_ms` | | | Instant de publication |
| `contract_version` | texte | — | Version servie, par exemple `1.0.0-draft` puis `1.0.0` |
| `frozen` | booléen | — | `true` après le gel |
| `freeze_date` | texte | date | Date du gel |
| `schemas_url` | texte | — | Où trouver les schémas de cette version |
| `deprecations` | liste | — | Éléments dépréciés : `item`, `announced`, `removal`, `replacement` |

```json
{
  "t": "2027-01-11T09:00:00.000Z",
  "t_gps_ms": 1483693218000,
  "contract_version": "1.0.0-draft",
  "frozen": false,
  "freeze_date": "2027-03-15",
  "schemas_url": "https://[domaine-a-definir]/ai-regatta/contrat/1.0/schemas/",
  "deprecations": []
}
```

## 7. Horloge et compte à rebours

L’écart d’horloge entre équipes, comité et médias doit rester **sous 5 ms** (P26). Deux règles, obligatoires :

**1. Synchroniser le PC avec le serveur de temps du PC course.** Chaque PC d’équipe qui affiche un chrono ou horodate un message doit faire tourner **chrony** (ou un client NTP équivalent) sur `10.20.0.1`. NTP (*Network Time Protocol*) recale l’horloge du PC en continu sur un serveur de référence ; chrony est le client le plus précis sous Linux.

```
# /etc/chrony/chrony.conf (extrait) — PC d'équipe sur le site
server 10.20.0.1 iburst minpoll 4 maxpoll 4 prefer
makestep 0.1 3          # corrige d'un coup un gros écart au démarrage
```

Vérification : `chronyc tracking` doit indiquer `Reference ID … (10.20.0.1)` et une ligne `System time` sous 0,005 s (5 ms), en pratique bien moins sur le réseau local. Sous Windows, le service de temps intégré est trop imprécis : utilisez un client NTP complet (par exemple l’implémentation NTP de référence portée sous Windows) ou faites tourner le logiciel de chrono sur une machine Linux. Sous macOS, chrony s’installe par Homebrew (à vérifier par chaque équipe).

**2. Calculer le compte à rebours localement, jamais à partir de l’arrivée des messages.** Le message `clock` donne l’**heure GPS du départ** (`start_t_gps_ms`). Votre logiciel calcule :

```
maintenant_gps_ms = temps_unix_local_ms − 315 964 800 000 + 1 000 × gps_utc_offset_s
reste_ms          = start_t_gps_ms − maintenant_gps_ms      (négatif après le départ = temps de course)
```

Ainsi, même si le réseau ralentit ou si un message arrive en retard, votre chrono reste juste : il ne dépend que de votre horloge synchronisée. Les rappels du message `clock` chaque seconde ne servent qu’à confirmer l’heure du départ et à rattraper un changement (retard, rappel général).

**Mesurer son écart avec `sys/time`.** À chaque réception de `sys/time`, calculez `écart = maintenant_gps_ms − t_gps_ms`. Cet écart contient le délai réseau (moins d’une milliseconde sur place) plus le décalage de votre horloge. Retenez la **plus petite valeur sur 60 s** : si elle dépasse 5 ms (ou est négative de plus de 5 ms), votre synchronisation est mauvaise ; vérifiez chrony avant la course. Le script [exemples/python/abonnement.py](exemples/python/abonnement.py) fait cette mesure.

## 8. Cas particuliers et pannes

### 8.1 Bateau perdu

Si le PC course ne reçoit plus rien d’un bateau depuis **plus de 1 s**, il publie à 1 Hz la dernière position connue avec `stale: true`, `fix: "none"` et `age_ms` qui augmente. Les champs mesurés (`sog_kn`, `cog`, `hdg`…) passent à `null`. Dès que la balise revient, les messages normaux reprennent. Si la balise elle-même n’a plus de position GPS, `fix` vaut `none` et `lat`/`lon` donnent la dernière position valable avec `stale: true`.

### 8.2 Passage sur la radio de secours

Quand la 4G d’une balise tombe, le PC course bascule seul sur la radio 868 MHz : `path` passe à `radio`, la cadence tombe à **2 Hz**, `hdg`, `heel`, `pitch` et `sats` deviennent `null` (la trame radio ne les contient pas), et l’étrave est estimée par la route fond (`bow_src: "cog"`). La précision RTK tient 10 à 30 s, puis devient métrique (`fix` passe de `rtk_fixed` à `rtk_float` puis `3d`). Votre logiciel doit accepter ces trous et ces cadences variables.

### 8.3 Doublons et désordre

En QoS 1, un message peut arriver **deux fois** ; un message QoS 0 peut arriver **après** un message plus récent, surtout au moment d’un changement de chemin. Règle simple : pour chaque sujet (chaque bateau pour les positions), **gardez le plus grand `seq` reçu et ignorez tout message dont le `seq` est inférieur ou égal**. Pour les événements, dédoublonnez sur `event_id` ; pour l’`inbox`, sur `msg_id`. Pour dater, utilisez toujours `t_gps_ms` du message, jamais l’heure de réception.

Exception : après une bascule de serveur, `seq` peut repartir d’une valeur plus basse sur certains sujets (à confirmer lors des essais). Si `seq` recule de plus de 1 000 ou si `t_gps_ms` est nettement plus récent que votre dernier message, acceptez-le et repartez de cette nouvelle valeur.

### 8.4 Reprise après une coupure

À chaque connexion (première ou reconnexion) :

1. connectez-vous avec le **même identifiant client** et `clean_session = false` ;
2. **réabonnez-vous à tout**, systématiquement (ne comptez pas sur la mémoire du broker) ;
3. les **messages conservés** vous redonnent aussitôt l’état complet : manche en cours, état, chrono, parcours, bouées, pavillons, classement, avis, version du contrat ;
4. les événements manqués pendant la coupure ne sont pas tous rejoués : reconstruisez la situation à partir du classement et de l’état, pas en rejouant les événements.

### 8.5 Bascule sur le serveur de secours

Si le serveur principal tombe, le serveur de secours reprend l’adresse `10.20.0.10` en quelques secondes. Votre client voit une déconnexion, puis se reconnecte. Le serveur de secours **ne connaît pas forcément votre session** (abonnements et messages QoS 1 en attente) : c’est pour cela que la règle 2 du §8.4 est obligatoire. Les messages de l’`inbox` envoyés pendant la bascule peuvent être perdus ; le comité renvoie ceux qui demandent un accusé de réception tant qu’il ne l’a pas reçu, et les avis restent dans la liste conservée de `notices`. Pendant la bascule, votre chrono continue de compter seul (§7).

### 8.6 Changement de parcours, rappel général, retard

- Un **changement de parcours** publie un nouveau `course` (avec `course_version` + 1), un événement `course_change`, et en général un avis. Relisez toujours `course` au lieu de corriger votre copie.
- Un **rappel général** publie `clock` avec `step: "general_recall"`, puis, quand le comité relance la procédure, un nouveau `start_time`. Un **retard** (`postponed`) fait de même.
- Une **manche annulée** passe `state.status` à `abandoned` ; la manche suivante apparaît dans `race/current`.

### 8.7 Perte du flux officiel en course (proposition au comité d’organisation)

Le flux officiel donne à toutes les équipes, au même instant, la position de tous les bateaux et des bouées, le vent, le chrono et les événements (règle 3.7). Votre IA peut s’en servir pour sa tactique ; vos propres capteurs (caméra, LIDAR de classe 1 ou 1M) restent permis en plus (règle 3.9).

**Comment détecter la perte.** Considérez le flux comme perdu si vous ne recevez plus `sys/time` depuis **3 s**, ou plus aucune position de bateau depuis **2 s** alors que la course est lancée.

**Ce que fait votre bateau.** Il applique le comportement que vous avez déclaré et montré à l’homologation, par exemple : garder son cap quelques secondes, puis se mettre face au vent, ou finir le bord en cours sans virer (règle 3.8). Votre IA ne doit pas continuer à naviguer sur des positions périmées.

**Ce que fait le comité.** Il peut interrompre la course (`race/{raceId}/state`, `status: "interrupted"`). Une équipe lésée par la panne peut demander réparation. Le journal du PC course prouve, à la milliseconde, ce que chaque équipe a reçu et quand.

## 9. Versions et politique de changement

- Numérotation **semver** (*semantic versioning*) : `MAJEUR.MINEUR.CORRECTIF`. Un changement **majeur** casse la compatibilité ; **mineur** ajoute un champ ou un sujet facultatif ; **correctif** ne touche que la documentation ou corrige un défaut sans changer la forme.
- **Jusqu’au 15 mars 2027** : version `1.0.0-draft`. Elle peut encore changer, après annonce aux équipes et test dans le bac à sable.
- **15 mars 2027 : gel** en version `1.0.0`. Après le gel, aucun changement majeur avant la fin de l’épreuve. Seuls des ajouts compatibles (mineurs) sont possibles, et uniquement s’ils sont annoncés **au moins 30 jours à l’avance**, donc pas après le 12 avril 2027.
- Toute **dépréciation** (un champ ou un sujet qui disparaîtra) est annoncée au moins 30 jours à l’avance, dans `meta/schema.deprecations` et par courriel aux équipes ; l’ancien et le nouveau coexistent pendant cette période.
- Une correction urgente qui touche la sécurité ou l’équité peut être faite à tout moment ; elle est annoncée par un avis `urgent`.
- Les schémas publiés refusent les champs inconnus, pour aider l’organisation à tester son propre code. **Dans votre logiciel, ignorez les champs inconnus** : vous resterez compatible avec les versions mineures suivantes.

## 10. Points à confirmer

| Point | Proposition actuelle |
|---|---|
| Écart GPS − UTC en mai 2027 | 18 s, à vérifier selon les annonces de l’IERS (le champ `gps_utc_offset_s` fait foi) |
| Limites de débit et de connexions | §3.3 |
| Signe de la gîte | Positive sur tribord, à aligner sur le firmware de la balise |
| Seuil `stale` des bouées | 3 s |
| Cadence de `wind/trend` | Toutes les 10 s |
| Contenu détaillé de `details` des événements | À figer avec les règles de course (P14) |
| Effet juridique des réclamations envoyées par `outbox` | Instructions de course |
| Liste exacte des pavillons utilisés | Instructions de course |
| Réenvoi de `seq` après bascule | À observer lors des tests de bascule |
| Adresse fixe par équipe | Sur demande |

## Annexe — Reprise de télécommande (proposition au comité d’organisation)

Le règlement de l’organisateur permet de reprendre la main à la télécommande pendant une course, 30 s au plus, contre un tour de pénalité (§ 2c, § 7). Nous proposons que chaque reprise soit déclarée dans `teams/{équipe}/outbox` :

| Champ | Type | Description |
|---|---|---|
| `type` | texte | `manual_control` |
| `payload.state` | texte | `start` (reprise) ou `end` (retour à l’IA) |
| `payload.reason` | texte | `start_line`, `after_finish`, `failure`, `zone_exit`, `penalty` |

Le PC course chronomètre la reprise, la montre à l’arbitre et signale tout dépassement des 30 s. Une reprise pour rallier le départ, après l’arrivée ou pour faire la pénalité n’est pas pénalisée.
