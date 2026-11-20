# Règles de course AI Regatta

> Ces règles s’appliquent à AI Regatta (Toulon, 12 – 16 mai 2027). Elles partent des Règles de course à la voile (RCV) 2025 – 2028 de World Sailing, de leur annexe E (bateaux radiocommandés) et de l’arbitrage en direct du match racing radiocommandé. Elles les remplacent là où elles diffèrent. Version 0.1 du 20 novembre 2026, à faire relire par un arbitre agréé avant publication aux équipes.

Les références entre crochets renvoient aux [postulats](postulats.md) (P) et aux décisions de la [spécification des applications](maquettes.md) (D). Les points marqués « à trancher » restent ouverts.

## 1. Définitions

- **1.1** **Bateau** : voilier drone engagé, sans personne à bord, équipé de la balise officielle.
- **1.2** **IA tactique** : le logiciel de l’équipe, à terre, qui décide de la conduite du bateau. **Pilote automatique** : l’électronique à bord qui exécute. [P37]
- **1.3** **Manche** : du signal d’avertissement jusqu’à l’arrivée du bateau, son abandon ou la fin du temps limite.
- **1.4** **Position officielle** : la position donnée par la balise RTK (précision ± 2 cm). Elle seule fait foi pour le départ, les bouées, la zone de course, l’arrivée et l’arbitrage. [P08]
- **1.5** **Zone de bouée** : le cercle de 4 m de rayon autour de chaque bouée (quatre longueurs d’un bateau de 1 m, valeur unique pour tous).
- **1.6** **Zone de course** : le rectangle délimité par le comité, matérialisé dans le logiciel (géorepérage) et sur les écrans des équipes.

## 2. Parcours et format

- **2.1** Parcours aller-retour d’environ 200 m (longueur à valider), orienté selon le vent du jour : départ, bouée au vent laissée à bâbord, porte sous le vent (deux bouées, au choix), deux tours, arrivée sous le vent. [P04]
- **2.2** Le comité peut changer le parcours entre deux manches. Une bouée est déplacée par un bateau d’assistance ; le comité l’annonce sur le flux de course, à toutes les équipes en même temps, avant que la nouvelle position ne serve. [P19]
- **2.3** Toutes les équipes reçoivent les mêmes données officielles au même instant : positions des bateaux et des bouées, vent, chrono. [P11]

## 3. Commande des bateaux

- **3.1** Pendant une manche, un bateau n’est commandé que par l’IA tactique de son équipe, sans aucune intervention humaine : ni manette, ni ordre saisi à la main, ni réglage manuel. [D11]
- **3.2** L’IA peut envoyer des ordres tactiques au pilote automatique (vire, empanne, abats, loffe, face au vent ; modes près, portant, VMG, haut, bas) ou commander directement le safran et les voiles. [P36, D11]
- **3.3** Seule action humaine permise : l’arrêt de sécurité, en cas de danger. Il met le bateau face au vent et prévient le comité. Le bateau abandonne la manche ; le comité peut accorder une réparation si le danger ne venait pas de l’équipe. [D11]
- **3.4** Chaque équipe enregistre, avec l’heure, toutes les commandes envoyées à son bateau et remet ce journal au comité sur demande. Une intervention humaine hors arrêt de sécurité entraîne la disqualification de la manche (DSQ).
- **3.5** Mise à jour du logiciel du bateau pendant une manche : à trancher (proposé : interdite pendant une manche, permise entre les manches). [D12]
- **3.6** Paramètres joints aux ordres et relais des données officielles vers le bateau : à trancher (proposé : autorisés). [D9, D10]

## 4. Balise officielle et équipement

- **4.1** Chaque bateau porte la balise fournie par l’organisation, scellée, sans lien avec l’électronique de l’équipe. [P09]
- **4.2** Les antennes de la balise sont sur le pont, dans l’axe du bateau, quelle que soit la matière de la coque. Le comité contrôle l’installation avant la première manche. [Q1]
- **4.3** Balise en panne pendant une manche : le bateau reçoit une réparation (RDG) si la panne vient du matériel officiel et qu’elle est prouvée par les journaux du PC course. Aucune réparation si la panne vient de l’installation de l’équipe. [D6]
- **4.4** Radiocommande de sécurité 2,4 GHz à bord : à trancher (obligatoire ou seulement conseillée). [D14]

## 5. Départ

- **5.1** Procédure d’une minute, signaux sonores déclenchés par le PC course : avertissement à −1:00, préparatoire (pavillon P) à −0:40, dernière étape à −0:20, départ à 0:00. [P18]
- **5.2** Départ anticipé : si, au signal, une partie de la coque est du côté parcours de la ligne, le logiciel le signale et l’arbitre ordonne un rappel individuel (pavillon X). Le bateau doit revenir couper la ligne du côté départ ; sinon il est classé OCS.
- **5.3** Le comité peut ordonner un rappel général, retarder le départ (Aperçu) ou annuler la manche (N). Chaque décision part sur le flux vers les équipes, la télévision et le public.
- **5.4** Un bateau qui n’a pas coupé la ligne 2 minutes après le signal de départ est classé non parti (DNS).

## 6. Règles de passage

- **6.1** **Bâbord et tribord** : un bateau bâbord amures (le vent arrive par sa gauche) s’écarte d’un bateau tribord amures (RCV 10). [D1]
- **6.2** **Au vent et sous le vent** : deux bateaux engagés à la même amure, celui qui est au vent s’écarte de celui qui est sous le vent (RCV 11). [D1]
- **6.3** **Route libre derrière** : deux bateaux non engagés à la même amure, celui qui est derrière s’écarte de celui qui est devant (RCV 12). Deux bateaux sont engagés quand aucun n’est entièrement derrière l’autre. [D1]
- **6.4** **En virant** : entre le passage face au vent et sa nouvelle route au près, un bateau qui vire s’écarte des autres (RCV 13). [D1]
- **6.5** **Éviter le contact** : chaque bateau, même prioritaire, évite le contact s’il le peut raisonnablement (RCV 14). [D1]
- **6.6** **Place à la bouée** : dans la zone de 4 m, le bateau qui y est entré le premier, ou engagé à l’intérieur au moment où le premier y entre, a droit à la place pour passer la bouée (RCV 18). Le logiciel établit l’ordre d’entrée et l’engagement à partir des positions officielles. [D1]
- **6.7** **Toucher une bouée** : un bateau qui touche une bouée fait un tour de pénalité (RCV 31). Le logiciel détecte la coque à moins de 0,75 m du centre de la bouée.
- **6.8** Le logiciel signale à l’arbitre tout rapprochement de deux bateaux à moins de 1,5 m, la règle qui s’applique selon leurs amures, leur position et la zone, et le bateau qui devait s’écarter. L’arbitre décide.

## 7. Pénalités

- **7.1** La pénalité est un tour de 360°, comprenant un virement et un empannage, fait à l’écart des autres bateaux. Le logiciel détecte le tour automatiquement. [D2]
- **7.2** La pénalité est notifiée à l’IA de l’équipe par le flux de course, en même temps qu’au comité, à la télévision et au public. L’IA doit savoir l’exécuter seule. [D2, D11]
- **7.3** Si le tour n’est pas fait dans les 20 secondes qui suivent la notification, le bateau reçoit une pénalité en temps de 20 secondes à l’arrivée. [D2]
- **7.4** Une faute grave, dangereuse ou répétée peut être sanctionnée par la disqualification de la manche (DSQ).

## 8. Zone de course

- **8.1** Un bateau qui sort de la zone de course de plus de 5 m, ou qui y reste dehors plus de 5 secondes, reçoit une pénalité d’un tour, à faire après être rentré. [D4]
- **8.2** Le logiciel signale la sortie, la distance et la durée ; l’équipe voit la limite sur son écran.

## 9. Arbitrage, réclamations et réparations

- **9.1** Deux arbitres à terre, chacun devant son écran : le premier suit le départ et les bouées, le second ouvre les rejeux et propose les décisions. Le logiciel signale, un arbitre décide. [Q6, P15]
- **9.2** Incidents signalés par le logiciel : jugés en direct, avec le rejeu vu de dessus. Décisions possibles : pénalité d’un tour, pénalité en temps, sans suite, renvoi au jury. [D3]
- **9.3** Les autres incidents passent par une réclamation, déposée sur l’application des équipes dans les 10 minutes qui suivent l’arrivée du dernier bateau. Une demande de réparation suit le même délai. [D3, D5]
- **9.4** Une décision prise en direct par l’arbitre ne peut pas faire l’objet d’une réclamation, sauf erreur de procédure.
- **9.5** Le jury juge les réclamations après la manche, avec les rejeux et les journaux du PC course. Composition du jury : à trancher.

## 10. Arrivée, temps limite et classement

- **10.1** Un bateau arrive quand une partie de sa coque coupe la ligne d’arrivée, après avoir fait le parcours, d’après la position officielle.
- **10.2** Temps limite : 15 minutes après le signal de départ. Un bateau qui n’est pas arrivé est classé non arrivé (DNF). [D5]
- **10.3** Points : 1 au premier, 2 au deuxième, etc. ; un bateau DNS, DNF, OCS ou DSQ reçoit le nombre d’inscrits plus un. Le plus petit total gagne. Manches retirées du total : à trancher.

## 11. Sécurité

- **11.1** Des bateaux d’assistance surveillent le plan d’eau. Un bateau désemparé est récupéré par l’assistance et abandonne la manche. [P16]
- **11.2** Le comité peut interrompre ou annuler une manche à tout moment pour la sécurité ; chaque équipe arrête alors son bateau.
