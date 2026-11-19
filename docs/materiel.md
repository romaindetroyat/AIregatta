# AI Regatta — Matériel retenu

> Version du 20 novembre 2026. Uniquement du matériel très bien noté ou de référence professionnelle ; deux petits composants sans avis publics sont signalés et seront validés au banc.

## Balise

### ArduSimple simpleRTK2B Lite — ≈ 190–210 €

*Très bons avis*

Le récepteur GPS de la balise. Il utilise la puce u-blox ZED-F9P, la référence des GPS précis à bas coût.

**Pourquoi ce choix.** C’est le récepteur le plus utilisé et le plus documenté dans sa catégorie : des milliers de drones, robots et tracteurs l’utilisent. Les tests publiés donnent environ 2 cm de précision.

- Fiche : [Page produit ArduSimple](https://www.ardusimple.com/product/simplertk2blite/)
- Fiche : [Fiche technique (PDF)](https://www.mouser.com/datasheet/2/1042/ArduSimple_Datasheet_simpleRTK2Blite-3238991.pdf)
- Fiche : [Résumé de la puce ZED-F9P (u-blox, PDF)](https://incremental-content.u-blox.com/sites/default/files/ZED-F9P_ProductSummary_UBX-17005151.pdf)
- Avis : [Test de terrain, université de Caroline du Sud : ≈ 2,2 cm](https://www.ardusimple.com/field-test-evaluation-of-the-ardusimple-simplertk2blite-zed-f9p-operating-in-rtk-mode-on-the-south-carolina-virtual-reference-network/)
- Avis : [Premières impressions d’un roboticien : « a great piece of kit »](https://msadowski.github.io/ardusimple-rtk-first-impressions)
- Avis : [Forum ArduPilot : ZED-F9P comparé à l’ancienne génération](https://discuss.ardupilot.org/t/comparing-a-ublox-f9p-with-a-m8p-with-rtk/43493)

### Antenne u-blox ANN-MB — ≈ 50–70 €

*Très bons avis*

L’antenne GPS, étanche, captant deux bandes de fréquences. Elle sert sur les balises et sur la base RTK.

**Pourquoi ce choix.** C’est l’antenne conçue par le fabricant de la puce pour aller avec elle. Une étude universitaire la classe parmi les bonnes antennes à bas coût. Une seule référence partout simplifie les rechanges.

- Fiche : [Fiche technique ANN-MB (PDF)](https://www.mouser.com/datasheet/2/813/ANN-MB_DataSheet__UBX-18049862_-1532371.pdf)
- Fiche : [Version récente ANN-MB2 (PDF)](https://content.u-blox.com/sites/default/files/documents/ANN-MB2_ProductSummary_UBXDOC-963802114-12691.pdf)
- Avis : [Université de Birmingham : évaluation de l’ANN-MB](https://research.birmingham.ac.uk/en/publications/assessment-of-the-performance-of-the-topgnss-and-ann-mb-antennas-/)

### Adafruit BNO085 — ≈ 25–30 €

*Très bons avis*

La centrale inertielle : elle mesure la gîte, le tangage et les rotations du bateau.

**Pourquoi ce choix.** Adafruit est réputé pour la qualité de ses cartes et de sa documentation. On n’utilise que les mesures de rotation et d’inclinaison, son point fort. Sa boussole magnétique, critiquée par certains utilisateurs, n’est pas utilisée : le cap vient du GPS.

- Fiche : [Page produit Adafruit](https://www.adafruit.com/products/4754)
- Avis : [Forum SparkFun : réserves sur le cap magnétique (non utilisé ici)](https://community.sparkfun.com/t/inaccurate-heading-and-calibration-issues-with-bno085-imu/47544)

### Carte ESP32-S3 avec modem 4G SIMCom A7670E — ≈ 40–50 €

*Peu d’avis : validé au banc*

Le cerveau de la balise et sa liaison 4G : un microcontrôleur ESP32-S3 et un modem 4G sur la même carte.

**Pourquoi ce choix.** Aucune carte de ce type n’a d’avis indépendants solides. Le modem SIMCom A7670E est en revanche très répandu. On teste deux cartes au prototype (LilyGO et Waveshare) et on garde la plus fiable sur l’eau.

- Fiche : [LilyGO T-A7670E-S3 : documentation officielle](https://github.com/Xinyuan-LilyGO/LilyGO-T-A76XX)
- Fiche : [Waveshare ESP32-S3-A7670E-4G](https://www.waveshare.com/product/esp32-related/boards-kits/esp32-s3/esp32-s3-a7670e-4g.htm)
- Avis : [CNX Software : présentation des cartes Waveshare 4G](https://www.cnx-software.com/2024/02/20/waveshare-esp32-s3-4g-dev-boards-feature-lte-cat-1-2g-and-camera-support/)

### Adafruit LoRa RFM95W (868 MHz) — ≈ 20 €

*Peu d’avis : validé au banc*

La radio de secours, sur la balise et dans les deux récepteurs du PC course.

**Pourquoi ce choix.** Une carte Adafruit, réputée et très documentée, avec peu d’avis publiés mais positifs. Même module partout : balises et récepteurs sont interchangeables. Validation au banc puis sur l’eau.

- Fiche : [Page produit Adafruit (version 868/915 MHz)](https://www.adafruit.com/products/3231)
- Avis : [Avis clients Pimoroni](https://reviews.co.uk/product-reviews/store/shop-pimoroni-com/ADA3231)

## Bouées

### Gill WindSonic M (option) — ≈ 1 000–1 300 €, sur devis

*Référence professionnelle*

L’anémomètre des bouées : il mesure la vitesse et la direction du vent par ultrasons, sans pièce mobile.

**Pourquoi ce choix.** C’est une référence professionnelle, montée sur des navires de recherche. Le boîtier en aluminium anodisé est fait pour la mer. On a écarté le Calypso, plus léger et moins cher, mais avec des avis seulement moyens.

- Fiche : [Fiche technique WindSonic M](https://observator.com/download/datasheet-windsonic-m)
- Fiche : [Fiche produit (NauticExpo)](https://www.nauticexpo.com/prod/gill-instruments-ltd/product-39900-485171.html)
- Avis : [Utilisé sur le navire de recherche britannique RRS James Cook (NOC)](https://NOC.ac.uk/files/documents/facilities/james_cook/Gill_WindSonic.pdf)
- Avis : [Utilisé sur le navire de recherche américain Sally Ride (NOAA)](https://downloads.psl.noaa.gov/psd3/cruises/PISTON_2019/Sally_Ride/SCS/Sally_Met_Manual/Wind/WindSonicWebDatasheet.pdf)

## Base RTK

### Réseau Centipede RTK — gratuit

*Très bons avis*

Un réseau public et gratuit de stations RTK en France. Il sert de secours à notre propre base.

**Pourquoi ce choix.** Très utilisé par les agriculteurs et les géomètres, avec de bons retours. Si notre base tombe, les balises s’y connectent directement.

- Fiche : [Carte des stations](https://map.centipede.fr)
- Fiche : [Documentation](https://docs.centipede.fr/docs/publication)
- Avis : [Réussir : un réseau nettement plus performant](https://www.reussir.fr/machinisme/autoguidage-le-reseau-centipede-rtk-nettement-plus-performant-avec-millipede)
- Avis : [SciTePress 2025 : récepteurs bas coût sur Centipede](https://scitepress.org/PublishedPapers/2025/134448)

## PC course

### ASUS NUC 14 Pro — ≈ 800–1 000 €

*Très bons avis*

Le mini-ordinateur du PC course, en deux exemplaires : un principal et un de secours.

**Pourquoi ce choix.** Petit, silencieux, très bien noté par la presse spécialisée. Deux machines identiques : si l’une tombe, l’autre prend le relais.

- Fiche : [Page produit ASUS](https://asus.com/displays-desktops/nucs/nuc-kits/asus-nuc-14-pro)
- Avis : [ServeTheHome](https://www.servethehome.com/asus-nuc-14-pro-review-intel-core/)
- Avis : [Notebookcheck](https://www.notebookcheck.net/Asus-NUC-14-Pro-review-NUC-mini-PC-with-Intel-Core-Ultra-5-125H-fast-Intel-Arc-iGPU-and-2x-Thunderbolt-4.881404.0.html)

### Ubiquiti UniFi Cloud Gateway Ultra — ≈ 130 €

*Très bons avis*

Le routeur du PC course : il gère le réseau local, les réseaux séparés (organisation, équipes, caméras) et la bascule automatique vers la 5G.

**Pourquoi ce choix.** Très bien noté, simple à administrer, avec la bascule automatique entre deux accès Internet. Il remplace le routeur Teltonika initialement prévu, qui sera arrêté en 2027 et dont le successeur n’a pas encore d’avis.

- Fiche : [Fiche technique Ubiquiti](https://techspecs.ui.com/unifi/cloud-gateways/ucg-ultra)
- Avis : [iFeelTech : « the best $129 gateway »](https://ifeeltech.com/blog/unifi-cloud-gateway-ultra-review)
- Avis : [LazyAdmin : test détaillé](https://lazyadmin.nl/network/unifi-cloud-gateway-ultra/)

### Netgear Nighthawk M6 Pro — ≈ 700–900 €

*Très bons avis*

Le routeur 5G de poche qui prend le relais si la ligne filaire du site tombe.

**Pourquoi ce choix.** Le routeur 5G portable le mieux noté par la presse. Point à surveiller selon quelques utilisateurs : il peut chauffer. On le place à l’ombre et ventilé.

- Fiche : [Page produit Netgear](https://www.netgear.com/mobile-wifi/hotspots/mr6550/)
- Avis : [TechRadar](https://www.techradar.com/reviews/netgear-nighthawk-m6-pro-wi-fi-router-review)
- Avis : [T3](https://t3.com/reviews/netgear-nighthawk-m6-pro-review)

### EcoFlow River 2 Pro — ≈ 420–600 €

*Très bons avis*

La batterie de secours du PC course : elle prend le relais en cas de coupure de courant, comme un onduleur.

**Pourquoi ce choix.** Très bien notée. Environ 600 Wh utiles mesurés, soit 1 à 2 heures pour le PC course.

- Fiche : [Fiche technique (PDF)](https://www.cliftoncameras.co.uk/uploads/specifications/EcoFlow%20RIVER%202%20Pro%20UK%20Specifications.pdf)
- Avis : [OutdoorGearLab (janvier 2026)](https://www.outdoorgearlab.com/reviews/camping-and-hiking/power-station/ecoflow-river-2-pro)
- Avis : [AppleInsider](https://appleinsider.com/articles/23/05/10/ecoflow-river-2-pro-review-compact-design-with-expansive-power)

## Caméras et météo

### Reolink RLC-823S2 (zoom 16×) — ≈ 450–500 €

*Très bons avis*

La caméra motorisée du point haut, avec un zoom optique 16× pour suivre les bateaux à 300 m.

**Pourquoi ce choix.** Le modèle précédent est très bien noté pour la qualité d’image et la résistance aux intempéries. Elle remplace la Hikvision prévue au départ, dont le modèle est arrêté et les avis mitigés.

- Fiche : [Page produit Reolink](https://reolink.com/product/rlc-823s2/)
- Avis : [Mighty Gadget : test du modèle 16× précédent](https://mightygadget.co.uk/?p=682276)
- Avis : [Modern Castle : test du RLC-823A](https://moderncastle.com/reolink-rlc-823a-review/)

### Blackmagic ATEM Mini Pro — ≈ 300–350 €

*Très bons avis*

Le mélangeur vidéo : il passe d’une caméra à l’autre, ajoute les incrustations et diffuse en direct.

**Pourquoi ce choix.** La référence des petites régies de diffusion, saluée par toute la presse.

- Fiche : [Page Blackmagic ATEM Mini](https://www.blackmagicdesign.com/products/atemmini/workflow)
- Avis : [TechRadar](https://www.techradar.com/reviews/atem-mini-pro)
- Avis : [Streaming Media](https://www.streamingmedia.com/Producer/Articles/Editorial/Featured-Articles/Review-Blackmagic-Design-ATEM-Mini-Pro-140958.aspx)

### Davis Vantage Pro2 + WeatherLink Live — ≈ 900–1 100 €

*Très bons avis*

La station météo à terre : vent de référence, rafales, pression.

**Pourquoi ce choix.** La station de référence des passionnés et de nombreux clubs, très robuste. Elle remplace l’Ecowitt, dont les avis restent anecdotiques. À vérifier : la disponibilité de la passerelle WeatherLink Live, que Davis remplace par la WeatherLink Console.

- Fiche : [Page produit Davis](https://davisinstruments.com/products/vantage-pro2-weatherlink-live-bundle-with-airlink)
- Avis : [The Weather Station Experts : test du Vantage Pro2](https://theweatherstationexperts.com/davis-instruments-vantage-pro2-review/)
- Avis : [The Weather Station Experts : test de la WeatherLink Live](https://theweatherstationexperts.com/davis-weatherlink-live/)

### NVIDIA Jetson Orin Nano Super (option) — ≈ 250–300 €

*Très bons avis*

Un petit ordinateur pour l’analyse d’image : incrustations calées sur la vidéo, essais de détection des risées.

**Pourquoi ce choix.** Très bien noté, le standard du calcul d’image embarqué. En option seulement.

- Fiche : [Page produit NVIDIA](https://marketplace.nvidia.com/en-us/enterprise/robotics-edge/jetson-orin-nano-super-developer-kit)
- Avis : [StorageReview](https://www.storagereview.com/review/nvidia-jetson-orin-nano-super-powering-deepseek-r1-70b-inference-at-the-edge)
- Avis : [CNX Software](https://cnx-software.com/2024/12/18/249-nvidia-jetson-orin-nano-super-developer-kit-targets-generative-ai-applications-at-the-edge/)

## Outils

### TinySA Ultra — ≈ 120–150 €

*Très bons avis*

Un petit analyseur de fréquences : il montre quelles radios émettent sur le site.

**Pourquoi ce choix.** Très bien noté pour son prix. Il sert à vérifier chaque matin qu’aucune équipe ne brouille la radio de secours.

- Fiche : [Page revendeur Passion Radio](https://passion-radio.com/meter/tiny-sa-ultra-2543.html)
- Avis : [RTL-SDR : synthèse des tests](https://www.rtl-sdr.com/tinysa-ultra-reviews-a-0-1-mhz-6-ghz-spectrum-analyzer-for-120/)
- Avis : [W. Reeve : comparaison avec un appareil professionnel](https://reeve.com/Documents/Articles%20Papers/Reeve_TinySA-FPL_Compare.pdf)

## Signaux de départ

### Relais connecté Shelly 1 Gen3 — ≈ 20–25 €

*Peu d’avis : validé au banc*

Le petit relais qui actionne la corne quand le PC course le lui demande.

**Pourquoi ce choix.** Le relais connecté le plus répandu en domotique, qui parle MQTT nativement et fonctionne sans Internet. Pas de test indépendant trouvé : il sera validé au banc (100 déclenchements) puis chaque matin.

- Fiche : [Documentation Shelly 1 Gen3](https://www.shelly.com/blogs/documentation/shelly-1-gen3)
- Avis : [Retour d’un utilisateur (SmartThings) : MQTT et relais fiables](https://community.smartthings.com/t/integration-solutions-using-mqtt/245186/624)

### Corne électrique marine 12 V — ≈ 100–150 €

*Peu d’avis : validé au banc*

La corne de départ, alimentée par une batterie, installée sur la digue face à la ligne.

**Pourquoi ce choix.** Le modèle sera choisi après un essai de portée sur place : il faut être entendu à 150 m, vent de face, malgré le bruit de la plage. Les systèmes de départ du commerce (AutoHoot, iStart, SailBot) ont leur propre minuterie ; ici, c’est le PC course qui commande, pour rester calé sur le chrono des équipes.

- Fiche : [Sailing World : l’automatisation du comité de course](https://sailingworld.com/racing/the-automated-race-committee)
- Avis : [Scuttlebutt : les signaux sonores de la procédure](https://www.sailingscuttlebutt.com/2023/02/20/start-sequence-sound-signals/)
