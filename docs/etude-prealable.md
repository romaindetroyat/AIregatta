# Le dispositif technique de l’AI Regatta

*Étude préalable · 22 novembre 2026*

## En bref

L’AI Regatta est une régate de voiliers radiocommandés pilotés par intelligence artificielle, organisée par l’association Twelve Med Events dans le cadre de la Toulon Provence Regatta. Les régates ont lieu le samedi 15 mai 2027 sur les plages du Mourillon, avec le dimanche en réserve.

Le règlement de l’organisateur, reçu le 21 novembre, fixe la course. Il dit aussi ce qui lui manque : transmettre en temps réel la position des bouées et le vent, « si nous trouvons les partenaires nécessaires ». Cette étude propose d’être ce partenaire, puis d’aller plus loin en suivant chaque bateau au centimètre pour aider l’arbitrage.

Le premier niveau coûte environ 6 300 € de matériel, le second environ 15 300 € de plus. Tout le monde est bénévole : seul le matériel se paie.

## Ce que fixe le règlement

Le règlement fait foi, et il est déjà précis. Les voiliers, de moins d’un mètre à 2,70 m, monocoques ou multicoques, courent en mode autonome de la ligne de départ à l’arrivée ; leur intelligence peut être embarquée ou à terre. La télécommande sert à rallier le départ et à reprendre la main après l’arrivée ou en cas de problème, mais chaque reprise en course est limitée à 30 secondes et coûte un tour de pénalité.

Le parcours compte trois bouées : une porte 1-2 qui sert de départ, de passage et d’arrivée, et une bouée au vent, la 3, à laisser deux fois à bâbord. Les pénalités se font à la fin, par une petite boucle autour de deux bouées, P1 et P2. Sont disqualifiés le bateau parti trop tôt qui n’est pas revenu dans les deux minutes, celui qui passe mal une bouée et celui qui arrive plus de cinq minutes après le premier. Les équipes s’inscrivent du 12 au 14 mai, passent une homologation statique, puis courent le 15.

Ce que le règlement ne dit pas est tout aussi instructif : rien ne permet de mesurer ce qu’il impose. Un départ anticipé, une bouée mal passée, la durée d’une reprise de télécommande ou la fenêtre des cinq minutes se jugent à l’œil, sur des bateaux d’un mètre, à plus de cent mètres de la plage.

## Ce que nous proposons

Nous proposons un dispositif en deux niveaux, le second prolongeant le premier.

**Le niveau 1 répond exactement à la demande de l’organisateur.** Une balise GPS précise au centimètre sur chacune des trois bouées, un anémomètre à ultrasons sur la bouée au vent et une station de référence à terre : la position des bouées et le vent partent chaque seconde vers un serveur en ligne, qui les transmet au même instant à toutes les équipes. Leurs IA n’ont plus à relever les bouées à la main, et elles naviguent avec le vent réellement mesuré sur l’eau.

**Le niveau 2 comble ce que le règlement ne couvre pas.** Chaque bateau porte une balise scellée, sans lien avec l’électronique de son équipe, qui donne sa position dix fois par seconde. Un PC course reçoit tout ; il détecte les départs anticipés, les passages de bouées, les tours de pénalité et les arrivées, et il chronomètre les reprises de télécommande. L’arbitre confirme toujours. Le même flux est partagé avec toutes les équipes : chaque IA connaît la position de tous les bateaux, ce qui est plus fiable qu’un capteur embarqué et évite aux équipes d’en acheter. Le public suit la course sur une application et en vidéo.

Le niveau 2 suppose que le comité d’organisation l’inscrive dans son règlement : la balise contrôlée à l’homologation, une bande radio réservée, et une règle pour le cas où le flux s’interrompt.

## Comment ça marche

Trois choix portent l’ensemble. La position vient d’un récepteur GPS RTK, précis à deux à cinq centimètres grâce aux corrections d’une station fixe : c’est la technique des drones et des tracteurs autonomes, abondamment documentée. Les données passent par la 4G, avec une radio 868 MHz en secours si le réseau sature un samedi de mai. Enfin, l’heure GPS date chaque mesure : c’est elle qui rend l’arbitrage incontestable et l’équité vérifiable.

Une balise pèse environ 250 g, tient une journée sur une batterie du commerce admise par le règlement, et coûte 455 € de pièces. La compatibilité de toute la chaîne a déjà été contrôlée ; ce contrôle a conduit à remplacer le mélangeur vidéo et à préciser plusieurs branchements. Le reste (serveurs, logiciel, applications) repose sur des briques connues. Meridia développe le logiciel avec des agents IA ; une personne fiable porte la technique.

## Ce que ça coûte

Le niveau 1 demande environ 6 300 € de matériel, imprévus compris : quatre balises (trois bouées et une de rechange), l’anémomètre, la station de référence, un routeur 5G et les prototypes. Le niveau 2 ajoute environ 15 300 € : douze balises pour les bateaux, le PC course et son réseau, la radio de secours, une caméra et sa régie, les signaux de départ et des caméras embarquées. Le total atteint 21 600 €.

Le temps passé ne coûte rien : tout le monde est bénévole. Le financement relève de l’organisateur ou d’une autre instance.

## Le calendrier

Tout commence par une présentation à Xavier Caux, de Twelve Med Events, avant le 11 décembre. Deux balises prototypes sont commandées en décembre (environ 1 900 €) et testées sur l’eau du 20 au 23 janvier ; fin janvier, une revue décide de la série.

Les seize balises sont commandées début février et montées jusqu’au 5 mars ; le niveau 1 peut alors être démontré à la régate de préchauffage que l’organisateur prévoit au premier trimestre. Mars et avril servent aux essais du système complet, à une régate blanche et à une répétition générale. Le montage sur site a lieu du 7 au 11 mai, avant l’homologation et la course.

Le chemin critique est celui des balises : un retard en février se répercute jusqu’en mai.

## Les chances de réussite

Nous les estimons ainsi au 22 novembre 2026.

**Le niveau 1 a environ quatre chances sur cinq (80 %)** de fonctionner le jour de la course. L’organisateur le demande lui-même, le matériel tient en quelques pièces éprouvées et l’équipe est en place. Le risque principal est de ne pas conclure à temps avec le comité, puis la 4G le samedi. Une présentation rapide et une démonstration à la régate de préchauffage le portent à 95 %. Avant le règlement, nous l’estimions à 90 % ; il dépend désormais aussi de l’accord de l’organisateur.

**Le niveau 2 a aujourd’hui un peu moins d’une chance sur deux (45 %).** Ce n’est pas la technique qui pèse le plus, c’est l’accord du comité, que nous estimons à deux chances sur trois tant que nous ne lui avons rien présenté. Viennent ensuite la fabrication des seize balises en février, qui repose sur une seule personne, et la préparation des équipes, qui ne dépend pas de nous. Avec les mesures proposées (présentation avant le 11 décembre, démonstration au préchauffage, fabrication à deux, kit des équipes livré tôt), il monte à environ 70 %.

**Une belle course a environ trois chances sur dix (30 %)**, six sur dix avec les mesures : le dispositif complet, des courses lisibles, des arbitres qui suivent et un vent entre 4 et 20 nœuds le 15 ou le 16. La météo d’une seule journée et la charge des arbitres sur une flotte entière restent les deux inconnues que personne ne maîtrise complètement.

Ces chiffres sont des estimations de jugement, pas des mesures : ils servent à voir où porter l’effort.

## Ce qu’il reste à décider

Avec l’organisateur : son accord sur les deux niveaux ; l’emplacement du PC course ; la longueur du parcours, la largeur de la porte et la position de P1 et P2 ; le nombre de voiliers attendus et le format des courses ; qui arbitre ; la date de la régate de préchauffage. Le mail annonce aussi une première masterclass le « vendredi 29 novembre », qui tombe un dimanche : la date est à vérifier.

De notre côté : les bateaux pour les essais de janvier, à trouver avant le 4 décembre, et le choix entre des mini-PC neufs et des ordinateurs existants, avant la commande de mars.

Les annexes détaillent chaque point : le règlement et nos propositions, le dispositif, la technique, le logiciel et le prototype, le projet, le kit des équipes et les questions.
