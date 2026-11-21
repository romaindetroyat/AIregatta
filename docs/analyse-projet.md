# AI Regatta — Analyse du projet

> Analyse du 21 novembre 2026. A-t-on pensé à tout ? Non, pas encore. Le dossier technique est solide ; les angles morts sont ailleurs : les équipes, le cadre juridique, l’argent, les bénévoles et le public. Les chiffres sont une estimation de jugement, pas un calcul.

## Les chances de succès

| Niveau | Aujourd’hui | Avec toutes les mesures |
|---|---|---|
| **L’événement a lieu, même réduit** — Deux ou trois bateaux, dont ceux de l’organisation, naviguent seuls devant du public. Une démonstration commentée. | ≈ 60 % | ≈ 80 % |
| **Une vraie régate** — Au moins 4 équipes, des manches classées sur 3 jours au moins, les positions suivies au centimètre. | ≈ 20 % | ≈ 60 % |
| **Le projet complet, tel que décrit** — 6 équipes ou plus, arbitrage assisté fiable toute la semaine, public nombreux qui suit sur l’application, aucun incident grave. | ≈ 5 % | ≈ 35 % |

« Aujourd’hui » veut dire : en appliquant la feuille de route telle qu’elle est écrite, sans rien y ajouter. L’estimation de 85 % donnée plus tôt ne portait que sur la technique, en supposant le plan d’essais suivi et les moyens réunis ; elle reste valable pour cette question-là.

### Les neuf conditions

Les sept premières conditionnent « une vraie régate » ; les deux dernières, le projet complet. Elles sont multipliées entre elles comme si elles étaient indépendantes : c’est une estimation prudente, car un projet bien mené les améliore toutes à la fois.

| Condition | Aujourd’hui | Avec les mesures | Pourquoi | Mesures |
|---|---|---|---|---|
| Autorisations, assurance et site | 85 % | 95 % | P05 dit le plan d’eau validé, mais rien n’est écrit sur le porteur, l’assurance, ni le statut des bateaux sans équipage. | Porteur désigné, assurance souscrite, cadre réglementaire confirmé par écrit avant Noël (+7) ; Convention signée avec La Plage en décembre (+3) |
| Au moins 4 équipes avec un bateau qui navigue seul | 55 % | 88 % | Aucune équipe n’est nommée dans le dossier. Avec un appel clos fin janvier, il reste trois mois pour construire un bateau et son IA. | 6 équipes pré-engagées avant Noël, sur invitation (+13) ; Bateau de référence documenté : coque du commerce, pilote automatique libre, IA minimale (+10) ; 2 bateaux de l’organisation, engagés d’office (+10) |
| Le suivi officiel fonctionne : balises, PC course, classement | 78 % | 91 % | Les briques sont éprouvées. Le risque est l’assemblage : 16 balises à fabriquer en trois semaines, des essais qui dépendent de la météo. | Un second intégrateur matériel formé dès janvier (+5) ; Série de balises et anémomètre commandés plus tôt (+4) ; Niveaux de repli décidés d’avance (+4) |
| L’équipe bénévole tient jusqu’en mai | 80 % | 92 % | ≈ 20 mois-personnes bénévoles, un chemin critique sans marge, une seule personne nommée. | Un responsable et un suppléant par pôle, engagement écrit de disponibilité (+7) ; Liste écrite de ce qu’on abandonne en premier (+5) |
| Le matériel est financé à temps | 85 % | 95 % | 18 600 € sans financeur identifié ; 1 900 € à engager en décembre, 9 500 € en février. | Prototype avancé tout de suite, financeurs trouvés avant fin janvier (+8) ; Budget complété des postes oubliés (+2) |
| Au moins 3 jours navigables sur 5 | 88 % | 92 % | Mi-mai à Toulon : brise l’après-midi, mais des épisodes de mistral et des matinées sans vent. Pas de jour de réserve. | Programme souple : mercredi et jeudi en marge, limites de vent écrites (+4) |
| Ni accident ni arrêt de dernière minute | 96 % | 98 % | Des bateaux de 1 m sont peu dangereux, mais la zone côtoie les baigneurs et les batteries sont au lithium. | Plan de sécurité, perte de liaison testée, zone balisée (+2) |
| Les IA régatent proprement (projet complet) | 70 % | 85 % | Notre simulation donne 12 alertes en une manche de 7 bateaux. De vraies IA débutantes feront pire. | Poules de 4 à 5 bateaux, manches de 8 à 10 minutes (+8) ; Qualification en trois étapes avant la régate (+7) |
| Le public vient et comprend ce qu’il voit (projet complet) | 70 % | 90 % | Depuis la plage, un bateau de 1 m à 150 m est un point. Ni écran, ni sonorisation, ni plan de communication. | Grand écran, sonorisation et commentateur au village (+12) ; Communication locale six semaines avant, un partenaire média (+8) |

## Ce qui manque au dossier

24 manques relevés, dont 7 bloquants.

### Équipes et bateaux

| Niveau | Manque | Constat | Quoi faire |
|---|---|---|---|
| Bloquant | **Aucune équipe n’est identifiée** | Le dossier ne nomme aucune équipe et ne fixe ni date limite d’inscription, ni conditions (frais, dotation, déplacement). L’appel court jusqu’à fin janvier : il resterait trois mois à une équipe pour construire son bateau et son IA. Les projets étudiants de l’année sont déjà attribués. | Publier l’appel début décembre. Viser 6 équipes pré-engagées avant Noël : écoles et laboratoires de robotique marine, clubs de voile radiocommandée associés à des développeurs, entreprises du naval et de l’IA. Dire ce qu’elles y gagnent. |
| Bloquant | **Pas de bateau de référence** | Chaque équipe doit tout inventer : coque, pilote automatique, liaison, IA. | Documenter un bateau type : voilier radiocommandé du commerce de 95 cm (≈ 400 à 520 €), pilote automatique libre qui sait déjà piloter un voilier (ArduPilot), exemple d’IA minimale. Une équipe navigue alors en quelques semaines. |
| Bloquant | **L’organisation n’a pas de bateau** | Les essais de janvier et de mars demandent 2 puis 4 bateaux : le dossier ne dit pas lesquels. | Acheter et équiper 2 bateaux de l’organisation (≈ 1 500 à 2 000 € les deux). Ils servent aux essais, garantissent une flotte minimale et valident le bateau de référence. |
| Important | **Pas de jauge** | « Architecture libre », sans longueur maximale. Les règles supposent pourtant des bateaux de 1 m (zone de 4 m). Et la réglementation française des drones maritimes vise les engins de plus de 1 m. | Fixer une jauge simple : 1 m hors tout au plus, poids et tirant d’eau maximum, emplacement de la balise et de ses antennes. |
| Important | **Pas d’épreuve de qualification** | Rien ne garantit qu’un bateau inscrit sait boucler un parcours, faire son tour de pénalité, rester dans la zone et s’arrêter sur ordre. | Trois étapes : février sur le simulateur, mars seul sur l’eau, avril en régate blanche. Un bateau non qualifié court hors classement. |
| À prévoir | **Kit équipes en français seulement** | Des équipes étrangères ne pourront pas l’utiliser. | Traduire le contrat d’interface et les règles en anglais si l’appel dépasse la France. |

### Cadre juridique et argent

| Niveau | Manque | Constat | Quoi faire |
|---|---|---|---|
| Bloquant | **Qui porte l’événement ?** | L’étude préalable posait la question (association, club, collectivité, entreprise) : elle n’a pas de réponse dans le dossier. Sans porteur, pas d’assurance, pas de convention, pas de subvention. | Désigner la structure avant Noël, avec le club de voile partenaire. |
| Bloquant | **Aucune assurance n’est mentionnée** | Ni responsabilité civile de l’organisateur, ni dommages entre bateaux, ni matériel, ni bénévoles. | Demander un devis dès que le porteur est connu ; faire signer une décharge aux équipes pour les collisions. |
| Bloquant | **Le matériel n’est pas financé** | 18 600 € sans financeur identifié. 1 900 € sont à engager en décembre et 9 500 € en février. | Avancer le prototype tout de suite. Boucler le financement avant fin janvier : collectivités, entreprises du naval et du numérique, opérateur mobile, dons en nature. |
| Important | **Le cadre réglementaire n’a pas de trace écrite** | P05 le dit « validé, hors périmètre ». Quatre points méritent une confirmation écrite : la déclaration de manifestation nautique (15 jours à 2 mois avant, selon les cas) ; le statut de voiliers sans équipage de 1 m ; le mouillage des bouées, notre plan montrant un herbier ; la déclaration en mairie au-delà de 1 500 personnes présentes en même temps, avec un dispositif de secours. | Écrire à la délégation à la mer de la DDTM du Var et à la mairie avant Noël ; déposer la déclaration nautique début mars au plus tard. |
| Important | **Des postes absents du budget** | Corps de bouées et mouillages, sonorisation, écran pour le public, tentes, tables et électricité de la zone équipes, assurance, secours, signalétique, carburant du bateau d’assistance, lots. | Les chiffrer. Ordre de grandeur : 5 000 à 10 000 € de plus, moins ce qui sera prêté ou offert. |
| À prévoir | **Nom de domaine et marque** | Le nom de domaine n’est toujours pas réservé ; la disponibilité de « AI Regatta » comme marque n’a pas été vérifiée. | Dix minutes pour le domaine ; une recherche à l’INPI. |

### Organisation

| Niveau | Manque | Constat | Quoi faire |
|---|---|---|---|
| Bloquant | **Une équipe entièrement bénévole, sans marge** | ≈ 20 mois-personnes bénévoles sur un chemin critique sans marge. L’intégrateur matériel doit être à plein temps en février. Une seule personne est nommée dans le dossier. | Nommer un responsable et un suppléant par pôle, avec un engagement écrit de disponibilité. Point hebdomadaire de 30 minutes. |
| Important | **Ni critères de décision, ni plan de repli** | Trois revues sont prévues, sans critère de feu vert. Rien ne dit ce qu’on abandonne en premier si le temps manque. | Adopter les critères et les quatre niveaux de repli proposés plus bas. |
| Important | **Des commandes à délai long passées tard** | L’anémomètre se vend sur devis. La série de balises est commandée début février pour un essai le 10 mars. | Demander le devis de l’anémomètre en décembre. Commander les pièces communes aux deux récepteurs dès janvier. |

### Sport et sécurité

| Niveau | Manque | Constat | Quoi faire |
|---|---|---|---|
| Important | **Le format sportif n’est pas écrit** | Nombre de manches par jour, poules ou flotte entière, manches retirées, programme des cinq jours. | Poules de 4 à 5 bateaux, manches de 8 à 10 minutes. Mercredi et jeudi : contrôles, essais, qualifications (c’est la marge cachée). Vendredi à dimanche : courses et finales. |
| Important | **Des IA en flotte : beaucoup d’incidents** | Notre propre simulation produit 12 alertes en une manche de 7 bateaux, dont 7 croisements au premier bord. Deux arbitres ne suivront pas. | Poules réduites, seuils d’alerte réglés aux essais, pénalité automatique pour les cas évidents (départ anticipé, bouée touchée). |
| Important | **Impossible de prouver qu’aucun humain n’intervient** | La règle 3.1 repose sur le journal tenu par l’équipe elle-même. | Zone équipes visible du comité, mains hors clavier pendant la manche, journal horodaté remis après chaque manche, contrôles au hasard. |
| Important | **Pas de limites de vent écrites** | Un voilier de 1 m ne court ni sans vent ni par mistral fort. | Fixer une plage, par exemple 4 à 20 nœuds, à valider aux essais, et dire qui décide. |
| À prévoir | **Batteries et bateau qui coule** | Charge, stockage et transport des batteries au lithium ne sont pas traités. Un bateau qui coule emporte une balise de 440 €. | Consignes de charge ; flotteur ou longe de récupération sur chaque balise. |
| À prévoir | **Un seul anémomètre sur l’eau** | C’est la donnée la plus attendue des équipes, sur un seul capteur. | Prendre le second en option (1 470 €), ou écrire le repli sur la station à terre. |

### Public

| Niveau | Manque | Constat | Quoi faire |
|---|---|---|---|
| Important | **Depuis la plage, on ne voit presque rien** | Un bateau de 1 m à 150 m est un point. Le spectacle est sur les écrans : or ni grand écran ni sonorisation ne sont au budget. | Écran, sonorisation et commentateur au village ; médiation pour expliquer ce que fait l’IA. |
| Important | **Rien ne dit comment faire venir le public** | Pas de plan de communication ni de partenaire média pour 500 à 2 000 personnes. Les dates vont du mercredi 12 au dimanche 16 mai : c’est le week-end de la Pentecôte. Foule probable samedi et dimanche, peu de monde en semaine, plages pleines et 4G chargée. | Concentrer le spectacle sur le week-end. Communication locale six semaines avant. |
| À prévoir | **Droit à l’image et données personnelles** | La vidéo filme le public ; l’application collecte peu, mais doit le dire. | Affichage sur place, mentions dans l’application. |

## Les douze risques qui pèsent le plus

Probabilité et gravité notées sur 5 ; le poids est leur produit.

| Risque | Probabilité | Gravité | Poids | Parade |
|---|---|---|---|---|
| Moins de 4 équipes prêtes | 4 | 5 | **20** | Pré-engagement avant Noël, bateau de référence, bateaux de l’organisation, qualification. |
| Bénévoles débordés, personne clé absente | 4 | 4 | **16** | Binômes, engagement écrit, liste de ce qu’on abandonne en premier. |
| Chaîne des balises en retard | 3 | 5 | **15** | Second intégrateur, commandes avancées, repli sans arbitrage automatique. |
| Matériel non financé à temps | 3 | 4 | **12** | Prototype avancé, financeurs avant fin janvier, dons en nature. |
| IA indisciplinées, manches illisibles | 4 | 3 | **12** | Poules réduites, manches courtes, qualification, pénalités automatiques évidentes. |
| Blocage réglementaire ou d’assurance tardif | 2 | 5 | **10** | Confirmations écrites avant Noël, déclaration nautique début mars. |
| Public absent, ou qui ne comprend pas | 3 | 3 | **9** | Écran, sonorisation, commentateur, communication, week-end de la Pentecôte. |
| 4G saturée le week-end | 3 | 3 | **9** | Déjà prévu : radio de secours, seconde carte SIM, test un jour de plage pleine. |
| Règles contestées, soupçon d’intervention humaine | 3 | 3 | **9** | Relecture par un arbitre agréé, contrôle visible des équipes, journaux remis. |
| Moins de 3 jours navigables sur 5 | 2 | 4 | **8** | Programme souple, limites de vent écrites, repli pour le public. |
| Panne au PC course | 2 | 4 | **8** | Déjà prévu : second serveur, batterie, 5G, radio. |
| Accident : baigneur, batterie, bateau à la dérive | 1 | 5 | **5** | Zone balisée, perte de liaison testée, bateau d’assistance, consignes de charge. |

Les risques techniques détaillés (antennes, étanchéité, moteur de course, radio…) restent dans [en-clair-succes-risques.md](en-clair-succes-risques.md) : ils sont bien couverts.

## Décider à temps

### Critères des trois revues

| Quand | Revue | Feu vert si |
|---|---|---|
| Fin janvier | Revue n°1 | 4 équipes au moins inscrites, bateau en construction ; Position RTK fixe plus de 95 % du temps à l’essai n°1 ; Financement de la série acquis ; Porteur désigné, assurance souscrite |
| Mi-mars | Revue n°2 | 4 bateaux au moins qualifiés seuls sur l’eau ; Le système complet a tourné à l’essai n°2 ; 12 balises recettées, déclaration nautique déposée |
| Mi-avril | Revue n°3 | Régate blanche courue avec 4 équipes au moins ; Modes dégradés testés ; Les 10 personnes de la semaine de course sont nommées |

Si un critère manque, on descend d’un niveau de repli et on le dit aux équipes le jour même.

### Niveaux de repli

| Niveau | Nom | Contenu |
|---|---|---|
| A | Complet | Suivi au centimètre, arbitrage assisté, application publique, vidéo. |
| B | Régate suivie | Suivi au centimètre et classement automatique ; arbitrage à vue, sans alertes automatiques ; ni carte de vent, ni habillage télé. |
| C | Régate simple | Départs et arrivées jugés par le comité, GPS ordinaire pour l’affichage. L’IA barre toujours. |
| D | Démonstration | Deux ou trois bateaux, dont ceux de l’organisation, sur un parcours commenté. |

## Ce que cette analyse ne sait pas

- Des équipes sont-elles déjà approchées ? Si quatre sont engagées, la condition « équipes » passe de 55 à 80 % et « une vraie régate » à environ 30 %.
- Où en est le dossier réglementaire, et qui porte l’événement ?
- Y a-t-il déjà un financeur pour le matériel ?
- Qui sont les bénévoles, et combien de temps peuvent-ils réellement donner en février et mars ?

## Sources des points vérifiés

- [Drones maritimes, réglementation mise à jour (Weblex)](https://www.weblex.fr/weblex-actualite/drones-maritimes-une-reglementation-mise-a-jour)
- [La France pionnière dans l’exploitation des drones maritimes (ministère de la Mer)](https://www.mer.gouv.fr/la-france-pionniere-dans-lexploitation-des-drones-maritimes)
- [Déclaration de manifestation nautique, formulaire de la préfecture du Var](https://www.var.gouv.fr/contenu/telechargement/25679/177774/file/declaration_de_manifestation_nautique_cle2d7aa9.pdf)
- [Déclaration de manifestation nautique en mer (démarche en ligne)](https://demarche.numerique.gouv.fr/commencer/declaration-de-manifestation-nautique-en-mer)
- [Déclaration des manifestations de 1 500 à 5 000 personnes (exemple de dossier préfectoral)](https://tarn-et-garonne.gouv.fr/contenu/telechargement/33893/226435/file/Dossier%20de%20déclaration%20de%201500%20à%205000%20personnes.pdf)
- [Prix d’un DragonFlite 95 V2 prêt à naviguer (Aviotiger, France)](https://www.aviotiger.com/en/voilier/131-dragon-flite-95-rtr.html)

Ces sources sont des résumés et des formulaires, pas les textes officiels : les seuils et les délais sont à confirmer auprès de la DDTM du Var et de la mairie.
