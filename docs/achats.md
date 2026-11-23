# AI Regatta — Achats

> Tout le matériel à acheter pour 6 bateaux : quantité, rôle, prix, où l’acheter (livraison France). Total : **19 100 €**, imprévus de 10 % compris. Seul le matériel coûte : tout le monde est bénévole.

| Commande | Montant |
|---|---|
| Décembre · Commande du prototype (C1) | 1 900 € |
| Février · Série, bouées, 2 caméras d’essai (C4, D2, D3, C7) | 8 570 € |
| Mars · PC course, caméras, signaux (H3) | 6 920 € |
| Imprévus (10 %) | 1 700 € |
| **Total** | **19 100 €** |

## Balise officielle · 12 exemplaires

| Qté | Article | Rôle | Commande | Prix | Total | Où acheter |
|---|---|---|---|---|---|---|
| 12 | ArduSimple simpleRTK2B Lite | Récepteur GPS RTK : la position au centimètre, 10 fois par seconde | Février | 199 € | 2 388 € | [ArduSimple, boutique officielle (UE)](https://www.ardusimple.com/product/simplertk2blite/) |
| 12 | Antenne u-blox ANN-MB-00 | Antenne GPS bi-fréquence, sur le pont du bateau ou en tête de mât des bouées | Février | 60 € | 720 € | [ArduSimple, ANN-MB-00 (L1/L2, adaptée au ZED-F9P)](https://www.ardusimple.com/product/ann-mb-00-ip67) · [Future Electronics (page FR)](https://futureelectronics.com/fr/p/semiconductors--wireless-rf--antennas--gps-antennas/ann-mb-00-u-blox-6120194) |
| 12 | Carte ESP32-S3 + modem 4G A7670E | Calcul de la balise et envoi des positions par la 4G | Février | 49 € | 588 € | [OpenELab (France), Waveshare ESP32-S3-A7670E-4G](https://openelab.io/fr/products/waveshare-esp32-s3-a7670e-4g) · [RobotShop Europe](https://eu.robotshop.com/products/waveshare-esp32-s3-a7670e-4g-development-board-lte-cat-1-2g-wifi-bluetooth-telephone-call-sms-gnss) |
| 12 | Module radio LoRa RFM95W 868 MHz | Chemin de secours si la 4G tombe | Février | 21 € | 252 € | [DigiKey (UE, livre en France)](https://www.digikey.es/en/products/detail/adafruit-industries-llc/3072/6005357) |
| 12 | Centrale inertielle BNO085 | Cap, gîte et mouvements du bateau ou de la bouée | Février | 30 € | 360 € | [Anodas (UE)](https://anodas.lt/en/bno085-9-dof-imu-fusion-breakout-3-axis-accelerometer-gyroscope-and-magnetometer-adafruit-4754) · [Go Tronic (France), réf. 37262](https://gotronic.fr/download-product-page/33477) |
| 12 | Boîtier IP67, batterie USB, alimentation, antennes de pont, carte SIM multi-opérateurs | Étanchéité, ≈ 12 h d’autonomie ; batterie admise par le règlement (§ 12) ; détail dans le manuel de fabrication | Février | 96 € | 1 152 € | — |

## Bouée au vent

| Qté | Article | Rôle | Commande | Prix | Total | Où acheter |
|---|---|---|---|---|---|---|
| 1 | Anémomètre Gill WindSonic M | Vitesse et direction du vent, par ultrasons | Février | 1 300 € | 1 300 € | [NauticExpo, demande de devis](https://www.nauticexpo.com/prod/gill-instruments-ltd/product-39900-485171.html) · [Campbell Scientific France, brochure et devis](https://s.campbellsci.com/documents/fr/product-brochures/b_windsonic_fr.pdf) |
| 1 | Support, câble et interface de l’anémomètre | Fixation en tête d’espar ; convertisseur RS-232 → 3,3 V vers la balise | Février | 170 € | 170 € | — |
| 2 | Batterie LiFePO4 12,8 V 6 Ah étanche | Alimente l’anémomètre et la balise de la bouée au vent ; une de rechange, rechargée chaque soir | Février | 60 € | 120 € | — |

## Base RTK et radio de secours

| Qté | Article | Rôle | Commande | Prix | Total | Où acheter |
|---|---|---|---|---|---|---|
| 1 | Base RTK (simpleRTK2B Budget + antenne ANN-MB-00 sur plan de masse, mât) | Station fixe au PC course : corrige le GPS de toutes les balises | Décembre | 300 € | 300 € | [ArduSimple, boutique officielle (UE)](https://www.ardusimple.com/product/simplertk2blite/) |
| 1 | Récepteurs radio 868 MHz du PC course (lot) | Reçoivent les positions de secours | Décembre | 250 € | 250 € | [DigiKey (UE, livre en France)](https://www.digikey.es/en/products/detail/adafruit-industries-llc/3072/6005357) |

## PC course

| Qté | Article | Rôle | Commande | Prix | Total | Où acheter |
|---|---|---|---|---|---|---|
| 2 | Mini-PC ASUS NUC 14 Pro | Serveur principal et serveur de secours : bus de données, moteur de course | Mars | 900 € | 1 800 € | [LDLC (barebone Core 3)](https://www.ldlc.com/en/product/PB00624811.html) · [ASUS France, page officielle](https://www.asus.com/fr/displays-desktops/nucs/nuc-mini-pcs/asus-nuc-14-pro/) |
| 1 | Routeur Ubiquiti UniFi Cloud Gateway Ultra | Réseau du PC course, bascule fibre ↔ 4G | Mars | 100 € | 100 € | [Ubiquiti Store Europe (officiel)](https://eu.store.ui.com/eu/en/products/ucg-ultra) |
| 1 | Routeur 5G Netgear Nighthawk M6 Pro | Internet de secours si la fibre tombe | Mars | 800 € | 800 € | [LDLC](https://ldlc.com/en/product/PB00540606.html) · [Galaxus.fr](https://www.galaxus.fr/fr/s1/product/netgear-nighthawk-m6-pro-routeur-mobile-routeur-23545594) |
| 1 | Batterie EcoFlow River 2 Pro | Le PC course tient sans secteur | Mars | 600 € | 600 € | [Castorama](https://www.castorama.fr/station-electrique-portable-ecoflow-river-2-pro-720wh/4895251601559_CAFR.prd) · [Boulanger](https://www.boulanger.com/ref/1187283) |
| 1 | Onduleur APC Back-UPS 950 VA | Entre la batterie et les serveurs : aucune coupure pendant une bascule | Mars | 110 € | 110 € | — |
| 1 | Écrans (3), commutateur PoE, borne Wi-Fi, câbles, rallonges | Consoles du directeur de course et des deux arbitres ; Wi-Fi du PC course ; alimentation de la caméra | Mars | 1 100 € | 1 100 € | — |

## Caméras et régie

| Qté | Article | Rôle | Commande | Prix | Total | Où acheter |
|---|---|---|---|---|---|---|
| 1 | Caméra motorisée Reolink RLC-823S2 (zoom 16×) | Image du parcours depuis le point haut | Mars | 480 € | 480 € | [Reolink France, boutique officielle](https://reolink.com/fr/product/rlc-823s2/) |
| 1 | Mini-PC de régie ASUS NUC 14 Pro, avec OBS Studio | Régie : lit la caméra par le réseau, ajoute l’habillage, diffuse ; même modèle que les serveurs, donc interchangeable | Mars | 900 € | 900 € | [LDLC (barebone Core 3)](https://www.ldlc.com/en/product/PB00624811.html) · [ASUS France, page officielle](https://www.asus.com/fr/displays-desktops/nucs/nuc-mini-pcs/asus-nuc-14-pro/) |
| 1 | Boîtier d’acquisition HDMI → USB | Fait entrer l’image des caméras embarquées dans la régie | Mars | 30 € | 30 € | — |
| 1 | Mât, fixations, câbles réseau | Caméra à 12 m au plus | Mars | 300 € | 300 € | — |

## Météo et outils

| Qté | Article | Rôle | Commande | Prix | Total | Où acheter |
|---|---|---|---|---|---|---|
| 1 | Station Davis Vantage Pro2 + WeatherLink Live | Vent à terre, référence pour la carte de vent | Février | 1 000 € | 1 000 € | [Conrad, Vantage Pro2 6252EU](https://www.conrad.com/en/p/davis-instruments-vantage-pro2-with-console-eu-6252eu-wireless-digital-weather-station-max-number-of-sensors-80-3123434.html) · [Conrad, WeatherLink Live 6100EU](https://www.conrad.com/en/p/davis-instruments-6100eu-6100eu-wi-fi-weather-station-3448772.html) |
| 1 | Analyseur de fréquences TinySA Ultra | Vérifier que la radio n’est pas brouillée | Décembre | 150 € | 150 € | [Lab401 (France)](https://lab401.com/products/tinysa-ultra) · [Passion Radio (France)](https://www.passion-radio.com/meter/tiny-sa-ultra-2543.html) |

## Signaux de départ

| Qté | Article | Rôle | Commande | Prix | Total | Où acheter |
|---|---|---|---|---|---|---|
| 2 | Relais connecté Shelly 1 Gen3 | Le PC course déclenche la corne, à moins de 50 ms près | Mars | 25 € | 50 € | [Domadoo (France)](https://www.domadoo.fr/de/smarte-beleuchtung/7507-shelly-intelligentes-universalmodul-w-lan-shelly-1-gen3-3800235261767.html) · [Shelly, boutique officielle (UE)](https://www.shelly.com/it/products/shelly-1-gen3) |
| 2 | Corne électrique marine 12 V | Signaux sonores du départ | Mars | 45 € | 90 € | [Poseidon Marine, klaxon Marco 12 V](https://www.poseidonmarine.eu/fr/products/electric-horn-12v-chrome-1) · [H2R Équipements (France), avertisseur Osculati 12 V](https://www.h2r-equipements.com/avertisseur-sonore-pour-bateau/2985-osculati-avertisseur-encastrable-12v.html) |
| 1 | Batterie 12 V et câblage | Alimentation des cornes | Mars | 160 € | 160 € | — |

## Caméras embarquées

| Qté | Article | Rôle | Commande | Prix | Total | Où acheter |
|---|---|---|---|---|---|---|
| 2 | Caméra embarquée légère, pour l’essai | Commandées avec la série, essayées en mars | Février | 100 € | 200 € | — |
| 1 | Récepteur vidéo au PC course | Reçoit l’image d’un bateau à la fois, choisi par la régie | Février | 300 € | 300 € | — |
| 1 | Convertisseur vidéo analogique → HDMI | Sort l’image du récepteur vers la régie | Février | 20 € | 20 € | — |
| 4 | Caméra embarquée légère | Les 4 autres, seulement si l’essai de mars est concluant | Mars | 100 € | 400 € | — |

## Prototypes

| Qté | Article | Rôle | Commande | Prix | Total | Où acheter |
|---|---|---|---|---|---|---|
| 1 | Lot prototype | 2 balises complètes (une carte 4G Waveshare, une LilyGO) et leurs rechanges, pour l’essai de janvier ; l’anémomètre est commandé sur devis avec la série | Décembre | 1 200 € | 1 200 € | — |

## Options non retenues

| Option | Coût | Où acheter |
|---|---|---|
| Second anémomètre, bouée sous le vent | 1 470 € | [NauticExpo, demande de devis](https://www.nauticexpo.com/prod/gill-instruments-ltd/product-39900-485171.html) · [Campbell Scientific France, brochure et devis](https://s.campbellsci.com/documents/fr/product-brochures/b_windsonic_fr.pdf) |
| Seconde caméra motorisée | 480 € | [Reolink France, boutique officielle](https://reolink.com/fr/product/rlc-823s2/) |
| Analyse d’image (Jetson Orin Nano Super) | 280 € | [Generation Robots (France)](https://www.generationrobots.com/en/404303-nvidia-jetson-orin-nano-super-developer-kit.html) · [RS Online France](https://fr.rs-online.com/web/p/modules-de-developpement-pour-processeurs/2647384) |

**Avant de commander :** les liens viennent d’une recherche et n’ont pas pu être ouverts depuis notre outil ; vérifiez la page et le prix. L’anémomètre Gill se vend sur devis. Les corps de bouées et les mouillages ne sont pas comptés : à voir avec le club partenaire.
