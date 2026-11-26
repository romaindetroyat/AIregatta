# Kit équipes — Le bateau de référence

> Fiche 0.2 du 26 novembre 2026. Un bateau type pour naviguer vite : **un IOM du commerce, une liaison ExpressLRS avec l’ordinateur, une IA minimale**. Il est **conseillé, non imposé** (P47) : vous restez libres de faire autrement, dans la jauge. Cette fiche est une proposition : aucun bateau n’a encore été monté ainsi, et plusieurs points restent à valider (voir la fin).

## En bref

- **Le bateau** : un voilier radiocommandé de la classe IOM (1 m), d’occasion de préférence : 450 à 1 500 €.
- **La liaison** : un des trois montages de [liaison-bateau.md](liaison-bateau.md). En A et B, seul le récepteur change dans le bateau (≈ 60 à 170 €) ; en C, on ajoute un pilote automatique à bord (≈ 240 à 260 €).
- **L’IA** : sur votre ordinateur à terre, elle lit le flux officiel et envoie des ordres de tacticien. Huit comportements suffisent pour la qualification.
- **Le délai** : huit semaines entre l’achat du bateau et le premier parcours complet.

## À bord

| N° | Élément | À qui | Où et pourquoi |
|---|---|---|---|
| 1 | **Balise officielle** | Organisation, implantée par l’équipe | Imposée et fournie par l’organisation, implantée par l’équipe selon la fiche d’implantation : boîtier de ≈ 250 g au fond, près de la quille ; antennes sur le pont, dans l’axe. Rien au-dessus de son antenne GPS. Contrôlée et scellée par l’arbitre à l’homologation. |
| 2 | **Récepteur ExpressLRS** | Équipe | Remplace le récepteur d’origine : ER4 en A et B (safran sur la sortie 1, écoute sur la sortie 3), RP2 relié au pilote en C. Antenne haute, au sec, à 20 cm au moins des antennes officielles. |
| 3 | **Pilote automatique** (montage C) | Équipe | Carte Matek H743-WING avec le logiciel libre ArduPilot, réglé en voilier. Il tient un cap, règle l’écoute et vire seul. |
| 4 | **GPS et compas de l’équipe** (montage C) | Équipe | Sur le pont arrière, loin du treuil (aimants) et à 20 cm au moins des antennes officielles. |
| 5 | **Girouette** (montage C) | Équipe | En tête de mât ou sur une petite perche à l’arrière : elle donne au pilote l’angle du vent. |
| 6 | **Treuil d’écoute** | Le bateau | Celui du bateau. Une seule écoute règle grand-voile et foc, comme sur tout IOM. |
| 7 | **Servo de safran** | Le bateau | Celui du bateau. |
| 8 | **Batterie** | Équipe | En A et B, celle d’origine suffit. En C, une batterie 3S (la carte demande 8 V au moins), qui alimente aussi les servos. La balise officielle a la sienne. |

L’installation de la balise est détaillée dans le document général, page « À bord ».

## La jauge

Le règlement de l’organisateur n’impose pas de jauge de classe : voile seule, moins de 1 m, 1,30 m ou 2,70 m, multicoques et foils admis. L’IOM reste le bateau de référence conseillé ; en IOM, on garde :

- Coque : 1 000 mm de long au plus ; pas de fibre plus raide que le verre, donc pas de carbone dans la coque
- Tirant d’eau : 420 mm au plus
- Quille et safran démontables ; lest (bulbe) de 2 500 g au plus
- Trois gréements monotypes A, B et C, et leurs voiles
- Poids du bateau prêt à naviguer : 4 000 g au moins
- Deux commandes seulement : le safran et une écoute (proposé : on garde cette limite)

**Libre, par dérogation** :

- La balise officielle et ses antennes sur le pont
- Un pilote automatique et son logiciel
- Les capteurs : GPS, compas, centrale inertielle, girouette, anémomètre
- Une liaison radio ExpressLRS, dans les deux sens (la jauge IOM interdit d’émettre depuis le bateau : on y déroge)
- La caméra embarquée de l’organisation
- Une batterie de capacité libre

Les limites IOM ci-dessus viennent de résumés de la classe ; le texte en vigueur (édition de mars 2026) fait foi. Les dérogations restent à écrire avec un jaugeur.

## Le budget

| Poste | Ordre de grandeur | Source |
|---|---|---|
| IOM d’occasion, en état de naviguer, gréement A au moins | 450 à 1 500 € | annonces relevées en France |
| ou IOM neuf, tout équipé | ≈ 3 000 € | jusqu’à 6 mois d’attente : trop tard pour mai |
| Liaison, montage A : radio imposée, récepteur, boîtier | ≈ 100 à 170 € | prix relevés en boutique, novembre 2026 |
| ou montage B : émetteur, câble, récepteur | ≈ 60 à 90 € | prix relevés en boutique, novembre 2026 |
| ou montage C : émetteur, récepteur, carte H743-WING (109,90 €), GPS et compas (26,91 €), girouette fabriquée (≈ 21 €), batterie 3S (18,90 €) | ≈ 240 à 260 € | prix relevés en boutique, novembre 2026 |

Soit **≈ 510 à 1 760 €** avec un IOM d’occasion. Un IOM neuf n’arrive pas à temps : cherchez d’occasion (forum de la Classe 1 Mètre France, petites annonces de modélisme) ou auprès d’un club de voile radiocommandée.

## Le poids

| Élément | Masse |
|---|---|
| Balise officielle | ≈ 250 g |
| Récepteur ExpressLRS et antenne | ≈ 5 g |
| Montage C seulement : carte, GPS et compas | ≈ 60 g |
| Montage C seulement : girouette et son câble | ≈ 40 g |
| Montage C seulement : câbles, supports | ≈ 30 g |
| Montage C seulement : batterie 3S (surpoids) | ≈ 70 g |
| **Total ajouté** | **≈ 255 g en A et B, ≈ 455 g en C** |

Un IOM pèse 4 000 g au moins, masses correctrices comprises quand il en porte. Retirer les masses correctrices compense en partie. Estimations à peser.

## Montage C : réglages de départ du pilote automatique

Les noms sont ceux d’ArduPilot Rover ; vérifiez-les dans la documentation de votre version.

1. **Activer le voilier.** SAIL_ENABLE = 1, puis redémarrer.
2. **Déclarer les deux commandes.** La sortie du treuil reçoit la fonction « écoute de grand-voile » (89) ; celle du safran, la fonction « direction ».
3. **Dire d’où vient le vent.** Avec une girouette : WNDVN_TYPE selon le capteur. Sans girouette, pour débuter : WNDVN_TYPE = 1, le vent est supposé rester celui du cap au moment de l’armement.
4. **Régler la voile.** SAIL_ANGLE_MIN et SAIL_ANGLE_MAX : l’angle de la bôme, écoute bordée puis choquée. SAIL_ANGLE_IDEAL : l’angle visé entre la bôme et le vent.
5. **Régler le près.** SAIL_NO_GO_ANGLE : l’angle au vent en dessous duquel le bateau ne va pas ; il vire seul quand le cap demandé tombe dedans. Partir de 45°.
6. **Brancher la liaison.** Le récepteur RP2 sur un port série de la carte ; l’émetteur et le récepteur réglés en mode « MAVLink » (ExpressLRS 3.5 au moins). L’ordinateur se branche en USB sur l’émetteur. Voir [liaison-bateau.md](liaison-bateau.md).
7. **Prévoir la perte de liaison.** Si l’ordinateur ne répond plus : garder le cap quelques secondes, puis rejoindre un point de sécurité ou se mettre face au vent. C’est le comportement à déclarer et à démontrer.

## L’IA minimale : huit comportements

Elle tourne sur votre ordinateur à terre, lit le flux officiel ([contrat-interface.md](contrat-interface.md)) : votre position et votre cap, les bouées, le vent, les autres bateaux, les événements. Elle envoie des ordres de tacticien au programme de liaison.

1. **Attendre** : avant le départ, tenir une zone sous la ligne et la couper au signal, pas avant.
2. **Remonter au vent** : tirer des bords vers la bouée au vent (en C, il suffit de donner au pilote le point à rejoindre).
3. **Contourner** : laisser la bouée au vent à bâbord, à 2 m, puis abattre ; à la porte, passer entre les deux bouées et loffer.
4. **Descendre** : viser la porte ; empanner si l’autre bord rapproche.
5. **Compter** : deux tours, puis la ligne d’arrivée.
6. **Rester dans la zone** : faire demi-tour avant la limite du parcours.
7. **Céder le passage** : s’écarter d’un bateau prioritaire à moins de 3 m : tribord amures, sous le vent, ou devant.
8. **Se pénaliser** : à la notification du comité, faire un tour complet avec un virement et un empannage, puis reprendre.

Les cinq premiers font boucler un parcours ; les trois derniers évitent les pénalités. Tout le reste, c’est votre tactique.

## Huit semaines pour naviguer

| Quand | Étape |
|---|---|
| Semaines 1 et 2 | Trouver l’IOM ; le faire naviguer à la main. |
| Semaine 3 | Monter la liaison sur table : récepteur, servos, ordinateur (en C : la carte et ses capteurs). |
| Semaine 4 | Première sortie : cap tenu, écoute réglée depuis l’ordinateur. |
| Semaine 5 | Virements et empannages automatiques ; un triangle de bouées. |
| Semaine 6 | Le parcours complet, seul, piloté par l’IA à terre. |
| Semaine 7 | Tour de pénalité sur ordre ; perte de liaison. |
| Semaine 8 | Branchement sur le flux officiel du bac à sable. |

## Ce que le bateau doit savoir faire

- Boucler seul le parcours n°3, deux tours, en mode autonome
- Faire le tour de pénalité par la zone P1-P2, avant l’arrivée
- Pour une équipe qui a une radio de secours : reprendre la main et la rendre à l’IA en moins de 30 s
- Au contrôle d’équipement (pas à la qualification) : montrer le comportement déclaré en cas de perte de liaison ou du flux officiel

## Ce qui reste à valider

- Les dérogations à la jauge IOM, à écrire avec un jaugeur de la classe : émissions radio, deux commandes seulement, et le poids. La balise et l’électronique pèsent ≈ 450 g : comptent-elles dans les 4 000 g, ou remplacent-elles les masses correctrices ?
- La place de la girouette : en tête de mât, elle voit un vent propre mais pèse en hauteur ; à l’arrière, elle est dans le dévent des voiles.
- Le compas près du treuil et du lest : étalonnage à faire bateau complet.
- La cohabitation des radios : la liaison de l’équipe ne doit gêner ni le GPS ni les antennes de la balise.
- Le choix du montage de liaison, après les essais des kits A, B et C.
- L’autonomie : viser une demi-journée sans changer de batterie ; à mesurer.
- Aucun bateau n’a encore été monté selon cette fiche. Les kits d’essai des trois montages seront testés sur un bateau avant le choix.

## Sources

- [Règles de la classe IOM (site de la classe)](https://iomclass.org/iom-class-rules/)
- [Classe One Metre : dimensions (Wikipédia)](https://en.wikipedia.org/wiki/One_Metre)
- [Classe IOM : résumé des limites (onemetre.net)](https://onemetre.net/OtherTopics/IOMclass/IOM.htm)
- [Contrôle de la coque et des appendices (formulaire de la classe)](https://www.iomclass.org/wp-content/uploads/simple-file-list/Measurement-Documents/Certification_Control_Form_Hull_and_Appendages_Check_List.pdf)
- [Émissions depuis le bateau : discussion de la classe](https://iomclass.org/phpBB3/viewtopic.php?p=10872)
- [Masses correctrices : discussion de la classe](https://www.iomclass.org/phpBB3/viewtopic.php?p=929)
- [Annonces de voiliers IOM (modelisme.com)](https://www.modelisme.com/annonces/1150-voilier-IOM.html)
- [Bateaux complets, forum de la Classe 1 Mètre France](https://classe1m.ipbhost.com/forum/26-bateau-complet-coques-gr%C3%A9%C3%A9ments-avec-ou-sans-radio/)
- [Coût de revient d’un IOM (forum)](https://membrevoilerc.forumactif.fr/t1218-cout-de-revient-iom)
- [Les bateaux de la voile radiocommandée (SNO Sablais)](https://www.snos-voile.com/les-bateaux-de-la-vrc)
- [ArduPilot, voilier : matériel](https://ardupilot.org/rover/docs/sailboat-hardware.html)
- [ArduPilot, voilier : configuration](https://ardupilot.org/rover/docs/sailboat-configure.html)
- [ArduPilot : girouette](https://ardupilot.org/rover/docs/wind-vane.html)
- [ArduPilot, voilier : modes](https://ardupilot.org/rover/docs/sailboat-modes.html)
- [ExpressLRS : liaison MAVLink avec l’ordinateur](https://www.expresslrs.org/software/mavlink/)
- [ArduPilot : carte Matek H743-WING](https://ardupilot.org/copter/docs/common-matekh743-wing.html)

Les prix de la liaison, de la carte, du GPS, de la batterie et des pièces de la girouette ont été relevés en boutique les 25 et 26 novembre 2026.
