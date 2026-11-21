# AI Regatta — Postulats de départ

> Le paramétrage initial du projet : ce sur quoi tout le dossier repose. Si l’un de ces postulats n’est plus vrai, on le modifie ici, puis on met à jour les sections qu’il touche.

Dernière mise à jour : 21 novembre 2026.

## Événement

| N° | Paramètre | Valeur | Statut |
|---|---|---|---|
| P01 | Nom de l’événement | AI Regatta | Acté |
| P02 | Dates | Du 12 au 16 mai 2027, sans jour de réserve | Acté |
| P03 | Lieu | Anse du Mourillon, Toulon ; zone resserrée près de la côte nord | Acté |
| P04 | Parcours | ≈ 200 m retenus pour les calculs ; la longueur et le tracé sont fixés par l’instance qui gère le plan d’eau | À confirmer |
| P05 | Réglementation du plan d’eau | Plan d’eau validé ; démarches hors du périmètre de ce dossier | Acté |

## Bateaux et équipes

| N° | Paramètre | Valeur | Statut |
|---|---|---|---|
| P06 | Nombre de bateaux | Moins de 10 ; dimensionné pour 10 + 2 balises de rechange | Acté |
| P07 | Architecture des bateaux | Jauge IOM (classe 1 m) pour la coque, les appendices, les gréements et le poids ; électronique libre par dérogation : pilote automatique, capteurs, balise | Acté |
| P08 | Source des positions | Une balise officielle dans chaque bateau, seule source pour le suivi, le classement et l’arbitrage | Acté |
| P09 | Balise à bord | ≈ 250 g, à l’intérieur si possible, poids en bas ; aucun lien avec l’électronique des équipes | Acté |
| P10 | Pilotage des bateaux | Depuis le PC à terre de chaque équipe, par sa propre liaison, dans le respect du plan de fréquences | Acté |
| P36 | Ordres tactiques des équipes | Libres : par sa propre liaison, chaque équipe envoie ce qu’elle veut à son bateau (ordres, paramètres, réglages, données officielles relayées) | Acté |
| P37 | Intelligence tactique | IA tactique de chaque équipe à terre ; le pilote automatique exécute à bord. C’est bien un drone : personne à bord. Tout embarqué : pour 2028 | Acté |
| P38 | Commande en course | L’IA de l’équipe barre seule, ordres ou commande directe du safran et des voiles ; aucune intervention humaine, sauf l’arrêt de sécurité | Acté |
| P39 | Antennes de la balise | Sur le pont, dans l’axe, quelle que soit la matière de la coque | Acté |
| P47 | Bateau de référence | Un IOM du commerce documenté dans le kit, avec un pilote automatique libre et une IA minimale : conseillé, non imposé | Acté |
| P44 | Intervention humaine | Interdite en course ; engagement sur l’honneur de chaque équipe, journal des commandes fourni en cas de réclamation | Acté |
| P45 | Mise à jour du logiciel | Interdite pendant une manche, libre entre les manches | Acté |
| P48 | Kit équipes | En français et en anglais ; bac à sable ouvert en février 2027 | Acté |
| P11 | Équité des informations | Toutes les équipes reçoivent les mêmes données au même instant : positions des bateaux et des bouées, vent, chrono | Acté |
| P12 | Assistant tactique | Aucun fourni : la tactique est le travail des équipes | Acté |
| P13 | Présence des équipes | Toutes sur place | Acté |

## Course et comité

| N° | Paramètre | Valeur | Statut |
|---|---|---|---|
| P14 | Règles de course | [Règles AI Regatta v0.2](regles-de-course.md) : match racing radiocommandé adapté ; restent le format des manches et le programme | Acté |
| P15 | Arbitrage | Deux arbitres à terre : le logiciel signale, un arbitre confirme toujours. Avec le directeur de course, ils forment le jury | Acté |
| P16 | Sécurité | Bateau d’assistance ; radiocommande de sécurité conseillée, non obligatoire | Acté |
| P17 | Chrono | Piloté par le PC course, transmis aux équipes, aux médias et au public | Acté |
| P18 | Signaux du départ | Sonores, déclenchés automatiquement par le PC course ; pavillons hissés à la main | Acté |
| P19 | Bouées | Ancrées ; déplacées par un bateau d’assistance si le vent tourne | Acté |
| P42 | Qualification | Sur place, le premier jour : parcours seul, tour de pénalité, arrêt sur ordre | Acté |
| P43 | Limites de vent | Pas de départ sous 4 nœuds ni au-dessus de 20, mesurés à la bouée au vent ; à valider aux essais | Acté |
| P46 | Classement | Un point au premier, deux au deuxième… ; une manche retirée à partir de 5 courues, deux à partir de 10 | Acté |

## Vent

| N° | Paramètre | Valeur | Statut |
|---|---|---|---|
| P20 | Mesure du vent sur l’eau | Un anémomètre sur la bouée au vent ; un second sous le vent en option | Acté |
| P21 | Vent à terre | Station météo Davis au PC course | Acté |

## Technique

| N° | Paramètre | Valeur | Statut |
|---|---|---|---|
| P22 | Distance PC course ↔ parcours | 500 m au plus ; en pratique ≈ 150 m | Acté |
| P23 | Infrastructure du site | Électricité et Internet filaire disponibles | Acté |
| P24 | Transmission des positions | 4G en principal, radio 868 MHz en secours ; Wi-Fi local en option, à tester | À confirmer |
| P25 | Bus de données | Mosquitto, au PC course, avec un serveur de secours | Acté |
| P26 | Synchronisation | Priorité absolue : écart d’horloge < 5 ms entre équipes, comité et médias | Acté |
| P27 | Caméras | 12 m de hauteur au maximum | Acté |
| P28 | Choix du matériel | Uniquement du matériel bien noté ; sinon validé au banc | Acté |
| P29 | Ordinateurs | Réutilisation d’ordinateurs existants s’ils respectent le cahier des charges | À confirmer |
| P40 | PC course et caméras | Au premier étage du bâtiment La Plage | Acté |

## Public et médias

| N° | Paramètre | Valeur | Statut |
|---|---|---|---|
| P30 | Public | Sur place, et sur l’application (iPhone, ordinateur), avec 1 s de différé | Acté |
| P31 | Commentaire | Commentateur humain, en français, aidé par le logiciel : lignes de vent et laylines, souffleur des moments forts, fiches prêtes à lire, résumé automatique | Acté |
| P41 | Fréquentation | 500 à 2 000 spectateurs en même temps ; Wi-Fi public conseillé au village | Acté |

## Projet

| N° | Paramètre | Valeur | Statut |
|---|---|---|---|
| P32 | Développement logiciel | Meridia, avec des agents IA (GSD) ; 2 à 3 mois de travail | Acté |
| P51 | Technique | Une personne fiable porte la technique : balises, bouées, réseau, caméras ; un suppléant à former | Acté |
| P33 | Licence du logiciel | Non open source | Acté |
| P34 | Budget matériel | ≈ 20 000 €, caméras embarquées comprises ; ordinateurs neufs ou existants à trancher. Le financement est géré par une autre instance | À confirmer |
| P35 | Présentation | Charte Meridia, version claire | Acté |
| P49 | Hors de notre périmètre | Réglementation et autorisations, porteur juridique et assurance, sécurité du public et secours, financement du matériel, accueil du public et communication, recrutement des équipes, tracé du parcours : gérés par d’autres instances | Acté |
| P50 | Niveaux de repli | Quatre niveaux (complet, régate suivie, régate simple, démonstration) et trois revues de feu vert : fin janvier, mi-mars, mi-avril | Acté |

