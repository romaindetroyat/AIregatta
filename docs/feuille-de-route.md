# Feuille de route AI Regatta

> Du 23/11/2026 à la régate (12 – 16 mai 2027) et au bilan. 52 actions, 7 pôles. Les actions d’un même mois qui ne dépendent pas l’une de l’autre avancent en parallèle.

## Chemin critique

Ces actions s’enchaînent sans marge : un retard sur l’une décale la régate.

**A1** Trancher les questions ouvertes → **C1** Commander le prototype (≈ 2 500 €) → **C2** Monter 3 balises et la base RTK, banc à terre → **J1** Essai n°1 : 2 balises sur l’eau → **A4** Revue n°1 : choix du récepteur → **C4** Commander la série → **C5** Fabriquer et recetter la série → **J2** Essai n°2 : système complet, 4 bateaux → **A5** Revue n°2 : bascule en préparation → **G5** Tests à quai des équipes → **J3** Régate blanche et test foule → **A6** Revue n°3 : feu vert de la régate → **J4** Répétition générale → **H6** Montage du site → **J5** AI Regatta

Le rythme est donné par le matériel et les sorties sur l’eau, pas par le logiciel : grâce aux agents IA, le logiciel a de la marge.

## Les actions, dans l’ordre

| N° | Action | Début | Fin | Pôle | Dépend de |
|---|---|---|---|---|---|
| A1 ★ | Trancher les questions ouvertes | 23/11/2026 | 04/12/2026 | Direction de projet | — |
| A2 | Budget matériel et financement | 23/11/2026 | 11/12/2026 | Direction de projet | — |
| A3 | Constituer l’équipe | 23/11/2026 | 18/12/2026 | Direction de projet | A2 |
| C1 ★ | Commander le prototype (≈ 2 500 €) | 30/11/2026 | 11/12/2026 | Matériel et terrain | A1, A2 |
| E1 | Format du flux équipes v0 et simulateur | 30/11/2026 | 18/12/2026 | Logiciel | A1 |
| G1 | Appel à équipes et inscriptions | 30/11/2026 | 29/01/2027 | Relations équipes | B1 |
| H1 | Convention avec La Plage (PC course) | 30/11/2026 | 15/01/2027 | Site, logistique et sécurité | A2 |
| B1 | Relecture des règles par un arbitre agréé | 01/12/2026 | 08/01/2027 | Course et arbitrage | A1 |
| I1 | Site public et réseaux | 01/12/2026 | 29/01/2027 | Communication et médias | A1 |
| I2 | Partenaires et sponsors | 01/12/2026 | 31/03/2027 | Direction de projet | A2 |
| C3 | Firmware de la balise v1 | 07/12/2026 | 15/01/2027 | Logiciel | E1 |
| D1 | Concevoir les bouées instrumentées | 07/12/2026 | 29/01/2027 | Matériel et terrain | C1 |
| E2 | Bus de données, serveur et secours | 07/12/2026 | 08/01/2027 | Logiciel | E1 |
| C2 ★ | Monter 3 balises et la base RTK, banc à terre | 14/12/2026 | 15/01/2027 | Matériel et terrain | C1 |
| G2 | Kit équipes v0 publié (jalon) | 21/12/2026 | 21/12/2026 | Relations équipes | E1 |
| E3 | Synchronisation des horloges (< 5 ms) | 04/01/2027 | 29/01/2027 | Logiciel | E2 |
| E4 | Moteur de course et consoles du comité | 04/01/2027 | 26/02/2027 | Logiciel | E2, B1 |
| H2 | Plan d’eau : mouillages et assistance | 04/01/2027 | 26/03/2027 | Site, logistique et sécurité | H1 |
| B2 | Règles v1 publiées aux équipes (jalon) | 11/01/2027 | 11/01/2027 | Course et arbitrage | B1 |
| B3 | Avis de course et instructions de course | 11/01/2027 | 12/03/2027 | Course et arbitrage | B2 |
| F1 | Application spectateur | 11/01/2027 | 26/02/2027 | Logiciel | E2 |
| G3 | Ouverture du bac à sable (jalon) | 11/01/2027 | 11/01/2027 | Relations équipes | E2, G2 |
| G4 | Support et ateliers en ligne | 11/01/2027 | 07/05/2027 | Relations équipes | G3 |
| I4 | Équipe vidéo et diffusion | 11/01/2027 | 12/03/2027 | Communication et médias | A2 |
| B4 | Procédures du comité et modes dégradés | 18/01/2027 | 05/03/2027 | Course et arbitrage | B2 |
| F2 | Console équipe | 18/01/2027 | 19/02/2027 | Logiciel | E1, B2 |
| J1 ★ | Essai n°1 : 2 balises sur l’eau | 20/01/2027 | 23/01/2027 | Matériel et terrain | C2, C3 |
| A4 ★ | Revue n°1 : choix du récepteur (jalon) | 29/01/2027 | 29/01/2027 | Direction de projet | J1 |
| C4 ★ | Commander la série | 01/02/2027 | 12/02/2027 | Matériel et terrain | A4 |
| D2 | Fabriquer et étalonner les bouées | 01/02/2027 | 05/03/2027 | Matériel et terrain | D1 |
| F3 | Habillage télévision et régie | 01/02/2027 | 19/03/2027 | Logiciel | F1, I4 |
| H5 | Plan de sécurité et bénévoles | 01/02/2027 | 23/04/2027 | Site, logistique et sécurité | H2 |
| I3 | Presse, commentateur, promotion | 01/02/2027 | 11/05/2027 | Communication et médias | I1 |
| C5 ★ | Fabriquer et recetter la série | 15/02/2027 | 05/03/2027 | Matériel et terrain | C4 |
| D3 | Station météo du PC course | 15/02/2027 | 26/02/2027 | Matériel et terrain | H1 |
| E6 | Carte de vent et tendance | 15/02/2027 | 26/03/2027 | Logiciel | D2, E2 |
| H4 | Wi-Fi public au village | 15/02/2027 | 09/04/2027 | Site, logistique et sécurité | H1 |
| B5 | Former les arbitres sur les consoles | 01/03/2027 | 09/04/2027 | Course et arbitrage | E4, B4 |
| F4 | Aide au commentateur | 01/03/2027 | 02/04/2027 | Communication et médias | F3 |
| H3 | Réseau et caméras du PC course | 01/03/2027 | 02/04/2027 | Matériel et terrain | H1, D2 |
| J2 ★ | Essai n°2 : système complet, 4 bateaux | 10/03/2027 | 13/03/2027 | Matériel et terrain | C5, D2, E4, F1 |
| E5 | Jalon : format du flux gelé (jalon) | 15/03/2027 | 15/03/2027 | Logiciel | E4, G4 |
| E7 | Tests de charge et modes dégradés | 15/03/2027 | 23/04/2027 | Logiciel | E5 |
| A5 ★ | Revue n°2 : bascule en préparation (jalon) | 19/03/2027 | 19/03/2027 | Direction de projet | J2 |
| C6 | Installer et contrôler les balises dans les bateaux | 05/04/2027 | 09/04/2027 | Relations équipes | C5, G5 |
| G5 ★ | Tests à quai des équipes | 05/04/2027 | 09/04/2027 | Relations équipes | E5, C5 |
| J3 ★ | Régate blanche et test foule | 10/04/2027 | 12/04/2027 | Course et arbitrage | J2, G5, B5, H3, H4 |
| A6 ★ | Revue n°3 : feu vert de la régate (jalon) | 16/04/2027 | 16/04/2027 | Direction de projet | J3 |
| J4 ★ | Répétition générale | 30/04/2027 | 02/05/2027 | Course et arbitrage | J3, E7, H5 |
| H6 ★ | Montage du site | 07/05/2027 | 11/05/2027 | Site, logistique et sécurité | J4 |
| J5 ★ | AI Regatta | 12/05/2027 | 16/05/2027 | Direction de projet | H6, J4 |
| J6 | Bilan, replays et retours d’expérience | 17/05/2027 | 31/05/2027 | Direction de projet | J5 |

★ : chemin critique.

## Ce qui avance en parallèle

### Novembre 2026

- **Direction de projet** : A1 Trancher les questions ouvertes ; A2 Budget matériel et financement ; A3 Constituer l’équipe
- **Logiciel** : E1 Format du flux équipes v0 et simulateur
- **Matériel et terrain** : C1 Commander le prototype (≈ 2 500 €)
- **Relations équipes** : G1 Appel à équipes et inscriptions
- **Site, logistique et sécurité** : H1 Convention avec La Plage (PC course)

### Décembre 2026

- **Direction de projet** : A1 Trancher les questions ouvertes ; A2 Budget matériel et financement ; A3 Constituer l’équipe ; I2 Partenaires et sponsors
- **Logiciel** : C3 Firmware de la balise v1 ; E1 Format du flux équipes v0 et simulateur ; E2 Bus de données, serveur et secours
- **Matériel et terrain** : C1 Commander le prototype (≈ 2 500 €) ; C2 Monter 3 balises et la base RTK, banc à terre ; D1 Concevoir les bouées instrumentées
- **Course et arbitrage** : B1 Relecture des règles par un arbitre agréé
- **Relations équipes** : G1 Appel à équipes et inscriptions
- **Site, logistique et sécurité** : H1 Convention avec La Plage (PC course)
- **Communication et médias** : I1 Site public et réseaux

### Janvier 2027

- **Direction de projet** : I2 Partenaires et sponsors
- **Logiciel** : C3 Firmware de la balise v1 ; E2 Bus de données, serveur et secours ; E3 Synchronisation des horloges (< 5 ms) ; E4 Moteur de course et consoles du comité ; F1 Application spectateur ; F2 Console équipe
- **Matériel et terrain** : C2 Monter 3 balises et la base RTK, banc à terre ; D1 Concevoir les bouées instrumentées ; J1 Essai n°1 : 2 balises sur l’eau
- **Course et arbitrage** : B1 Relecture des règles par un arbitre agréé ; B3 Avis de course et instructions de course ; B4 Procédures du comité et modes dégradés
- **Relations équipes** : G1 Appel à équipes et inscriptions ; G4 Support et ateliers en ligne
- **Site, logistique et sécurité** : H1 Convention avec La Plage (PC course) ; H2 Plan d’eau : mouillages et assistance
- **Communication et médias** : I1 Site public et réseaux ; I4 Équipe vidéo et diffusion

### Février 2027

- **Direction de projet** : I2 Partenaires et sponsors
- **Logiciel** : E4 Moteur de course et consoles du comité ; E6 Carte de vent et tendance ; F1 Application spectateur ; F2 Console équipe ; F3 Habillage télévision et régie
- **Matériel et terrain** : C4 Commander la série ; C5 Fabriquer et recetter la série ; D2 Fabriquer et étalonner les bouées ; D3 Station météo du PC course
- **Course et arbitrage** : B3 Avis de course et instructions de course ; B4 Procédures du comité et modes dégradés
- **Relations équipes** : G4 Support et ateliers en ligne
- **Site, logistique et sécurité** : H2 Plan d’eau : mouillages et assistance ; H4 Wi-Fi public au village ; H5 Plan de sécurité et bénévoles
- **Communication et médias** : I3 Presse, commentateur, promotion ; I4 Équipe vidéo et diffusion

### Mars 2027

- **Direction de projet** : I2 Partenaires et sponsors
- **Logiciel** : E6 Carte de vent et tendance ; E7 Tests de charge et modes dégradés ; F3 Habillage télévision et régie
- **Matériel et terrain** : C5 Fabriquer et recetter la série ; D2 Fabriquer et étalonner les bouées ; H3 Réseau et caméras du PC course ; J2 Essai n°2 : système complet, 4 bateaux
- **Course et arbitrage** : B3 Avis de course et instructions de course ; B4 Procédures du comité et modes dégradés ; B5 Former les arbitres sur les consoles
- **Relations équipes** : G4 Support et ateliers en ligne
- **Site, logistique et sécurité** : H2 Plan d’eau : mouillages et assistance ; H4 Wi-Fi public au village ; H5 Plan de sécurité et bénévoles
- **Communication et médias** : F4 Aide au commentateur ; I3 Presse, commentateur, promotion ; I4 Équipe vidéo et diffusion

### Avril 2027

- **Logiciel** : E7 Tests de charge et modes dégradés
- **Matériel et terrain** : H3 Réseau et caméras du PC course
- **Course et arbitrage** : B5 Former les arbitres sur les consoles ; J3 Régate blanche et test foule ; J4 Répétition générale
- **Relations équipes** : C6 Installer et contrôler les balises dans les bateaux ; G4 Support et ateliers en ligne ; G5 Tests à quai des équipes
- **Site, logistique et sécurité** : H4 Wi-Fi public au village ; H5 Plan de sécurité et bénévoles
- **Communication et médias** : F4 Aide au commentateur ; I3 Presse, commentateur, promotion

### Mai 2027

- **Direction de projet** : J5 AI Regatta ; J6 Bilan, replays et retours d’expérience
- **Course et arbitrage** : J4 Répétition générale
- **Relations équipes** : G4 Support et ateliers en ligne
- **Site, logistique et sécurité** : H6 Montage du site
- **Communication et médias** : I3 Presse, commentateur, promotion

## Répartition des forces vives

Tous les participants sont bénévoles : la charge sert à savoir quelle disponibilité demander à chacun, pas à chiffrer un coût. Seul le matériel coûte.

| Pôle | Rôle | Qui | Nov. | Déc. | Janv. | Févr. | Mars | Avr. | Mai | Semaine de course |
|---|---|---|---|---|---|---|---|---|---|---|
| Direction de projet | Pilote l’ensemble, tranche, tient le budget, signe les partenaires, anime la revue mensuelle. | Romain (Meridia), appuyé par un agent IA de suivi | 0,4 | 0,5 | 0,5 | 0,5 | 0,5 | 0,6 | 0,8 | 1 pers. |
| Logiciel | Flux de données, moteur de course, consoles, applications ; développe avec des agents IA (P32). | 2 développeurs (Meridia) + agents IA, dont un seul à plein temps au plus fort | 0,2 | 1 | 1,2 | 1,2 | 0,8 | 0,5 | 0,6 | 1 pers. |
| Matériel et terrain | Balises, base RTK, radio, bouées instrumentées, réseau et caméras du PC course. | 1 intégrateur électronique, à mi-temps, à plein temps en février pour la série et les bouées | 0,2 | 0,6 | 0,6 | 1 | 0,8 | 0,5 | 0,5 | 1 pers. |
| Course et arbitrage | Règles, instructions de course, procédures du comité, formation des arbitres, jury. | Directeur de course et 2 arbitres (club de voile partenaire), qui forment aussi le jury après les manches | 0 | 0,1 | 0,1 | 0,1 | 0,2 | 0,3 | 0,5 | 3 pers. |
| Relations équipes | Appel à équipes, kit et bac à sable, support, contrôle des installations. | 1 référent technique à temps partiel, qui protège les développeurs des sollicitations | 0 | 0,1 | 0,2 | 0,2 | 0,2 | 0,3 | 0,4 | 1 pers. |
| Site, logistique et sécurité | PC course à La Plage, plan d’eau, bateaux d’assistance, Wi-Fi public, sécurité, montage. | 1 coordinateur ; sur l’eau, 1 bateau d’assistance (club partenaire) | 0 | 0,1 | 0,1 | 0,2 | 0,2 | 0,3 | 0,5 | 2 pers. |
| Communication et médias | Site public, partenaires, presse, réseaux, régie vidéo et commentateur. | 1 chargé de communication, qui commente ; la vidéo par des bénévoles ou un partenaire | 0,1 | 0,2 | 0,2 | 0,3 | 0,3 | 0,4 | 0,6 | 1 pers. |
| **Total (ETP)** | | | 0,9 | 2,6 | 2,9 | 3,5 | 3,0 | 2,9 | 3,9 | 10 pers. |

### Principes

- **Le matériel est sur le chemin critique** : l’intégrateur est disponible dès décembre, à mi-temps, et à plein temps en février pour fabriquer la série et les bouées.
- **Les développeurs ne font pas le support** : le référent équipes, à temps partiel, répond aux équipes dès l’ouverture du bac à sable.
- **Un responsable par pôle**, une revue mensuelle et trois revues de décision (fin janvier, mi-mars, mi-avril). Plusieurs pôles peuvent être tenus par la même personne : seuls le logiciel et le matériel demandent un vrai temps de travail continu.
- **Le club de voile partenaire** fournit le directeur de course, les arbitres et le bateau d’assistance.
- **Semaine de course** : 10 personnes sur place (direction, 1 développeur, 1 technicien matériel, directeur de course et 2 arbitres, référent équipes, 2 personnes sur le bateau d’assistance, 1 commentateur), plus le second développeur d’astreinte à distance et l’équipe vidéo. La sécurité du public relève du site et de la commune.
