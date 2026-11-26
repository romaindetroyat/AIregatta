# AI Regatta — Analyse du projet

> Analyse du 21 novembre 2026, après arbitrages. Elle ne porte que sur notre périmètre : le dispositif technique et sportif. Sont gérés par d’autres instances, et donc sortis de l’analyse : la réglementation et les autorisations ; le porteur juridique et l’assurance ; la sécurité du public et les secours ; le financement du matériel ; l’accueil du public et la communication ; le recrutement des équipes ; le tracé et la longueur du parcours ; le règlement de course (comité d’organisation : Twelve Med Events). Les chiffres sont une estimation de jugement, pas un calcul.

## Tranché le 21 novembre 2026

| Sujet | Décision |
|---|---|
| Équipe | Meridia réalise le logiciel. Le matériel (balises, bouées, réseau, caméras) est préconisé ; son achat, son installation et sa mise en œuvre relèvent de l’organisateur et d’un partenaire matériel. |
| Jauge | Remplacé par le règlement de l’organisateur : voile seule, moins de 1 m, 1,30 m ou 2,70 m, sans jauge de classe. L’IOM reste le bateau de référence conseillé. |
| Bateau de référence | Un IOM du commerce documenté dans le kit : conseillé, non imposé. |
| Qualification | Remplacé par le règlement : homologation statique par un arbitre, du 12 au 14 mai. |
| Limites de vent | De 4 à 20 nœuds, à valider aux essais. |
| Intervention humaine | Remplacé par le règlement : reprises de télécommande permises, 30 s au plus, un tour de pénalité. Notre proposition : les chronométrer. |
| Mise à jour du logiciel | Interdite pendant une course, libre entre les courses. |
| Radiocommande | Remplacé par le règlement : la télécommande sert à rallier le départ, elle est de fait indispensable. |
| Liaison équipe → bateau | Tout est libre : ordres, paramètres, réglages, données officielles relayées. |
| Pénalités | Le tour par la zone P1-P2 est celui du règlement ; « le logiciel signale, l’arbitre confirme » devient notre proposition. |
| Jury | Le directeur de course et les deux arbitres. |
| Classement | Par type de régate (règlement) ; une course retirée dès 5 courues : notre proposition. |
| Bac à sable | Ouverture en février 2027. |
| Kit équipes | En français et en anglais. |
| Aides au commentateur | Lignes de vent et laylines, souffleur des moments forts, fiches prêtes à lire, résumé automatique. |
| Options de matériel | Caméras embarquées ajoutées (≈ 920 € pour six bateaux, achetées en deux temps) : la liste d’achats passe à ≈ 19 100 €. |
| Niveaux de repli et revues | Quatre niveaux de repli et critères de feu vert adoptés. |

## Les chances de succès techniques

L’accord du comité d’organisation, la tenue de l’équipe, les bateaux d’essai, la préparation des équipes et le travail des arbitres sont supposés acquis : ces pronostics ne mesurent que la technique. Le niveau 1 compte les bouées et le vent ; le niveau 2 y ajoute le suivi de chaque bateau, le PC course et le flux partagé ; « au point », c’est en plus un jugement assisté fiable.

| Niveau | Aujourd’hui | Avec toutes les mesures |
|---|---|---|
| **Bouées et vent en temps réel** — La position RTK des bouées et le vent arrivent à toutes les équipes, toute la journée de course. | ≈ 90 % | ≈ 95 % |
| **Le suivi complet fonctionne** — En plus : chaque bateau suivi au centimètre, le PC course et le flux partagé tiennent toute la journée. | ≈ 80 % | ≈ 90 % |
| **… et le jugement assisté est fiable** — En plus : des détections justes au départ, aux bouées et à l’arrivée, et des rejeux fidèles pour juger les réclamations. | ≈ 75 % | ≈ 90 % |

« Aujourd’hui » tient compte des décisions prises.

| Condition | Aujourd’hui | Avec les mesures | Pourquoi | Mesures |
|---|---|---|---|---|
| Les bouées et le vent fonctionnent toute la journée | 92 % | 97 % | Quatre balises (une de rechange), une base RTK doublée par le réseau Centipede, un anémomètre éprouvé en mer. Points faibles : l’anémomètre est unique, et la 4G peut saturer un samedi de mai. | Essai complet à la régate de préchauffage (+3) ; Radio de secours active sur les bouées (+2) |
| Les balises des bateaux, le PC course et le flux tiennent toute la journée | 85 % | 93 % | Des briques éprouvées (GPS RTK, 4G, MQTT), un prototype qui tourne déjà en simulation, des secours prévus (radio, serveur, onduleur). Points faibles : douze balises fabriquées en trois semaines, la 4G en pleine foule, la carte 4G encore à choisir. | Essais sur l’eau en janvier, en mars et au préchauffage (+5) ; Répétition générale avec tous les modes dégradés (+3) |
| Le jugement assisté détecte juste et rejoue fidèlement | 95 % | 98 % | Les contacts se jugent sur réclamation des équipes : le logiciel n’a plus à les trouver seul, seulement à rejouer fidèlement les positions. Il détecte lui-même le départ anticipé, les bouées et l’arrivée, des mesures simples au centimètre ; l’arbitre confirme toujours. | Rejeux et seuils du départ et de l’arrivée vérifiés à la régate blanche (+3) |

## Ce qui reste vraiment

14 points.

### À formaliser

| Niveau | Point | Constat | Quoi faire |
|---|---|---|---|
| Important | **L’équipe logiciel et technique** | Meridia réalise le logiciel ; le matériel revient à un partenaire de l’organisateur, à désigner. Reste à l’écrire : qui décide de quoi, quelles disponibilités en février (plein temps pour la fabrication), et qui la remplace en cas d’absence. | Une page « qui fait quoi » avant le 27 novembre ; un suppléant technique formé dès janvier, en montant le prototype avec elle. |

### À trancher

| Niveau | Point | Constat | Quoi faire |
|---|---|---|---|
| Important | **Quels bateaux pour les essais ?** | L’essai du 20 janvier demande 2 bateaux, celui du 10 mars en demande 4. Les équipes n’auront pas les leurs à temps. | Choisir avant le 4 décembre : acheter deux IOM, les emprunter à un club de voile radiocommandée, ou attendre les bateaux des équipes (risqué pour janvier). |
| Bloquant | **Faire retenir le dispositif par le comité** | Le règlement ne prévoit ni balise dans les bateaux, ni sous-bande réservée, ni jugement assisté. Sans son accord, le dispositif se limite aux bouées et au vent. | Rendez-vous avec Xavier Caux avant le 11 décembre ; démonstration à la régate de préchauffage. |
| Important | **Le nombre de courses et les poules** | Le règlement fixe le parcours (n°3, deux tours) et une journée de course, mais ni le nombre de courses ni les poules. | À proposer au comité avec le dispositif. |
| À prévoir | **Ordinateurs neufs ou existants** | Deux mini-PC neufs (≈ 1 800 €) ou deux machines prêtées, conformes au cahier des charges (≈ 2 250 € de moins avec les écrans). | À décider avant la commande de mars. |

### Décidé, reste à produire

| Niveau | Point | Constat | Quoi faire |
|---|---|---|---|
| Important | **Éprouver le bateau de référence** | La fiche est écrite (version 0.1) : un IOM d’occasion à 450 – 1 500 €, une liaison ExpressLRS (trois montages à tester), huit comportements d’IA. Mais aucun bateau n’a encore été monté ainsi, et il manque l’exemple de code de l’IA minimale. | Monter un bateau selon la fiche dès qu’un IOM est disponible ; écrire l’exemple de code ; corriger la fiche après l’essai de janvier. |
| Important | **La balise sur des bateaux très différents** | Le règlement admet des voiliers de moins de 1 m à 2,70 m, multicoques et foils. La balise d’≈ 250 g et ses antennes sur le pont doivent s’y adapter ; sur un petit bateau, son poids compte. Et dire si les 250 g de la balise comptent dans le poids minimum de 4 kg. | À écrire avec un jaugeur de la classe avant le 8 janvier. |
| Important | **La pose des balises à l’homologation** | Le règlement prévoit une homologation statique par un arbitre, du 12 au 14 mai. La pose et le contrôle des balises doivent y trouver leur place. | Proposé : chaque équipe implante sa balise à son arrivée, selon la fiche d’implantation ; l’arbitre la contrôle et la scelle sur un poste dédié de la chaîne d’inscription (≈ 15 min par bateau). |
| Important | **Nos propositions de règles** | La version 0.3 reprend le règlement de l’organisateur et y ajoute 25 propositions. | À soumettre au comité avec le dispositif, avant le 11 décembre. |
| Important | **Les commandes à délai long** | L’anémomètre se vend sur devis ; la série de balises est commandée début février pour un essai le 10 mars. | Devis de l’anémomètre en décembre ; commande de série dès le 1er février, réception mi-février. |
| À prévoir | **La version anglaise du kit** | Décidée. Contrat d’interface, règles et bateau de référence à traduire. | Fin janvier, après l’accord du comité sur nos propositions. |
| À prévoir | **Les seuils des détections automatiques** | Départ anticipé, bouée touchée, tour de pénalité et arrivée sont signalés par le logiciel ; les contacts se jugent sur réclamation. Les seuils de détection doivent être justes au centimètre. | À vérifier sur les données des essais de mars et de la régate blanche. |
| À prévoir | **Un seul anémomètre sur l’eau** | Le second n’est pas retenu. La donnée la plus attendue des équipes repose sur un capteur. | Écrire le repli sur la station à terre et le dire aux équipes. |
| À prévoir | **Batteries et bateau qui coule** | Charge et transport des batteries au lithium ne sont pas décrits. Un bateau qui coule emporte une balise de 455 €. | Consignes de charge ; flotteur ou longe de récupération sur chaque balise. |

## Ce que nous attendons des autres instances

| Quand | Quoi | Pour quoi faire |
|---|---|---|
| Avant le 20 janvier | La longueur du parcours n°3 et l’emplacement de la zone | pour placer les bouées de l’essai n°1 et régler le moteur de course |
| Fin janvier | Le nombre d’équipes inscrites | pour commander la bonne quantité de balises début février |
| Décembre, février, mars | Le financement des trois commandes | ≈ 1 900 €, 8 570 € et 6 920 €, plus 1 700 € d’imprévus |
| Mars | Le dispositif d’accueil du public | écran, sonorisation et commentateur : notre logiciel fournit le mode grand écran et les aides au commentateur |

## Les risques qui pèsent le plus

Probabilité et gravité notées sur 5 ; le poids est leur produit.

| Risque | Probabilité | Gravité | Poids | Parade |
|---|---|---|---|---|
| Chaîne des balises en retard | 3 | 5 | **15** | Fabrication à deux avec le suppléant, manuel de fabrication, niveaux de repli B et C. |
| Pas de bateau pour l’essai de janvier | 3 | 4 | **12** | Deux IOM achetés ou prêtés avant le 15 janvier. |
| Équipes pas prêtes malgré le kit | 3 | 4 | **12** | Bateau de référence avant Noël, simulateur dès décembre, support, régate blanche. |
| IA indisciplinées, arbitres débordés | 4 | 3 | **12** | Poules réduites, réclamations limitées à 3 par équipe et par course, régate blanche. |
| Responsable technique indisponible ou débordé en février | 2 | 5 | **10** | Un suppléant formé dès janvier, commandes avancées, liste de ce qu’on abandonne en premier. |
| 4G saturée le week-end de la Pentecôte | 3 | 3 | **9** | Déjà prévu : radio de secours, cartes SIM multi-opérateurs, régate blanche un jour de plage pleine. |
| Règles contestées, soupçon d’intervention humaine | 3 | 3 | **9** | Relecture par un arbitre agréé ; journal des commandes exigé en cas de réclamation. |
| Flux officiel interrompu en pleine course | 2 | 4 | **8** | Les IA perdent la vue des autres bateaux : comportement déclaré et montré à l’homologation, serveur de secours, radio de secours ; le comité peut interrompre la course. |
| Bateau à la dérive ou incontrôlable | 2 | 4 | **8** | Comportement en perte de liaison testé à la qualification ; bateau d’assistance. |
| Moins de 3 jours navigables sur 5 | 2 | 4 | **8** | Limites de vent écrites ; un jour de marge si le programme le permet. |
| Panne au PC course | 2 | 4 | **8** | Déjà prévu : second serveur, batterie, 5G, radio. |
| Mesure du vent indisponible | 2 | 3 | **6** | Repli écrit sur la station à terre. |

Les risques techniques détaillés restent dans [en-clair-succes-risques.md](en-clair-succes-risques.md).

## Décider à temps (adopté)

| Quand | Revue | Feu vert si |
|---|---|---|
| Fin janvier | Revue n°1 | Position RTK fixe plus de 95 % du temps à l’essai n°1 ; Responsable technique et son suppléant en place ; Bateau de référence et règles v1 publiés |
| Mi-mars | Revue n°2 | Le système complet a tourné à l’essai n°2 ; 12 balises recettées ; Format des données gelé |
| Mi-avril | Revue n°3 | Régate blanche courue ; Modes dégradés testés ; Les personnes du PC course pour la semaine sont nommées |

Si un critère manque, on descend d’un niveau de repli et on le dit aux équipes le jour même.

| Niveau | Nom | Contenu |
|---|---|---|
| A | Complet | Suivi au centimètre, arbitrage assisté, application publique, vidéo. |
| B | Régate suivie | Suivi au centimètre et classement automatique ; arbitrage à vue et sur réclamation, sans détections automatiques ; ni carte de vent, ni habillage télé. |
| C | Régate simple | Départs et arrivées jugés par le comité, GPS ordinaire pour l’affichage. L’IA barre toujours. |
| D | Démonstration | Deux ou trois bateaux sur un parcours commenté. |
