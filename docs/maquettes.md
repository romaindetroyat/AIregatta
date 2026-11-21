# AI Regatta — Maquettes et spécification des applications

> Ce document accompagne le prototype en direct ([prototype-en-direct.html](prototype-en-direct.html) : une manche simulée, vue par le spectateur, le comité et la télévision) et les maquettes écran par écran (planche « AI Regatta — Maquettes »). Pour chaque application, il dit ce qu’elle reçoit, ce qu’on y fait, ce qu’elle émet, et ce qui reste à trancher avant le développement. Le détail technique destiné aux équipes est dans [docs/equipes/](equipes/README.md).

Dernière mise à jour : 20 novembre 2026. Version des maquettes : 0.1.

## Principe commun

Un seul flux, trois publics. Le PC course reçoit les balises (positions 10 Hz), le vent (1 Hz) et le chrono. Le broker Mosquitto redistribue les mêmes messages, au même instant, au comité et aux équipes (réseau local, moins de 1 ms d’écart entre destinataires). Le public reçoit une version allégée, via le hub cloud, avec 1 s de différé (P30).

Chaque écran calcule le chrono sur sa propre horloge, synchronisée sur le GPS, à partir de l’heure du départ reçue. C’est ce qui garantit qu’équipes, comité et médias affichent le même temps à quelques millisecondes près (P26).

| | Comité | Équipes | Public |
|---|---|---|---|
| Positions | 10 Hz, toutes | 10 Hz, toutes | 1 à 2 Hz, différé 1 s |
| Vent | brut + consolidé + tendance | idem comité | résumé en mots |
| Alertes du moteur de course | toutes, y compris non confirmées | non | non |
| Décisions | les prend | les reçoit, avec motif | les reçoit, en une phrase |
| Santé des balises | oui | non | non |
| Écrit sur le flux | oui (console) | uniquement sa boîte « outbox » | non |

---

## 1. Application du comité de course

**Utilisateurs** : directeur de course, arbitre(s), responsable sécurité, jury. **Matériel** : PC du PC course, deux écrans (voir [ordinateurs.md](ordinateurs.md)). **Type** : application web locale (module S10), servie par le serveur du PC course, utilisable sans Internet.

### 1.1 Ce qu’il reçoit

- Positions officielles de tous les bateaux (10 Hz) avec la position de l’étrave, la qualité de la solution GPS (RTK fixe ou flottant), le chemin (4G ou radio de secours).
- Vent : anémomètre de la bouée au vent (et sous le vent en option), station Davis à terre, carte de vent fusionnée, tendance.
- Alertes du moteur de course (S8) : bateau au-delà de la ligne, contact possible, entrée dans la zone des trois longueurs, bouée touchée possible, sortie de zone, passage de bouée manqué, liaison basculée en secours. Chaque alerte porte un niveau de confiance.
- Santé du matériel (S7) : balises, batteries, liaisons, horloges (écart en ms), corne.
- Demandes des équipes : accusés de lecture, réclamations, demandes de réparation, abandons, problèmes techniques, demandes d’assistance, questions.
- Vidéo des caméras fixes, calée sur la même heure que les positions.

### 1.2 Écrans (maquettes)

| Écran | Rôle | Éléments clés |
|---|---|---|
| Départ | Piloter la procédure | Carte de la ligne avec position prévue à 0:00, biais de ligne, compte à rebours GPS, étapes (avertissement, préparatoire, une minute, départ), choix du pavillon préparatoire (P, I, Z, U, noir), boutons rappel individuel, rappel général, report, annulation, corne manuelle ; état de chaque balise |
| Course et arbitrage | Suivre et juger | Carte du parcours, file d’alertes, rejeu instantané vu de dessus avec écart minimal et priorités, décision en un clic (pas de suite, pénalité à effectuer, pénalité en temps, renvoi au jury), aperçu du message envoyé aux équipes et du libellé public, classement provisoire, actions de parcours (déplacer une bouée, réduire, annuler, arrêt sécurité) |
| Décisions | Référentiel | Les 21 décisions d’un comité, classées par moment, avec signal, règle, qui décide, effet sur le moteur de course, message aux équipes, libellé public |
| Messages | Communiquer | Rédaction d’avis (toutes les équipes, une équipe, ou équipes + public), suivi des accusés de lecture, boîte des demandes des équipes avec réponses types, règle de visibilité publique |

### 1.3 Toutes les décisions du comité

| Moment | Décision | Signal | Effet système | Statut |
|---|---|---|---|---|
| Avant | Choisir et orienter le parcours | parcours affiché | message `course` conservé | Acté (P04, P19) |
| Avant | Retarder à terre | Aperçu sur H, 2 sons | chronos en attente | Acté |
| Avant | Retarder sur l’eau | Aperçu, 2 sons | compte à rebours arrêté partout | Acté |
| Avant | Plus de course aujourd’hui | Aperçu sur A, 3 sons | journée close | Acté |
| Avant | Programmer le départ | heure GPS | message `clock` conservé | Acté (P17) |
| Départ | Pavillon préparatoire | P, I, Z, U ou noir | règle activée dans le contrôle du départ | Acté |
| Départ | Rappel individuel | X, 1 son | suivi du retour du bateau | Acté |
| Départ | Rappel général | 1er substitut, 2 sons | nouvelle procédure | Acté |
| Départ | Classer OCS, UFD, BFD | statut | classement | Acté |
| Pendant | Changer le parcours | C, sons répétés | nouvelle bouée publiée, contrôle des passages mis à jour | Acté |
| Pendant | Réduire le parcours | S, 2 sons | arrivée déplacée | Acté |
| Pendant | Annuler la manche | N, 3 sons | résultats effacés, enregistrement conservé | Acté |
| Pendant | Pénaliser en course | message | pénalité enregistrée, exécution vérifiée | **À trancher** : boucle ou temps ; direct ou après la manche |
| Pendant | Sortie de zone | message | détection sur l’étrave | **À trancher** : tolérance et sanction |
| Sécurité | Retirer un bateau | message + assistance | statut RET/DNF | Acté (P16) |
| Sécurité | Interrompre | N sur H, 3 sons | tout arrêté | Acté |
| Après | Valider les arrivées | son court (option) | temps au millième | Acté |
| Après | Temps limite | DNF | manche close | **À trancher** : durée (proposé 15 min) |
| Après | Recevoir une réclamation | numérique | rien tant que le jury n’a pas jugé | **À trancher** : délai (proposé 10 min) |
| Après | Accorder une réparation | RDG | points recalculés | **À trancher** : cas de la balise en panne |
| Après | Classement définitif | avis officiel | résultats figés et archivés | Acté |

Statuts au classement : DNC, DNS, OCS, UFD, BFD, DNF, RET, DSQ, DNE, RDG.

### 1.4 Comment il communique avec les équipes

| Canal | Support | Usage | Fait foi |
|---|---|---|---|
| Avis officiels | sujet `race/{raceId}/notices` (conservé) | consignes à toutes les équipes, avec accusé de lecture si demandé | oui |
| Messages individuels | sujet `teams/{teamId}/inbox` | décision, réponse, consigne de sécurité | oui |
| Demandes des équipes | sujet `teams/{teamId}/outbox`, seul sujet où une équipe écrit | accusé, réclamation, réparation, abandon, problème, assistance, question | oui (horodaté) |
| Voix | talkie-walkie PMR 446, canal dédié aux chefs d’équipe | sécurité, urgence, relance d’un avis non lu | non (secours) |
| Visuel et sonore | pavillons hissés à la main, corne automatique | règles de course (RCV 26) | oui pour l’heure des signaux |

Un avis non accusé après 60 s est relancé automatiquement, puis par radio.

### 1.5 Ce qui est visible du public

Le public reçoit les décisions, jamais les délibérations, toujours 1 s après les équipes.

- **Visible** : pavillons et sons avec leur sens, chrono, rappels, changements de parcours, pénalités avec un motif en une phrase, « incident à l’étude », réclamation en cours (sans le texte), statuts, avis marqués « public ».
- **Jamais visible** : discussions de l’arbitre, alertes non confirmées, texte des réclamations, santé des balises, messages à une seule équipe, demandes techniques ou d’assistance.

Chaque décision du référentiel porte donc deux textes : le message aux équipes (précis, avec la règle) et le libellé public (une phrase compréhensible par tous).

### 1.6 Exigences

- Chaque geste est journalisé avec l’heure GPS, l’auteur et les données utilisées ; tout est rejouable.
- Une décision prend moins de 10 s entre l’alerte et la diffusion.
- Prise en main par un arbitre en 30 min.
- Fonctionne sans Internet ; console de secours sur le serveur de secours.

---

## 2. Application du public

**Type** : PWA (application web installable), module S14 ; carte MapLibre. **Appareils** : iPhone, Android, ordinateur.

### 2.1 Comment on y accède

- Sur place : QR codes sur les panneaux, les drapeaux de plage et le programme.
- Ailleurs : une adresse web (nom de domaine **à réserver**).
- Rien à télécharger, pas de compte. Pour recevoir les alertes, ajouter la page à l’écran d’accueil (obligatoire sur iPhone, iOS 16.4 ou plus récent).
- Pensée pour une 4G saturée par la foule : moins de 2 ko/s en direct, chargement en moins de 2 s.

### 2.2 Ce qu’il voit

| Écran | Contenu |
|---|---|
| Accueil | prochaine manche, meilleur point de vue, bouton « voir la course » |
| En direct | chrono, carte avec bateaux numérotés par place, incident à l’étude, écarts ; onglets Classement (écarts, notes : rappel, pénalité, abandon) et Vent (force, direction, tendance expliquée en mots, gauche contre droite) |
| Mode plage | vue « depuis la digue » (les bateaux proches en bas, plus grands) ou vue de dessus ; choix d’un bateau avec un repère visuel (« voile orange n° 5, le plus proche de la digue à droite »), vitesse, distance à vous, prochaine bouée ; accès au commentaire audio |
| Alertes | aperçu, réglages par thème, équipe favorite |
| Fiche bateau | présentation de l’équipe, place à chaque bouée ou à chaque manche, replay commenté |

### 2.3 Les alertes

| Thème | Alerte | Par défaut |
|---|---|---|
| Course | départ dans 5 min | oui |
| Course | départ, rappel individuel ou général | oui |
| Course | arrivées, classement définitif | oui |
| Mon équipe | passage de bouée (place, écart) | oui si équipe suivie |
| Mon équipe | gain ou perte de place | oui si équipe suivie |
| Mon équipe | pénalité, réclamation | oui si équipe suivie |
| Programme | retard, annulation, changement d’horaire | oui |
| Spectacle | arrivée serrée (moins d’1 s) | non |
| Spectacle | grosse bascule de vent | non |

Au plus une alerte par minute, sauf départ et arrivée. Notifications Web Push ; l’abonnement reste sur le téléphone, sans inscription.

### 2.4 Ce qu’il apprend en plus de ce qu’il voit sur l’eau

Depuis la plage, on voit des voiles, pas une course. L’application ajoute :

- **Qui mène vraiment** : les bateaux ne sont pas alignés ; le classement se calcule sur la distance restante.
- **Les écarts** en secondes, et leur évolution.
- **Qui est qui** : couleur, numéro, repère par rapport à la bouée ou à la digue.
- **Le vent invisible** : force, rafales, bascule qui se prépare, côté favorisé.
- **Pourquoi** un bateau fait un tour sur lui-même (pénalité) ou revient vers la ligne (rappel).
- **Les décisions du comité** expliquées en une phrase.
- **Le replay** des moments clés et le commentaire en français.

### 2.5 À trancher

- Nom de domaine et marque.
- Vidéo dans l’application dès la v1 ou plus tard (coût de diffusion, débit sur la plage).
- Commentaire audio en direct dans l’application (flux audio) ou seulement sur la sono.
- Alertes activées par défaut.
- Orientation automatique du mode plage par la boussole du téléphone (demande une autorisation sur iPhone).

---

## 3. Ce que reçoivent les équipes

Les équipes développent leur propre logiciel. L’organisation fournit les données, les connecteurs, l’horloge, le canal du comité, le simulateur et la documentation. Tout est décrit dans le kit : [docs/equipes/](equipes/README.md).

| Question | Réponse courte | Détail |
|---|---|---|
| Que leur fournit-on ? | Flux officiel en lecture (positions, bouées, vent, parcours, chrono, pavillons, événements, classement), canal comité, horloge GPS, simulateur, rejeux, schémas, exemples | [equipes/README.md](equipes/README.md) |
| Par quels connecteurs ? | MQTT (conseillé), WebSocket, NMEA 0183 / AIS, fichiers de rejeu ; bac à sable cloud dès janvier | [equipes/connecteurs.md](equipes/connecteurs.md) |
| Comment intégrer les données ? | Abonnement aux sujets, schémas JSON, état de flotte reconstruit à partir des messages conservés, chrono calculé localement | [equipes/contrat-interface.md](equipes/contrat-interface.md), [exemples](equipes/exemples/) |
| Comment parler à leur bateau ? | Par leur propre liaison (radio 433 MHz conseillée, 868 hors sous-bande réservée, 4G), vers un pilote automatique à bord | [equipes/liaison-bateau.md](equipes/liaison-bateau.md) |
| Que peuvent-ils transmettre ? | Les ordres tactiques (acté) : manœuvres (vire, empanne, abats, loffe, face au vent) et modes (près, portant, VMG, haut, bas) ; paramètres, relais des données officielles, barre à distance, mise à jour en course : à trancher | [equipes/liaison-bateau.md](equipes/liaison-bateau.md) |

### Maquettes côté équipes

| Écran | Rôle |
|---|---|
| Le kit | Les 12 éléments fournis, leur accès, leur format, leur date ; calendrier ; partage des responsabilités |
| Explorateur de flux | Chaque sujet : sens, cadence, QoS, message conservé, exemple JSON, code d’abonnement Python, JavaScript, NMEA ; budget de latence |
| Exemple de console | Ce qu’une équipe pourrait construire : distinction donnée officielle / calcul de l’équipe / liaison de l’équipe, ordres avec suivi (envoyé, reçu, en cours, confirmé par la position officielle), canal comité, télémétrie |
| Liaison bateau | Les deux chaînes séparées, choix du support, règles de transmission à trancher, format d’ordre proposé, perte de liaison |

---

## 3 bis. Médias et carte tactique du comité

Quatre interfaces complémentaires, au style inspiré des retransmissions de grandes régates et des jeux de voile en ligne (sans reprendre leurs designs) :

| Écran | Pour qui | Contenu |
|---|---|---|
| Habillage antenne (1920 × 1080) | Téléspectateurs, flux en ligne | Vue aérienne reconstituée à partir des positions officielles ; étiquettes de bateaux (place, vitesse) ; classement avec écarts et tendance ; vent ; mini-carte ; bas d’écran au choix : duel pour la tête, pénalité expliquée, passage de bouée |
| Régie graphique | Réalisateur, opérateur graphique | Aperçu et antenne ; 8 graphiques (classement, duel, pénalité, passage, vent, fiche équipe, départ, rejeu) ; moments forts détectés par le logiciel avec le graphique conseillé ; rejeu ; fiche du commentateur |
| Écran géant de la plage | Public sur place | Lisible à 50 m : classement en très grand et carte « vue de la digue » ; compte à rebours du départ ; décision du comité |
| Carte tactique du comité | Directeur de course, arbitres | Vent par cases colorées selon sa force, flèches, laylines, traces, zones des trois longueurs ; rejeu à −60, −30, −10 s ; fiche du bateau sélectionné (vitesse, VMG, cap, distance à la layline, qualité GPS) ; alerte de bascule |

Les médias reçoivent le même flux que le comité et les équipes, au même chrono, mais n’affichent que les décisions publiques.

## 4. Décisions à prendre avant de développer

| N° | Application | Question | Recommandation |
|---|---|---|---|
| D1 | Comité | Adaptation des RCV aux drones (P14) | **Acté le 20 novembre 2026** : Partir des règles de match racing radiocommandé, arbitrage en direct |
| D2 | Comité | Forme de la pénalité | **Acté le 20 novembre 2026** : Boucle de 360° détectée automatiquement ; pénalité en temps si non effectuée |
| D3 | Comité | Arbitrage direct ou réclamations | **Acté le 20 novembre 2026** : Direct pour les incidents détectés ; réclamations pour le reste |
| D4 | Comité | Sortie de zone | **Acté le 20 novembre 2026** : Tolérance 5 m ou 5 s ; puis pénalité |
| D5 | Comité | Temps limite et délai de réclamation | **Acté le 20 novembre 2026** : 15 min ; 10 min |
| D6 | Comité | Balise en panne en course | **Acté le 20 novembre 2026** : Réparation (RDG) si la panne est prouvée |
| D7 | Public | Nom de domaine | **Hors périmètre** : géré par une autre instance (communication) |
| D8 | Public | Vidéo et commentaire audio en v1 | Audio oui, vidéo en v2 |
| D9 | Équipes | Paramètres d’ordre | **Acté le 21 novembre 2026** : libre |
| D10 | Équipes | Relais des données officielles vers le bateau | **Acté le 21 novembre 2026** : libre |
| D11 | Équipes | Barre à distance : la commande directe du safran et des voiles par l’IA à terre, sans intervention humaine, est-elle autorisée en course ? Faut-il interdire seulement l’intervention humaine (joystick), sauf pour la sécurité ? | **Acté le 20 novembre 2026** : L’IA barre seule, ordres ou commande directe ; aucune intervention humaine, sauf l’arrêt de sécurité |
| D14 | Équipes | Radiocommande de sécurité 2,4 GHz obligatoire ? (§9 de l’architecture la dit obligatoire, P16 ne l’impose pas) | **Acté le 21 novembre 2026** : conseillée, non obligatoire |
| D12 | Équipes | Mise à jour du logiciel du bateau en course | **Acté le 21 novembre 2026** : interdite pendant une manche, libre entre les manches |
| D13 | Équipes | Ouverture du bac à sable | **Acté le 21 novembre 2026** : février 2027 |
| D15 | Équipes | Intelligence à terre ou embarquée | **Acté le 20 novembre 2026 (P37)** : IA à terre pour 2027 ; tout embarqué pour 2028 (voir section 5) |
| D16 | Équipes | Réglages fins : choque, borde, cap | **Acté le 21 novembre 2026** : libres, chaque équipe envoie ce qu’elle veut à son bateau |

Une fois tranchées, ces décisions passent dans les [postulats](postulats.md).

---

## 5. Est-ce encore un drone si l’IA est à terre ?

Oui. Un drone est un bateau **sans personne à bord**. Ici, personne n’est à bord et personne ne barre : l’IA de l’équipe décide à terre, le pilote automatique exécute à bord. Le système complet (bateau + IA à terre) est autonome ; seule l’intelligence tactique est déportée, comme pour beaucoup de drones commandés depuis une station au sol. Pour 2027, rien n’oblige à l’embarquer.

### Si tout doit être embarqué, ce qui change

| Sujet | IA à terre (2027) | Tout embarqué |
|---|---|---|
| Données officielles | Reçues à terre par câble, 10 Hz, < 1 ms d’écart entre équipes | Il faut les **envoyer aux bateaux** : une nouvelle liaison descendante officielle, diffusée à tous en même temps (4G chargée par la foule, ou radio de diffusion à concevoir). C’est le plus gros chantier |
| Équité | Garantie par le câble identique | À garantir sur l’eau : même liaison, même latence, même débit pour tous |
| Liaison équipe → bateau | Ordres tactiques en continu | **Interdite en course**, sauf arrêt de sécurité ; contrôle du spectre radio pour le vérifier |
| Calcul | PC puissant à terre | Ordinateur embarqué (type Raspberry Pi 5 ou Jetson) : 5 à 15 W, + 150 à 400 g de batterie et de boîtier étanche sur un bateau de 4 kg |
| Capteurs | Flux officiel + capteurs de l’équipe | Girouette et anémomètre à bord, GPS propre ; la balise officielle reste séparée (P09), sauf à prévoir une sortie de données à sens unique |
| Mise au point | Facile : logs et correctifs à terre | Plus dure : pas de modification pendant une manche, journal récupéré après |
| Spectacle et récit | « L’IA pilote depuis la terre » | « Le bateau pense seul » : plus fort, mais moins d’équipes capables |

### Décision (P37, actée le 20 novembre 2026)

L’IA reste à terre pour 2027 (c’est déjà un drone, et c’est réaliste en 6 mois). Prévoir, si l’on veut, une **catégorie ou un bonus « tout embarqué »** sans relais des données officielles (le bateau ne voit que ses propres capteurs), ce qui évite de construire la liaison descendante. Viser le tout embarqué avec données officielles pour une édition 2028.
