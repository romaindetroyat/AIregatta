# AI Regatta — Liaisons et logiciel

> Version du 20 novembre 2026. Même contenu que les sections « Liaisons » et « Logiciel » de la présentation interactive (`docs/dispositif.html`).

## Les liaisons

### 1. Positions des bateaux, chemin principal (flux essentiel)

**Balise officielle → Hub cloud, puis PC course** · Données officielles

| | |
|---|---|
| Support physique | 4G LTE Cat-1 (modem SIMCom A7670E), SIM IoT multi-opérateurs |
| Protocole et format | UDP, trame binaire de 48 octets signée (HMAC-SHA256 tronqué), avec numéro de séquence |
| Ce qui circule | Position RTK, vitesse et route fond, cap, gîte, tangage, qualité RTK, précision estimée, batterie, qualité 4G |
| Cadence | 10 Hz |
| Débit | ≈ 0,5 ko/s par balise, ≈ 3 ko/s pour 6 bateaux |
| Latence | 50 à 150 ms ; plusieurs secondes si la 4G sature |
| Sécurité | Clé propre à chaque balise ; trame modifiée ou rejouée rejetée |
| Secours | Radio 868 MHz (liaison suivante) ; tout est aussi enregistré sur la carte SD de la balise |
| Si elle tombe | Le PC course bascule seul sur la radio, à 2 Hz. La précision RTK tient 10 à 60 s environ, puis passe à ≈ 1 m jusqu’au retour de la 4G. |
| Modules logiciels | S1, S4, S5 |

### 2. Positions des bateaux, chemin de secours

**Balise officielle → Antenne du PC course** · Données officielles

| | |
|---|---|
| Support physique | Radio LoRa 868 MHz, sous-bande 869,4–869,65 MHz (500 mW, 10 % du temps) ; module Adafruit RFM95W vers 2 récepteurs identiques au PC course |
| Protocole et format | Trame binaire de 12 octets (LoRa SF7, 250 kHz, ≈ 21 ms) ; chaque balise émet dans son créneau fixe de 30 ms, calé sur l’heure GPS : aucune collision |
| Ce qui circule | Position compacte (écart au centimètre par rapport à un point de référence du plan d’eau), vitesse, route, qualité RTK, batterie |
| Cadence | 2 Hz |
| Débit | ≈ 24 octets/s par bateau ; ≈ 4 % du temps d’émission par bateau |
| Latence | < 1 s |
| Sécurité | Contrôle d’erreur LoRa, sans signature : une trame n’est acceptée que dans le créneau de sa balise, et comparée à la dernière position 4G |
| Secours | 4G (liaison principale) |
| Si elle tombe | Si un récepteur tombe, le second continue. Si les deux tombent, la 4G suffit. |
| Modules logiciels | S1, S3, S5 |

### 3. Positions et vent des bouées

**Bouée au vent (3) et bouées 1 et 2 → PC course** · Données officielles

| | |
|---|---|
| Support physique | Mêmes chemins que les bateaux : 4G et radio 868 MHz |
| Protocole et format | Même trame, avec les champs vent remplis (vitesse, direction vraie, rafale, écart-type) |
| Ce qui circule | Position de la bouée, qui bouge sur son mouillage, et vent mesuré à 2 m, corrigé du mouvement de la bouée |
| Cadence | Position 1 Hz ; vent 1 à 4 Hz, moyenné sur 5 à 10 s |
| Débit | ≈ 0,1 ko/s par bouée |
| Latence | < 1 s |
| Sécurité | Identique aux balises |
| Secours | Radio 868 MHz |
| Si elle tombe | Sans le vent d’une bouée, le moteur vent s’appuie sur l’autre bouée et la station à terre. La position reste gelée à la dernière valeur connue. |
| Modules logiciels | S2, S5, S9 |

### 4. Corrections RTK

**Base RTK, sur le toit de La Plage, au-dessus du PC course → Toutes les balises** · Données officielles

| | |
|---|---|
| Support physique | USB série vers le PC course, tunnel vers le hub cloud, puis 4G vers les balises |
| Protocole et format | RTCM 3 (messages MSM4 et position de la base), diffusé par un caster NTRIP sur le hub ; chaque balise est cliente NTRIP |
| Ce qui circule | Corrections des erreurs GPS communes à toute la zone |
| Cadence | 1 Hz |
| Débit | ≈ 0,3 à 0,6 ko/s vers chaque balise |
| Latence | < 1 s ; les corrections restent valables quelques secondes |
| Sécurité | Accès au caster par identifiant |
| Secours | Réseau public Centipede (caster.centipede.fr, port 2101), directement depuis la balise |
| Si elle tombe | Sans corrections, la précision passe de 2 cm à environ 1 m en 10 à 60 s. Le PC course le sait grâce à la qualité RTK de chaque trame, et l’arbitrage automatique se met en retrait. |
| Modules logiciels | S1, S4 |

### 5. Heure de référence

**Base RTK (heure GPS) → PC course, puis tout le réseau local** · Données officielles

| | |
|---|---|
| Support physique | USB vers le PC course, puis réseau local |
| Protocole et format | chrony calé sur l’heure GPS de la base (impulsion de seconde si la carte la sort, sinon messages GPS, à quelques millisecondes près) ; le PC course donne l’heure (NTP) à tous, équipes comprises. Les balises ont leur propre heure GPS. |
| Ce qui circule | Heure GPS, à quelques millisecondes près au plus |
| Cadence | Continu |
| Débit | Négligeable |
| Latence | — |
| Sécurité | — |
| Secours | Serveurs de temps publics |
| Si elle tombe | Les balises gardent l’heure GPS. Seul l’horodatage côté PC course se dégrade, à la milliseconde près. |
| Modules logiciels | S5 |

### 6. Redistribution à toutes les équipes (flux essentiel)

**PC course → PC à terre de chaque équipe** · Équipes

| | |
|---|---|
| Support physique | Câble Ethernet, même longueur pour toutes les équipes, sur un réseau séparé « équipes » |
| Protocole et format | MQTT : lecture du flux, écriture dans la seule boîte d’envoi (un compte par équipe) ; WebSocket JSON pour les navigateurs ; en option, flux NMEA 0183 (AIS) pour les logiciels de navigation |
| Ce qui circule | Positions de tous les bateaux et des bouées, vent mesuré et carte de vent, état de la course (chrono, séquence), événements (départs, passages, pénalités), classement |
| Cadence | Positions 10 Hz ; vent 1 Hz ; événements à la volée |
| Débit | ≈ 10 à 20 ko/s par équipe |
| Latence | < 50 ms |
| Sécurité | Comptes individuels : lecture du flux, écriture dans la seule boîte d’envoi de l’équipe ; réseau isolé de celui de l’organisation |
| Secours | Borne Wi-Fi de la zone équipes |
| Si elle tombe | Si le serveur principal tombe, le serveur de secours reprend en quelques secondes, à la même adresse. |
| Modules logiciels | S5, S12 |

### 7. Consignes de l’équipe vers son bateau (flux essentiel)

**PC à terre de l’équipe → Son bateau** · Équipes

| | |
|---|---|
| Support physique | Au choix de l’équipe : 4G, radio de télémétrie (433 MHz, ou 868 MHz hors sous-bande réservée), Wi-Fi |
| Protocole et format | Au choix de l’équipe, par exemple MAVLink avec ArduPilot |
| Ce qui circule | Consignes tactiques : vire, empanne, abats (bouée au vent passée), loffe (bouée sous le vent passée), face au vent, mode près, mode portant, mode VMG, mode haut, mode bas |
| Cadence | Libre |
| Débit | Faible |
| Latence | Dépend de l’équipe ; le pilotage fin doit rester à bord |
| Sécurité | Sous la responsabilité de l’équipe |
| Secours | Bateaux d’assistance |
| Si elle tombe | Hors système officiel : le bateau reste suivi et classé par sa balise. Le comportement en cas de perte de liaison est défini par l’équipe. |
| Modules logiciels | aucun (liaison à la charge de l’équipe) |

### 8. Consoles du PC course

**PC course → Direction de course, arbitrage, sécurité, commentateur** · Organisation

| | |
|---|---|
| Support physique | Réseau local de l’organisation, par câble ou Wi-Fi dédié |
| Protocole et format | Application web : WebSocket pour le temps réel, API HTTP pour les actions |
| Ce qui circule | Tout le flux, plus les actions : lancer la séquence, déplacer une bouée, valider une pénalité, signaler un incident |
| Cadence | Temps réel |
| Débit | Faible |
| Latence | < 100 ms |
| Sécurité | Comptes nominatifs, chaque action journalisée |
| Secours | Serveur de secours |
| Si elle tombe | Les consoles se reconnectent seules au serveur de secours. |
| Modules logiciels | S10, S16 |

### 9. Bateaux d’assistance

**PC course → Bateaux d’assistance** · Organisation

| | |
|---|---|
| Support physique | VHF marine pour la voix ; téléphone avec la console sécurité en option |
| Protocole et format | Voix ; page web sécurité (positions, alertes) |
| Ce qui circule | Bateau en difficulté, sortie de zone, balise muette, demande de récupération |
| Cadence | À la demande |
| Débit | — |
| Latence | — |
| Sécurité | — |
| Secours | Téléphone |
| Si elle tombe | La VHF ne dépend d’aucun autre élément du dispositif. |
| Modules logiciels | S10 |

### 10. Station météo

**Station Davis Vantage Pro2 → PC course** · Organisation

| | |
|---|---|
| Support physique | Réseau local (passerelle WeatherLink Live, en Wi-Fi ou câble) |
| Protocole et format | Interface locale de la passerelle WeatherLink Live, lue puis convertie en MQTT |
| Ce qui circule | Vent moyen, rafales, direction, pression, température |
| Cadence | Une lecture toutes les 5 à 10 s |
| Débit | Négligeable |
| Latence | — |
| Sécurité | Réseau local uniquement |
| Secours | Bouées |
| Si elle tombe | Le moteur vent continue avec les bouées seules. |
| Modules logiciels | S5, S9 |

### 11. Vidéo

**Caméras du point haut (12 m) → Régie, commentateur, application** · Organisation

| | |
|---|---|
| Support physique | Câble Ethernet PoE (alimentation et données) |
| Protocole et format | RTSP (H.264 ou H.265) ; ONVIF pour piloter la caméra motorisée ; sortie RTMP ou SRT vers YouTube Live |
| Ce qui circule | Image en direct, orientation de la caméra motorisée pour les incrustations |
| Cadence | 25 à 30 images/s |
| Débit | 4 à 8 Mbit/s par caméra ; ≈ 6 Mbit/s vers Internet |
| Latence | 1 à 3 s en local ; 5 à 20 s sur YouTube |
| Sécurité | Réseau caméras séparé |
| Secours | Enregistrement local |
| Si elle tombe | La course et le suivi continuent ; seule la vidéo est perdue. |
| Modules logiciels | S15 |

### 12. Flux public

**PC course → Hub cloud, puis application publique** · Public et Internet

| | |
|---|---|
| Support physique | Internet par le tunnel, puis un CDN vers les téléphones et ordinateurs |
| Protocole et format | WebSocket JSON, flux agrégé et lissé ; replays en fichiers sur un stockage en ligne |
| Ce qui circule | Positions lissées, classement, écarts, vent, événements, lien vidéo |
| Cadence | 1 à 2 Hz |
| Débit | ≈ 1 à 2 ko/s par spectateur |
| Latence | Différé volontaire de 2 à 5 s |
| Sécurité | Lecture seule, aucun accès au réseau du site |
| Secours | Mode replay si le direct est coupé |
| Si elle tombe | Le public perd le direct ; la course, les équipes et l’arbitrage ne sont pas touchés. |
| Modules logiciels | S4, S14 |

### 13. Tunnel entre le site et le cloud

**Routeur du PC course → Hub cloud** · Public et Internet

| | |
|---|---|
| Support physique | Ligne filaire du site en principal ; 5G du routeur de poche Netgear Nighthawk M6 Pro en secours, branché sur la passerelle UniFi |
| Protocole et format | Tunnel chiffré WireGuard ; à l’intérieur, trames des balises relayées et pont MQTT |
| Ce qui circule | Trames 4G des balises vers le site ; flux public et corrections RTK vers le cloud |
| Cadence | Continu |
| Débit | < 1 Mbit/s hors vidéo |
| Latence | 20 à 50 ms |
| Sécurité | Chiffrement de bout en bout |
| Secours | 5G, bascule automatique en quelques secondes |
| Si elle tombe | Si le filaire et la 5G tombent ensemble, la radio 868 MHz garde le suivi et le flux équipes reste local. |
| Modules logiciels | S4 |

### 14. Contrôle et mise à jour des balises

**Poste de contrôle d’équipement → Balises, à terre** · Organisation

| | |
|---|---|
| Support physique | Wi-Fi ou USB au contrôle ; 4G pour les mises à jour à distance |
| Protocole et format | Outil de recette ; mise à jour du firmware signée |
| Ce qui circule | Test complet, mesure antenne → étrave et hauteur d’antenne, appairage au bateau, batterie, scellé |
| Cadence | Avant chaque journée |
| Débit | — |
| Latence | — |
| Sécurité | Firmware signé ; balise verrouillée pendant la course |
| Secours | Balises de rechange |
| Si elle tombe | Une balise qui échoue au contrôle est remplacée par une balise de rechange. |
| Modules logiciels | S11, S1 |

### 15. Chrono et procédure de départ (flux essentiel)

**Console de direction de course (comité) → Équipes, médias, application publique** · Données officielles

| | |
|---|---|
| Support physique | Réseau local par câble pour les équipes et la régie ; Internet via le hub cloud pour le public |
| Protocole et format | MQTT, message conservé par le broker : heure GPS du départ, étape de la procédure (avertissement à −1:00, préparatoire à −0:40, dernière étape à −0:20, départ), rappels, temps de passage et d’arrivée |
| Ce qui circule | Heure exacte du prochain départ, étape en cours, chrono de course, rappels individuels ou généraux, temps de passage aux bouées, temps d’arrivée |
| Cadence | À chaque changement, plus un rappel chaque seconde |
| Débit | Négligeable |
| Latence | < 1 ms sur place ; chaque écran calcule le compte à rebours sur sa propre horloge, donc le chrono affiché est identique partout à quelques millisecondes près |
| Sécurité | Seule la console du comité peut publier sur ce sujet |
| Secours | Signaux sonores et visuels classiques du comité ; console de secours sur le second serveur |
| Si elle tombe | Si le réseau ralentit, les écrans continuent de compter seuls à partir de l’heure du départ déjà reçue. Si le comité change la procédure, le nouveau message arrive en moins d’une milliseconde sur place. |
| Modules logiciels | S8, S10, S12, S14, S15 |

### 16. Signaux sonores du départ

**Moteur de course (PC course) → Corne de départ, sur la digue** · Organisation

| | |
|---|---|
| Support physique | Réseau local de l’organisation (câble ou Wi-Fi) jusqu’à un relais connecté, puis fil électrique jusqu’à la corne |
| Protocole et format | MQTT : ordre « son court », « son long » ou « deux sons », avec l’heure GPS prévue |
| Ce qui circule | Les signaux de la procédure : avertissement à −1:00, préparatoire à −0:40, dernière étape à −0:20, départ ; rappel individuel ; rappel général |
| Cadence | À chaque étape de la procédure |
| Latence | 10 à 50 ms jusqu’à la corne ; le son met ensuite ≈ 0,4 s pour traverser 150 m |
| Sécurité | Seuls le moteur de course et la console du comité peuvent donner l’ordre |
| Secours | Bouton manuel sur la console, corne à main ; les pavillons restent hissés à la main |
| Si elle tombe | Comme dans les règles de course à la voile, dont notre procédure d’une minute (règle 5.1) adapte la règle 26, les temps sont pris sur les signaux visuels et un signal sonore manquant est ignoré. Les équipes ont de toute façon le chrono GPS exact. |
| Modules logiciels | S8, S10, S17 |

## Les modules logiciels

### S1 — Firmware de la balise

*Embarqué · Indispensable*

- **Besoin** : Produire sur chaque bateau une position officielle fiable et inviolable, 10 fois par seconde, pendant une journée entière.
- **Solution** : ESP32-S3 (ESP-IDF ou Arduino) : lecture des trames UBX du ZED-F9P, fusion avec le BNO085, envoi UDP signé par la 4G, émission radio dans son créneau GPS, client NTRIP, enregistrement complet sur carte SD, mise à jour à distance signée, gestion de l’énergie.
- **But** : Des positions au centimètre, sans trou et sans possibilité de triche.
- **Critère de réussite** : > 99 % des trames reçues ; RTK fixe > 95 % du temps ; 12 h d’autonomie au minimum
- **Entrées → sorties** : GPS, centrale inertielle, corrections RTK → Trames 4G et radio, fichier sur carte SD
- **Dépend de** : Matériel du prototype
- **Charge** : 2 à 3 semaines, surtout de mise au point sur banc et sur l’eau

### S2 — Firmware des bouées

*Embarqué · Indispensable*

- **Besoin** : Mesurer le vent réel sur le parcours malgré le mouvement de la bouée.
- **Solution** : Même base que S1, plus lecture de l’anémomètre Gill WindSonic, correction du roulis, du tangage et de la rotation (compas), moyennes glissantes de 5 à 10 s, surveillance de la batterie.
- **But** : Un vent fiable au vent et sous le vent, envoyé à toutes les équipes.
- **Critère de réussite** : Écart < 5° et < 10 % avec une station de référence, par temps calme
- **Entrées → sorties** : Anémomètre, centrale inertielle, GPS → Trames avec le vent
- **Dépend de** : S1
- **Charge** : 1 semaine, plus le réglage

### S3 — Passerelle radio

*Embarqué · Indispensable*

- **Besoin** : Recevoir le chemin de secours sans dépendre d’Internet.
- **Solution** : Firmware des récepteurs radio (écoute, horodatage) et service sur le PC course qui décode, vérifie et publie dans le bus ; suppression des doublons avec la 4G grâce au numéro de séquence.
- **But** : Le suivi continue si la 4G sature.
- **Critère de réussite** : Bascule sans perte visible au PC course
- **Entrées → sorties** : Trames radio → Positions dans le bus de données
- **Dépend de** : S1, S5
- **Charge** : 3 à 5 jours

### S4 — Hub cloud

*Infrastructure · Indispensable*

- **Besoin** : Recevoir les balises en 4G, diffuser les corrections RTK et servir le public sans charger la connexion du site.
- **Solution** : Serveur virtuel : récepteur UDP qui vérifie les signatures, tunnel WireGuard vers le site, caster NTRIP (RTKLIB str2str ou SNIP), relais WebSocket derrière un CDN (Cloudflare), stockage des replays.
- **But** : Un point d’entrée unique, sûr, dimensionné pour des milliers de spectateurs.
- **Critère de réussite** : Test de charge à 5 000 connexions ; reprise automatique après redémarrage
- **Entrées → sorties** : Trames 4G, flux RTK, flux public → Trames vers le site, corrections vers les balises, direct vers le public
- **Dépend de** : —
- **Charge** : 1 semaine

### S5 — Bus de données et modèle

*Infrastructure · Indispensable*

- **Besoin** : Que tous les modules parlent le même langage, à la même heure.
- **Solution** : Broker MQTT (Mosquitto) sur le PC course, schémas JSON versionnés, fusion 4G et radio, horodatage GPS, droits d’accès par compte.
- **But** : Une seule source de vérité, horodatée et rejouable.
- **Critère de réussite** : Latence interne < 10 ms ; aucun doublon
- **Entrées → sorties** : Tous les flux → Tous les flux, normalisés
- **Dépend de** : —
- **Charge** : 3 à 5 jours

### S6 — Enregistreur (boîte noire)

*Infrastructure · Indispensable*

- **Besoin** : Pouvoir tout rejouer : réclamation, analyse, replay public, tests.
- **Solution** : Enregistrement de toutes les trames brutes et des événements, base temporelle (TimescaleDB ou fichiers Parquet), export par manche.
- **But** : Aucune donnée perdue ; chaque décision justifiable.
- **Critère de réussite** : Le rejeu d’une manche donne exactement le même résultat
- **Entrées → sorties** : Bus de données → Archives, fichiers de replay
- **Dépend de** : S5
- **Charge** : 3 jours

### S7 — Supervision

*Infrastructure · Important*

- **Besoin** : Voir d’un coup d’œil si tout le dispositif est sain.
- **Solution** : Tableau de santé : batterie, qualité RTK, chemin utilisé, latence, dernière trame de chaque balise, état des récepteurs radio, du tunnel et des serveurs ; alertes sonores.
- **But** : Détecter un problème avant qu’il touche la course.
- **Critère de réussite** : Alerte moins de 5 s après la perte d’une balise
- **Entrées → sorties** : Bus de données, état des machines → Écran et alertes
- **Dépend de** : S5
- **Charge** : 3 à 5 jours

### S8 — Moteur de course

*PC course · Indispensable*

- **Besoin** : Faire tourner la course sans erreur : départ, passages de bouées, arrivée, classement.
- **Solution** : Machine à états par bateau : séquence de départ calée sur l’heure GPS, départs anticipés, passages de bouées dans le bon sens, entrée en zone, limites du parcours, arrivée, classement provisoire puis définitif. Position de l’étrave calculée depuis l’antenne (distance mesurée au contrôle, cap, gîte).
- **But** : Un classement juste et immédiat, expliqué événement par événement.
- **Critère de réussite** : Concordance totale avec un jugement humain sur les manches d’essai
- **Entrées → sorties** : Positions, parcours, règles → Événements, classement
- **Dépend de** : S5, règles de course
- **Charge** : 2 à 3 semaines

### S9 — Moteur vent

*PC course · Important*

- **Besoin** : Donner aux équipes et au public une lecture claire du vent sur le parcours.
- **Solution** : Fusion des bouées et de la station à terre : vent moyen, rafales, bascules, différence entre la gauche et la droite du parcours ; tendance à 5–15 min par des méthodes statistiques simples, avec un niveau de confiance.
- **But** : Les mêmes données de vent, propres, pour toutes les équipes.
- **Critère de réussite** : Données publiées chaque seconde ; tendance jugée utile par les équipes à la régate blanche
- **Entrées → sorties** : Vent des bouées et de la station → Vent consolidé, tendance
- **Dépend de** : S2, S5
- **Charge** : 1 à 2 semaines

### S10 — Consoles du PC course

*PC course · Indispensable*

- **Besoin** : Piloter la course et la sécurité depuis la terre.
- **Solution** : Application web : direction de course (parcours, séquence, bouées déplacées, rappels), arbitrage (alertes automatiques, rejeu instantané, décision), sécurité (santé des balises, sorties de zone, positions pour les bateaux d’assistance).
- **But** : Une décision prise en quelques secondes, et tracée.
- **Critère de réussite** : Chaque action journalisée ; prise en main en 30 min par un arbitre
- **Entrées → sorties** : Bus de données, enregistreur → Actions de course, décisions
- **Dépend de** : S5, S6, S8
- **Charge** : 2 semaines

### S11 — Contrôle d’équipement

*PC course · Important*

- **Besoin** : Garantir que chaque balise fonctionne et est bien installée avant la course.
- **Solution** : Outil de recette : test complet de la balise, appairage au bateau, mesure antenne → étrave et hauteur d’antenne, vérification du scellé, liste de contrôle.
- **But** : Aucune balise défaillante au départ.
- **Critère de réussite** : Recette d’un bateau en moins de 10 min
- **Entrées → sorties** : Balise, mesures → Fiche de contrôle par bateau
- **Dépend de** : S1
- **Charge** : 3 à 5 jours

### S12 — Flux équipes et documentation

*Équipes · Indispensable*

- **Besoin** : Que chaque équipe puisse développer son logiciel tactique dès l’hiver.
- **Solution** : Contrat d’interface publié (sujets MQTT, formats JSON, unités, cadences), documentation, exemples en Python et JavaScript, flux NMEA en option. Gel le 15 mars.
- **But** : Toutes les équipes branchées le jour J, à égalité.
- **Critère de réussite** : Au moins 3 équipes connectées au simulateur en février
- **Entrées → sorties** : Bus de données → Flux en lecture, plus la boîte d’envoi de chaque équipe
- **Dépend de** : S5
- **Charge** : 1 semaine

### S13 — Simulateur de régate

*Équipes · Indispensable*

- **Besoin** : Développer et tester sans bateau ni plan d’eau, pour l’organisation comme pour les équipes.
- **Solution** : Générateur de régates (bateaux, vent qui bascule, bouées) et rejeu des enregistrements, avec le même protocole que le vrai système.
- **But** : Tout le logiciel testé avant le premier essai sur l’eau.
- **Critère de réussite** : Un logiciel d’équipe passe du simulateur au réel sans modification
- **Entrées → sorties** : Scénarios, enregistrements → Flux identique au vrai
- **Dépend de** : S5
- **Charge** : 1 semaine

### S14 — Application publique (PWA)

*Public · Indispensable*

- **Besoin** : Faire vivre la course au public, sur place et en ligne.
- **Solution** : PWA installable sur iPhone et ordinateur : carte en direct (MapLibre), classement, écarts, vent, vidéo, replay ; légère pour passer sur une 4G chargée.
- **But** : Comprendre la course d’un coup d’œil, sur la plage comme à la maison.
- **Critère de réussite** : Chargement < 2 s ; moins de 2 ko/s en direct
- **Entrées → sorties** : Flux public → Application
- **Dépend de** : S4
- **Charge** : 1 à 2 semaines

### S15 — Vidéo et incrustations

*Public · Important*

- **Besoin** : Une image façon SailGP pour le commentateur et l’application.
- **Solution** : Incrustations générées depuis les données (noms, classement, chrono) dans OBS ; en option, incrustations calées sur l’image (ligne de départ, laylines) grâce à l’orientation de la caméra motorisée.
- **But** : Une diffusion lisible et spectaculaire.
- **Critère de réussite** : Incrustations à jour à moins d’une seconde près
- **Entrées → sorties** : Vidéo, bus de données → Flux vidéo habillé
- **Dépend de** : S5
- **Charge** : 1 semaine ; option calée sur l’image : 1 à 2 de plus

### S16 — Aide au commentateur

*Public · Bonus*

- **Besoin** : Aider le commentateur humain à ne rien manquer.
- **Solution** : Écran souffleur : moments forts détectés (croisement serré, changement de leader, bascule), fiches équipes, statistiques ; résumé automatique de chaque manche.
- **But** : Un commentaire plus riche, sans remplacer le commentateur.
- **Critère de réussite** : Jugé utile par le commentateur à la régate blanche
- **Entrées → sorties** : Événements, vent → Écran souffleur, résumés
- **Dépend de** : S8, S9
- **Charge** : 3 à 5 jours

### S17 — Signaux de départ automatiques

*PC course · Important*

- **Besoin** : Donner les signaux sonores à l’heure exacte, sans erreur humaine, parfaitement calés sur le chrono reçu par les équipes.
- **Solution** : Le moteur de course envoie, à l’heure GPS prévue, un ordre MQTT à un relais connecté qui actionne la corne : un son à l’avertissement, au préparatoire et au départ, un son long à une minute, un son pour un rappel individuel, deux pour un rappel général. Bouton manuel et corne à main en secours ; les pavillons restent hissés à la main.
- **But** : Une procédure de départ sonore, juste et identique à chaque manche.
- **Critère de réussite** : Son déclenché à moins de 50 ms de l’heure prévue, sur 100 essais consécutifs ; test de la corne chaque matin
- **Dépend de** : S8, S10
- **Charge** : 2 à 3 jours

## Méthode (IA agentique)

1. Une spécification par module dans le dépôt : besoin, entrées, sorties, critère de réussite.
2. Le simulateur d’abord : tout le logiciel tourne sur des régates simulées avant le premier essai sur l’eau.
3. Des tests sur données réelles : chaque essai enregistré devient un test automatique.
4. Une revue humaine sur tout ce qui touche au classement, à l’arbitrage et à la sécurité.
5. Un essai sur l’eau toutes les 2 à 3 semaines : c’est lui qui donne le rythme.

Charge totale pilotée : ≈ 15 à 20 semaines, soit 2 à 3 mois à deux personnes, essais compris.
