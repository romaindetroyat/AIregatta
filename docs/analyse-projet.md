# AI Regatta — Analyse du projet

> Analyse du 21 novembre 2026, après arbitrages. Elle ne porte que sur notre périmètre : le dispositif technique et sportif. Sont gérés par d’autres instances, et donc sortis de l’analyse : la réglementation et les autorisations ; le porteur juridique et l’assurance ; la sécurité du public et les secours ; le financement du matériel ; l’accueil du public et la communication ; le recrutement des équipes ; le tracé et la longueur du parcours. Les chiffres sont une estimation de jugement, pas un calcul.

## Tranché le 21 novembre 2026

| Sujet | Décision |
|---|---|
| Équipe | Meridia porte le logiciel ; une personne fiable porte la technique (balises, bouées, réseau, caméras). |
| Jauge | Jauge IOM (classe 1 m) pour la coque, les appendices, les gréements et le poids ; électronique libre par dérogation. |
| Bateau de référence | Un IOM du commerce documenté dans le kit : conseillé, non imposé. |
| Qualification | Sur place, le premier jour : parcours seul, tour de pénalité, arrêt sur ordre. |
| Limites de vent | De 4 à 20 nœuds, à valider aux essais. |
| Intervention humaine | Engagement sur l’honneur ; journal fourni en cas de réclamation. |
| Mise à jour du logiciel | Interdite pendant une manche, libre entre les manches. |
| Radiocommande de sécurité | Conseillée, non obligatoire. |
| Liaison équipe → bateau | Tout est libre : ordres, paramètres, réglages, données officielles relayées. |
| Pénalités | Le logiciel signale, l’arbitre confirme toujours. |
| Jury | Le directeur de course et les deux arbitres. |
| Classement | Une manche retirée à partir de 5 courues, deux à partir de 10. |
| Bac à sable | Ouverture en février 2027. |
| Kit équipes | En français et en anglais. |
| Aides au commentateur | Lignes de vent et laylines, souffleur des moments forts, fiches prêtes à lire, résumé automatique. |
| Options de matériel | Caméras embarquées ajoutées (≈ 1 320 €, achetées en deux temps) : la liste d’achats passe à ≈ 21 600 €. |
| Niveaux de repli et revues | Quatre niveaux de repli et critères de feu vert adoptés. |

## Les chances de succès de notre part

À condition que les autres instances tiennent la leur. **Révision du 21 novembre** : la première version multipliait les conditions comme si elles étaient indépendantes, alors qu’elles dépendent toutes de la même petite équipe ; et le minimum ne dépend pas du système complet, puisque le repli C se passe des balises RTK. Les conditions sont maintenant combinées avec une corrélation (exposant 0,75).

| Niveau | Aujourd’hui | Avec toutes les mesures |
|---|---|---|
| **La régate a lieu et classe** — Les bateaux courent et sont classés toute la semaine, quitte à descendre au niveau de repli B (régate suivie, arbitrage à vue) ou C (régate simple : GPS ordinaire, départs jugés par le comité). | ≈ 90 % | ≈ 95 % |
| **Le dispositif complet fonctionne** — Suivi au centimètre, arbitrage assisté, flux aux équipes, application et vidéo : le niveau A. | ≈ 60 % | ≈ 80 % |
| **… et les manches sont réussies** — En plus : des manches lisibles, un arbitrage qui suit, au moins trois jours courus. | ≈ 45 % | ≈ 70 % |

« Aujourd’hui » tient compte des décisions prises.

| Condition | Aujourd’hui | Avec les mesures | Pourquoi | Mesures |
|---|---|---|---|---|
| L’équipe tient jusqu’en mai | 90 % | 95 % | Meridia porte le logiciel, avec ses agents IA ; une personne fiable porte la technique. Reste le risque d’une seule personne au matériel : maladie, indisponibilité en février. | Un suppléant formé à la technique dès janvier (+3) ; Liste écrite de ce qu’on abandonne en premier (+2) |
| Le suivi officiel fonctionne : balises, PC course, classement | 85 % | 93 % | Des briques éprouvées (GPS RTK, 4G, MQTT), un prototype qui tourne déjà en simulation, des niveaux de repli adoptés. Le point dur : 16 balises à fabriquer en trois semaines en février. | Fabrication à deux en février, avec le manuel et la fiche de recette (+5) ; Devis de l’anémomètre en décembre, commande de série dès le 1er février (+3) |
| Des bateaux pour les essais de janvier et de mars | 85 % | 95 % | L’IOM est la classe radiocommandée la plus pratiquée : un club peut en prêter deux. Rien n’est encore demandé. | 2 IOM prêtés par un club, ou achetés d’occasion, avant le 15 janvier (+8) ; 4 bateaux assurés pour l’essai de mars (+2) |
| Pas d’accident sur l’eau | 96 % | 98 % | Des bateaux de 1 m et 4 kg, un bateau d’assistance. La radiocommande de sécurité n’est que conseillée : un bateau qui perd sa liaison dépend de son comportement déclaré. | Arrêt sur ordre testé à la qualification ; perte de liaison vérifiée au contrôle d’équipement (+2) |
| Les équipes ont de quoi se préparer | 85 % | 93 % | Contrat d’interface, schémas, exemples et fiche du bateau de référence sont écrits. Manquent l’exemple de code de l’IA minimale, le simulateur distribuable et les règles relues ; le bac à sable n’ouvre qu’en février. | Exemple d’IA minimale et simulateur fournis dès décembre (+4) ; Règles v1 relues par un arbitre et publiées le 11 janvier (+4) |
| Des manches lisibles, un arbitrage tenable | 75 % | 85 % | Notre simulation donne 12 alertes pour 7 bateaux, et l’arbitre confirme chaque pénalité : en flotte entière, deux arbitres seront débordés. | Poules de 4 à 5 bateaux (+6) ; Participation à la régate blanche d’avril demandée à chaque équipe (+4) |
| Au moins 3 jours navigables sur 5 | 90 % | 93 % | Limites fixées de 4 à 20 nœuds. Mi-mai : brise l’après-midi, mais des épisodes de mistral ; pas de jour de réserve. | Un jour de marge dans le programme (+3) |

## Ce qui reste vraiment

14 points.

### À formaliser

| Niveau | Point | Constat | Quoi faire |
|---|---|---|---|
| Important | **L’équipe logiciel et technique** | Meridia porte le logiciel ; une personne fiable porte la technique. Reste à l’écrire : qui décide de quoi, quelles disponibilités en février (plein temps pour la fabrication), et qui la remplace en cas d’absence. | Une page « qui fait quoi » avant le 27 novembre ; un suppléant technique formé dès janvier, en montant le prototype avec elle. |

### À trancher

| Niveau | Point | Constat | Quoi faire |
|---|---|---|---|
| Important | **Quels bateaux pour les essais ?** | L’essai du 20 janvier demande 2 bateaux, celui du 10 mars en demande 4. Les équipes n’auront pas les leurs à temps. | Choisir avant le 4 décembre : acheter deux IOM, les emprunter à un club de voile radiocommandée, ou attendre les bateaux des équipes (risqué pour janvier). |
| Important | **Le format des manches** | Poules de 4 à 5 bateaux, flotte entière ou duels. Le choix règle la charge des arbitres, qui confirment chaque pénalité. | Trancher avant la relecture des règles (8 janvier) ; à défaut, après la régate blanche. |
| À prévoir | **Le programme des cinq jours** | Seul le mercredi est fixé : contrôles et qualification. | À fixer avec le directeur de course dans l’avis de course (mi-mars au plus tard). |
| À prévoir | **Ordinateurs neufs ou existants** | Deux mini-PC neufs (≈ 1 800 €) ou deux machines prêtées, conformes au cahier des charges (≈ 2 250 € de moins avec les écrans). | À décider avant la commande de mars. |

### Décidé, reste à produire

| Niveau | Point | Constat | Quoi faire |
|---|---|---|---|
| Important | **Éprouver le bateau de référence** | La fiche est écrite (version 0.1) : un IOM d’occasion à 450 – 1 500 €, ArduPilot, huit comportements d’IA. Mais aucun bateau n’a encore été monté ainsi, et il manque l’exemple de code de l’IA minimale. | Monter un bateau selon la fiche dès qu’un IOM est disponible ; écrire l’exemple de code ; corriger la fiche après l’essai de janvier. |
| Important | **Les dérogations à la jauge IOM** | La jauge IOM limite l’électronique à deux commandes radio. Il faut écrire ce qui est admis : pilote automatique, capteurs, balise. Et dire si les 250 g de la balise comptent dans le poids minimum de 4 kg. | À écrire avec un jaugeur de la classe avant le 8 janvier. |
| Important | **Le contenu de la qualification** | Décidée pour le premier jour : parcours seul, tour de pénalité, arrêt sur ordre. Restent les critères précis et ce que devient un bateau recalé. | Proposé : il peut se représenter et ne court en manche classée qu’une fois qualifié. |
| Important | **La relecture des règles** | La version 0.2 intègre vos décisions. Elle n’a été relue par aucun arbitre. | Relecture par un arbitre agréé avant le 8 janvier, publication le 11. |
| Important | **Les commandes à délai long** | L’anémomètre se vend sur devis ; la série de balises est commandée début février pour un essai le 10 mars. | Devis de l’anémomètre en décembre ; commande de série dès le 1er février, réception mi-février. |
| À prévoir | **La version anglaise du kit** | Décidée. Contrat d’interface, règles et bateau de référence à traduire. | Fin janvier, après la publication des règles v1. |
| À prévoir | **Les seuils d’alerte de l’arbitrage** | Trop d’alertes noient les arbitres, trop peu laissent passer des fautes. | À régler sur les données des essais de mars et de la régate blanche. |
| À prévoir | **Un seul anémomètre sur l’eau** | Le second n’est pas retenu. La donnée la plus attendue des équipes repose sur un capteur. | Écrire le repli sur la station à terre et le dire aux équipes. |
| À prévoir | **Batteries et bateau qui coule** | Charge et transport des batteries au lithium ne sont pas décrits. Un bateau qui coule emporte une balise de 455 €. | Consignes de charge ; flotteur ou longe de récupération sur chaque balise. |

## Ce que nous attendons des autres instances

| Quand | Quoi | Pour quoi faire |
|---|---|---|
| Avant le 20 janvier | Le tracé et la longueur du parcours | pour placer les bouées de l’essai n°1 et régler le moteur de course |
| Fin janvier | Le nombre d’équipes inscrites | pour commander la bonne quantité de balises début février |
| Décembre, février, mars | Le financement des trois commandes | ≈ 1 900 €, 10 390 € et 7 320 €, plus 2 000 € d’imprévus |
| Mars | Le dispositif d’accueil du public | écran, sonorisation et commentateur : notre logiciel fournit le mode grand écran et les aides au commentateur |

## Les risques qui pèsent le plus

Probabilité et gravité notées sur 5 ; le poids est leur produit.

| Risque | Probabilité | Gravité | Poids | Parade |
|---|---|---|---|---|
| Chaîne des balises en retard | 3 | 5 | **15** | Fabrication à deux avec le suppléant, manuel de fabrication, niveaux de repli B et C. |
| Pas de bateau pour l’essai de janvier | 3 | 4 | **12** | Deux IOM achetés ou prêtés avant le 15 janvier. |
| Équipes pas prêtes malgré le kit | 3 | 4 | **12** | Bateau de référence avant Noël, simulateur dès décembre, support, régate blanche. |
| IA indisciplinées, arbitres débordés | 4 | 3 | **12** | Poules réduites, seuils d’alerte réglés aux essais, régate blanche. |
| Responsable technique indisponible ou débordé en février | 2 | 5 | **10** | Un suppléant formé dès janvier, commandes avancées, liste de ce qu’on abandonne en premier. |
| 4G saturée le week-end de la Pentecôte | 3 | 3 | **9** | Déjà prévu : radio de secours, cartes SIM multi-opérateurs, régate blanche un jour de plage pleine. |
| Règles contestées, soupçon d’intervention humaine | 3 | 3 | **9** | Relecture par un arbitre agréé ; journal des commandes exigé en cas de réclamation. |
| Bateau à la dérive ou incontrôlable | 2 | 4 | **8** | Comportement en perte de liaison testé à la qualification ; bateau d’assistance. |
| Moins de 3 jours navigables sur 5 | 2 | 4 | **8** | Limites de vent écrites ; un jour de marge si le programme le permet. |
| Panne au PC course | 2 | 4 | **8** | Déjà prévu : second serveur, batterie, 5G, radio. |
| Mesure du vent indisponible | 2 | 3 | **6** | Repli écrit sur la station à terre. |

Les risques techniques détaillés restent dans [en-clair-succes-risques.md](en-clair-succes-risques.md).

## Décider à temps (adopté)

| Quand | Revue | Feu vert si |
|---|---|---|
| Fin janvier | Revue n°1 | Position RTK fixe plus de 95 % du temps à l’essai n°1 ; Responsable technique et son suppléant en place ; Bateau de référence et règles v1 publiés |
| Mi-mars | Revue n°2 | Le système complet a tourné à l’essai n°2 ; 16 balises recettées ; Format des données gelé |
| Mi-avril | Revue n°3 | Régate blanche courue ; Modes dégradés testés ; Les personnes du PC course pour la semaine sont nommées |

Si un critère manque, on descend d’un niveau de repli et on le dit aux équipes le jour même.

| Niveau | Nom | Contenu |
|---|---|---|
| A | Complet | Suivi au centimètre, arbitrage assisté, application publique, vidéo. |
| B | Régate suivie | Suivi au centimètre et classement automatique ; arbitrage à vue, sans alertes automatiques ; ni carte de vent, ni habillage télé. |
| C | Régate simple | Départs et arrivées jugés par le comité, GPS ordinaire pour l’affichage. L’IA barre toujours. |
| D | Démonstration | Deux ou trois bateaux sur un parcours commenté. |
