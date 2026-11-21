# AI Regatta — Les connecteurs du flux équipes

> Version 1.0-draft, 20 novembre 2026. Le contenu des messages est défini dans le [contrat d’interface](contrat-interface.md) ; ce document explique **par quel moyen** le recevoir.

Toutes les équipes reçoivent **les mêmes données, au même instant** (P11), quel que soit le connecteur. Un connecteur n’est qu’une autre façon de présenter le même flux : il ne donne jamais plus d’informations qu’un autre. Le connecteur de référence est MQTT ; les autres en sont dérivés.

## En un coup d’œil

| Connecteur | Adresse sur le site | Délai ajouté (sur place) | Effort pour l’équipe | Pour qui | Données |
|---|---|---|---|---|---|
| **(a) MQTT direct** (recommandé) | `mqtts://10.20.0.10:8883` | Référence : < 50 ms de bout en bout | Moyen : une bibliothèque MQTT et du JSON | Logiciel tactique de l’équipe | Toutes |
| **(b) MQTT sur WebSocket** | `wss://10.20.0.10:8884/mqtt` | Identique à MQTT, à quelques ms près | Faible pour une application web | Tableau de bord dans un navigateur | Toutes |
| **(c) NMEA 0183 sur TCP** | `10.20.0.10:10110` | + quelques dizaines de ms (conversion, à mesurer) | Presque nul : se brancher | Logiciels de navigation (OpenCPN, qtVlm, Expedition…) | Positions, bouées, vent, heure ; pas d’événements ni de classement |
| **(d) Pont Signal K** (option, à décider) | `ws://10.20.0.10:3000/signalk/v1/stream` (à confirmer) | + quelques dizaines de ms (à mesurer) | Faible si votre outil parle Signal K | Outils de l’écosystème Signal K | Positions, bouées, vent |
| **(e) Fichiers de rejeu et simulateur** | Bac à sable cloud, et fichiers téléchargeables | Hors ligne | Faible | Développement, tests, analyse après course | Toutes |

Conseil : **développez sur MQTT** (a), ajoutez le NMEA (c) si vous voulez un affichage cartographique sans effort, et testez tout dans le **bac à sable** (e) dès février.

---

## (a) MQTT direct — recommandé

C’est le flux d’origine, celui que décrit le contrat d’interface : tous les sujets, toutes les données, avec la latence la plus faible.

- **Protocole** : MQTT 3.1.1 ou 5, broker Mosquitto (P25).
- **Adresses** : `mqtt://10.20.0.10:1883` (sans chiffrement, réseau local fermé) ou `mqtts://10.20.0.10:8883` (TLS, recommandé).
- **Compte** : `equipe-<code>`, lecture seule sur `race/#`, écriture seule sur votre `teams/<code>/outbox`.
- **Bibliothèques conseillées** : Python **paho-mqtt 2.x** ; JavaScript et Node.js **mqtt.js 5** ; C/C++ **Eclipse Paho C** ou **libmosquitto** ; Rust **rumqttc** ; outil en ligne de commande **mosquitto_sub** pour regarder passer les messages.
- **Quand l’utiliser** : toujours, pour votre logiciel tactique et pour envoyer vos messages au comité (seul MQTT, direct ou par WebSocket, permet d’écrire dans `outbox`).

Regarder le flux en une ligne (mot de passe dans une variable, jamais en clair dans un script partagé) :

```
mosquitto_sub -h 10.20.0.10 -p 8883 --cafile ca-ai-regatta.crt \
  -u equipe-fra07 -P "$AIR_PASSWORD" -t 'race/+/clock' -t 'race/current' -v
```

Exemples complets : [exemples/python/abonnement.py](exemples/python/abonnement.py), [exemples/javascript/node-abonnement.mjs](exemples/javascript/node-abonnement.mjs).

## (b) MQTT sur WebSocket — pour les applications web

Un navigateur ne sait pas ouvrir une connexion MQTT classique ; il passe par **WebSocket**, un canal permanent entre la page et le serveur. Le broker accepte MQTT encapsulé dans WebSocket : **ce sont exactement les mêmes sujets et les mêmes messages JSON**, avec les mêmes droits.

- **Adresse** : `wss://10.20.0.10:8884/mqtt`.
- **Bibliothèque** : mqtt.js 5 (`https://unpkg.com/mqtt@5.10.1/dist/mqtt.min.js`), ou toute bibliothèque MQTT qui sait faire du WebSocket.
- **Point d’attention** : le navigateur doit faire confiance au certificat de l’organisation ; installez `ca-ai-regatta.crt` dans le magasin de certificats du système avant la course. Sinon la connexion échoue sans message clair.
- **Quand l’utiliser** : tableau de bord pour l’équipe, écran de chrono, carte maison en JavaScript.

Exemple complet : [exemples/javascript/navigateur.html](exemples/javascript/navigateur.html).

## (c) NMEA 0183 sur TCP — pour les logiciels de navigation

NMEA 0183 est le format texte historique des instruments de bord : une ligne (une « phrase ») par information, qui commence par `$` ou `!` et finit par une somme de contrôle `*hh`. Presque tous les logiciels de navigation savent le lire. Le PC course traduit le flux officiel en phrases NMEA, diffusées sur une connexion **TCP** (connexion réseau simple, sans identification ; lecture seule).

- **Adresse** : `10.20.0.10:10110` (port habituel du NMEA sur TCP). Sans mot de passe sur le réseau équipes (à confirmer).
- **Réglage type** : dans OpenCPN, *Options → Connexions → Ajouter*, protocole *Réseau*, *TCP*, adresse `10.20.0.10`, port `10110`, entrée seulement. Dans qtVlm ou Expedition, une entrée NMEA « TCP client » avec les mêmes paramètres.
- **Quand l’utiliser** : pour voir sans effort la flotte et les bouées sur une carte, ou alimenter un logiciel tactique du commerce. Pas pour le chrono officiel, les événements ou le classement, qui n’existent pas en NMEA standard.

### Ce que contient le flux

| Phrase | Contenu | Cadence |
|---|---|---|
| `!AIVDM` type 18 | Position de **chaque bateau**, présenté comme un bateau AIS de classe B : position de l’**étrave** (`bow_lat`/`bow_lon`, à confirmer), vitesse fond, route fond, cap | À chaque position officielle : 10 Hz par la 4G, 2 Hz par la radio |
| `!AIVDM` type 24 (partie A) | Nom du bateau = son `boat_id` (`FRA-07`) | Toutes les 10 s |
| `!AIVDM` type 21 | Position de **chaque bouée**, présentée comme une aide à la navigation (nom = `mark_id`) | 1 Hz |
| `$WIMWD` | Vent moyen sur le parcours (`mean` de la carte de vent) : direction vraie, vitesse en nœuds et en m/s | 1 Hz |
| `$PAIRW` | Vent mesuré à une bouée équipée : `mark_id`, direction vraie, vitesse, rafale, écart-type de direction, heure UTC (phrase propre à AI Regatta, à confirmer) | 1 Hz par bouée équipée |
| `$PAIRS` | Chrono : `race_id`, étape, heure UTC du départ, date (phrase propre à AI Regatta, à confirmer) | 1 Hz |
| `$GPZDA` | Heure et date UTC du serveur | 1 Hz |

L’AIS (*Automatic Identification System*) est le système de suivi des navires ; ses messages `!AIVDM` sont le moyen standard de montrer **d’autres bateaux** dans un logiciel de navigation. Ici, **aucun signal AIS n’est émis par radio** : les phrases n’existent que sur le réseau équipes.

**Votre propre bateau** apparaît comme les autres, en AIS. Le flux ne contient **pas** de phrase `$GPRMC` ou `$GPGGA` pour votre bateau : le PC course ne diffuse que les positions officielles de tous les bateaux, identiques pour tous. Si votre logiciel a besoin d’un « bateau propre », alimentez-le avec votre propre GPS de bord.

La phrase `$WIMWV` n’est pas diffusée : elle donne un angle de vent **par rapport à l’axe d’un bateau**, ce qui n’a pas de sens pour une bouée ni pour un flux commun à tous. Votre logiciel le calcule à partir de `$WIMWD` et du cap de votre bateau.

### Exemple de flux

```
!AIVDM,1,1,,A,H3IKIuhI86o3L000000000000000,0*6C
!AIVDM,1,1,,A,B3IKIuh08`6k;WV:b0@n0d3UT000,0*1E
!AIVDM,1,1,,A,E>jCuG@ccP00000000000000000@=VLL<ECb000003v010,4*55
$WIMWD,131.0,T,,M,9.9,N,5.1,M*73
$PAIRW,WW,132.5,9.8,12.1,6.2,130407.00*40
$PAIRS,2027-05-14-M3,preparatory,130000.00,14052027*53
$GPZDA,130407.00,14,05,2027,00,00*60
```

Les trois premières lignes donnent : le nom `FRA-07` du MMSI 227990007, sa position (43,106993 N, 5,941678 E, 3,4 nœuds, route 86°, cap 88°), puis la bouée `WW`.

### Correspondance bateaux ↔ MMSI

Le MMSI est le numéro à 9 chiffres qui identifie un navire en AIS. Les numéros ci-dessous sont **fictifs**, réservés à cet usage local ; la table définitive sera publiée avec la liste des inscrits (à confirmer).

| Élément | MMSI | Règle |
|---|---|---|
| Bateaux | `2279900NN` | `NN` = numéro d’ordre attribué à l’inscription, publié dans la table ci-dessous |
| Bouées | `99227990N` | Une valeur par bouée |

| `boat_id` | MMSI | | `mark_id` | MMSI |
|---|---|---|---|---|
| FRA-03 | 227990003 | | WW | 992279901 |
| FRA-07 | 227990007 | | LW1 | 992279902 |
| FRA-12 | 227990012 | | LW2 | 992279903 |
| ITA-05 | 227990021 | | SB | 992279904 |
| MON-01 | 227990031 | | PIN | 992279905 |
| ESP-21 | 227990041 | | FIN1 / FIN2 | 992279906 / 992279907 |

(Table d’exemple, avec les bateaux fictifs du contrat d’interface.)

### Limites du NMEA, à connaître

- **Précision réduite** : l’AIS arrondit la position au 1/10 000 de minute d’arc (≈ 20 cm), la vitesse à 0,1 nœud, la route à 0,1° et le cap au degré. Le MQTT donne le centimètre.
- **Pas d’horodatage précis** : une phrase AIS ne porte que la seconde de la mesure. Pour dater au milliseconde près, utilisez MQTT (`t_gps_ms`).
- **Pas de qualité de position** (`fix`, `stale`) : un bateau perdu cesse simplement d’être mis à jour.
- **10 Hz par bateau** : certains logiciels peinent à afficher autant de messages ; un second port limité à 1 Hz par bateau est envisagé (à confirmer).

Exemple de lecture sans logiciel de navigation : [exemples/nmea/lire-nmea.py](exemples/nmea/lire-nmea.py).

## (d) Pont Signal K — option à décider

**Signal K** est un format ouvert et moderne pour les données de bord (JSON sur WebSocket), utilisé par une partie des outils de navigation libres. Un serveur Signal K pourrait être installé au PC course et alimenté par le flux officiel (§6 de l’architecture).

| Point | Situation |
|---|---|
| Intérêt | Les équipes qui ont déjà des outils Signal K les branchent sans écrire de code |
| Contenu | Autres bateaux dans `vessels.*` (`navigation.position`, `navigation.speedOverGround`, `navigation.courseOverGroundTrue`, `navigation.headingTrue`), vent dans `environment.wind.*` |
| Attention | Signal K utilise les unités du système international : **m/s et radians**, pas nœuds et degrés |
| Adresse envisagée | `ws://10.20.0.10:3000/signalk/v1/stream` (à confirmer) |
| Décision | **À trancher par l’organisation** : proposé si au moins deux équipes le demandent à l’inscription ; sinon, pas de pont Signal K (le NMEA couvre le même besoin) |

## (e) Fichiers de rejeu, simulateur et bac à sable

### Le bac à sable cloud (dès février 2027)

Un broker dans le cloud, **identique à celui du site** (mêmes sujets, mêmes formats, mêmes droits), alimenté en continu par le **simulateur de régate** (S13) : bateaux simulés, vent qui bascule, bouées, procédure de départ, événements, classement. C’est là que vous développez et testez votre logiciel tout l’hiver.

| Service | Adresse |
|---|---|
| MQTT chiffré | `mqtts://bac-a-sable.[domaine à définir]:8883` |
| MQTT sur WebSocket | `wss://bac-a-sable.[domaine à définir]:8884/mqtt` (à confirmer) |
| NMEA sur TCP | `bac-a-sable.[domaine à définir]:10110` (à confirmer) |
| Fichiers de rejeu | `https://bac-a-sable.[domaine à définir]/replays/` (à confirmer) |

- Même identifiant `equipe-<code>`, **mot de passe différent** de celui du site.
- Certificat signé par une autorité publique : pas de fichier `ca-ai-regatta.crt` à installer pour le bac à sable (à confirmer).
- Les manches simulées portent un `race_id` préfixé par `SIM-` (par exemple `SIM-2027-01-20-M4`), pour ne jamais les confondre avec une vraie manche.
- Une manche démarre régulièrement (rythme à confirmer, par exemple toutes les 20 minutes), avec des scénarios variés : bascules, rappel général, changement de parcours, bateau perdu, passage sur la radio de secours, bascule de serveur.
- Un **robot comité** répond à vos messages `outbox` (accusé de réception `receipt`, réponses types), publie des avis de test avec `requires_ack`, et vous permet de tester votre chaîne de bout en bout.
- La latence est celle d’Internet (quelques dizaines de ms), pas celle du câble du site : ne réglez pas vos temporisations fines sur le bac à sable.
- **Piloter un bateau simulé** depuis votre logiciel (envoyer vos ordres tactiques au simulateur) : extension envisagée, à décider par l’organisation.

Le jour J, il suffit de changer l’adresse du broker et le mot de passe : un logiciel qui marche sur le bac à sable doit marcher sur le site sans autre modification (critère de réussite de S13).

### Les fichiers de rejeu

Chaque manche réelle (essais d’avril, régate blanche, puis manches de l’épreuve) et une sélection de manches simulées sont enregistrées et mises à disposition **de toutes les équipes en même temps**, après la manche.

| Format | Contenu | Usage |
|---|---|---|
| **JSON Lines** compressé (`2027-05-14-M3.jsonl.gz`) | Une ligne JSON par message reçu, dans l’ordre : `{"rx_t_gps_ms": …, "topic": "…", "qos": 0, "retain": false, "payload": {…}}`, précédée d’une ligne d’en-tête `{"type": "header", "contract_version": "1.0.0", "race_id": "…"}` | Rejouer exactement le flux dans votre logiciel |
| **Parquet** (`2027-05-14-M3/positions.parquet`, `marks.parquet`, `wind_field.parquet`, `events.parquet`, `leaderboard.parquet`) | Une table par type de message, une colonne par champ du contrat | Analyse avec pandas, Polars, DuckDB, R… |

Parquet est un format de tableau compact, lu directement par les outils d’analyse de données ; JSON Lines est un simple fichier texte avec un message JSON par ligne.

Le simulateur sait aussi **rejouer un fichier sur le bac à sable**, en temps réel ou accéléré : c’est le meilleur moyen de tester votre logiciel sur des données réelles avant l’épreuve. Une version du simulateur à faire tourner sur votre propre ordinateur (par exemple en image Docker) est envisagée, à confirmer : le logiciel de l’organisation n’est pas open source (P33).

Où sont les fichiers sur le site : sur le serveur du PC course, réseau équipes, après chaque manche (adresse à confirmer).
