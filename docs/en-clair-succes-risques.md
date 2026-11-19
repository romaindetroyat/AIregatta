# AI Regatta — Le projet en clair, succès et risques

## Le principe en 5 étapes

1. **Mesurer** — Chaque bateau porte une balise officielle qui mesure sa position au centimètre près, 10 fois par seconde.
2. **Envoyer** — La balise envoie cette position au PC course par la 4G. Une radio privée prend le relais si la 4G flanche.
3. **Le vent** — Les bouées font pareil, et mesurent en plus le vent sur le parcours.
4. **Redistribuer** — Le PC course rassemble tout, fait tourner la course (départ, bouées, arrivée, classement) et renvoie le tout à toutes les équipes au même instant.
5. **Décider et montrer** — Chaque équipe décide de sa tactique et envoie ses consignes à son bateau. Le public suit sur l’application et sur la vidéo.

## Nos choix techniques

### Qui mesure la position des bateaux ?

**Une balise officielle, identique dans chaque bateau.**

- Pourquoi : Toutes les équipes ont la même précision, personne ne peut tricher, et un bateau dont l’électronique tombe en panne reste suivi et classé.
- Écarté : Laisser chaque équipe envoyer la position de son propre GPS : précision inégale et invérifiable.

### Quelle précision ?

**Le RTK, au centimètre.**

- Pourquoi : Un GPS ordinaire se trompe de 1 à 3 m, soit la longueur d’un bateau. Au départ, il faut savoir au centimètre qui a franchi la ligne trop tôt.
- Écarté : Un GPS ordinaire, dix fois moins cher mais inutilisable pour l’arbitrage.

### Comment transmettre ?

**La 4G, doublée d’une radio privée.**

- Pourquoi : La 4G est simple et rapide. Mais la foule peut la saturer : la radio privée, elle, ne dépend de personne.
- Écarté : Une radio privée seule : plus de travail de développement, et pas de corrections RTK par ce chemin.

### Où faire tourner la course ?

**Sur des ordinateurs installés au PC course.**

- Pourquoi : Si Internet tombe, la course continue. Un second ordinateur est prêt à prendre le relais.
- Écarté : Tout dans le cloud : une coupure d’Internet arrêterait la régate.

### Comment informer les équipes ?

**Par câble, sur place.**

- Pourquoi : Même délai pour tout le monde, au centième de seconde, et sans dépendre de la 4G.
- Écarté : La 4G ou le Wi-Fi : délais variables d’une équipe à l’autre.

### Comment servir le public ?

**Par un serveur sur Internet (le hub cloud).**

- Pourquoi : Les milliers de spectateurs ne chargent pas la connexion du site.
- Écarté : Servir le public depuis le site : la ligne saturerait.

### Comment relier les logiciels entre eux ?

**Un bus de données MQTT.**

- Pourquoi : C’est le standard des objets connectés : chaque programme s’abonne seulement aux informations dont il a besoin. Les équipes le connaissent.
- Écarté : Des liaisons sur mesure entre chaque logiciel : fragile et long à faire.

### Où placer le poids ?

**En bas : le boîtier au fond, seules les antennes montent.**

- Pourquoi : La stabilité du bateau est préservée. Les antennes, légères, restent dans l’axe et au-dessus de la flottaison.
- Écarté : Tout en tête de mât : meilleure réception GPS, mais du poids en hauteur.

### Quel matériel ?

**Uniquement des références bien notées, ou validées au banc quand il n’existe pas d’avis.**

- Pourquoi : Le jour J, on ne fait pas d’expérience sur le matériel.
- Écarté : Les modules les moins chers, sans retour d’expérience.

### Comment développer ?

**Avec de l’IA agentique, encadrée par des spécifications et des tests.**

- Pourquoi : Le code s’écrit vite. Le vrai rythme est donné par les essais sur l’eau.
- Écarté : Un développement classique, plus long et plus cher.

## Les clés du succès

1. **Une balise fiable avant tout** — Tout repose sur elle. Prototype sur l’eau dès janvier, puis chaque balise testée avant chaque journée.
2. **Des essais sur l’eau réguliers** — Un essai toutes les 2 à 3 semaines, avec de vrais bateaux. C’est là qu’on découvre les vrais problèmes.
3. **Le format des données figé tôt** — Publié en décembre avec un simulateur, figé le 15 mars. Les équipes arrivent prêtes.
4. **Une installation à bord contrôlée** — Antennes dans l’axe et au-dessus de la flottaison, distance antenne → étrave mesurée, scellé posé. Contrôle d’équipement rigoureux.
5. **Toujours un plan B** — 4G et radio, deux ordinateurs, batterie de secours, balises de rechange, Internet filaire et 5G.
6. **Un plan de fréquences respecté** — Chaque équipe déclare ses radios. Un analyseur vérifie chaque matin que personne ne brouille.
7. **Des décisions humaines** — Le logiciel détecte et propose ; l’arbitre décide. Tout est enregistré pour pouvoir rejouer.
8. **Un responsable technique le jour J** — Une personne qui décide, une liste de contrôle, et une deuxième personne formée pour la remplacer.
9. **Une régate blanche complète** — Mi-avril, avec les équipes et le public sur la plage, pour tout tester en conditions réelles.
10. **Un vent mesuré proprement** — Les bouées bien réglées et comparées à la station à terre. C’est la donnée la plus attendue par les équipes.

## Ce qui peut foirer

| Risque | Probabilité | Gravité | Signal d’alerte | Parade |
|---|---|---|---|---|
| Une antenne mal placée | moyenne | forte | Bateau qui « saute » ou disparaît à la gîte ; précision RTK qui chute. | Contrôle d’équipement : antennes dans l’axe, au-dessus de la flottaison, rien de carbone au-dessus. |
| Une balise qui s’éteint en course | moyenne | forte | Plus aucune trame d’un bateau, sur les deux chemins. | 20 h d’autonomie pour 8 h de course, charge vérifiée le matin, balises de rechange, enregistrement sur carte SD. |
| De l’eau dans le boîtier | moyenne | forte | Coupures aléatoires, puis panne. | Boîtier étanche testé en immersion, sachet déshydratant, contrôle à chaque retour à terre. |
| Une erreur du moteur de course | moyenne | forte | Un départ anticipé ou un passage de bouée mal détecté, classement contesté. | Tests sur toutes les manches enregistrées, décision humaine, rejeu possible grâce à la boîte noire. |
| Pas de vent, ou trop, sans jour de réserve | moyenne | forte | Manches annulées sur cinq jours sans rattrapage. | Format court et souple, plusieurs manches par jour, programme de repli pour le public (replays, démonstrations). |
| Du code écrit par les agents mal vérifié | moyenne | forte | Erreurs discrètes qui apparaissent le jour J. | Spécifications précises, tests automatiques sur données réelles, revue humaine de tout ce qui touche au classement. |
| Tout repose sur une seule personne | moyenne | forte | Blocage si elle est absente ou débordée. | Documentation à jour dans le dépôt, deux personnes formées sur chaque poste. |
| La 4G saturée par la foule | moyenne | moyenne | Latence qui grimpe, trames 4G qui manquent au PC course. | La radio privée prend le relais seule ; SIM d’un autre opérateur ; essai un week-end de plage pleine en avril. |
| Des radios d’équipes qui brouillent | moyenne | moyenne | Trames radio perdues, consignes d’équipes perturbées. | Plan de fréquences imposé, contrôle à l’analyseur chaque matin, sous-bande réservée à l’organisation. |
| Un changement tardif du format de données | moyenne | moyenne | Logiciels d’équipes cassés à quelques jours de la course. | Format figé le 15 mars ; ensuite, seuls des ajouts compatibles. |
| Des équipes pas prêtes | moyenne | moyenne | Bateaux ou logiciels qui ne fonctionnent pas le jour J. | Simulateur dès décembre, accompagnement, régate blanche obligatoire. |
| Une panne de courant ou d’Internet au PC course | faible | forte | Écrans noirs, plus de direct public. | Batterie de secours, 5G en relais, radio privée, flux équipes local. |
| Un vent faussé par le mouvement des bouées | moyenne | moyenne | Directions qui oscillent, vitesses incohérentes. | Espar lesté, correction par la centrale inertielle, comparaison avec la station à terre. |
| Une mauvaise heure sur une machine | faible | forte | Départs anticipés détectés à tort. | Heure GPS partout, vérification automatique de l’heure de chaque machine. |
| Le GPS perturbé par les murs du fort ou de la digue | faible | moyenne | Précision qui se dégrade près des obstacles (multi-trajets). | Parcours tracé à distance des murs ; qualité RTK surveillée en direct. |
| Du matériel livré en retard | faible | moyenne | Prototype ou série décalés de plusieurs semaines. | Commande du prototype dès maintenant, série en février, stock de pièces de rechange. |
| L’application publique qui rame | faible | faible | Carte figée sur les téléphones des spectateurs. | Serveur cloud et CDN, version légère, test de charge. |

## Glossaire

- **4G** : Réseau des téléphones mobiles. La balise s’en sert comme un téléphone pour envoyer ses positions.
- **5G** : Génération suivante du réseau mobile, plus rapide. Sert ici de secours à la ligne Internet du site.
- **868 MHz** : Bande de fréquences radio libre d’usage en Europe, avec des règles de puissance et de temps d’émission.
- **API** : Porte d’entrée documentée qui permet à un logiciel de recevoir ou d’envoyer des données à un autre.
- **ArduPilot** : Pilote automatique libre pour drones, qui sait piloter un voilier (virements, points de passage).
- **balise** : Petit boîtier officiel fixé dans chaque bateau. Il mesure la position et l’envoie au PC course.
- **broker** : Le serveur central de MQTT, qui reçoit tous les messages et les redistribue aux abonnés.
- **caster** : Serveur qui distribue les corrections RTK aux récepteurs qui les demandent.
- **CDN** : Réseau de serveurs répartis dans le monde qui distribue un site à des milliers de personnes sans saturer.
- **centrale inertielle** : Capteur qui mesure les rotations et l’inclinaison : gîte, tangage, virements.
- **débit** : Quantité de données transmise par seconde.
- **départs anticipés** : Bateau qui franchit la ligne de départ avant le signal. On dit aussi « OCS ».
- **ESP32-S3** : Petit processeur très répandu, peu cher et économe, qui fait tourner le firmware de la balise.
- **firmware** : Le programme qui tourne à l’intérieur d’un appareil électronique, comme la balise.
- **flottaison** : La ligne où la coque rencontre l’eau.
- **GPS** : Système de positionnement par satellites. On l’emploie ici au sens large : GPS américain, Galileo européen et les autres constellations.
- **gîte** : L’inclinaison du bateau sur le côté, sous l’effet du vent.
- **HMAC** : Signature numérique : prouve qu’un message vient bien de la balise et n’a pas été modifié.
- **hub cloud** : Notre serveur sur Internet : il reçoit les balises en 4G et diffuse le direct au public.
- **Hz** : Hertz : nombre de fois par seconde. 10 Hz = 10 positions par seconde.
- **IA agentique** : Des assistants d’IA qui écrivent et testent du code de façon autonome, sous la conduite d’une personne.
- **JSON** : Format de texte simple et lisible pour échanger des données entre logiciels.
- **latence** : Délai entre le moment où une information part et celui où elle arrive.
- **laylines** : Lignes idéales pour atteindre une bouée au près sans virer de bord une fois de plus.
- **LoRa** : Technique radio à longue portée et faible débit, très économe en énergie. Sert ici de radio de secours.
- **MAVLink** : Langage de commande des drones, utilisé notamment par ArduPilot.
- **MQTT** : Langage commun des objets connectés. Chaque programme publie ses informations sur des « sujets » et s’abonne à ceux qui l’intéressent.
- **multi-trajets** : Quand le signal GPS rebondit sur un mur ou sur l’eau avant d’arriver : la position devient moins précise.
- **NMEA** : Format standard des instruments de navigation (GPS, vent, AIS). Compris par la plupart des logiciels de navigation.
- **NTP** : Protocole qui met tous les ordinateurs d’un réseau à la même heure.
- **NTRIP** : Protocole qui transporte les corrections RTK par Internet.
- **onduleur** : Batterie qui prend le relais instantanément en cas de coupure de courant.
- **ONVIF** : Norme qui permet de piloter les caméras de surveillance de toutes marques et de connaître leur orientation.
- **passe-coque** : Pièce étanche qui permet de faire passer un câble à travers la coque ou le pont.
- **PC course** : Le poste de commandement à terre : ordinateurs, écrans et personnes qui font tourner la régate.
- **plan de fréquences** : Le tableau qui dit quelle équipe a le droit d’émettre sur quelle fréquence, pour que personne ne se brouille.
- **PoE** : Power over Ethernet : un seul câble réseau transporte les données et l’alimentation électrique.
- **PPS** : Pulse Per Second : une impulsion électrique envoyée par le GPS à chaque seconde exacte. Sert à régler les horloges.
- **PWA** : Progressive Web App : un site web qui s’installe sur l’iPhone ou l’ordinateur comme une application, sans passer par l’App Store.
- **RTCM** : Format standard des corrections RTK.
- **RTK** : Real Time Kinematic. Technique qui corrige le GPS grâce à une station fixe à terre. Précision : 2 à 5 cm au lieu de 1 à 3 m.
- **RTSP** : Protocole standard pour transmettre la vidéo d’une caméra sur un réseau.
- **SailGP** : Circuit international de régates en catamarans volants, réputé pour sa diffusion très riche en données.
- **secours chaud** : Machine de secours allumée en permanence, prête à prendre le relais en quelques secondes.
- **SIM IoT** : Carte SIM prévue pour les objets connectés, avec des petits forfaits de données.
- **simulateur** : Programme qui fabrique des régates virtuelles, avec les mêmes données que les vraies, pour développer et tester sans bateau.
- **tunnel** : Liaison chiffrée et privée entre deux machines, à travers Internet.
- **UDP** : Manière d’envoyer des petits paquets sur Internet sans attendre d’accusé de réception. Rapide, idéal pour des positions qui se renouvellent sans cesse.
- **VHF** : La radio maritime classique, pour parler entre bateaux et avec la terre.
- **WebSocket** : Connexion permanente entre un navigateur et un serveur, pour recevoir des données en direct.
- **WireGuard** : Logiciel qui crée un tunnel chiffré entre deux machines par Internet.

## Mosquitto, le cœur du système

Mosquitto est un logiciel libre et gratuit de la fondation Eclipse. Il joue le rôle de « broker » MQTT : le standard central par lequel passent toutes les données. Il tourne sur l’ordinateur du PC course ; les balises (via leurs récepteurs), les bouées, le moteur de course et le chrono y déposent leurs informations, et les équipes, le comité, la régie et le hub cloud s’y abonnent. Il renvoie chaque information au même instant à tous ses abonnés, garde en mémoire le dernier état (chrono, parcours), refuse tout accès anonyme et applique une liste de droits (les équipes lisent seulement). Un second ordinateur est prêt à reprendre à la même adresse. Volume prévu : ≈ 1 500 messages par seconde, très en dessous de ses capacités.

## Quelles chances de réussite ?

Estimation de jugement, pas un calcul :

- **≈ 85 %** : la régate se déroule avec des données justes pour tous, malgré de petits incidents, si le plan d’essais est suivi (prototype sur l’eau en janvier, régate blanche mi-avril, contrôle quotidien, radio de secours, format figé le 15 mars, deux personnes formées). Sans ces mesures : ≈ 35–40 %.
- **≈ 25 %** : aucun incident visible pendant les cinq jours.
- **≈ 0 %** : « parfait ». Aucun événement en direct ne l’est.

Les briques prises une à une sont éprouvées ; ce qui échoue sur ce genre d’événement, c’est l’assemblage non testé, l’eau, les batteries, les antennes mal placées et le manque de temps sur l’eau.
