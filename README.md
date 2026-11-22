# AI Regatta

Système de suivi, d'arbitrage, d'analyse du vent et de diffusion publique pour une régate de voiliers drones (Toulon, mai 2027), inspiré de SailGP.

## Documents

- [Étude préalable](docs/etude-prealable.md) : faisabilité, architecture, choix matériels, logiciels à développer, budget, feuille de route, risques et questions à trancher.
- [Présentation interactive](docs/dispositif.html) : plan d'eau animé, liaisons, état d'avancement, coûts ajustables, feuille de route, questions.
- [Matériel et communications](docs/architecture-materiel-communications.md) : entités, liaisons entre elles, références de matériel, conception radio, réseau à terre, formats de messages, modes dégradés, nomenclature chiffrée.
- [Liaisons et logiciel](docs/liaisons-et-logiciel.md) : chaque liaison en détail (support, protocole, cadence, débit, latence, sécurité, secours, panne) et chaque module logiciel (besoin, solution, but, critère).
- [Matériel retenu](docs/materiel.md) : chaque référence, pourquoi ce choix, fiches techniques et avis.
- [Chaîne matérielle](docs/chaine-materiel.md) : les appareils de la position des bateaux jusqu’aux écrans, avec la fiabilité, le logiciel à développer, le coût, et le contrôle de compatibilité de chaque liaison.
- [Fabrication de la balise](docs/fabrication-balise.md) : le manuel de montage de la balise officielle : pièces, câblage, réglages du GPS, cahier des charges du firmware, recette de chaque balise, variante bouée, organisation de la série.
- [En clair, succès et risques](docs/en-clair-succes-risques.md) : le principe, nos choix expliqués, les clés du succès, ce qui peut foirer, le glossaire.
- [Cahier des charges des ordinateurs](docs/ordinateurs.md) : serveurs du PC course, régie, consoles, poste de contrôle, tablette, conseils aux équipes.
- [Règles de course](docs/regles-de-course.md) : version 0.3. Le règlement du comité d’organisation (Twelve Med Events, V1.4, reçu le 21 novembre 2026) fait foi ; chaque règle dit si elle vient du comité (avec son paragraphe) ou si c’est notre proposition. Le résumé « décidé par le comité / nos propositions » est en tête de la page Règlement du document général.
- [Analyse du projet](docs/analyse-projet.md) : après les arbitrages du 21 novembre : ce qui est tranché, ce qui reste à trouver, à trancher et à produire, les chances de succès de notre part, les risques, ce que nous attendons des autres instances, les revues et les niveaux de repli.
- [Feuille de route](docs/feuille-de-route.md) : 51 actions dans l’ordre, dépendances, chemin critique, ce qui avance en parallèle mois par mois, répartition des forces vives en 7 pôles.
- [Achats](docs/achats.md) : la liste de courses complète, quantités, rôle, prix, mois de commande et liens d’achat avec livraison en France (≈ 21 600 €, caméras embarquées comprises).
- Le dispositif en deux niveaux (page Dispositif du document général) : niveau 1, ce que demande le règlement (bouées RTK et vent en temps réel, ≈ 6 300 €) ; niveau 2, notre proposition (balise dans chaque bateau, jugement assisté, vidéo, ≈ 15 300 € de plus). Chaque section du document commence par « ce que dit le règlement », puis « notre approche ».
- [Le règlement](docs/postulats.md) : ce que nous retenons du règlement de l’organisateur (Twelve Med Events, V1.4), ce qui manque dans le document et ce que nous proposons, puis nos postulats.
- [Maquettes et spécification des applications](docs/maquettes.md) : comité de course, public, équipes ; ce que chaque application reçoit, décide et émet ; décisions à prendre avant le développement.
- [Prototype en direct](docs/prototype-en-direct.html) : une manche simulée en deux tours, au design clair et ludique, vue par le spectateur (téléphone), le comité de course (avec rejeu d'arbitrage), la télévision et la console d'équipe ; cartes zoomables (molette, boutons, deux doigts, glisser) ; les décisions du comité se propagent aux autres vues.
- [Logo animé](docs/logo/logo-anime.html) : le symbole se construit, puis le nom et les dates (≈ 4 s), bouton « Rejouer ».
- [Logo](docs/logo/logo.html) : logo retenu : R3 monochrome ([blanc](docs/logo/ai-regatta-mark.svg), [noir](docs/logo/ai-regatta-mark-noir.svg)) ; la planche garde toutes les pistes explorées ; le symbole seul : [ai-regatta-mark.svg](docs/logo/ai-regatta-mark.svg).
- [Bateau de référence](docs/equipes/bateau-de-reference.md) : la fiche du bateau type conseillé aux équipes : un IOM du commerce, un pilote automatique libre, une IA minimale.
- [Kit équipes](docs/equipes/README.md) : documentation technique pour les équipes (contrat d'interface, connecteurs, schémas JSON, exemples de code, liaison avec le bateau, règles d'équité).
