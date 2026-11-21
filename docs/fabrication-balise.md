# AI Regatta — Manuel de fabrication de la balise officielle

> Pour la personne en charge de la technique et son suppléant. Ce manuel suit la chaîne matérielle contrôlée (voir `chaine-materiel.md`) : les branchements corrigés y sont appliqués. Ce qui reste à vérifier au prototype est signalé.

| À fabriquer | Coût par balise | Masse visée | Autonomie | Temps de montage |
|---|---|---|---|---|
| **16** — 10 bateaux, 4 bouées, 2 de rechange | **≈ 455 €** — pièces seules | **≤ 250 g** — boîtier ≈ 170 g + antennes | **≈ 20 h** — 2 accus, ≈ 25 Wh | **≈ 4 h** — par balise, essais compris |

## 1. Ce qu’on fabrique

Un boîtier étanche, scellé, avec ses accus, qui donne la position officielle du bateau ou de la bouée au centimètre, 10 fois par seconde. Il envoie par la 4G, garde une radio de secours, enregistre tout sur carte microSD, et n’a aucun lien avec l’électronique de l’équipe.

## 2. Les pièces, pour une balise

| Qté | Pièce | Référence | Rôle | Prix |
|---|---|---|---|---|
| | **Électronique** | | | |
| 1 | Récepteur GPS RTK | ArduSimple simpleRTK2B Lite (puce u-blox ZED-F9P) | La position au centimètre, 10 fois par seconde | 199 € |
| 1 | Antenne GPS | u-blox ANN-MB-00, avec un disque métallique de 10 cm dessous | Deux fréquences, étanche, connecteur SMA | 60 € |
| 1 | Carte calcul et 4G | ESP32-S3 + modem SIMCom A7670E (Waveshare ou LilyGO : choisie au prototype) | Le cerveau de la balise, l’envoi en 4G, la carte microSD | 49 € |
| 1 | Radio de secours | Adafruit RFM95W 868 MHz | Positions de secours si la 4G tombe | 21 € |
| 1 | Centrale inertielle | Adafruit BNO085 | Cap, gîte et tangage | 30 € |
| | **Boîtier, énergie et petites pièces** | | | |
| 1 | Boîtier étanche IP67 | Couvercle transparent (gamme Hammond 1554 ou équivalent), ≈ 120 × 65 × 40 mm, à valider avec les cartes et la trappe du pont | Protège tout ; la LED se voit à travers | 20 € |
| 1 | Accus et support | 2 accus 18650 protégés de 3 500 mAh, en parallèle, sur support 2 places | ≈ 25 Wh, ≈ 20 h | 18 € |
| 1 | Convertisseur 3,3 V | Pololu S7V8F3 (abaisseur-élévateur, 1 A) | Alimente proprement GPS, centrale et radio, même quand la 4G tire 2 A | 8 € |
| 1 | Interrupteur | Interrupteur électronique Pololu (Mini Pushbutton Power Switch LV) commandé par un interrupteur à aimant (ILS) | On allume et on éteint avec un aimant, sans percer le boîtier | 8 € |
| 1 | Prise étanche | Embase M8 4 points + câble USB-C court à l’intérieur | Charge et programmation sans ouvrir | 10 € |
| 1 | Antennes 4G et radio | Antennes 4G et 868 MHz courtes et étanches, câbles d’antenne, 3 traversées SMA, connecteur uFL pour la radio | Sur le pont, dans l’axe (P39), comme l’antenne GPS | 15 € |
| 1 | Voyant | LED RGB adressable (type NeoPixel) | Montre l’état : GPS, RTK, 4G, radio | 1 € |
| 1 | Petites pièces | Presse-étoupe, visserie, sachet déshydratant, étiquettes de scellé |  | 6 € |
| 1 | Carte SIM | Carte SIM IoT multi-opérateurs, ≈ 500 Mo pour la saison | Passe seule d’Orange à SFR ou Bouygues | 10 € |
| | **Total** | | | **≈ 455 €** |

C’est le montant compté dans la liste d’achats. Liens d’achat : `achats.md` et `materiel.md`.

## 3. Outils

- Station de soudage, fil fin, flux, gaine thermorétractable
- Pince à dénuder, pince à sertir pour les petits connecteurs
- Multimètre et wattmètre USB
- Perceuse, foret étagé, gabarit de perçage imprimé
- Colle époxy, adhésif double face épais, colliers
- Balance de cuisine au gramme
- PC avec u-center 2 (réglage GPS) et l’outil de programmation de l’ESP32
- Bac d’eau de 50 cm pour l’étanchéité

## 4. Le câblage

Schéma : voir le document général, page Matériel, « Fabriquer la balise ».

### Alimentation

| De | Broche | Vers | Broche | Signal | Remarque |
|---|---|---|---|---|---|
| Accus 18650 (+) | — | Interrupteur électronique | VIN | 3,0 – 4,2 V | Fil 0,5 mm² ; un fusible réarmable de 3 A en série |
| Interrupteur électronique | VOUT | Carte ESP32-S3 + 4G | BAT+ | Batterie commutée | La carte alimente elle-même son modem, qui tire des pointes de 2 A |
| Interrupteur électronique | VOUT | Convertisseur 3,3 V | VIN | Batterie commutée |  |
| ILS (interrupteur à aimant) | — | Interrupteur électronique | A / B | Marche / arrêt | À la place du bouton-poussoir ; repère « aimant ici » sur le couvercle |
| Convertisseur 3,3 V | VOUT | GPS Lite | broche 1 du connecteur XBee (VCC) | 3,3 V | Le GPS alimente aussi son antenne active |
| Convertisseur 3,3 V | VOUT | BNO085 | VIN | 3,3 V |  |
| Convertisseur 3,3 V | VOUT | RFM95W | VIN | 3,3 V |  |
| Convertisseur 3,3 V | VOUT | LED RGB | VDD | 3,3 V |  |
| Toutes les masses | GND | Point de masse unique | — | Masse | En étoile, près du convertisseur |
| Embase M8 | 1 : 5 V · 2 : D− · 3 : D+ · 4 : GND | Carte ESP32-S3 + 4G | USB-C | Charge et programmation | La carte charge les accus ; balise allumée, le firmware passe en veille dès qu’il voit le 5 V |

### Signaux

| De | Broche | Vers | Broche | Signal | Remarque |
|---|---|---|---|---|---|
| GPS Lite | broche 2 du connecteur XBee (TX) | ESP32-S3 | GPIO « GPS_RX » (UART1) | Positions du GPS | 230 400 bauds |
| ESP32-S3 | GPIO « GPS_TX » (UART1) | GPS Lite | broche 3 du connecteur XBee (RX) | Corrections RTK | Venues de la 4G |
| BNO085 | P0 | BNO085 | 3,3 V | Choix du mode UART-RVC | À souder avant tout essai |
| BNO085 | SDA (devient l’émission en mode RVC) | ESP32-S3 | GPIO « IMU_RX » (UART0) | Cap, gîte, tangage | 115 200 bauds, 100 mesures par seconde, sens unique |
| RFM95W | SCK · MISO · MOSI | ESP32-S3 | bus SPI | Radio | Si la carte microSD est sur le même bus, une broche CS chacune |
| RFM95W | CS · RST · G0 | ESP32-S3 | 3 GPIO | Sélection, remise à zéro, interruption | G0 signale la fin d’émission |
| LED RGB | DIN | ESP32-S3 | GPIO « LED » | Voyant |  |
| Accus | + (avant l’interrupteur), par pont 100 k / 100 k | ESP32-S3 | GPIO « VBAT » (entrée analogique) | Niveau de batterie | Inutile si la carte mesure déjà sa batterie |

**Les numéros de GPIO.** Les numéros de GPIO se fixent sur la carte retenue au prototype (Waveshare ou LilyGO), d’après sa documentation : le modem, la carte microSD et l’USB y prennent déjà des broches. Éviter les broches de démarrage (GPIO 0, 3, 45, 46), l’USB (19, 20) et celles de la mémoire (26 à 32, et 33 à 37 si la carte a une mémoire PSRAM « octale »). Une fois fixés, les numéros sont écrits dans le firmware et sur cette fiche, et ne changent plus d’une balise à l’autre.

## 5. Le montage, pas à pas

### 1. Contrôler les pièces — 15 min

- Compter les pièces de la nomenclature, lot par lot.
- Noter le numéro de série du GPS et l’IMEI du modem sur la fiche de la balise.
- Vérifier la version de firmware du GPS : la même sur les 16 (mettre à jour avec u-center 2 si besoin).

### 2. Régler le GPS — 15 min

- Brancher le simpleRTK2B Lite seul, en USB, sur un PC avec u-center 2.
- Charger le fichier de réglages commun (ci-dessous), l’enregistrer dans la mémoire du GPS (« BBR + Flash »).
- Débrancher, rebrancher : vérifier que les réglages sont restés et que NAV-PVT sort 10 fois par seconde.

### 3. Préparer les cartes — 30 min

- BNO085 : souder la barrette, relier P0 au 3,3 V (mode UART-RVC).
- RFM95W : souder le connecteur uFL et la barrette.
- Carte ESP32-S3 + 4G : insérer la carte SIM et la carte microSD, relier le modem à sa traversée SMA.

### 4. Préparer le boîtier — 30 min

- Percer avec le gabarit commun (imprimé une fois pour toutes) : 3 traversées SMA (GPS, 4G, radio), embase M8.
- Les trois antennes vont sur le pont, dans l’axe (P39) ; dans le boîtier, seulement les câbles et les traversées.
- Coller l’ILS contre la paroi et marquer « aimant ici » à l’extérieur.
- Les 16 boîtiers se percent à la suite : c’est plus rapide et plus régulier.

### 5. Monter l’alimentation — 30 min

- Support d’accus au fond du boîtier, sur adhésif double face épais.
- Fusible réarmable, interrupteur électronique, convertisseur 3,3 V, point de masse.
- Avant de brancher une carte : mesurer 3,3 V en sortie du convertisseur, et vérifier que l’aimant allume et éteint.

### 6. Câbler les signaux — 45 min

- Suivre le tableau de câblage, fil par fil, en cochant.
- Fils souples et courts, gaine thermorétractable sur chaque soudure, rien ne tient par un seul fil : tout est collé ou sanglé.
- La centrale est fixée à plat, axe X vers l’avant de la balise (flèche dessinée sur le couvercle).

### 7. Programmer et identifier — 15 min

- Par l’embase M8, en USB : charger le firmware de série.
- Écrire dans la mémoire de la carte le numéro de la balise (01 à 16), sa clé de signature et le profil : bateau ou bouée.
- Coller l’étiquette numérotée sur le couvercle.

### 8. Essayer au banc — 30 min

- Dérouler la fiche de recette ci-dessous, avec l’antenne GPS dehors, à ciel ouvert.
- Lancer l’essai d’autonomie : il tourne seul, une nuit, pendant qu’on monte les balises suivantes.

### 9. Fermer et sceller — 15 min

- Sachet déshydratant, graisse silicone sur le joint, serrage en croix des vis du couvercle.
- Étiquette de scellé à cheval sur le couvercle et le boîtier : elle se déchire si on ouvre.

### 10. Éprouver l’étanchéité — 30 min

- Balise allumée, 30 min sous 50 cm d’eau, avec un papier absorbant à l’intérieur avant la fermeture définitive pour les deux premières.
- Ensuite, une balise sur quatre seulement, tirée au hasard.

## 6. Les réglages du GPS (fichier commun)

| Clé | Valeur | Pourquoi |
|---|---|---|
| `CFG-RATE-MEAS` | 100 | Une position toutes les 100 ms : 10 par seconde |
| `CFG-NAVSPG-DYNMODEL` | 5 (mer) | Modèle de mouvement adapté à un bateau |
| `CFG-UART1-BAUDRATE` | 230400 | Vitesse de la liaison avec la carte |
| `CFG-UART1OUTPROT-UBX / -NMEA` | 1 / 0 | En sortie, seulement le format binaire u-blox |
| `CFG-UART1INPROT-RTCM3X` | 1 | En entrée, les corrections RTK |
| `CFG-MSGOUT-UBX_NAV_PVT_UART1` | 1 | Un seul message : NAV-PVT, qui contient position, vitesse, route, précision, type de solution et l’heure GPS exacte |
| `CFG-SIGNAL (constellations)` | GPS, Galileo, BeiDou | À 10 positions par seconde, le ZED-F9P ne tient pas toutes les constellations : en garder trois, et vérifier la limite dans la fiche de la version de firmware reçue |

Le fichier est exporté depuis u-center 2 sur la première balise réglée, puis chargé à l’identique sur les 15 autres. Même récepteur, même firmware, mêmes réglages partout : c’est l’équité.

## 7. Le firmware (cahier des charges)

Écrit avec les agents IA ; c’est le plus gros logiciel côté matériel.

| Fonction | Ce qu’elle fait |
|---|---|
| Lecture GPS | Lit NAV-PVT 10 fois par seconde : position, vitesse, route, précision, type de solution, heure GPS. |
| Lecture centrale | Lit les trames UART-RVC (19 octets, 100 par seconde), en garde la dernière. |
| Horloge | Cale l’horloge de la balise sur l’arrivée de chaque NAV-PVT (heure GPS, à 1 ou 2 ms près) : pas besoin d’impulsion de seconde. |
| Envoi 4G | Trame binaire de 48 octets, signée (HMAC tronqué à 8 octets), 10 fois par seconde, en UDP vers le serveur en ligne. |
| Corrections RTK | Client NTRIP : reçoit les corrections de la base par la 4G et les passe au GPS. |
| Radio de secours | Trame de 12 octets dans le créneau de la balise : 869,525 MHz, LoRa SF7, 250 kHz, ≈ 21 ms d’émission. Bateaux : 2 trames par seconde ; bouées : 1 toutes les 5 s. |
| Carte microSD | Enregistre tout, 10 fois par seconde, un fichier par jour : preuve en cas de réclamation. |
| Surveillance | Chien de garde (redémarrage en moins de 10 s), reconnexion 4G, niveau de batterie, voyant, veille quand le 5 V de charge est présent. |
| Mise à jour | Par la 4G ou par l’embase, signée, seulement hors des manches, sur ordre du PC course. |

### Trame radio de secours (12 octets)

| Octets | Contenu | Taille |
|---|---|---|
| 0 | Numéro de balise | 1 octet |
| 1 – 2 | Temps en dixièmes de seconde dans la minute (0 – 599) et 6 bits de drapeaux | 2 octets |
| 3 – 5 | Latitude, écart au point de référence du plan d’eau | 3 octets, au centimètre |
| 6 – 8 | Longitude, idem | 3 octets, au centimètre |
| 9 | Vitesse | 1 octet, par pas de 5 cm/s |
| 10 | Route | 1 octet, par pas de 1,4° |
| 11 | Type de solution (2 bits), batterie (4 bits), réserve (2 bits) | 1 octet |

Pas de signature dans 12 octets : le récepteur n’accepte une trame que dans le créneau de sa balise, et la compare à la dernière position reçue par la 4G. La radio ne sert qu’en secours.

### Le voyant

| Couleur | État |
|---|---|
| Rouge clignotant | Pas de position GPS |
| Jaune | Position GPS, pas encore RTK |
| Vert | RTK fixe : prête à courir |
| Éclair bleu | Trame 4G partie (une fois par seconde) |
| Violet | 4G perdue : la radio de secours prend le relais |
| Blanc lent | En charge, en veille |

## 8. La recette de chaque balise

Une fiche par balise, signée, rangée dans le registre.

| Essai | Comment | Attendu |
|---|---|---|
| Allumage et extinction | à l’aimant, 10 fois de suite | Sans échec |
| Consommation moyenne | wattmètre USB sur l’embase, 10 min | ≈ 1,2 W ; alerte au-delà de 1,6 W |
| Premier point GPS | ciel dégagé, départ à froid | En moins de 1 min |
| Précision RTK | corrections de la base, 10 min immobile sur un point repéré | RTK fixe en moins de 2 min ; dispersion sous 3 cm |
| Envoi 4G | 30 min, réception au serveur | 10 trames par seconde, moins de 1 % de pertes, signatures valides |
| Radio de secours | récepteur du PC course, 10 min | Trames dans le bon créneau, 2 par seconde (bateau) |
| Centrale | balise posée sur un plan incliné de 20° | Gîte lue : 20° ± 1° |
| Carte microSD | après 30 min | Fichier du jour complet, lisible |
| Autonomie | une nuit, sur accus | Au moins 18 h |
| Étanchéité | 30 min sous 50 cm | Papier sec |
| Masse | balance de cuisine | Boîtier ≤ 180 g ; avec antennes ≤ 250 g |

## 9. La variante bouée

- Même électronique, même firmware, profil « bouée » : 1 position par seconde en 4G, 1 trame radio toutes les 5 s.
- Bouée au vent : boîtier plus grand, en pied d’espar ; sa batterie LiFePO4 12,8 V remplace les accus, et un convertisseur 12 V → 5 V alimente la carte par son entrée USB.
- Les bouées de parcours et de ligne gardent les accus de la balise. Bouée au vent : l’anémomètre Gill WindSonic M passe par un convertisseur RS-232 → 3,3 V (module MAX3232, alimenté en 3,3 V). Sa sortie va sur une broche libre de l’ESP32, lue en liaison série logicielle à 9 600 bauds, la vitesse d’usine. L’anémomètre est alimenté directement en 12,8 V.
- La bouée tourne sur son mouillage : il faut son cap absolu pour corriger la direction du vent. À vérifier au banc dès décembre : si le cap du mode UART-RVC n’est pas magnétique, la centrale de la bouée passe en liaison série complète (mode SHTP), qui donne le cap magnétique.
- Antenne GPS à côté de l’anémomètre, à la même hauteur ; rien au-dessus de l’anémomètre.

## 10. La pose à bord

- Boîtier au fond, près de la quille, sanglé : le poids en bas.
- Antennes au-dessus de la flottaison et dans l’axe du bateau : à la gîte, une antenne sur le côté sous le vent passe sous l’eau.
- Les trois antennes sur le pont, dans l’axe, quelle que soit la matière de la coque (P39) ; câbles par passe-coque étanche.
- Rien au-dessus de l’antenne GPS ; 10 à 15 cm d’un mât en carbone ; 20 cm au moins des antennes de l’équipe.
- La distance de l’antenne à l’étrave est mesurée au contrôle : le PC course en déduit la position de l’étrave.

Détail pour les équipes : `equipes/bateau-de-reference.md`.

## 11. À vérifier sur le prototype de décembre

- La carte ESP32-S3 + 4G : Waveshare ou LilyGO, la plus stable sur l’eau.
- Le cap du mode UART-RVC : magnétique ou relatif au démarrage (important pour les bouées).
- Les constellations que le GPS tient à 10 positions par seconde.
- Le courant de pointe du modem (2 A) : pas de redémarrage quand la 4G émet, accus à moitié vides.
- La chaleur : boîtier fermé, couvercle transparent, plein soleil de mai.
- La réception et la tenue des antennes sur le pont mouillé, sur un vrai IOM.
- La masse réelle de l’antenne GPS et de son câble : si elle pèse trop, essayer une antenne hélicoïdale légère.

## 12. Organiser la série

| Quand | Quoi |
|---|---|
| Décembre | Commander les pièces de 2 prototypes (une carte Waveshare, une LilyGO) ; monter, écrire le firmware de base, tester au banc. |
| Janvier | Essai sur l’eau ; choisir la carte ; figer le brochage, le gabarit de perçage et le fichier de réglages GPS. |
| 1er – 12 février | Commande de la série (C4) ; perçage des boîtiers et réglage des GPS dès réception. |
| 15 février – 5 mars | Montage par lots de 4 (C5) : ≈ 4 h par balise, soit ≈ 16 h par lot ; essais d’autonomie la nuit. |
| Début mars | Recette complète des 16, étanchéité, scellés ; registre des balises à jour avant l’essai du 10 mars. |
| Mars | Essai à 4 bateaux ; corrections du firmware ; recharge et contrôle avant la régate blanche d’avril. |

Le montage de série se fait à deux : l’un perce et câble, l’autre règle, programme et essaie. Le suppléant technique apprend dès janvier, sur les deux prototypes.
