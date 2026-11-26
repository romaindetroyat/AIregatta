# AI Regatta — La chaîne matérielle

> Les appareils, dans l’ordre où circulent les données, de la position des bateaux jusqu’aux écrans. Pour chacun : la fiabilité estimée, le logiciel à développer et le coût ; pour chaque liaison, un contrôle de compatibilité.
> La fiabilité est une estimation de jugement : la chance que l’appareil tienne la semaine sans incident bloquant, une fois validé aux essais. Les coûts sont ceux de la liste d’achats.

**28 liaisons contrôlées** : 19 compatibles d’emblée, 6 corrigées, 3 à vérifier à l’essai, 0 incompatible. Coût des appareils : ≈ 18 260 € (hors prototypes, analyseur de fréquences et imprévus ; le hub cloud est un abonnement).

## Ce que le contrôle a trouvé, et ce qu’on a changé

Le premier contrôle avait trouvé 1 liaison incompatible (caméra → mélangeur ATEM) et 7 sous condition. Cinq sont corrigées par un changement de matériel ou de branchement, plus une sixième trouvée en corrigeant (l’heure du serveur, même cause que les balises) ; trois restent à vérifier aux essais, faute de pouvoir les trancher sur le papier.

- **Corrigé** — Récepteur RTK simpleRTK2B Lite (u-blox ZED-F9P) → Carte ESP32-S3 avec modem 4G SIMCom A7670E (liaison série 3,3 V ; heure tirée des messages GPS) : Corrigé : on se passe de l’impulsion de seconde, absente du brochage public de la version Lite. Chaque position porte déjà son heure GPS exacte (message NAV-PVT) ; la balise cale son horloge sur l’arrivée de ces messages, à 1 ou 2 ms près, ce qui suffit pour les créneaux radio.
- **Corrigé** — Centrale inertielle Adafruit BNO085 → Carte ESP32-S3 avec modem 4G SIMCom A7670E (liaison série, mode UART-RVC (100 mesures par seconde)) : Corrigé : plus d’I2C, où le BNO085 provoque des erreurs de lecture sur ESP32. En mode UART-RVC, la centrale envoie seule cap, gîte et tangage 100 fois par seconde, sans pilote. La carte a trois liaisons série : GPS, modem 4G, centrale ; la console passe par l’USB.
- **À vérifier à l’essai** — Radio LoRa Adafruit RFM95W (868 MHz) → Récepteurs LoRa du PC course (869,4 – 869,65 MHz, un canal partagé en créneaux) : Réglé dans le cahier des charges du firmware : messages de 12 octets, largeur 250 kHz, facteur d’étalement 7, soit ≈ 21 ms par message ; un créneau fixe par balise, calé sur l’heure GPS, avec 5 ms de garde ; bateaux à 2 messages par seconde, bouées à 1 toutes les 5 s. Occupation ≈ 45 % du canal ; chaque bateau émet ≈ 4 % du temps, sous la limite de 10 %. Reste à le mesurer à l’essai de janvier avec l’analyseur de fréquences, car d’autres utilisateurs peuvent occuper la bande ; sinon, le secours passe à 1 position par seconde.
- **À vérifier à l’essai** — Base RTK (simpleRTK2B Budget + antenne ANN-MB-00), secours Centipede → Réseau 4G (cartes SIM multi-opérateurs) (corrections RTCM par Internet (NTRIP), puis 4G) : Les corrections n’arrivent que par la 4G : la radio de secours est trop lente pour elles. Si la 4G tombe, une balise perd le centimètre en 10 à 60 s environ (à mesurer en janvier) et retombe à ≈ 1 m, ce qui suffit pour suivre mais plus pour juger un départ. Parade adoptée : des cartes SIM IoT multi-opérateurs, qui passent seules d’Orange à SFR ou Bouygues quand un réseau sature ; si la 4G tombe pour tous, niveau de repli C (régate simple : GPS ordinaire, départs jugés par le comité). Reste à mesurer le réseau sur place un samedi de printemps.
- **Corrigé** — Base RTK (simpleRTK2B Budget + antenne ANN-MB-00), secours Centipede → 2 mini-PC ASUS NUC 14 Pro (principal et secours) (USB ; heure GPS pour le serveur) : Corrigé : comme pour les balises, on ne dépend plus de l’impulsion de seconde. Le serveur prend l’heure GPS dans les messages de la base (chrony), à quelques millisecondes près ; si la carte sort l’impulsion, on l’utilise en plus. C’est assez : chaque position porte sa propre heure GPS, et les cornes, de quelques dizaines de millisecondes.
- **Corrigé** — Anémomètre Gill WindSonic M → Carte ESP32-S3 avec modem 4G SIMCom A7670E (RS-232 → convertisseur 3,3 V ; alimentation 12,8 V) : Corrigé : un convertisseur RS-232 → 3,3 V (module MAX3232, ≈ 10 €) est compté dans « support, câble et interface ». Les trois liaisons série de la balise étant prises, l’anémomètre est lu en liaison série logicielle à 9 600 bauds, sa vitesse d’usine : sans difficulté à ce débit. L’alimentation 12,8 V est dans sa plage de 9 à 30 V.
- **Corrigé** — Onduleur APC Back-UPS 950 VA → 2 mini-PC ASUS NUC 14 Pro (principal et secours) (prises 230 V) : Corrigé : on ne compte plus sur la bascule de l’EcoFlow (≈ 30 ms annoncés, non vérifiés), trop longue pour certains blocs d’alimentation. Branché entre l’EcoFlow et les serveurs, l’onduleur couvre toute coupure. Test de mars maintenu : débrancher le secteur, les deux mini-PC branchés.
- **Corrigé** — Caméra motorisée Reolink RLC-823S2 → Mini-PC de régie ASUS NUC 14 Pro + OBS Studio, boîtier d’acquisition (flux vidéo RTSP par le réseau) : Corrigé : le mélangeur ATEM Mini Pro, qui n’a que des entrées HDMI, est retiré (− 320 €). La régie est un mini-PC avec OBS Studio (gratuit), qui lit directement le flux réseau de la caméra.
- **À vérifier à l’essai** — Caméras embarquées, récepteur 5,8 GHz et convertisseur → Mini-PC de régie ASUS NUC 14 Pro + OBS Studio, boîtier d’acquisition (5,8 GHz → récepteur → convertisseur HDMI → boîtier USB) : Branchement réglé : un convertisseur analogique → HDMI (≈ 20 €) et le boîtier d’acquisition USB (≈ 30 €) font entrer l’image dans la régie, qui choisit le bateau à montrer. Restent deux réserves que seul l’essai lève : la portée à 150 m avec 25 mW au ras de l’eau, et un seul bateau visible à la fois par récepteur. Achat en deux temps : 2 caméras pour l’essai de mars, les 8 autres si l’essai est concluant.

## Les maillons les plus fragiles

- **Caméras embarquées, récepteur 5,8 GHz et convertisseur** : 70 %
- **Carte ESP32-S3 avec modem 4G SIMCom A7670E** : 85 %
- **Centrale inertielle Adafruit BNO085** : 90 %
- **Boîtier IP67, batterie USB, alimentation, antennes de pont, carte SIM multi-opérateurs** : 90 %
- **Réseau 4G (cartes SIM multi-opérateurs)** : 90 %
- **Diffusion vidéo** : 90 %

Avec deux balises de rechange, le secours radio et les niveaux de repli, une panne d’appareil coûte une manche, pas la régate.

## À bord · la balise officielle, 12 exemplaires

| Appareil | Fiabilité | Logiciel | Coût | Relié à |
|---|---|---|---|---|
| **Antenne u-blox ANN-MB-00** ×12 — Capte les satellites GPS, Galileo et les autres, sur deux fréquences. | 98 % | Aucun | ≈ 720 € | ✓ Récepteur RTK simpleRTK2B Lite (u-blox ZED-F9P) (câble SMA, bandes L1 et L2) |
| **Récepteur RTK simpleRTK2B Lite (u-blox ZED-F9P)** ×12 — Calcule la position au centimètre, 10 fois par seconde, avec les corrections de la base. | 95 % | Réglage : Réglage du récepteur (cadence, messages, corrections) ; pas de code. | ≈ 2 388 € | ✓ Carte ESP32-S3 avec modem 4G SIMCom A7670E (liaison série 3,3 V ; heure tirée des messages GPS) |
| **Centrale inertielle Adafruit BNO085** ×12 — Mesure cap, gîte et tangage du bateau. | 90 % | Petit logiciel : Lecture du mode UART-RVC et filtrage dans le firmware de la balise. | ≈ 360 € | ✓ Carte ESP32-S3 avec modem 4G SIMCom A7670E (liaison série, mode UART-RVC (100 mesures par seconde)) |
| **Carte ESP32-S3 avec modem 4G SIMCom A7670E** ×12 — Le cerveau de la balise : rassemble les mesures, horodate, envoie en 4G et par radio. | 85 % | Gros logiciel : Firmware de la balise (S1) : lecture GPS et centrale, envoi 10 Hz signé, client NTRIP pour les corrections, radio de secours en créneaux, carte SD. | ≈ 588 € | ✓ Réseau 4G (cartes SIM multi-opérateurs) (4G LTE Cat-1, petits paquets UDP signés)<br>✓ Radio LoRa Adafruit RFM95W (868 MHz) (bus SPI) |
| **Radio LoRa Adafruit RFM95W (868 MHz)** ×12 — Chemin de secours si la 4G tombe. | 92 % | Gros logiciel : Dans le firmware : messages de 12 octets, créneaux calés sur l’heure GPS. | ≈ 252 € | ! Récepteurs LoRa du PC course (869,4 – 869,65 MHz, un canal partagé en créneaux) |
| **Boîtier IP67, batterie USB, alimentation, antennes de pont, carte SIM multi-opérateurs** ×12 — Étanchéité et ≈ 12 h d’autonomie ; batterie du commerce admise par le règlement (§ 12). | 90 % | Aucun | ≈ 1 152 € | ✓ Carte ESP32-S3 avec modem 4G SIMCom A7670E (5 V USB) |

## Les liaisons

| Appareil | Fiabilité | Logiciel | Coût | Relié à |
|---|---|---|---|---|
| **Réseau 4G (cartes SIM multi-opérateurs)** — — Transporte les positions vers le serveur en ligne, et les corrections vers les balises. | 90 % | Aucun | — | ✓ Hub cloud (serveur en ligne) (Internet) |
| **Base RTK (simpleRTK2B Budget + antenne ANN-MB-00), secours Centipede** ×1 — Station fixe au PC course : donne à toutes les balises la correction qui les rend précises au centimètre. | 96 % | Réglage : Serveur de corrections existant (RTKLIB) ; réglage seulement. | ≈ 300 € | ! Réseau 4G (cartes SIM multi-opérateurs) (corrections RTCM par Internet (NTRIP), puis 4G)<br>✓ 2 mini-PC ASUS NUC 14 Pro (principal et secours) (USB ; heure GPS pour le serveur) |
| **Récepteurs LoRa du PC course** ×2 — Reçoivent les positions de secours. | 93 % | Petit logiciel : Passerelle : décode les messages radio et les publie sur le bus de données. | ≈ 250 € | ✓ 2 mini-PC ASUS NUC 14 Pro (principal et secours) (USB série) |
| **Hub cloud (serveur en ligne)** ×1 — Reçoit les positions par la 4G, les renvoie au PC course et sert le public. Abonnement, hors budget matériel. | 98 % | Gros logiciel : Relais des positions et diffusion au public (S4, S14). | — | ✓ Routeur Ubiquiti UniFi Cloud Gateway Ultra (tunnel chiffré WireGuard)<br>✓ Téléphones du public (WebSocket et réseau de diffusion) |

## Sur l’eau · la bouée au vent

| Appareil | Fiabilité | Logiciel | Coût | Relié à |
|---|---|---|---|---|
| **Anémomètre Gill WindSonic M** ×1 — Vitesse et direction du vent, par ultrasons, sans pièce mobile. | 96 % | Petit logiciel : Lecture du vent et correction des mouvements de la bouée (S2). | ≈ 1 470 € | ✓ Carte ESP32-S3 avec modem 4G SIMCom A7670E (RS-232 → convertisseur 3,3 V ; alimentation 12,8 V) |
| **Batterie LiFePO4 de la bouée, et sa rechange** ×2 — Alimente l’anémomètre et la balise de la bouée ; rechargée chaque soir. | 96 % | Aucun | ≈ 120 € | ✓ Anémomètre Gill WindSonic M (12,8 V) |

## Au PC course

| Appareil | Fiabilité | Logiciel | Coût | Relié à |
|---|---|---|---|---|
| **Internet par fibre du site** — — Accès principal à Internet. | 97 % | Aucun | — | ✓ Routeur Ubiquiti UniFi Cloud Gateway Ultra (port WAN 1) |
| **Routeur 5G Netgear Nighthawk M6 Pro** ×1 — Internet de secours si la fibre tombe. | 93 % | Réglage : Réglage de la bascule. | ≈ 800 € | ✓ Routeur Ubiquiti UniFi Cloud Gateway Ultra (port Ethernet, WAN 2) |
| **Routeur Ubiquiti UniFi Cloud Gateway Ultra** ×1 — Réseau du PC course et de la zone équipes. | 98 % | Réglage : Réglage : réseaux séparés, bascule, tunnel. | ≈ 100 € | ✓ 2 mini-PC ASUS NUC 14 Pro (principal et secours) (Ethernet) |
| **2 mini-PC ASUS NUC 14 Pro (principal et secours)** ×2 — Font tourner le bus de données, le moteur de course et les consoles. | 99 % | Gros logiciel : Bus de données Mosquitto (existant) ; moteur de course, consoles du comité et de l’arbitrage, carte de vent (S8, S9, S10) à développer. | ≈ 1 800 € | ✓ PC des équipes (câble Ethernet, MQTT chiffré)<br>✓ Consoles du directeur de course et des deux arbitres (3 écrans) (réseau local)<br>✓ Relais Shelly 1 Gen3 et cornes 12 V (Wi-Fi local, MQTT) |
| **Batterie EcoFlow River 2 Pro** ×1 — Le PC course tient des heures sans secteur. | 97 % | Aucun | ≈ 600 € | ✓ Onduleur APC Back-UPS 950 VA (prise 230 V) |
| **Onduleur APC Back-UPS 950 VA** ×1 — Tient les serveurs pendant toute bascule, quelques minutes au besoin. | 97 % | Aucun | ≈ 110 € | ✓ 2 mini-PC ASUS NUC 14 Pro (principal et secours) (prises 230 V) |
| **Station météo Davis Vantage Pro2 + WeatherLink Live** ×1 — Vent de référence à terre. | 95 % | Petit logiciel : Petit adaptateur : lit la station et publie sur le bus. | ≈ 1 000 € | ✓ Routeur Ubiquiti UniFi Cloud Gateway Ultra (Ethernet ou Wi-Fi, interface HTTP locale) |
| **Relais Shelly 1 Gen3 et cornes 12 V** ×2 — Déclenchent les signaux sonores du départ. | 93 % | Petit logiciel : Commande des cornes depuis le chrono officiel. | ≈ 300 € | — |

## La vidéo

| Appareil | Fiabilité | Logiciel | Coût | Relié à |
|---|---|---|---|---|
| **Caméra motorisée Reolink RLC-823S2** ×1 — Filme le parcours depuis le point haut. | 92 % | Réglage : Réglage ; orientation par ONVIF. | ≈ 780 € | ✓ Routeur Ubiquiti UniFi Cloud Gateway Ultra (câble réseau avec alimentation (PoE), flux RTSP)<br>✓ Mini-PC de régie ASUS NUC 14 Pro + OBS Studio, boîtier d’acquisition (flux vidéo RTSP par le réseau) |
| **Mini-PC de régie ASUS NUC 14 Pro + OBS Studio, boîtier d’acquisition** ×1 — Régie : caméras, habillage, diffusion. Même modèle que les serveurs : les trois sont interchangeables. | 95 % | Réglage : OBS se règle ; l’habillage télé (S15) s’y affiche comme une page web. | ≈ 930 € | ✓ Diffusion vidéo (diffusion en direct (RTMP)) |
| **Caméras embarquées, récepteur 5,8 GHz et convertisseur** ×6 + 1 — Images à bord des bateaux. | 70 % | Réglage : Réglage des canaux. | ≈ 920 € | ! Mini-PC de régie ASUS NUC 14 Pro + OBS Studio, boîtier d’acquisition (5,8 GHz → récepteur → convertisseur HDMI → boîtier USB) |

## Les destinataires

| Appareil | Fiabilité | Logiciel | Coût | Relié à |
|---|---|---|---|---|
| **PC des équipes** — — Reçoivent le flux officiel, décident, commandent leur bateau par radio ExpressLRS (trois montages proposés). | 98 % | Aucun : Côté organisation : contrat d’interface et exemples, déjà écrits. | — | — |
| **Consoles du directeur de course et des deux arbitres (3 écrans)** ×3 — Procédure, alertes, rejeux, décisions. | 98 % | Gros logiciel : Consoles (S10) : comptées avec les mini-PC. | ≈ 1 100 € | — |
| **Téléphones du public** — — L’application publique, avec 1 s de différé. | 95 % | Gros logiciel : Application publique (S14). | — | — |
| **Diffusion vidéo** — — La course en direct, avec l’habillage. | 90 % | Gros logiciel : Habillage télé (S15). | — | — |

## Sources des contrôles

- [Gill WindSonic M : sorties et alimentation (fiche technique)](https://observator.com/download/datasheet-windsonic-m)
- [Gill WindSonic : manuel](https://NOC.ac.uk/files/documents/facilities/james_cook/Gill_WindSonic.pdf)
- [BNO085 et étirement d’horloge I2C sur ESP32 (forum ESP32)](https://esp32.com/viewtopic.php?p=38691)
- [BNO085 : passage en liaison série (forum Core Electronics)](https://forum.core-electronics.com.au/t/problems-using-bno085-imu-with-pi-zer0-w/9218?page=2)
- [ATEM Mini : pas de vidéo par le réseau (forum Blackmagic)](https://forum.blackmagicdesign.com/viewtopic.php?p=1108216)
- [simpleRTK2B Lite : guide de branchement](https://www.ardusimple.com/simplertk2blite-hookup-guide/)
- [simpleRTK2B Lite : fiche technique](https://www.mouser.com/datasheet/2/1042/ArduSimple_Datasheet_simpleRTK2Blite-3238991.pdf)

Le calcul d’occupation du canal LoRa est fait d’après la formule de temps d’antenne de Semtech ; la bascule de 30 ms de l’EcoFlow n’a pas été vérifiée.
