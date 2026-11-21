# Kit équipes — Le bateau de référence

> Fiche 0.1 du 21 novembre 2026. Un bateau type pour naviguer vite : **un IOM du commerce, un pilote automatique libre, une IA minimale**. Il est **conseillé, non imposé** (P47) : vous restez libres de faire autrement, dans la jauge. Cette fiche est une proposition : aucun bateau n’a encore été monté ainsi, et plusieurs points restent à valider (voir la fin).

## En bref

- **Le bateau** : un voilier radiocommandé de la classe IOM (1 m), d’occasion de préférence : 450 à 1 500 €.
- **Le pilote** : un contrôleur de vol du commerce avec ArduPilot Rover réglé en voilier, une girouette, une liaison vers votre PC à terre : ≈ 300 à 400 € (estimation).
- **L’IA** : sur votre PC à terre, elle lit le flux officiel et donne au pilote des points à rejoindre. Huit comportements suffisent pour la qualification.
- **Le délai** : huit semaines entre l’achat du bateau et le premier parcours complet.

## À bord

| N° | Élément | À qui | Où et pourquoi |
|---|---|---|---|
| 1 | **Balise officielle** | Organisation | Fournie et scellée par l’organisation : boîtier de ≈ 250 g au fond, près de la quille ; antennes sur le pont, dans l’axe. Rien au-dessus de son antenne GPS. |
| 2 | **Pilote automatique** | Équipe | Un contrôleur de vol du commerce avec le logiciel libre ArduPilot Rover, réglé en voilier. Il tient un cap, règle l’écoute et vire seul. |
| 3 | **GPS et compas de l’équipe** | Équipe | Sur le pont arrière, loin du treuil (aimants) et à 20 cm au moins des antennes officielles. |
| 4 | **Girouette** | Équipe | En tête de mât ou sur une petite perche à l’arrière : elle donne au pilote l’angle du vent. Conseillée, pas indispensable pour les premiers essais. |
| 5 | **Antenne de la liaison** | Équipe | Vers le PC à terre de l’équipe : radio 433 MHz réglée à 10 mW, ou modem 4G. Jamais dans la sous-bande réservée 869,4 – 869,65 MHz. |
| 6 | **Treuil d’écoute** | Le bateau | Celui du bateau. Une seule écoute règle grand-voile et foc, comme sur tout IOM. |
| 7 | **Servo de safran** | Le bateau | Celui du bateau. |
| 8 | **Batterie** | Équipe | Plus grosse que celle d’origine : elle alimente aussi le pilote, le GPS et la radio. La balise officielle a la sienne. |

L’installation de la balise est détaillée dans le document général, page « À bord ».

## La jauge

**Reste dans la jauge IOM** (P07) :

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
- Une liaison radio dans les deux sens (la jauge IOM interdit d’émettre depuis le bateau : on y déroge)
- La caméra embarquée de l’organisation
- Une batterie de capacité libre

Les limites IOM ci-dessus viennent de résumés de la classe ; le texte en vigueur (édition de mars 2026) fait foi. Les dérogations restent à écrire avec un jaugeur.

## Le budget

| Poste | Ordre de grandeur | Source |
|---|---|---|
| IOM d’occasion, en état de naviguer, gréement A au moins | 450 à 1 500 € | annonces relevées en France |
| ou IOM neuf, tout équipé | ≈ 3 000 € | jusqu’à 6 mois d’attente : trop tard pour mai |
| Contrôleur de vol (type Matek H743) | ≈ 80 € | estimation |
| GPS et compas | ≈ 40 € | estimation |
| Girouette légère | ≈ 50 à 150 € | estimation |
| Liaison : paire de radios 433 MHz, ou modem 4G | ≈ 60 € | estimation |
| Batterie, régulateur 5 V, câbles, supports | ≈ 60 € | estimation |

Soit **≈ 800 à 1 900 €** avec un IOM d’occasion. Un IOM neuf n’arrive pas à temps : cherchez d’occasion (forum de la Classe 1 Mètre France, petites annonces de modélisme) ou auprès d’un club de voile radiocommandée.

## Le poids

| Élément | Masse |
|---|---|
| Balise officielle | ≈ 250 g |
| Contrôleur de vol, GPS et compas | ≈ 25 g |
| Radio et antenne | ≈ 25 g |
| Girouette et son câble | ≈ 40 g |
| Régulateur, câbles, supports | ≈ 40 g |
| Batterie plus grosse (surpoids) | ≈ 70 g |
| **Total ajouté** | **≈ 450 g** |

Un IOM pèse 4 000 g au moins, masses correctrices comprises quand il en porte. Ajouter ≈ 450 g l’enfonce de quelques millimètres ; retirer les masses correctrices compense en partie. Estimations à peser.

## Le pilote automatique : réglages de départ

Les noms sont ceux d’ArduPilot Rover ; vérifiez-les dans la documentation de votre version.

1. **Activer le voilier.** SAIL_ENABLE = 1, puis redémarrer.
2. **Déclarer les deux commandes.** La sortie du treuil reçoit la fonction « écoute de grand-voile » (89) ; celle du safran, la fonction « direction ».
3. **Dire d’où vient le vent.** Avec une girouette : WNDVN_TYPE selon le capteur. Sans girouette, pour débuter : WNDVN_TYPE = 1, le vent est supposé rester celui du cap au moment de l’armement.
4. **Régler la voile.** SAIL_ANGLE_MIN et SAIL_ANGLE_MAX : l’angle de la bôme, écoute bordée puis choquée. SAIL_ANGLE_IDEAL : l’angle visé entre la bôme et le vent.
5. **Régler le près.** SAIL_NO_GO_ANGLE : l’angle au vent en dessous duquel le bateau ne va pas ; il vire seul quand le cap demandé tombe dedans. Partir de 45°.
6. **Prévoir la perte de liaison.** Si le PC à terre ne répond plus : garder le cap quelques secondes, puis rejoindre un point de sécurité ou se mettre face au vent. C’est le comportement à déclarer et à démontrer.

Liaison : en 433 MHz, la limite est de 10 mW et de 10 % du temps d’émission ; réduisez la télémétrie envoyée par le pilote. Voir [liaison-bateau.md](liaison-bateau.md).

## L’IA minimale : huit comportements

Elle tourne sur votre PC à terre, lit le flux officiel ([contrat-interface.md](contrat-interface.md)) : votre position et votre cap, les bouées, le vent, les autres bateaux, les événements. Elle envoie au pilote un point à rejoindre ou un ordre.

1. **Attendre** : avant le départ, tenir une zone sous la ligne et la couper au signal, pas avant.
2. **Remonter au vent** : donner au pilote le point de contournement de la bouée au vent : il tire ses bords seul.
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
| Semaine 3 | Monter le pilote sur table : capteurs, sorties, liaison. |
| Semaine 4 | Première sortie : cap tenu, écoute réglée seule. |
| Semaine 5 | Virements et empannages automatiques ; un triangle de bouées. |
| Semaine 6 | Le parcours complet, seul, piloté par l’IA à terre. |
| Semaine 7 | Tour de pénalité sur ordre ; perte de liaison. |
| Semaine 8 | Branchement sur le flux officiel du bac à sable. |

## Ce que demande la qualification du premier jour

- Boucler seul le parcours, deux tours
- Faire un tour de pénalité à la notification du comité
- S’arrêter sur ordre de l’équipe
- Montrer le comportement déclaré en cas de perte de liaison

## Ce qui reste à valider

- Les dérogations à la jauge IOM, à écrire avec un jaugeur de la classe : émissions radio, deux commandes seulement, et le poids. La balise et l’électronique pèsent ≈ 450 g : comptent-elles dans les 4 000 g, ou remplacent-elles les masses correctrices ?
- La place de la girouette : en tête de mât, elle voit un vent propre mais pèse en hauteur ; à l’arrière, elle est dans le dévent des voiles.
- Le compas près du treuil et du lest : étalonnage à faire bateau complet.
- La cohabitation des radios : la liaison de l’équipe ne doit gêner ni le GPS ni les antennes de la balise.
- L’autonomie : viser une demi-journée sans changer de batterie ; à mesurer.
- Aucun bateau n’a encore été monté selon cette fiche. L’organisation l’éprouvera sur ses bateaux d’essai, si elle en a, en janvier.

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

Les prix des composants électroniques sont des estimations non vérifiées.
