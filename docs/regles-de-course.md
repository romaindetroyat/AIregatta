# Règles de course AI Regatta

> Le règlement du comité d’organisation fait foi. Ces règles en reprennent ce qui touche le dispositif, avec le paragraphe d’origine, et y ajoutent nos propositions, à soumettre au comité. Elles visent les régates de voiliers sous intelligence artificielle, sur parcours construit. Version 0.3 du 22 novembre 2026.

Source : Règlement de course AI Regatta 2027, V1.4 du 15/10/2026, de l’association Twelve Med Events (autorité organisatrice), reçu le 21 novembre 2026 de Xavier Caux.

« **Comité** » : repris du règlement de l’organisateur (paragraphe indiqué), il fait foi. « **Proposition** » : ajout de notre part, à soumettre au comité. Les P renvoient aux [postulats](postulats.md).

## 1. Cadre

- **1.1** **[Comité, § intro, 2d]** Le règlement de l’organisateur fait foi. Les Règles de course à la voile (RCV) de World Sailing s’appliquent au parcours construit. 
- **1.2** **[Comité, § 1]** Épreuve concernée : les régates de voiliers sous intelligence artificielle (drones voiliers autonomes). Les slaloms, les Battleboats et les régates télécommandées ne relèvent pas de ce dossier.
- **1.3** **[Proposition]** **Position officielle** : la position donnée par la balise RTK (précision de 2 à 5 cm) fait foi pour le départ, les passages de bouées, la pénalité et l’arrivée. 
- **1.4** **[Proposition]** **Zone de bouée** : 4 m autour de chaque bouée pour les bateaux de moins de 1,30 m; à fixer avec le comité si des bateaux de 2,70 m courent ensemble.
- **1.5** **[Comité, § 5]** La zone de régate, sur les plages du Mourillon, est matérialisée par des bouées. **Proposition** : elle est aussi tracée dans le logiciel et sur les écrans des équipes.

## 2. Bateaux et homologation

- **2.1** **[Comité, § 3]** Propulsion vélique seule. Longueur hors tout, mesurée au départ : type 1 (moins de 1 m), type 1.3 (moins de 1,30 m), type 2.7 (moins de 2,70 m). Monocoques et multicoques, avec ou sans foils. Le bateau reste toujours en contact avec la mer; le comité peut faire courir deux types ensemble. 
- **2.2** **[Comité, § 2b, 11]** Homologation statique par un arbitre avant les régates; toute modification significative ensuite lui est déclarée. Aucune pièce ne doit être larguée sur le plan d’eau. 
- **2.3** **[Comité, § 12]** Batteries : LiFePO4, ou lithium avec circuit de protection (BMS) intégré et enveloppe solide du commerce, non démontée; sinon sacs ignifuges et chargeur présenté à l’homologation. 48 V au plus. Un jeu de rechange chargé; de quoi courir trois courses de suite. 
- **2.4** **[Comité, § 10]** Numéro fourni à l’inscription, sur chaque côté de la voile, chiffres de 10 cm.
- **2.5** **[Proposition]** **Balise officielle**, imposée et fournie par l’organisation, implantée par l’équipe dans son bateau selon la fiche d’implantation (boîtier près de la quille, antennes sur le pont dans l’axe), sans lien avec l’électronique de l’équipe; contrôlée et scellée à l’homologation.
- **2.6** **[Proposition]** Balise en panne pendant une course : réparation (RDG) si la panne vient du matériel officiel et qu’elle est prouvée par les journaux du PC course.
- **2.7** **[Proposition]** La sous-bande 869,4 – 869,65 MHz est réservée aux balises; les équipes déclarent leurs émetteurs. Le règlement conseille déjà le Wi-Fi en 5 GHz (§ 13).
- **2.8** **[Proposition]** Bateau de référence : un IOM du commerce documenté dans le kit, conseillé, non imposé. 

## 3. Commande des bateaux

- **3.1** **[Comité, § 2c]** Mode autonome obligatoire du passage de la ligne de départ jusqu’à l’arrivée. L’IA peut être embarquée ou à terre; à terre, la télécommande est actionnée par programme, sans intervention humaine. 
- **3.2** **[Comité, § 2c]** Mode manuel à la télécommande permis pour rallier la ligne de départ, après l’arrivée, et pour reprendre la main en cas de défaillance, de sortie de la zone ou pour faire la pénalité. 
- **3.3** **[Comité, § 2c, 7]** Chaque reprise de la télécommande en course dure au plus Y secondes (30 s par défaut, annoncé avant chaque régate) et coûte un tour de pénalité, sauf pour faire la pénalité. 
- **3.4** **[Proposition]** L’équipe déclare chaque reprise par un message `manual_control` (début, fin) dans sa boîte d’envoi; le logiciel la chronomètre et l’affiche à l’arbitre. Chaque équipe garde le journal horodaté de ses commandes, fourni en cas de réclamation. 
- **3.5** **[Proposition]** Le logiciel du bateau et de l’IA ne change pas pendant une course; les mises à jour sont libres entre les courses. 
- **3.6** **[Proposition]** Par sa propre liaison, une équipe envoie ce qu’elle veut à son bateau : ordres, paramètres, réglages, données officielles relayées. 
- **3.7** **[Proposition]** **Flux officiel partagé** : toutes les équipes reçoivent, au même instant, la position de tous les bateaux et des bouées, le vent, le chrono et les événements. Même flux et même délai pour tous; un journal horodaté le prouve. 
- **3.8** **[Proposition]** **Perte du flux** : si le flux officiel s’interrompt en course, chaque bateau applique le comportement déclaré et montré à l’homologation (par exemple garder son cap quelques secondes, puis se mettre face au vent). Le comité peut interrompre la course; une équipe lésée par la panne peut demander réparation. 
- **3.9** **[Proposition]** **Capteurs libres** : une équipe peut embarquer ses propres capteurs (caméra, LIDAR de classe 1 ou 1M, § 12) en plus du flux officiel.

## 4. Parcours et départ

- **4.1** **[Comité, § 5, parcours n°3]** Parcours construit : la porte 1-2 sert de départ, de porte et d’arrivée; la bouée au vent est la 3, l’axe 1-3 perpendiculaire à la porte. Deux tours : départ par la porte 1-2, bouée 3 à bâbord, porte 1-2 (en contournant 1 ou 2, au choix), bouée 3 à bâbord, arrivée par la porte 1-2. 
- **4.2** **[Comité, § 5]** Procédure de départ de la RCV 26 : signaux à 5 minutes, 4 minutes, 1 minute, puis départ. Par dérogation, une procédure d’une minute peut être courue. 
- **4.3** **[Proposition]** Les signaux sonores sont déclenchés par le PC course à l’heure GPS, pour l’une ou l’autre procédure; les pavillons restent hissés à la main. 
- **4.4** **[Comité, § 5]** Chacun relève les coordonnées des bouées avant les courses; l’organisateur cherche des partenaires pour les transmettre en temps réel (GPS RTK) avec la direction et la vitesse du vent. 
- **4.5** **[Proposition]** **Réponse à cette demande** : la position RTK des bouées 1, 2, 3, P1 et P2 et le vent mesuré à la bouée 3 sont transmis en temps réel, au même instant, à toutes les équipes. 
- **4.6** **[Proposition]** Pas de départ sous 4 nœuds ni au-dessus de 20 nœuds, mesurés à la bouée 3; valeurs à valider avec le directeur de course. 
- **4.7** **[Comité, § 4]** Briefing chaque jour à 9 h 30 près de la zone de régate. Le tableau officiel est sur battleboats.fr; les nouvelles publications sont annoncées sur WhatsApp. 

## 5. Passages, pénalités et disqualifications

- **5.1** **[Comité, § 2d]** Les RCV s’appliquent : bâbord-tribord (10), au vent (11), route libre derrière (12), en virant (13), éviter le contact (14), place à la bouée (18), toucher une bouée (31). 
- **5.2** **[Proposition]** Le logiciel ne juge pas les contacts : il enregistre tout rapprochement de deux bateaux à moins de 1,5 m et prépare le rejeu, avec la règle qui s’applique et la zone de bouée. L’arbitre ne l’ouvre que sur réclamation (6.2).
- **5.3** **[Comité, § 7]** Toute pénalité est un tour, fait à la fin, avant de franchir l’arrivée : passer entre la bouée 2 et P1, contourner P2 puis P1 en les laissant à bâbord. Le tour se fait en mode automatique ou à la télécommande. 
- **5.4** **[Proposition]** Le logiciel suit le tour dans la zone P1-P2 et le valide pour l’arbitre. 
- **5.5** **[Comité, § 7]** Disqualification : départ anticipé non réparé dans les 2 minutes; bouée ou porte non franchie ou mal franchie; ligne d’arrivée non franchie 5 minutes après le premier. 
- **5.6** **[Proposition]** Le logiciel détecte au centimètre les départs anticipés, les passages de bouées et de portes, les bouées touchées et les arrivées, et ouvre la fenêtre des 5 minutes; il le signale de lui-même à l’arbitre, qui confirme.
- **5.7** **[Proposition]** Une sortie de la zone de régate de plus de 5 m ou de plus de 5 s est signalée à l’arbitre et à l’équipe.
- **5.8** **[Comité, § 7]** Une organisation présente sur l’eau récupère les bateaux en difficulté; le bateau de sécurité peut dérouter un bateau en course. 

## 6. Arbitrage, réclamations et classement

- **6.1** **[Proposition]** Deux arbitres à terre, chacun devant son écran : le premier confirme ce que le logiciel détecte (départ, bouées, tour de pénalité, arrivée), le second juge les réclamations sur rejeu.
- **6.2** **[Proposition]** Réclamation en direct. Un contact ou une question de priorité (règles 10 à 18) n’est jugé que sur réclamation : l’équipe envoie un message `protest` (bateau visé, instant, règle) dans les 10 s qui suivent l’incident, à la main ou par son IA. L’arbitre décide sur le rejeu dans la minute : pénalité (un tour, 5.3), rejet ou renvoi au jury; la décision part aux deux équipes, puis au public.
- **6.3** **[Proposition]** Garde-fous : une réclamation n’est recevable que si les balises montrent les deux bateaux à moins de 2 m l’un de l’autre dans les 10 s qui précèdent; trois réclamations au plus par équipe et par course; une réclamation rejetée ne coûte rien, mais elle est publiée.
- **6.4** **[Proposition]** Une réclamation qui ne peut plus se régler par un tour (bateau visé déjà arrivé, renvoi au jury) se juge après la course : disqualification ou rejet. Les autres incidents passent par une réclamation dans les 10 minutes qui suivent l’arrivée du dernier bateau.
- **6.5** **[Comité, § 8]** Un classement par type de régate, sur les résultats des différentes courses. 
- **6.6** **[Proposition]** Points : 1 au premier, 2 au deuxième, etc.; une course retirée à partir de 5 courues. 
- **6.7** **[Comité, § 17]** Un prix au premier de chaque type de régate; des prix spéciaux.

## 7. Programme et équipes

- **7.1** **[Comité, § 6]** Du mercredi 12 au vendredi 14 mai, de 9 h à 18 h : chaîne d’inscription; un parcours d’entraînement est mis à disposition. 
- **7.2** **[Comité, § 6]** Samedi 15 mai : régates officielles, mise à disposition à 10 h. En cas de report au dimanche 16, les courses finissent au plus tard à 14 h 30; remise des prix le 16 à 16 h 30. 
- **7.3** **[Comité, § 6]** Une régate de préchauffage au premier trimestre 2027; un bâtiment près du plan d’eau pendant un mois; arrivée des équipes une semaine avant. 
- **7.4** **[Comité, § 14]** Chaque équipe envoie avant le 1er mai une vidéo de moins de 30 s et une fiche A4 de présentation. 
- **7.5** **[Proposition]** Chaque équipe reçoit la fiche d’implantation de la balise en décembre, et la balise à son arrivée sur le site, une semaine avant la course; elle l’implante, puis l’arbitre la contrôle et la scelle pendant la chaîne d’inscription, du 12 au 14 mai. Les équipes testent leur liaison au flux officiel dans le bâtiment prêté.
