# AI Regatta — Postulats de départ

> Le paramétrage initial du projet : ce sur quoi tout le dossier repose. Si l’un de ces postulats n’est plus vrai, on le modifie ici, puis on met à jour les sections qu’il touche.

Dernière mise à jour : 20 novembre 2026.

## Événement

| N° | Paramètre | Valeur | Statut |
|---|---|---|---|
| P01 | Nom de l’événement | AI Regatta | Acté |
| P02 | Dates | Du 12 au 16 mai 2027, sans jour de réserve | Acté |
| P03 | Lieu | Anse du Mourillon, Toulon ; zone resserrée près de la côte nord | Acté |
| P04 | Parcours | ≈ 200 m, avec du près et du portant ; orienté selon le vent du jour (longueur retenue pour tous les calculs, à valider) | À confirmer |
| P05 | Réglementation du plan d’eau | Plan d’eau validé ; démarches hors du périmètre de ce dossier | Acté |

## Bateaux et équipes

| N° | Paramètre | Valeur | Statut |
|---|---|---|---|
| P06 | Nombre de bateaux | Moins de 10 ; dimensionné pour 10 + 2 balises de rechange | Acté |
| P07 | Architecture des bateaux | Libre | Acté |
| P08 | Source des positions | Une balise officielle dans chaque bateau, seule source pour le suivi, le classement et l’arbitrage | Acté |
| P09 | Balise à bord | ≈ 250 g, à l’intérieur si possible, poids en bas ; aucun lien avec l’électronique des équipes | Acté |
| P10 | Pilotage des bateaux | Depuis le PC à terre de chaque équipe, par sa propre liaison, dans le respect du plan de fréquences | Acté |
| P36 | Ordres tactiques des équipes | Vire, empanne, abats (bouée au vent passée), loffe (bouée sous le vent passée), face au vent, mode près, mode portant, mode VMG, mode haut, mode bas ; réglages à définir (choque, borde, cap) : envoyés en direct par chaque équipe à son bateau | Acté |
| P37 | Intelligence tactique | IA tactique de chaque équipe à terre ; le pilote automatique exécute à bord. C’est bien un drone : personne à bord. Tout embarqué : pour 2028 | Acté |
| P38 | Barre à distance | Barre à distance (commande directe du safran et des voiles) interdite en course ; autorisée seulement pour la sécurité (arrêt, dégagement, retour au ponton), signalée au comité | Acté |
| P11 | Équité des informations | Toutes les équipes reçoivent les mêmes données au même instant : positions des bateaux et des bouées, vent, chrono | Acté |
| P12 | Assistant tactique | Aucun fourni : la tactique est le travail des équipes | Acté |
| P13 | Présence des équipes | Toutes sur place | Acté |

## Course et comité

| N° | Paramètre | Valeur | Statut |
|---|---|---|---|
| P14 | Règles de course | À définir | À confirmer |
| P15 | Arbitrage | À terre, en temps réel, sur écran : le logiciel signale, un arbitre décide | À confirmer |
| P16 | Sécurité | Bateaux d’assistance ; pas de reprise en main obligatoire des drones | Acté |
| P17 | Chrono | Piloté par le PC course, transmis aux équipes, aux médias et au public | Acté |
| P18 | Signaux du départ | Sonores, déclenchés automatiquement par le PC course ; pavillons hissés à la main | Acté |
| P19 | Bouées | Ancrées ; déplacées par un bateau d’assistance si le vent tourne | Acté |

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

## Public et médias

| N° | Paramètre | Valeur | Statut |
|---|---|---|---|
| P30 | Public | Sur place, et sur l’application (iPhone, ordinateur), avec 1 s de différé | Acté |
| P31 | Commentaire | Commentateur humain, en français | Acté |

## Projet

| N° | Paramètre | Valeur | Statut |
|---|---|---|---|
| P32 | Développement logiciel | IA agentique (GSD), 2 à 3 mois à deux personnes | Acté |
| P33 | Licence du logiciel | Non open source | Acté |
| P34 | Budget matériel | ≈ 18 600 € (≈ 16 200 € avec des ordinateurs existants) | À confirmer |
| P35 | Présentation | Charte Meridia, version claire | Acté |

