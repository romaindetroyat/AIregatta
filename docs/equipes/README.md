# Kit équipes : ce que l’organisation vous fournit

> AI Regatta — Anse du Mourillon, Toulon, du 12 au 16 mai 2027.
> Version 1.0-draft du 20 novembre 2026. Tout ce qui est marqué « à confirmer » peut encore changer.

## Le principe en une phrase

**Toutes les équipes reçoivent les mêmes données, au même instant, dans le même format** (P11) : la position officielle de tous les bateaux, la position des bouées, le vent mesuré et la carte de vent, le chrono, les événements, le classement et les avis du comité. À vous d’en faire la meilleure tactique.

## Ce que vous recevez

| Donnée | D’où elle vient | Cadence |
|---|---|---|
| Position de **tous** les bateaux, le vôtre compris (position de l’antenne et de l’étrave, vitesse, route, cap, gîte) | Balise officielle scellée dans chaque bateau (P08) | 10 par seconde (2 en secours radio) |
| Position des bouées | Balises des bouées | 1 par seconde |
| Vent mesuré aux bouées | Anémomètre sur la bouée au vent, et sous le vent en option (P20) | 1 par seconde |
| Carte de vent (mailles de 20 m) et tendance à 5–15 min | Moteur vent du PC course (S9) | 1 par seconde ; tendance toutes les 10 s |
| Chrono officiel : heure GPS exacte du départ, étape de la procédure | Comité, console de direction de course (P17) | À chaque changement + chaque seconde |
| Parcours : bouées, portes, lignes, ordre des bords, côté où laisser les bouées, limites | Comité | À chaque changement |
| Événements : signaux de départ, départ anticipé, passages de bouée, pénalités, arrivées… | Moteur de course (S8) et comité | À la volée |
| Pavillons envoyés, classement live, avis officiels | Comité et moteur de course | À chaque changement |
| Messages du comité à votre seule équipe, et canal pour lui répondre | Comité | À la volée |
| Heure de référence (serveur NTP + balise de temps) | Base RTK et serveur du PC course | En continu |

## Par quels moyens

| Connecteur | Pour quoi faire | Document |
|---|---|---|
| **MQTT** (recommandé) | Votre logiciel tactique ; seul moyen d’écrire au comité | [contrat-interface.md](contrat-interface.md) |
| MQTT sur **WebSocket** | Une application dans un navigateur | [connecteurs.md](connecteurs.md#b-mqtt-sur-websocket--pour-les-applications-web) |
| **NMEA 0183** sur TCP | Brancher OpenCPN, qtVlm, Expedition… | [connecteurs.md](connecteurs.md#c-nmea-0183-sur-tcp--pour-les-logiciels-de-navigation) |
| Pont **Signal K** | Option, à décider | [connecteurs.md](connecteurs.md#d-pont-signal-k--option-à-décider) |
| **Bac à sable** cloud, **simulateur**, **fichiers de rejeu** | Développer et tester tout l’hiver | [connecteurs.md](connecteurs.md#e-fichiers-de-rejeu-simulateur-et-bac-à-sable) |

Sur le site, chaque équipe a une **prise Ethernet** dans la zone équipes : câbles de même longueur pour tous, réseau isolé, borne Wi-Fi en secours. Un compte par équipe (`equipe-<code>`), en lecture seule sur les données de course.

## Le contenu du kit

| Document | Contenu |
|---|---|
| [contrat-interface.md](contrat-interface.md) | Le contrat d’interface : conventions, connexion, tous les sujets MQTT avec leurs champs et un exemple, horloge, pannes, versions |
| [connecteurs.md](connecteurs.md) | Les connecteurs proposés et quand utiliser chacun |
| [liaison-bateau.md](liaison-bateau.md) | Communiquer avec votre bateau : fréquences, puissances, architecture conseillée, ordres tactiques, points à trancher |
| [regles-equite-et-faq.md](regles-equite-et-faq.md) | Règles d’équité, liste de contrôle avant le jour J, questions fréquentes |
| [schemas/](schemas/) | Les schémas JSON (JSON Schema 2020-12) de chaque type de message |
| [exemples/](exemples/) | Code prêt à lancer en Python, JavaScript (navigateur et Node.js) et NMEA |

## Le calendrier

| Date | Étape |
|---|---|
| Novembre 2026 | Publication de ce kit en version 1.0-draft |
| **Janvier 2027** | **Ouverture du bac à sable cloud** : broker identique à celui du site, alimenté par le simulateur ; comptes équipes distribués |
| Février 2027 | Objectif : au moins 3 équipes connectées au simulateur (critère de réussite de S12) |
| **15 mars 2027** | **Gel du contrat d’interface** (version `1.0.0`) ; ensuite, seulement des ajouts compatibles annoncés 30 jours à l’avance |
| **Avril 2027** | **Régate blanche et essais sur l’eau** : premières données réelles, publiées en fichiers de rejeu |
| [date à définir] | Date limite d’inscription et de déclaration des fréquences |
| [date à définir], avant la première manche | Contrôle des bateaux, pose des balises, test de connexion sur le site |
| **12 mai 2027** | **Jour J** : première journée de course (l’épreuve dure jusqu’au 16 mai, sans jour de réserve) |

## Ce qui est de votre responsabilité

- **Votre logiciel** : réception du flux, tactique, affichage, envoi de vos messages au comité. L’organisation fournit le flux, la documentation et des exemples, **pas d’assistant tactique** (P12).
- **Votre liaison avec votre bateau** (P10, P36) : matériel, protocole, fiabilité, dans le respect du plan de fréquences, avec des émetteurs déclarés à l’inscription.
- **Votre bateau** : architecture libre (P07), autopilote, capteurs, et comportement en cas de perte de liaison, déclaré à l’avance.
- **Votre tactique** : c’est le cœur de l’épreuve.
- **L’heure de vos PC** : synchronisée sur le serveur de temps du site (écart < 5 ms, P26).

L’organisation, elle, fournit et pose la **balise officielle** (scellée, sans lien avec votre électronique, P09), fait tourner le PC course et le comité, et assure la sécurité sur l’eau avec des bateaux d’assistance (P16).

## Les règles d’équité, en bref

Même câble, même broker, mêmes données au même instant ; lecture seule ; aucun accès aux données internes de l’organisation ; une seule source de position officielle ; pas d’autre source de données sur l’eau que les capteurs de votre bateau (à confirmer) ; réponses du comité utiles à tous publiées à tous. Le détail est dans [regles-equite-et-faq.md](regles-equite-et-faq.md).

## Contact

Questions techniques sur le flux : [adresse à définir]. Pendant l’épreuve : message `question` dans votre `outbox`, ou directement au PC course.
