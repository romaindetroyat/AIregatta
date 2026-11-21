# Feuille de route AI Regatta

> Du 23/11/2026 à la régate (12 – 16 mai 2027) et au bilan. 51 actions, 7 pôles, pour ce qui relève de notre périmètre : le dispositif technique et sportif. Les actions d’un même mois qui ne dépendent pas l’une de l’autre avancent en parallèle.

## Chemin critique

Ces actions s’enchaînent sans marge : un retard sur l’une décale la régate.

**A3** Trouver les 2 développeurs et l’intégrateur matériel → **C1** Commander le prototype (≈ 1 900 €) → **C2** Monter 3 balises et la base RTK, banc à terre → **J1** Essai n°1 : 2 balises sur l’eau → **A4** Revue n°1 : choix du récepteur → **C4** Commander la série → **C5** Fabriquer et recetter la série → **J2** Essai n°2 : système complet, 4 bateaux → **A5** Revue n°2 : bascule en préparation → **G5** Tests à quai des équipes → **J3** Régate blanche → **A6** Revue n°3 : feu vert de la régate → **J4** Répétition générale → **H6** Montage du PC course et des bouées → **J5** AI Regatta

Le rythme est donné par le matériel et les sorties sur l’eau, pas par le logiciel : grâce aux agents IA, le logiciel a de la marge.

## Les actions, dans l’ordre

| N° | Action | Début | Fin | Pôle | Dépend de |
|---|---|---|---|---|---|
| A1 | Trancher les dernières questions | 23/11/2026 | 04/12/2026 | Direction de projet | — |
| A2 | Transmettre la liste d’achats aux financeurs | 23/11/2026 | 27/11/2026 | Direction de projet | — |
| A3 ★ | Trouver les 2 développeurs et l’intégrateur matériel | 23/11/2026 | 11/12/2026 | Direction de projet | — |
| C1 ★ | Commander le prototype (≈ 1 900 €) | 30/11/2026 | 11/12/2026 | Matériel et terrain | A2, A3 |
| E1 | Format du flux équipes v0 et simulateur | 30/11/2026 | 18/12/2026 | Logiciel | A3 |
| H1 | Installation à La Plage : repérage | 30/11/2026 | 15/01/2027 | Site et logistique sur l’eau | — |
| B1 | Relecture des règles par un arbitre agréé | 01/12/2026 | 08/01/2027 | Course et arbitrage | A1 |
| B6 | Dérogations à la jauge IOM et épreuve de qualification | 01/12/2026 | 08/01/2027 | Course et arbitrage | A1 |
| G6 | Bateau de référence documenté | 01/12/2026 | 23/12/2026 | Relations équipes | A1 |
| J0 | Bateaux pour les essais | 01/12/2026 | 15/01/2027 | Matériel et terrain | A1 |
| C3 | Firmware de la balise v1 | 07/12/2026 | 15/01/2027 | Logiciel | E1, A3 |
| D1 | Concevoir les bouées instrumentées | 07/12/2026 | 29/01/2027 | Matériel et terrain | C1 |
| E2 | Bus de données, serveur et secours | 07/12/2026 | 08/01/2027 | Logiciel | E1 |
| C2 ★ | Monter 3 balises et la base RTK, banc à terre | 14/12/2026 | 15/01/2027 | Matériel et terrain | C1 |
| G2 | Kit équipes v0 publié (jalon) | 21/12/2026 | 21/12/2026 | Relations équipes | E1 |
| E3 | Synchronisation des horloges (< 5 ms) | 04/01/2027 | 29/01/2027 | Logiciel | E2 |
| E4 | Moteur de course et consoles du comité | 04/01/2027 | 26/02/2027 | Logiciel | E2, B1 |
| H2 | Plan d’eau : mouillages et assistance | 04/01/2027 | 26/03/2027 | Site et logistique sur l’eau | H1 |
| B2 | Règles v1 publiées aux équipes (jalon) | 11/01/2027 | 11/01/2027 | Course et arbitrage | B1, B6 |
| B3 | Avis de course et instructions de course | 11/01/2027 | 12/03/2027 | Course et arbitrage | B2 |
| F1 | Application spectateur | 11/01/2027 | 26/02/2027 | Logiciel | E2 |
| G4 | Support et ateliers en ligne | 11/01/2027 | 07/05/2027 | Relations équipes | G2 |
| G7 | Kit et règles traduits en anglais | 11/01/2027 | 29/01/2027 | Relations équipes | G2, B2 |
| H7 | Équipe vidéo et diffusion | 11/01/2027 | 12/03/2027 | Vidéo | — |
| B4 | Procédures du comité et modes dégradés | 18/01/2027 | 05/03/2027 | Course et arbitrage | B2 |
| F2 | Console équipe | 18/01/2027 | 19/02/2027 | Logiciel | E1, B2 |
| J1 ★ | Essai n°1 : 2 balises sur l’eau | 20/01/2027 | 23/01/2027 | Matériel et terrain | C2, C3, J0 |
| A4 ★ | Revue n°1 : choix du récepteur (jalon) | 29/01/2027 | 29/01/2027 | Direction de projet | J1 |
| C4 ★ | Commander la série | 01/02/2027 | 12/02/2027 | Matériel et terrain | A4 |
| D2 | Fabriquer et étalonner les bouées | 01/02/2027 | 05/03/2027 | Matériel et terrain | D1 |
| F3 | Habillage télévision et régie | 01/02/2027 | 19/03/2027 | Logiciel | F1, H7 |
| G3 | Ouverture du bac à sable (jalon) | 01/02/2027 | 01/02/2027 | Relations équipes | E2, G2 |
| C5 ★ | Fabriquer et recetter la série | 15/02/2027 | 05/03/2027 | Matériel et terrain | C4 |
| C7 | Caméras embarquées : choix, achat, essai | 15/02/2027 | 26/03/2027 | Matériel et terrain | A4 |
| D3 | Station météo du PC course | 15/02/2027 | 26/02/2027 | Matériel et terrain | H1 |
| E6 | Carte de vent et tendance | 15/02/2027 | 26/03/2027 | Logiciel | D2, E2 |
| B5 | Former les arbitres sur les consoles | 01/03/2027 | 09/04/2027 | Course et arbitrage | E4, B4 |
| F4 | Aides au commentateur | 01/03/2027 | 02/04/2027 | Logiciel | F3, E6 |
| H3 | Réseau et caméras du PC course | 01/03/2027 | 02/04/2027 | Matériel et terrain | H1, D2 |
| J2 ★ | Essai n°2 : système complet, 4 bateaux | 10/03/2027 | 13/03/2027 | Matériel et terrain | C5, D2, E4, F1 |
| E5 | Jalon : format du flux gelé (jalon) | 15/03/2027 | 15/03/2027 | Logiciel | E4, G4 |
| E7 | Tests de charge et modes dégradés | 15/03/2027 | 23/04/2027 | Logiciel | E5 |
| A5 ★ | Revue n°2 : bascule en préparation (jalon) | 19/03/2027 | 19/03/2027 | Direction de projet | J2 |
| C6 | Installer et contrôler les balises dans les bateaux | 05/04/2027 | 09/04/2027 | Relations équipes | C5, G5 |
| G5 ★ | Tests à quai des équipes | 05/04/2027 | 09/04/2027 | Relations équipes | E5, C5 |
| J3 ★ | Régate blanche | 10/04/2027 | 12/04/2027 | Course et arbitrage | J2, G5, B5, H3 |
| A6 ★ | Revue n°3 : feu vert de la régate (jalon) | 16/04/2027 | 16/04/2027 | Direction de projet | J3 |
| J4 ★ | Répétition générale | 30/04/2027 | 02/05/2027 | Course et arbitrage | J3, E7 |
| H6 ★ | Montage du PC course et des bouées | 07/05/2027 | 11/05/2027 | Site et logistique sur l’eau | J4 |
| J5 ★ | AI Regatta | 12/05/2027 | 16/05/2027 | Direction de projet | H6, J4 |
| J6 | Bilan, replays et retours d’expérience | 17/05/2027 | 31/05/2027 | Direction de projet | J5 |

★ : chemin critique.

## Ce qui avance en parallèle

### Novembre 2026

- **Direction de projet** : A1 Trancher les dernières questions ; A2 Transmettre la liste d’achats aux financeurs ; A3 Trouver les 2 développeurs et l’intégrateur matériel
- **Logiciel** : E1 Format du flux équipes v0 et simulateur
- **Matériel et terrain** : C1 Commander le prototype (≈ 1 900 €)
- **Site et logistique sur l’eau** : H1 Installation à La Plage : repérage

### Décembre 2026

- **Direction de projet** : A1 Trancher les dernières questions ; A3 Trouver les 2 développeurs et l’intégrateur matériel
- **Logiciel** : C3 Firmware de la balise v1 ; E1 Format du flux équipes v0 et simulateur ; E2 Bus de données, serveur et secours
- **Matériel et terrain** : C1 Commander le prototype (≈ 1 900 €) ; C2 Monter 3 balises et la base RTK, banc à terre ; D1 Concevoir les bouées instrumentées ; J0 Bateaux pour les essais
- **Course et arbitrage** : B1 Relecture des règles par un arbitre agréé ; B6 Dérogations à la jauge IOM et épreuve de qualification
- **Relations équipes** : G6 Bateau de référence documenté
- **Site et logistique sur l’eau** : H1 Installation à La Plage : repérage

### Janvier 2027

- **Logiciel** : C3 Firmware de la balise v1 ; E2 Bus de données, serveur et secours ; E3 Synchronisation des horloges (< 5 ms) ; E4 Moteur de course et consoles du comité ; F1 Application spectateur ; F2 Console équipe
- **Matériel et terrain** : C2 Monter 3 balises et la base RTK, banc à terre ; D1 Concevoir les bouées instrumentées ; J0 Bateaux pour les essais ; J1 Essai n°1 : 2 balises sur l’eau
- **Course et arbitrage** : B1 Relecture des règles par un arbitre agréé ; B6 Dérogations à la jauge IOM et épreuve de qualification ; B3 Avis de course et instructions de course ; B4 Procédures du comité et modes dégradés
- **Relations équipes** : G7 Kit et règles traduits en anglais ; G4 Support et ateliers en ligne
- **Site et logistique sur l’eau** : H1 Installation à La Plage : repérage ; H2 Plan d’eau : mouillages et assistance
- **Vidéo** : H7 Équipe vidéo et diffusion

### Février 2027

- **Logiciel** : E4 Moteur de course et consoles du comité ; E6 Carte de vent et tendance ; F1 Application spectateur ; F2 Console équipe ; F3 Habillage télévision et régie
- **Matériel et terrain** : C4 Commander la série ; C5 Fabriquer et recetter la série ; C7 Caméras embarquées : choix, achat, essai ; D2 Fabriquer et étalonner les bouées ; D3 Station météo du PC course
- **Course et arbitrage** : B3 Avis de course et instructions de course ; B4 Procédures du comité et modes dégradés
- **Relations équipes** : G4 Support et ateliers en ligne
- **Site et logistique sur l’eau** : H2 Plan d’eau : mouillages et assistance
- **Vidéo** : H7 Équipe vidéo et diffusion

### Mars 2027

- **Logiciel** : E6 Carte de vent et tendance ; E7 Tests de charge et modes dégradés ; F3 Habillage télévision et régie ; F4 Aides au commentateur
- **Matériel et terrain** : C5 Fabriquer et recetter la série ; C7 Caméras embarquées : choix, achat, essai ; D2 Fabriquer et étalonner les bouées ; H3 Réseau et caméras du PC course ; J2 Essai n°2 : système complet, 4 bateaux
- **Course et arbitrage** : B3 Avis de course et instructions de course ; B4 Procédures du comité et modes dégradés ; B5 Former les arbitres sur les consoles
- **Relations équipes** : G4 Support et ateliers en ligne
- **Site et logistique sur l’eau** : H2 Plan d’eau : mouillages et assistance
- **Vidéo** : H7 Équipe vidéo et diffusion

### Avril 2027

- **Logiciel** : E7 Tests de charge et modes dégradés ; F4 Aides au commentateur
- **Matériel et terrain** : H3 Réseau et caméras du PC course
- **Course et arbitrage** : B5 Former les arbitres sur les consoles ; J3 Régate blanche ; J4 Répétition générale
- **Relations équipes** : C6 Installer et contrôler les balises dans les bateaux ; G4 Support et ateliers en ligne ; G5 Tests à quai des équipes

### Mai 2027

- **Direction de projet** : J5 AI Regatta ; J6 Bilan, replays et retours d’expérience
- **Course et arbitrage** : J4 Répétition générale
- **Relations équipes** : G4 Support et ateliers en ligne
- **Site et logistique sur l’eau** : H6 Montage du PC course et des bouées

## Répartition des forces vives

Tous les participants sont bénévoles : la charge sert à savoir quelle disponibilité demander à chacun, pas à chiffrer un coût. Réglementation, assurance, financement, recrutement des équipes, accueil et communication sont gérés par d’autres instances et ne figurent pas ici.

| Pôle | Rôle | Qui | Nov. | Déc. | Janv. | Févr. | Mars | Avr. | Mai | Semaine de course |
|---|---|---|---|---|---|---|---|---|---|---|
| Direction de projet | Pilote l’ensemble, tranche, anime les revues, fait le lien avec les autres instances (autorisations, financement, équipes, public). | Romain (Meridia), appuyé par un agent IA de suivi | 0,4 | 0,5 | 0,5 | 0,5 | 0,5 | 0,6 | 0,8 | 1 pers. |
| Logiciel | Flux de données, moteur de course, consoles, applications, aides au commentateur ; développe avec des agents IA (P32). | 2 développeurs à trouver, + agents IA ; un seul à plein temps au plus fort | 0,2 | 1 | 1,2 | 1,2 | 0,8 | 0,5 | 0,6 | 1 pers. |
| Matériel et terrain | Balises, base RTK, radio, bouées instrumentées, réseau et caméras du PC course, caméras embarquées. | 1 intégrateur électronique à trouver : à mi-temps, à plein temps en février pour la série et les bouées | 0,2 | 0,6 | 0,6 | 1 | 0,8 | 0,5 | 0,5 | 1 pers. |
| Course et arbitrage | Règles, dérogations à la jauge IOM, qualification, procédures du comité, formation des arbitres, jury. | Directeur de course et 2 arbitres (club de voile partenaire), qui forment aussi le jury | 0 | 0,1 | 0,1 | 0,1 | 0,2 | 0,3 | 0,5 | 3 pers. |
| Relations équipes | Kit en français et en anglais, bateau de référence, bac à sable, support, contrôle des installations. | 1 référent technique à temps partiel, qui protège les développeurs des sollicitations | 0 | 0,1 | 0,2 | 0,2 | 0,2 | 0,3 | 0,4 | 1 pers. |
| Site et logistique sur l’eau | PC course à La Plage, mouillages, bateau d’assistance, montage. | 1 coordinateur ; sur l’eau, 1 bateau d’assistance (club partenaire) | 0 | 0,1 | 0,1 | 0,2 | 0,2 | 0,3 | 0,5 | 2 pers. |
| Vidéo | Caméras, régie et diffusion sur l’application. | 1 personne à la régie, bénévole ou partenaire | 0 | 0,1 | 0,1 | 0,2 | 0,2 | 0,2 | 0,4 | 1 pers. |
| **Total (ETP)** | | | 0,8 | 2,5 | 2,8 | 3,4 | 2,9 | 2,7 | 3,7 | 10 pers. |

### Principes

- **Le matériel est sur le chemin critique** : l’intégrateur est disponible dès décembre, à mi-temps, et à plein temps en février pour fabriquer la série et les bouées.
- **Les développeurs ne font pas le support** : le référent équipes, à temps partiel, répond aux équipes dès l’ouverture du bac à sable.
- **Un responsable par pôle**, une revue mensuelle et trois revues de décision (fin janvier, mi-mars, mi-avril). Plusieurs pôles peuvent être tenus par la même personne : seuls le logiciel et le matériel demandent un vrai temps de travail continu.
- **Le club de voile partenaire** fournit le directeur de course, les arbitres et le bateau d’assistance.
- **Semaine de course** : 10 personnes sur place (direction, 1 développeur, 1 technicien matériel, directeur de course et 2 arbitres, référent équipes, 2 personnes sur le bateau d’assistance, 1 personne à la régie vidéo), plus le second développeur d’astreinte à distance. Le commentateur, l’accueil du public et sa sécurité sont assurés par d’autres instances.
