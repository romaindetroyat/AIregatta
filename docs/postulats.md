# AI Regatta — Le règlement

> Règlement de course AI Regatta 2027, V1.4 du 15/10/2026, de l’association Twelve Med Events (autorité organisatrice), reçu le 21 novembre 2026 de Xavier Caux. Il fait foi.

## 1. Ce que nous retenons du document

- **Dates** (P02) : Inscriptions et homologation du 12 au 14 mai ; régates le samedi 15 mai dès 10 h ; report au dimanche 16 (courses finies à 14 h 30) ; remise des prix le 16 à 16 h 30
- **Lieu** (P03) : Plages du Mourillon, autour du Fort Saint-Louis (Toulon), dans le cadre de la Toulon Provence Regatta ; zone de régate matérialisée par des bouées
- **Parcours** (P04) : Parcours construit n°3 : porte 1-2 (départ, porte et arrivée), bouée au vent 3 laissée à bâbord, deux tours ; zone de pénalité P1-P2. Longueur fixée par l’organisateur (≈ 200 m retenus pour les calculs)
- **Bateaux admis** (P07) : Voile seule ; longueur hors tout de moins de 1 m, 1,30 m ou 2,70 m ; monocoques, multicoques, foils admis. Pas de jauge de classe
- **Pilotage des bateaux** (P10) : Mode autonome obligatoire de la ligne de départ à l’arrivée ; l’IA peut être embarquée ou à terre (télécommande actionnée par programme)
- **Intelligence tactique** (P37) : Au choix des équipes : embarquée ou à terre (règlement § 2c). Le kit et le bateau de référence partent d’une IA à terre
- **Commande en course** (P38) : Autonome en course ; télécommande permise pour rallier le départ, après l’arrivée, en cas de panne, de sortie de zone ou pour la pénalité ; chaque reprise : 30 s au plus et un tour de pénalité
- **Présence des équipes** (P13) : Sur place : arrivée une semaine avant la compétition, chaîne d’inscription du 12 au 14 mai (règlement § 6)
- **Règles de course** (P14) : Le règlement de l’organisateur (Twelve Med Events, V1.4) fait foi ; RCV pour le parcours construit. Nos règles v0.3 le reprennent et ajoutent nos propositions
- **Sécurité** (P16) : Une organisation sur l’eau récupère les bateaux en difficulté ; le bateau de sécurité peut dérouter un bateau. Télécommande de fait indispensable (mode manuel)
- **Signaux du départ** (P18) : Procédure RCV 26 (5, 4, 1 minute, départ) ; une minute par dérogation. Proposition : signaux sonores déclenchés par le PC course à l’heure GPS
- **Bouées** (P19) : Bouées matérialisant la zone et le parcours ; chacun relève leurs coordonnées ; l’organisateur cherche à les transmettre en temps réel (RTK et vent)
- **Pénalité** (P53) : Un tour par la zone P1-P2, fait à la fin, avant l’arrivée ; un tour aussi pour chaque reprise de télécommande
- **Batteries** (P54) : LiFePO4, ou lithium avec BMS intégré et enveloppe solide du commerce ; 48 V au plus. La balise passe à une batterie USB du commerce
- **Communication avec les équipes** (P55) : battleboats.fr, groupe WhatsApp, briefing chaque jour à 9 h 30 ; vidéo et fiche de présentation avant le 1er mai
- **Préparation sur place** (P56) : Régate de préchauffage au premier trimestre 2027 ; bâtiment prêté un mois ; arrivée des équipes une semaine avant
- **Organisateur** (P57) : L’association Twelve Med Events, autorité organisatrice, sous le patronage de la DGA ; l’AI Regatta fait partie de la Toulon Provence Regatta
- **Épreuves** (P58) : Six types de régates : slaloms en duel et Battleboats (bateaux à moteur), régates de voiliers télécommandés ou sous IA. Ce dossier ne couvre que les voiliers sous IA
- **Inscription** (P59) : En ligne sur battleboats.fr, ouverte à tous (écoles, entreprises, particuliers, clubs) ; 20 € par personne, moins 20 € par bateau inscrit
- **Équipement des équipes** (P60) : Batteries § 12, 48 V au plus ; lasers de classe 1 ou 1M seulement ; son ≤ 80 dBA à 1 m ; air comprimé ≤ 4 bars ; radiocommande conforme à la réglementation française ; numéro de 10 cm sur la voile
- **Assurance et responsabilité** (P61) : Chaque bateau présente une attestation de responsabilité civile ; l’équipe décide seule de courir (§ 16). Hors de notre périmètre
- **Image et données** (P62) : En participant, les équipes autorisent l’organisateur et ses partenaires à utiliser leurs images et leurs données (§ 15) : la vidéo et l’application peuvent les montrer
- **Niveau 1 : demandé par le comité** (P63) : Transmettre en temps réel la position RTK des bouées et le vent (règlement § 5 : l’organisateur cherche des partenaires). ≈ 6 300 € de matériel
- **Homologation** (P42) : Homologation statique par un arbitre avant les régates (chaîne d’inscription, 12 – 14 mai) ; pas d’épreuve de qualification sur l’eau
- **Classement** (P46) : Par type de régate, sur les résultats des courses. Disqualification : départ anticipé non réparé en 2 min, bouée mal passée, arrivée plus de 5 min après le premier. Proposition : points 1, 2, 3… et une course retirée dès 5 courues
- **Caméras** (P27) : Caméras fixes de 12 m au plus. Le règlement interdit les drones aériens et le survol de la zone, sauf dérogation (§ 10)

## 2. Ce qui manque dans le document, et ce que nous proposons

- **Suivre les bateaux** (Priorité 2) : Rien ne donne la position des bateaux : le départ, les passages et l’arrivée se jugent à l’œil. *Notre proposition :* Une balise scellée dans chaque bateau, posée à l’homologation (règle 2.5, P08).
- **Juger au centimètre** (Priorité 2) : Départ anticipé, bouée mal passée, tour P1-P2, fenêtre des 5 minutes : aucun moyen de mesure. *Notre proposition :* Le logiciel détecte, l’arbitre confirme toujours (règles 5.2 à 5.6).
- **Partager la position des bateaux** (Priorité 2) : Le règlement ne dit pas ce que reçoivent les IA ; il laisse les capteurs libres dans les limites du § 12 (lasers de classe 1 ou 1M). *Notre proposition :* Toutes les équipes reçoivent la position de tous les bateaux, des bouées et le vent, au même instant : plus fiable qu’un LIDAR sur l’eau, sans capteur coûteux pour les équipes. Garde-fous : même délai prouvé, comportement déclaré en cas de perte du flux, capteurs embarqués libres en plus (règles 3.7 à 3.9, P11, P65).
- **Mesurer les reprises de télécommande** (Priorité 2) : La limite de 30 s est fixée, mais rien ne la mesure. *Notre proposition :* Chaque reprise déclarée par l’équipe (`manual_control`) et chronométrée (règle 3.4, P44).
- **Transmettre les données aux équipes** (Priorité 1) : Le règlement demande la position RTK des bouées et le vent en temps réel (§ 5), sans dire comment. *Notre proposition :* Une page web et un flux MQTT, mêmes données au même instant pour toutes les équipes (niveau 1, P11, P52).
- **Les fréquences** (À inscrire) : Rien sur la radio des balises ; le Wi-Fi 5 GHz est seulement conseillé (§ 13). *Notre proposition :* La sous-bande 869,4 – 869,65 MHz réservée aux balises (règle 2.7).
- **L’arbitrage et les réclamations** (À proposer) : Seul l’arbitre de l’homologation est décrit ; ni jury, ni délai de réclamation. *Notre proposition :* Deux arbitres à terre devant les rejeux ; réclamation par message dans les 10 minutes (règles 6.1, 6.2, P15).
- **Le barème du classement** (À proposer) : « Sur les résultats des courses », sans barème ni course retirée. *Notre proposition :* 1, 2, 3… ; une course retirée dès 5 courues (règle 6.4).
- **Le nombre de courses et les poules** (À proposer) : Une journée de course, sans nombre de courses ni format. *Notre proposition :* Poules de 4 à 5 bateaux, pour que deux arbitres suivent.
- **Les limites de vent** (À proposer) : Aucune. *Notre proposition :* Pas de départ sous 4 ni au-dessus de 20 nœuds, mesurés à la bouée 3 (règle 4.6, P43).
- **Le logiciel pendant une course** (À proposer) : Rien sur les mises à jour. *Notre proposition :* Pas de mise à jour pendant une course, libre entre les courses (règle 3.5, P45).
- **La zone de bouée** (À proposer) : Les RCV s’appliquent, mais des bateaux de 1 m à 2,70 m peuvent courir ensemble. *Notre proposition :* 4 m pour les bateaux de moins de 1,30 m ; à fixer pour 2,70 m (règle 1.4).
- **Les signaux de départ** (À proposer) : La procédure est fixée, pas la façon de la donner. *Notre proposition :* Signaux sonores déclenchés à l’heure GPS, pour l’une ou l’autre procédure (règle 4.3).

## À vérifier avec l’organisateur

- La date de la première masterclass : le mail annonce « vendredi 29 novembre », or le 29 novembre 2026 est un dimanche.
- L’emplacement exact de la zone de régate et du PC course (le premier étage de La Plage convient-il ?).
- Le nombre de voiliers IA attendus, et si plusieurs types de longueur courent ensemble.
- La longueur du parcours n°3, la largeur de la porte 1-2 et la position de P1-P2.
- Qui arbitre et qui forme le jury.
- La date et le lieu de la régate de préchauffage.

## 3. Nos postulats

| N° | Sujet | Valeur | Statut |
|---|---|---|---|
| P01 | Nom de l’événement | AI Regatta | Acté |
| P05 | Réglementation du plan d’eau | Plan d’eau validé ; démarches hors du périmètre de ce dossier | Acté |
| P06 | Nombre de bateaux | Inscriptions ouvertes à tous sur battleboats.fr : nombre inconnu. Dimensionné pour 10 bateaux, 3 bouées et 3 balises de rechange | À confirmer |
| P08 | Source des positions | Proposition au comité : une balise officielle dans chaque bateau, seule source pour le départ, les passages, la pénalité et l’arrivée | *Notre proposition* |
| P09 | Balise à bord | ≈ 250 g, au fond du bateau, poids en bas ; aucun lien avec l’électronique des équipes ; batterie du commerce admise par le règlement | *Notre proposition* |
| P36 | Ordres tactiques des équipes | Libres : par sa propre liaison, chaque équipe envoie ce qu’elle veut à son bateau (ordres, paramètres, réglages, données officielles relayées) | *Notre proposition* |
| P39 | Antennes de la balise | Sur le pont, dans l’axe, quelle que soit la matière de la coque | *Notre proposition* |
| P47 | Bateau de référence | Un IOM du commerce documenté dans le kit, avec un pilote automatique libre et une IA minimale : conseillé, non imposé | *Notre proposition* |
| P44 | Reprises de télécommande | Proposition : chaque reprise de télécommande est déclarée par l’équipe, chronométrée par le logiciel et montrée à l’arbitre ; journal des commandes fourni en cas de réclamation | *Notre proposition* |
| P45 | Mise à jour du logiciel | Interdite pendant une manche, libre entre les manches | *Notre proposition* |
| P48 | Kit équipes | En français et en anglais ; bac à sable ouvert en février 2027 | Acté |
| P11 | Données partagées | Proposition retenue : toutes les équipes reçoivent, au même instant, la position de tous les bateaux et des bouées, le vent, le chrono et les événements. Garde-fous : même délai pour tous, prouvé par un journal ; comportement déclaré en cas de perte du flux ; capteurs embarqués libres en plus | *Notre proposition* |
| P12 | Assistant tactique | Aucun fourni : la tactique est le travail des équipes | Acté |
| P15 | Arbitrage | Proposition : deux arbitres à terre ; le logiciel signale, un arbitre confirme toujours. Le règlement ne décrit que l’arbitre de l’homologation | *Notre proposition* |
| P17 | Chrono | Proposition (niveau 2) : chrono piloté par le PC course, transmis aux équipes, aux médias et au public | *Notre proposition* |
| P52 | Bouées et vent en temps réel | Proposition, en réponse au règlement (§ 5) : position RTK des bouées 1, 2, 3, P1, P2 et vent à la bouée 3, transmis à toutes les équipes au même instant | *Notre proposition* |
| P65 | Perte du flux officiel | Proposition : si le flux s’interrompt en course, chaque bateau applique le comportement déclaré et montré à l’homologation ; le comité peut interrompre la course ; réparation possible pour une équipe lésée | *Notre proposition* |
| P64 | Niveau 2 : notre proposition | Balise dans chaque bateau, jugement assisté, reprises de télécommande chronométrées, application publique, vidéo. ≈ 15 300 € de plus ; à faire retenir par le comité | *Notre proposition* |
| P43 | Limites de vent | Pas de départ sous 4 nœuds ni au-dessus de 20, mesurés à la bouée au vent ; à valider aux essais | *Notre proposition* |
| P20 | Mesure du vent sur l’eau | Réponse au règlement (§ 5, niveau 1) : un anémomètre sur la bouée 3 ; un second en option | *Notre proposition* |
| P21 | Vent à terre | Proposition (niveau 2) : station météo Davis au PC course, vent de référence à terre | *Notre proposition* |
| P22 | Distance PC course ↔ parcours | 500 m au plus ; en pratique ≈ 150 m | Acté |
| P23 | Infrastructure du site | Électricité et Internet filaire disponibles | Acté |
| P24 | Transmission des positions | 4G en principal, radio 868 MHz en secours. Le règlement conseille le Wi-Fi en 5 GHz aux équipes et signale que l’organisation utilise des radios HF (§ 13) : plan de fréquences à partager avec elle | À confirmer |
| P25 | Bus de données | Mosquitto, au PC course, avec un serveur de secours | Acté |
| P26 | Synchronisation | Priorité absolue : écart d’horloge < 5 ms entre équipes, comité et médias | Acté |
| P28 | Choix du matériel | Uniquement du matériel bien noté ; sinon validé au banc | Acté |
| P29 | Ordinateurs | Réutilisation d’ordinateurs existants s’ils respectent le cahier des charges | À confirmer |
| P40 | PC course et caméras | Au premier étage du bâtiment La Plage : à confirmer avec l’organisateur, la zone étant autour du Fort Saint-Louis | À confirmer |
| P30 | Public | Proposition (niveau 2) : sur place et sur l’application, avec 1 s de différé. Le règlement prévoit seulement le tableau officiel en ligne (battleboats.fr) | *Notre proposition* |
| P31 | Commentaire | Proposition (niveau 2) : commentateur humain, aidé par le logiciel (lignes de vent et laylines, souffleur, fiches, résumé automatique) | *Notre proposition* |
| P41 | Fréquentation | 500 à 2 000 spectateurs en même temps ; Wi-Fi public conseillé au village | Acté |
| P32 | Développement logiciel | Meridia, avec des agents IA (GSD) ; 2 à 3 mois de travail | Acté |
| P51 | Technique | Une personne fiable porte la technique : balises, bouées, réseau, caméras ; un suppléant à former | Acté |
| P33 | Licence du logiciel | Non open source | Acté |
| P34 | Budget matériel | ≈ 21 600 €, imprévus compris, caméras embarquées comprises ; ordinateurs neufs ou existants à trancher. Le financement est géré par une autre instance | À confirmer |
| P35 | Présentation | Charte Meridia, version claire | Acté |
| P49 | Hors de notre périmètre | Règlement de course (comité d’organisation : Twelve Med Events), réglementation et autorisations, porteur juridique et assurance, sécurité du public et secours, financement du matériel, accueil du public et communication, recrutement des équipes, tracé et longueur du parcours : gérés par d’autres instances | Acté |
| P50 | Niveaux de repli | Deux niveaux : niveau 1, ce que demande le règlement (bouées RTK et vent) ; niveau 2, notre proposition (balise à bord, jugement assisté, vidéo). Niveaux de repli et trois revues de feu vert conservés | *Notre proposition* |

Dernière mise à jour : 22 novembre 2026.
