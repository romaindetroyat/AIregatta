# AI Regatta — Le règlement

> Règlement de course AI Regatta 2027, V1.4 du 15/10/2026, de l’association Twelve Med Events (autorité organisatrice), reçu le 21 novembre 2026 de Xavier Caux. Il fait foi.

## 1. Ce que nous retenons du document

- **Dates**  : Inscriptions et homologation du 12 au 14 mai; régates le samedi 15 mai dès 10 h; report au dimanche 16 (courses finies à 14 h 30); remise des prix le 16 à 16 h 30
- **Lieu**  : Plages du Mourillon, autour du Fort Saint-Louis (Toulon), dans le cadre de la Toulon Provence Regatta; zone de régate matérialisée par des bouées
- **Parcours**  : Parcours construit n°3 : porte 1-2 (départ, porte et arrivée), bouée au vent 3 laissée à bâbord, deux tours; zone de pénalité P1-P2. Longueur fixée par l’organisateur (≈ 200 m retenus pour les calculs)
- **Bateaux admis**  : Voile seule; longueur hors tout de moins de 1 m, 1,30 m ou 2,70 m; monocoques, multicoques, foils admis. Pas de jauge de classe
- **Pilotage des bateaux**  : Mode autonome obligatoire de la ligne de départ à l’arrivée; l’IA peut être embarquée ou à terre (télécommande actionnée par programme)
- **Intelligence tactique**  : Au choix des équipes : embarquée ou à terre (règlement § 2c). Le kit et le bateau de référence partent d’une IA à terre
- **Commande en course**  : Autonome en course; télécommande permise pour rallier le départ, après l’arrivée, en cas de panne, de sortie de zone ou pour la pénalité; chaque reprise : 30 s au plus et un tour de pénalité
- **Présence des équipes**  : Sur place : arrivée une semaine avant la compétition, chaîne d’inscription du 12 au 14 mai (règlement § 6)
- **Règles de course**  : Le règlement de l’organisateur (Twelve Med Events, V1.4) fait foi; RCV pour le parcours construit. Nos règles v0.3 le reprennent et ajoutent nos propositions
- **Sécurité**  : Une organisation sur l’eau récupère les bateaux en difficulté; le bateau de sécurité peut dérouter un bateau. Télécommande de fait indispensable (mode manuel)
- **Signaux du départ**  : Procédure RCV 26 (5, 4, 1 minute, départ); une minute par dérogation. Proposition : signaux sonores déclenchés par le PC course à l’heure GPS
- **Bouées**  : Bouées matérialisant la zone et le parcours; chacun relève leurs coordonnées; l’organisateur cherche à les transmettre en temps réel (RTK et vent)
- **Pénalité**  : Un tour par la zone P1-P2, fait à la fin, avant l’arrivée; un tour aussi pour chaque reprise de télécommande
- **Batteries**  : LiFePO4, ou lithium avec BMS intégré et enveloppe solide du commerce; 48 V au plus. La balise passe à une batterie USB du commerce
- **Communication avec les équipes**  : battleboats.fr, groupe WhatsApp, briefing chaque jour à 9 h 30; vidéo et fiche de présentation avant le 1er mai
- **Préparation sur place**  : Régate de préchauffage au premier trimestre 2027; bâtiment prêté un mois; arrivée des équipes une semaine avant
- **Organisateur**  : L’association Twelve Med Events, autorité organisatrice, sous le patronage de la DGA; l’AI Regatta fait partie de la Toulon Provence Regatta
- **Épreuves**  : Six types de régates : slaloms en duel et Battleboats (bateaux à moteur), régates de voiliers télécommandés ou sous IA. Ce dossier ne couvre que les voiliers sous IA
- **Inscription**  : En ligne sur battleboats.fr, ouverte à tous (écoles, entreprises, particuliers, clubs); 20 € par personne, moins 20 € par bateau inscrit
- **Équipement des équipes**  : Batteries § 12, 48 V au plus; lasers de classe 1 ou 1M seulement; son ≤ 80 dBA à 1 m; air comprimé ≤ 4 bars; radiocommande conforme à la réglementation française; numéro de 10 cm sur la voile
- **Assurance et responsabilité**  : Chaque bateau présente une attestation de responsabilité civile; l’équipe décide seule de courir (§ 16). Hors de notre périmètre
- **Image et données**  : En participant, les équipes autorisent l’organisateur et ses partenaires à utiliser leurs images et leurs données (§ 15) : la vidéo et l’application peuvent les montrer
- **Niveau 1 : demandé par le comité**  : Transmettre en temps réel la position RTK des bouées et le vent (règlement § 5 : l’organisateur cherche des partenaires). ≈ 6 300 € de matériel
- **Homologation**  : Homologation statique par un arbitre avant les régates (chaîne d’inscription, 12 – 14 mai); pas d’épreuve de qualification sur l’eau
- **Classement**  : Par type de régate, sur les résultats des courses. Disqualification : départ anticipé non réparé en 2 min, bouée mal passée, arrivée plus de 5 min après le premier. Proposition : points 1, 2, 3… et une course retirée dès 5 courues
- **Caméras**  : Caméras fixes de 12 m au plus. Le règlement interdit les drones aériens et le survol de la zone, sauf dérogation (§ 10)

## 2. Ce qui manque dans le document, et ce que nous proposons

- **Suivre les bateaux** (Priorité 2) : Rien ne donne la position des bateaux : le départ, les passages et l’arrivée se jugent à l’œil. *Notre proposition :* Une balise scellée dans chaque bateau, posée à l’homologation (règle 2.5).
- **Juger au centimètre** (Priorité 2) : Départ anticipé, bouée mal passée, tour P1-P2, fenêtre des 5 minutes : aucun moyen de mesure. *Notre proposition :* Le logiciel détecte, l’arbitre confirme toujours (règles 5.2 à 5.6).
- **Partager la position des bateaux** (Priorité 2) : Le règlement ne dit pas ce que reçoivent les IA; il laisse les capteurs libres dans les limites du § 12 (lasers de classe 1 ou 1M). *Notre proposition :* Toutes les équipes reçoivent la position de tous les bateaux, des bouées et le vent, au même instant : plus fiable qu’un LIDAR sur l’eau, sans capteur coûteux pour les équipes. Garde-fous : même délai prouvé, comportement déclaré en cas de perte du flux, capteurs embarqués libres en plus (règles 3.7 à 3.9).
- **Mesurer les reprises de télécommande** (Priorité 2) : La limite de 30 s est fixée, mais rien ne la mesure. *Notre proposition :* Chaque reprise déclarée par l’équipe (`manual_control`) et chronométrée (règle 3.4).
- **Transmettre les données aux équipes** (Priorité 1) : Le règlement demande la position RTK des bouées et le vent en temps réel (§ 5), sans dire comment. *Notre proposition :* Une page web et un flux MQTT, mêmes données au même instant pour toutes les équipes (niveau 1).
- **Les fréquences** (À inscrire) : Rien sur la radio des balises; le Wi-Fi 5 GHz est seulement conseillé (§ 13). *Notre proposition :* La sous-bande 869,4 – 869,65 MHz réservée aux balises (règle 2.7).
- **L’arbitrage et les réclamations** (À proposer) : Seul l’arbitre de l’homologation est décrit; ni jury, ni délai de réclamation. *Notre proposition :* Deux arbitres à terre devant les rejeux; réclamation par message dans les 10 minutes (règles 6.1, 6.2).
- **Le barème du classement** (À proposer) : « Sur les résultats des courses », sans barème ni course retirée. *Notre proposition :* 1, 2, 3…; une course retirée dès 5 courues (règle 6.4).
- **Le nombre de courses et les poules** (À proposer) : Une journée de course, sans nombre de courses ni format. *Notre proposition :* Poules de 4 à 5 bateaux, pour que deux arbitres suivent.
- **Les limites de vent** (À proposer) : Aucune. *Notre proposition :* Pas de départ sous 4 ni au-dessus de 20 nœuds, mesurés à la bouée 3 (règle 4.6).
- **Le logiciel pendant une course** (À proposer) : Rien sur les mises à jour. *Notre proposition :* Pas de mise à jour pendant une course, libre entre les courses (règle 3.5).
- **La zone de bouée** (À proposer) : Les RCV s’appliquent, mais des bateaux de 1 m à 2,70 m peuvent courir ensemble. *Notre proposition :* 4 m pour les bateaux de moins de 1,30 m; à fixer pour 2,70 m (règle 1.4).
- **Les signaux de départ** (À proposer) : La procédure est fixée, pas la façon de la donner. *Notre proposition :* Signaux sonores déclenchés à l’heure GPS, pour l’une ou l’autre procédure (règle 4.3).

## À vérifier avec l’organisateur

- L’emplacement exact de la zone de régate et du PC course (le premier étage de La Plage convient-il ?).
- Le nombre de voiliers IA attendus, et si plusieurs types de longueur courent ensemble.
- La longueur du parcours n°3, la largeur de la porte 1-2 et la position de P1-P2.
- Qui arbitre et qui forme le jury.
- La date et le lieu de la régate de préchauffage.

## 3. Nos postulats, en résumé

**Ce que nous proposons au comité.** Le dispositif s’appuie sur deux niveaux. Le premier répond à sa demande : la position RTK des bouées et le vent mesuré sur la bouée au vent, transmis à toutes les équipes au même instant. Le second ajoute une balise scellée dans chaque bateau, qui devient la seule source pour juger le départ, les passages, la pénalité et l’arrivée; toutes les équipes reçoivent alors la position de tous les bateaux. Autour de ce noyau, quelques règles simples : des reprises de télécommande déclarées et chronométrées, un comportement déclaré si le flux s’interrompt, pas de mise à jour du logiciel pendant une course, des départs entre 4 et 20 nœuds, et un arbitre qui confirme toujours ce que le logiciel signale.

**Ce que nous avons fixé de notre côté.** Le matériel est choisi parmi des références bien notées ou validées au banc. Les données passent par la 4G, avec une radio de secours, et toutes les machines partagent l’heure GPS à quelques millisecondes près. Meridia développe le logiciel avec des agents IA; une personne fiable porte la technique. Les équipes reçoivent un kit en français et en anglais, un bac à sable en février et la fiche d’un bateau de référence; la tactique reste leur affaire.

**Ce qui reste à confirmer.** Le nombre de bateaux inscrits, l’emplacement du PC course, le choix entre ordinateurs neufs et existants, et le financement du matériel, estimé à 21 600 €.


Dernière mise à jour : 22 novembre 2026.
