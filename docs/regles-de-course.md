# Règles de course AI Regatta

> Le règlement du comité d’organisation fait foi. Ces règles en reprennent ce qui touche le dispositif, avec le paragraphe d’origine, et y ajoutent nos propositions, à soumettre au comité. Elles visent les régates de voiliers sous intelligence artificielle, sur parcours construit. Version 0.3 du 22 novembre 2026.

Source : Règlement de course AI Regatta 2027, V1.4 du 15/10/2026, de l’association Twelve Med Events (autorité organisatrice), reçu le 21 novembre 2026 de Xavier Caux.

« **Comité** » : repris du règlement de l’organisateur (paragraphe indiqué), il fait foi. « **Proposition** » : ajout de notre part, à soumettre au comité. Les P renvoient aux [postulats](postulats.md).

## 1. Cadre

- **1.1** **[Comité, § intro, 2d]** Le règlement de l’organisateur fait foi. Les Règles de course à la voile (RCV) de World Sailing s’appliquent au parcours construit. (P14)
- **1.2** **[Comité, § 1]** Épreuve concernée : les régates de voiliers sous intelligence artificielle (drones voiliers autonomes). Les slaloms, les Battleboats et les régates télécommandées ne relèvent pas de ce dossier.
- **1.3** **[Proposition]** **Position officielle** : la position donnée par la balise RTK (précision de 2 à 5 cm) fait foi pour le départ, les passages de bouées, la pénalité et l’arrivée. (P08)
- **1.4** **[Proposition]** **Zone de bouée** : 4 m autour de chaque bouée pour les bateaux de moins de 1,30 m ; à fixer avec le comité si des bateaux de 2,70 m courent ensemble.
- **1.5** **[Comité, § 5]** La zone de régate, sur les plages du Mourillon, est matérialisée par des bouées. **Proposition** : elle est aussi tracée dans le logiciel et sur les écrans des équipes.

## 2. Bateaux et homologation

- **2.1** **[Comité, § 3]** Propulsion vélique seule. Longueur hors tout, mesurée au départ : type 1 (moins de 1 m), type 1.3 (moins de 1,30 m), type 2.7 (moins de 2,70 m). Monocoques et multicoques, avec ou sans foils. Le bateau reste toujours en contact avec la mer ; le comité peut faire courir deux types ensemble. (P07)
- **2.2** **[Comité, § 2b, 11]** Homologation statique par un arbitre avant les régates ; toute modification significative ensuite lui est déclarée. Aucune pièce ne doit être larguée sur le plan d’eau. (P42)
- **2.3** **[Comité, § 12]** Batteries : LiFePO4, ou lithium avec circuit de protection (BMS) intégré et enveloppe solide du commerce, non démontée ; sinon sacs ignifuges et chargeur présenté à l’homologation. 48 V au plus. Un jeu de rechange chargé ; de quoi courir trois courses de suite. (P54)
- **2.4** **[Comité, § 10]** Numéro fourni à l’inscription, sur chaque côté de la voile, chiffres de 10 cm.
- **2.5** **[Proposition]** **Balise officielle** fournie et scellée par l’organisation dans chaque bateau, sans lien avec l’électronique de l’équipe, antennes sur le pont dans l’axe ; contrôlée à l’homologation. (P08, P09, P39)
- **2.6** **[Proposition]** Balise en panne pendant une course : réparation (RDG) si la panne vient du matériel officiel et qu’elle est prouvée par les journaux du PC course.
- **2.7** **[Proposition]** La sous-bande 869,4 – 869,65 MHz est réservée aux balises ; les équipes déclarent leurs émetteurs. Le règlement conseille déjà le Wi-Fi en 5 GHz (§ 13).
- **2.8** **[Proposition]** Bateau de référence : un IOM du commerce documenté dans le kit, conseillé, non imposé. (P47)

## 3. Commande des bateaux

- **3.1** **[Comité, § 2c]** Mode autonome obligatoire du passage de la ligne de départ jusqu’à l’arrivée. L’IA peut être embarquée ou à terre ; à terre, la télécommande est actionnée par programme, sans intervention humaine. (P10, P37)
- **3.2** **[Comité, § 2c]** Mode manuel à la télécommande permis pour rallier la ligne de départ, après l’arrivée, et pour reprendre la main en cas de défaillance, de sortie de la zone ou pour faire la pénalité. (P16, P38)
- **3.3** **[Comité, § 2c, 7]** Chaque reprise de la télécommande en course dure au plus Y secondes (30 s par défaut, annoncé avant chaque régate) et coûte un tour de pénalité, sauf pour faire la pénalité. (P38)
- **3.4** **[Proposition]** L’équipe déclare chaque reprise par un message `manual_control` (début, fin) dans sa boîte d’envoi ; le logiciel la chronomètre et l’affiche à l’arbitre. Chaque équipe garde le journal horodaté de ses commandes, fourni en cas de réclamation. (P44)
- **3.5** **[Proposition]** Le logiciel du bateau et de l’IA ne change pas pendant une course ; les mises à jour sont libres entre les courses. (P45)
- **3.6** **[Proposition]** Par sa propre liaison, une équipe envoie ce qu’elle veut à son bateau : ordres, paramètres, réglages, données officielles relayées. (P36)

## 4. Parcours et départ

- **4.1** **[Comité, § 5, parcours n°3]** Parcours construit : la porte 1-2 sert de départ, de porte et d’arrivée ; la bouée au vent est la 3, l’axe 1-3 perpendiculaire à la porte. Deux tours : départ par la porte 1-2, bouée 3 à bâbord, porte 1-2 (en contournant 1 ou 2, au choix), bouée 3 à bâbord, arrivée par la porte 1-2. (P04)
- **4.2** **[Comité, § 5]** Procédure de départ de la RCV 26 : signaux à 5 minutes, 4 minutes, 1 minute, puis départ. Par dérogation, une procédure d’une minute peut être courue. (P18)
- **4.3** **[Proposition]** Les signaux sonores sont déclenchés par le PC course à l’heure GPS, pour l’une ou l’autre procédure ; les pavillons restent hissés à la main. (P18)
- **4.4** **[Comité, § 5]** Chacun relève les coordonnées des bouées avant les courses ; l’organisateur cherche des partenaires pour les transmettre en temps réel (GPS RTK) avec la direction et la vitesse du vent. (P19)
- **4.5** **[Proposition]** **Réponse à cette demande** : la position RTK des bouées 1, 2, 3, P1 et P2 et le vent mesuré à la bouée 3 sont transmis en temps réel, au même instant, à toutes les équipes. (P52)
- **4.6** **[Proposition]** Pas de départ sous 4 nœuds ni au-dessus de 20 nœuds, mesurés à la bouée 3 ; valeurs à valider avec le directeur de course. (P43)
- **4.7** **[Comité, § 4]** Briefing chaque jour à 9 h 30 près de la zone de régate. Le tableau officiel est sur battleboats.fr ; les nouvelles publications sont annoncées sur WhatsApp. (P55)

## 5. Passages, pénalités et disqualifications

- **5.1** **[Comité, § 2d]** Les RCV s’appliquent : bâbord-tribord (10), au vent (11), route libre derrière (12), en virant (13), éviter le contact (14), place à la bouée (18), toucher une bouée (31). (P14)
- **5.2** **[Proposition]** Le logiciel signale à l’arbitre tout rapprochement de deux bateaux à moins de 1,5 m, la règle qui s’applique et la zone de bouée ; l’arbitre confirme toujours. (P15)
- **5.3** **[Comité, § 7]** Toute pénalité est un tour, fait à la fin, avant de franchir l’arrivée : passer entre la bouée 2 et P1, contourner P2 puis P1 en les laissant à bâbord. Le tour se fait en mode automatique ou à la télécommande. (P53)
- **5.4** **[Proposition]** Le logiciel suit le tour dans la zone P1-P2 et le valide pour l’arbitre. (P53)
- **5.5** **[Comité, § 7]** Disqualification : départ anticipé non réparé dans les 2 minutes ; bouée ou porte non franchie ou mal franchie ; ligne d’arrivée non franchie 5 minutes après le premier. (P46)
- **5.6** **[Proposition]** Le logiciel détecte au centimètre les départs anticipés, les passages de bouées et de portes et les arrivées, et ouvre la fenêtre des 5 minutes ; l’arbitre confirme.
- **5.7** **[Proposition]** Une sortie de la zone de régate de plus de 5 m ou de plus de 5 s est signalée à l’arbitre et à l’équipe.
- **5.8** **[Comité, § 7]** Une organisation présente sur l’eau récupère les bateaux en difficulté ; le bateau de sécurité peut dérouter un bateau en course. (P16)

## 6. Arbitrage, réclamations et classement

- **6.1** **[Proposition]** Deux arbitres à terre, chacun devant son écran : le premier suit le départ et les bouées, le second ouvre les rejeux et propose les décisions. (P15)
- **6.2** **[Proposition]** Les autres incidents passent par une réclamation, envoyée par un message `protest` dans la boîte d’envoi de l’équipe, dans les 10 minutes qui suivent l’arrivée du dernier bateau.
- **6.3** **[Comité, § 8]** Un classement par type de régate, sur les résultats des différentes courses. (P46)
- **6.4** **[Proposition]** Points : 1 au premier, 2 au deuxième, etc. ; une course retirée à partir de 5 courues. (P46)
- **6.5** **[Comité, § 17]** Un prix au premier de chaque type de régate ; des prix spéciaux.

## 7. Programme et équipes

- **7.1** **[Comité, § 6]** Du mercredi 12 au vendredi 14 mai, de 9 h à 18 h : chaîne d’inscription ; un parcours d’entraînement est mis à disposition. (P02)
- **7.2** **[Comité, § 6]** Samedi 15 mai : régates officielles, mise à disposition à 10 h. En cas de report au dimanche 16, les courses finissent au plus tard à 14 h 30 ; remise des prix le 16 à 16 h 30. (P02)
- **7.3** **[Comité, § 6]** Une régate de préchauffage au premier trimestre 2027 ; un bâtiment près du plan d’eau pendant un mois ; arrivée des équipes une semaine avant. (P56)
- **7.4** **[Comité, § 14]** Chaque équipe envoie avant le 1er mai une vidéo de moins de 30 s et une fiche A4 de présentation. (P55)
- **7.5** **[Proposition]** Les balises sont installées et contrôlées pendant la chaîne d’inscription, du 12 au 14 mai ; les équipes testent leur liaison au flux officiel dans le bâtiment prêté.
