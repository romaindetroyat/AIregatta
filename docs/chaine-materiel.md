# AI Regatta — La chaîne matérielle

> Les appareils, dans l’ordre où circulent les données, de la position des bateaux jusqu’aux écrans. Pour chacun : la fiabilité estimée, le logiciel à développer et le coût ; pour chaque liaison, un contrôle de compatibilité.
> La fiabilité est une estimation de jugement : la chance que l’appareil tienne la semaine sans incident bloquant, une fois validé aux essais. Les coûts sont ceux de la liste d’achats.

**26 liaisons contrôlées** : 18 compatibles, 7 sous condition, 1 incompatible. Coût des appareils : ≈ 17 280 € (hors prototypes et imprévus).

## Ce que le contrôle a trouvé

- **Compatible sous condition** — Récepteur RTK simpleRTK2B Lite (u-blox ZED-F9P) → Carte ESP32-S3 avec modem 4G SIMCom A7670E (liaison série 3,3 V et impulsion de seconde (PPS)) : La liaison série est bien sortie sur le connecteur XBee de la carte. L’impulsion de seconde, utile à l’horodatage précis, n’apparaît pas dans le brochage public de la version Lite : à vérifier sur le prototype, sinon prendre une carte qui la sort.
- **Compatible sous condition** — Centrale inertielle Adafruit BNO085 → Carte ESP32-S3 avec modem 4G SIMCom A7670E (bus I2C) : Le BNO085 « étire l’horloge » du bus I2C, ce qui provoque des erreurs de lecture signalées sur ESP32. Le brancher en liaison série (mode UART ou UART-RVC) plutôt qu’en I2C.
- **Compatible sous condition** — Radio LoRa Adafruit RFM95W (868 MHz) → Récepteurs LoRa du PC course (869,4 – 869,65 MHz, un seul canal pour 16 émetteurs) : Le calcul ne passe que serré. Un message de 20 octets dure ≈ 33 ms ; 16 balises à 2 messages par seconde occuperaient plus que le canal. Il faut des messages de 12 octets, une largeur de 250 kHz, des créneaux calés sur l’heure GPS, et les bouées à 1 message toutes les 5 s : ≈ 75 % d’occupation, chaque balise restant sous sa limite de 10 % du temps. Sinon, le secours passe à 1 position par seconde.
- **Compatible sous condition** — Base RTK (simpleRTK2B + antenne géodésique), secours Centipede → Réseau 4G des opérateurs (cartes SIM de deux opérateurs) (corrections RTCM par Internet (NTRIP), puis 4G) : Les corrections n’arrivent que par la 4G : la radio de secours est trop lente pour elles. Si la 4G tombe, une balise perd le centimètre en une minute environ et retombe à ≈ 1 m, ce qui suffit pour suivre mais plus pour juger un départ. Parade : deux opérateurs, et le niveau de repli B.
- **Compatible sous condition** — Anémomètre Gill WindSonic M → Carte ESP32-S3 avec modem 4G SIMCom A7670E (liaison série RS-232 ou RS-422 ; alimentation 9 – 30 V) : La balise attend du 3,3 V : il faut un petit convertisseur RS-232 → 3,3 V (prévu dans « support, câble et interface »). L’alimentation 12,8 V de la batterie de la bouée convient.
- **Compatible sous condition** — Batterie EcoFlow River 2 Pro → 2 mini-PC ASUS NUC 14 Pro (principal et secours) (prises 230 V, bascule automatique) : La bascule annoncée est de l’ordre de 30 ms, chiffre non vérifié : la tester avec les deux mini-PC branchés. Sinon, ajouter un petit onduleur.
- **Incompatible** — Caméra motorisée Reolink RLC-823S2 → Mélangeur Blackmagic ATEM Mini Pro (flux vidéo sur réseau → mélangeur à entrées HDMI) : Incompatible : l’ATEM Mini Pro n’a que des entrées HDMI et n’accepte pas la vidéo par le réseau. Correction : un logiciel de régie (OBS, gratuit) sur un ordinateur lit le flux de la caméra, ajoute l’habillage et diffuse. L’ATEM devient inutile (− 320 €) ; on peut le garder pour une caméra HDMI.
- **Compatible sous condition** — Caméras embarquées et récepteur 5,8 GHz → Mélangeur Blackmagic ATEM Mini Pro (vidéo analogique 5,8 GHz → récepteur → entrée HDMI) : Trois réserves : la puissance est limitée à 25 mW, avec des antennes au ras de l’eau, donc une portée incertaine à 150 m ; le récepteur sort de la vidéo analogique, il faut un convertisseur vers HDMI ou vers l’ordinateur de régie ; un récepteur ne montre qu’un bateau à la fois. À tester à l’essai de mars avant d’en acheter dix.

## Les maillons les plus fragiles

- **Caméras embarquées et récepteur 5,8 GHz** : 70 %
- **Carte ESP32-S3 avec modem 4G SIMCom A7670E** : 85 %
- **Centrale inertielle Adafruit BNO085** : 90 %
- **Boîtier IP67, batterie, connecteurs, carte SIM** : 90 %
- **Réseau 4G des opérateurs (cartes SIM de deux opérateurs)** : 90 %
- **Diffusion vidéo** : 90 %

Avec deux balises de rechange, le secours radio et les niveaux de repli, une panne d’appareil coûte une manche, pas la régate.

## À bord · la balise officielle, 16 exemplaires

| Appareil | Fiabilité | Logiciel | Coût | Relié à |
|---|---|---|---|---|
| **Antenne u-blox ANN-MB-00** ×16 — Capte les satellites GPS, Galileo et les autres, sur deux fréquences. | 98 % | Aucun | ≈ 960 € | ✓ Récepteur RTK simpleRTK2B Lite (u-blox ZED-F9P) (câble SMA, bandes L1 et L2) |
| **Récepteur RTK simpleRTK2B Lite (u-blox ZED-F9P)** ×16 — Calcule la position au centimètre, 10 fois par seconde, avec les corrections de la base. | 95 % | Réglage : Réglage du récepteur (cadence, messages, corrections) ; pas de code. | ≈ 3 184 € | ! Carte ESP32-S3 avec modem 4G SIMCom A7670E (liaison série 3,3 V et impulsion de seconde (PPS)) |
| **Centrale inertielle Adafruit BNO085** ×16 — Mesure cap, gîte et tangage du bateau. | 90 % | Petit logiciel : Lecture et filtrage dans le firmware de la balise. | ≈ 480 € | ! Carte ESP32-S3 avec modem 4G SIMCom A7670E (bus I2C) |
| **Carte ESP32-S3 avec modem 4G SIMCom A7670E** ×16 — Le cerveau de la balise : rassemble les mesures, horodate, envoie en 4G et par radio. | 85 % | Gros logiciel : Firmware de la balise (S1) : lecture GPS et centrale, envoi 10 Hz signé, client NTRIP pour les corrections, radio de secours en créneaux, carte SD. | ≈ 784 € | ✓ Réseau 4G des opérateurs (cartes SIM de deux opérateurs) (4G LTE Cat-1, petits paquets UDP signés)<br>✓ Radio LoRa Adafruit RFM95W (868 MHz) (bus SPI) |
| **Radio LoRa Adafruit RFM95W (868 MHz)** ×16 — Chemin de secours si la 4G tombe. | 92 % | Gros logiciel : Dans le firmware : créneaux de parole calés sur l’heure GPS. | ≈ 336 € | ! Récepteurs LoRa du PC course (869,4 – 869,65 MHz, un seul canal pour 16 émetteurs) |
| **Boîtier IP67, batterie, connecteurs, carte SIM** ×16 — Étanchéité et ≈ 20 h d’autonomie. | 90 % | Aucun | ≈ 1 296 € | ✓ Carte ESP32-S3 avec modem 4G SIMCom A7670E (alimentation 3,7 V et 5 V) |

## Les liaisons

| Appareil | Fiabilité | Logiciel | Coût | Relié à |
|---|---|---|---|---|
| **Réseau 4G des opérateurs (cartes SIM de deux opérateurs)** — — Transporte les positions vers le serveur en ligne, et les corrections vers les balises. | 90 % | Aucun | — | ✓ Serveur en ligne (hub) (Internet) |
| **Base RTK (simpleRTK2B + antenne géodésique), secours Centipede** ×1 — Station fixe au PC course : donne à toutes les balises la correction qui les rend précises au centimètre. | 96 % | Réglage : Serveur de corrections existant (RTKLIB) ; réglage seulement. | ≈ 300 € | ! Réseau 4G des opérateurs (cartes SIM de deux opérateurs) (corrections RTCM par Internet (NTRIP), puis 4G) |
| **Récepteurs LoRa du PC course** ×2 — Reçoivent les positions de secours. | 93 % | Petit logiciel : Passerelle : décode les messages radio et les publie sur le bus de données. | ≈ 250 € | ✓ 2 mini-PC ASUS NUC 14 Pro (principal et secours) (USB série) |
| **Serveur en ligne (hub)** ×1 — Reçoit les positions par la 4G, les renvoie au PC course et sert le public. | 98 % | Gros logiciel : Relais des positions et diffusion au public (S3, S11). | ≈ 300 € | ✓ Routeur Ubiquiti UniFi Cloud Gateway Ultra (tunnel chiffré WireGuard)<br>✓ Téléphones du public (WebSocket et réseau de diffusion) |

## Sur l’eau · la bouée au vent

| Appareil | Fiabilité | Logiciel | Coût | Relié à |
|---|---|---|---|---|
| **Anémomètre Gill WindSonic M** ×1 — Vitesse et direction du vent, par ultrasons, sans pièce mobile. | 96 % | Petit logiciel : Lecture du vent et correction des mouvements de la bouée (S2). | ≈ 1 470 € | ! Carte ESP32-S3 avec modem 4G SIMCom A7670E (liaison série RS-232 ou RS-422 ; alimentation 9 – 30 V) |
| **Batterie LiFePO4 de la bouée, et sa rechange** ×2 — Alimente l’anémomètre et la balise de la bouée ; rechargée chaque soir. | 96 % | Aucun | ≈ 120 € | ✓ Anémomètre Gill WindSonic M (12,8 V) |

## Au PC course

| Appareil | Fiabilité | Logiciel | Coût | Relié à |
|---|---|---|---|---|
| **Internet par fibre du site** — — Accès principal à Internet. | 97 % | Aucun | — | ✓ Routeur Ubiquiti UniFi Cloud Gateway Ultra (port WAN 1) |
| **Routeur 5G Netgear Nighthawk M6 Pro** ×1 — Internet de secours si la fibre tombe. | 93 % | Réglage : Réglage de la bascule. | ≈ 500 € | ✓ Routeur Ubiquiti UniFi Cloud Gateway Ultra (port Ethernet, WAN 2) |
| **Routeur Ubiquiti UniFi Cloud Gateway Ultra** ×1 — Réseau du PC course et de la zone équipes. | 98 % | Réglage : Réglage : réseaux séparés, bascule, tunnel. | ≈ 100 € | ✓ 2 mini-PC ASUS NUC 14 Pro (principal et secours) (Ethernet) |
| **2 mini-PC ASUS NUC 14 Pro (principal et secours)** ×2 — Font tourner le bus de données, le moteur de course et les consoles. | 99 % | Gros logiciel : Bus de données Mosquitto (existant) ; moteur de course, consoles du comité et de l’arbitrage, carte de vent (S8, S9, S10) à développer. | ≈ 1 800 € | ✓ PC des équipes (câble Ethernet, MQTT chiffré)<br>✓ Consoles du comité et de l’arbitrage (2 écrans) (réseau local)<br>✓ Relais Shelly 1 Gen3 et cornes 12 V (Wi-Fi local, commande HTTP) |
| **Batterie EcoFlow River 2 Pro** ×1 — Le PC course tient sans secteur. | 97 % | Aucun | ≈ 600 € | ! 2 mini-PC ASUS NUC 14 Pro (principal et secours) (prises 230 V, bascule automatique) |
| **Station météo Davis Vantage Pro2 + WeatherLink Live** ×1 — Vent de référence à terre. | 95 % | Petit logiciel : Petit adaptateur : lit la station et publie sur le bus. | ≈ 1 000 € | ✓ Routeur Ubiquiti UniFi Cloud Gateway Ultra (Ethernet ou Wi-Fi, interface HTTP locale) |
| **Relais Shelly 1 Gen3 et cornes 12 V** ×2 — Déclenchent les signaux sonores du départ. | 93 % | Petit logiciel : Commande des cornes depuis le chrono officiel. | ≈ 300 € | — |

## La vidéo

| Appareil | Fiabilité | Logiciel | Coût | Relié à |
|---|---|---|---|---|
| **Caméra motorisée Reolink RLC-823S2** ×1 — Filme le parcours depuis le point haut. | 92 % | Réglage : Réglage ; orientation par ONVIF. | ≈ 780 € | ✓ Routeur Ubiquiti UniFi Cloud Gateway Ultra (câble réseau avec alimentation (PoE), flux RTSP)<br>✗ Mélangeur Blackmagic ATEM Mini Pro (flux vidéo sur réseau → mélangeur à entrées HDMI) |
| **Mélangeur Blackmagic ATEM Mini Pro** ×1 — Régie : caméras, habillage, diffusion. | 97 % | Aucun : Habillage télé à développer (S11), quelle que soit la régie. | ≈ 320 € | ✓ Diffusion vidéo (diffusion en direct (RTMP)) |
| **Caméras embarquées et récepteur 5,8 GHz** ×10 + 1 — Images à bord des bateaux. | 70 % | Réglage : Réglage des canaux. | ≈ 1 300 € | ! Mélangeur Blackmagic ATEM Mini Pro (vidéo analogique 5,8 GHz → récepteur → entrée HDMI) |

## Les destinataires

| Appareil | Fiabilité | Logiciel | Coût | Relié à |
|---|---|---|---|---|
| **PC des équipes** — — Reçoivent le flux officiel, décident, commandent leur bateau par leur propre liaison. | 98 % | Aucun : Côté organisation : contrat d’interface et exemples, déjà écrits. | — | — |
| **Consoles du comité et de l’arbitrage (2 écrans)** ×2 — Procédure, alertes, rejeux, décisions. | 98 % | Gros logiciel : Consoles (S10) : comptées avec les mini-PC. | ≈ 1 100 € | — |
| **Téléphones du public** — — L’application, avec 1 s de différé. | 95 % | Gros logiciel : Application spectateur (S11). | — | — |
| **Diffusion vidéo** — — La course en direct, avec l’habillage. | 90 % | Gros logiciel : Habillage télé (S11). | — | — |

## Sources des contrôles

- [Gill WindSonic M : sorties et alimentation (fiche technique)](https://observator.com/download/datasheet-windsonic-m)
- [Gill WindSonic : manuel](https://NOC.ac.uk/files/documents/facilities/james_cook/Gill_WindSonic.pdf)
- [BNO085 et étirement d’horloge I2C sur ESP32 (forum ESP32)](https://esp32.com/viewtopic.php?p=38691)
- [BNO085 : passage en liaison série (forum Core Electronics)](https://forum.core-electronics.com.au/t/problems-using-bno085-imu-with-pi-zer0-w/9218?page=2)
- [ATEM Mini : pas de vidéo par le réseau (forum Blackmagic)](https://forum.blackmagicdesign.com/viewtopic.php?p=1108216)
- [simpleRTK2B Lite : guide de branchement](https://www.ardusimple.com/simplertk2blite-hookup-guide/)
- [simpleRTK2B Lite : fiche technique](https://www.mouser.com/datasheet/2/1042/ArduSimple_Datasheet_simpleRTK2Blite-3238991.pdf)

Le calcul d’occupation du canal LoRa est fait d’après la formule de temps d’antenne de Semtech ; la bascule de 30 ms de l’EcoFlow n’a pas été vérifiée.
