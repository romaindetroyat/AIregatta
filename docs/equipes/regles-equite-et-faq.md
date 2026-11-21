# AI Regatta — Règles d’équité, liste de contrôle et questions fréquentes

> Version 1.0-draft, 20 novembre 2026. Les règles de course elles-mêmes (P14) et l’arbitrage (P15) seront publiés à part.

## 1. Règles d’équité

Le principe : **toutes les équipes reçoivent les mêmes données, au même instant, par le même chemin** (P11). La différence doit venir du bateau et de la tactique, pas de l’accès à l’information.

| # | Règle | Statut |
|---|---|---|
| E1 | **Même câble pour tous** : chaque équipe est branchée par un câble Ethernet de même longueur, sur le même commutateur, au même réseau « équipes » | Acté |
| E2 | **Même broker, même flux** : un seul broker (Mosquitto, P25), les mêmes sujets et les mêmes messages pour toutes les équipes ; aucun flux privilégié, aucune priorité | Acté |
| E3 | **Lecture seule** : une équipe ne peut écrire que dans son propre `outbox`. Elle ne voit ni l’`inbox` ni l’`outbox` des autres | Acté |
| E4 | **Pas d’accès aux données internes** : la santé des balises (`sys/beacons/#`), les consoles du comité et les flux de l’organisation sont fermés aux équipes | Acté |
| E5 | **Une seule source de position officielle** : la balise officielle (P08). Les équipes ne reçoivent aucune donnée de la balise par un autre chemin (P09) | Acté |
| E6 | **Pas d’autre source de données sur l’eau** que les capteurs de son propre bateau : pas de bouée, drone, bateau suiveur, observateur ou caméra de l’équipe sur ou au-dessus du plan d’eau | À confirmer |
| E7 | **Pas d’assistant tactique** fourni par l’organisation (P12). La tendance du vent (`wind/trend`) est une donnée commune, pas un conseil | Acté |
| E8 | **Même information pour les réponses du comité** : une réponse qui intéresse tout le monde est publiée en avis (`notices`) à toutes les équipes | Acté |
| E9 | **Fichiers de rejeu** mis à disposition de toutes les équipes en même temps | Acté |
| E10 | **Plan de fréquences** respecté, émetteurs déclarés, puissance réglée ([liaison-bateau.md](liaison-bateau.md)) | Acté |
| E11 | **Pas de brouillage** ni d’écoute de la liaison d’une autre équipe ; pas de tentative d’accès aux comptes ou au réseau des autres | Acté |
| E12 | **Corrections RTK** de la base officielle (pour un GPS centimétrique sur votre bateau) : soit offertes à toutes les équipes sur le réseau, soit à personne | À confirmer (architecture §12, question 4) |
| E13 | **Sources à terre** (anémomètre de l’équipe sur la digue, prévisions météo sur Internet, vidéo publique) : autorisées ou non | À confirmer |

## 2. Liste de contrôle avant le jour J

À faire, et à cocher, avant la première manche (au plus tard la veille, lors du test de connexion sur le site).

**Inscription et comptes**

- [ ] Compte `equipe-<code>` reçu et testé sur le **bac à sable** (identifiant et mot de passe)
- [ ] Mot de passe du **site** reçu (différent de celui du bac à sable) et stocké hors du code (variable d’environnement, gestionnaire de mots de passe)
- [ ] Certificat `ca-ai-regatta.crt` installé (logiciel et, si besoin, navigateur)
- [ ] Contrat d’interface en version `1.0.0` (gelée) : vérifié dans `meta/schema`

**Heure**

- [ ] chrony (ou client NTP équivalent) réglé sur `10.20.0.1` sur **chaque** PC qui affiche le chrono ou envoie des messages
- [ ] `chronyc tracking` : écart **< 5 ms**
- [ ] Écart mesuré avec `sys/time` (minimum sur 60 s) **< 5 ms**
- [ ] Compte à rebours calculé à partir de `start_t_gps_ms`, **pas** de l’heure d’arrivée des messages

**Flux**

- [ ] Abonnement à `race/current`, puis à `race/<raceId>/#` : parcours, chrono, positions de tous les bateaux reçus
- [ ] Reconnexion testée : câble débranché 30 s, puis rebranché ; le logiciel se réabonne seul et reconstruit l’état
- [ ] Doublons et messages en retard écartés (`seq`)
- [ ] Bateau perdu (`stale: true`) et passage radio (`path: "radio"`, 2 Hz, cap `null`) gérés sans plantage
- [ ] Repli testé sur le **Wi-Fi** de la zone équipes

**Messages au comité**

- [ ] `ack` envoyé sur un avis de test, `receipt` reçu en retour dans l’`inbox`
- [ ] Réclamation de test (`protest`) envoyée et accusée sur le bac à sable
- [ ] Procédure connue pour `assistance_request` **et** l’appel direct à l’officier de sécurité

**Bateau**

- [ ] Fréquences, canaux et puissances **déclarés** à l’inscription, et réglages conformes
- [ ] Comportement en **perte de liaison** déclaré et **testé** (couper l’émetteur à terre, observer le bateau)
- [ ] Arrêt de sécurité testé, si l’équipe en a un
- [ ] Balise officielle installée, scellé vérifié, distance antenne-étrave mesurée au contrôle (S11)

## 3. Questions fréquentes

**1. Pouvons-nous recevoir le flux par la 4G ou Internet au lieu du câble ?**
Non, pas pendant les manches : toutes les équipes sont sur place (P13) et reçoivent le flux par câble, pour une latence identique. Il n’y a pas de miroir cloud du flux équipes le jour J. Le bac à sable cloud sert au développement, avant l’épreuve.

**2. Le chrono que j’affiche peut-il être en retard sur celui du comité ?**
Pas si vous suivez le §7 du contrat : avec chrony calé sur `10.20.0.1` et un compte à rebours calculé à partir de l’heure GPS du départ, votre chrono est juste à quelques millisecondes près, même si le réseau ralentit. Il ne faut jamais décompter à partir de l’arrivée des messages.

**3. Quelle est la position « officielle » d’un bateau : l’antenne ou l’étrave ?**
L’arbitrage utilise l’**étrave** (`reference_point: "bow"`) : c’est `bow_lat`/`bow_lon`, calculée par le PC course à partir de l’antenne, de la distance antenne-étrave mesurée au contrôle et du cap. `lat`/`lon` donnent l’antenne.

**4. Pourquoi mon bateau saute-t-il parfois à 2 positions par seconde ?**
Sa balise est passée sur la **radio de secours** 868 MHz (`path: "radio"`), en général parce que la 4G est saturée. Le cap et la gîte ne sont alors pas transmis (`null`), et l’étrave est estimée par la route fond. La balise revient seule sur la 4G.

**5. Pouvons-nous utiliser les positions de notre propre GPS ?**
Oui, pour votre propre pilotage et votre tactique. Mais elles ne servent ni au suivi, ni au classement, ni à l’arbitrage (P08), et vous ne pouvez pas les publier sur le broker.

**6. Pouvons-nous renvoyer à notre bateau les positions des autres bateaux ?**
C’est acté depuis le 21 novembre 2026 (P36). Les données sont les mêmes pour tous, donc cela ne crée pas d’inégalité.

**7. Pouvons-nous barrer notre bateau au joystick ?**
C’est acté depuis le 20 novembre 2026 (règles 3.2 à 3.4) : **un humain ne barre pas en course**, sauf l’arrêt de sécurité ; **une IA qui barre seule, sans intervention humaine**, est autorisée, même depuis la terre. En course, vous envoyez des ordres tactiques (vire, empanne, mode VMG, haut, bas), éventuellement avec un angle visé.

**8. Notre liaison avec le bateau est tombée en pleine manche. Que se passe-t-il ?**
Votre bateau applique le comportement que vous avez déclaré (par exemple : garder le mode, puis rejoindre un point de sécurité, puis se mettre bout au vent). Il reste suivi et classé par sa balise. Prévenez le comité (`technical_issue`), et demandez de l’aide si le bateau devient dangereux (`assistance_request`, plus appel direct).

**9. Comment faire une réclamation ?**
Par un message `protest` dans votre `outbox`, en précisant le ou les bateaux, l’instant de l’incident et ce qui s’est passé ; vous recevez un `receipt` avec un numéro de réclamation. Délais et forme exacte : règle 9.3 : dans les 10 minutes qui suivent l’arrivée du dernier bateau. Le jury dispose des traces officielles et de la vidéo.

**10. Que faire si nous voyons une donnée officielle manifestement fausse (bouée mal placée, bateau absent) ?**
Envoyez un `technical_issue` avec `component: "data_feed"` et l’heure UTC. Si cela vous a fait perdre des places, une `redress_request` (demande de réparation) est possible, selon les instructions de course.

**11. Le contrat peut-il encore changer ?**
Oui jusqu’au **15 mars 2027**, après annonce et test sur le bac à sable. Ensuite il est gelé en `1.0.0` : seuls des ajouts compatibles annoncés 30 jours à l’avance sont possibles. Ignorez les champs inconnus et vous resterez compatibles.

**12. Pouvons-nous connecter plusieurs ordinateurs avec le même compte ?**
Oui, jusqu’à 3 connexions simultanées (à confirmer), chacune avec un **identifiant client différent** (`equipe-fra07-tactique`, `equipe-fra07-ecran`…). Deux connexions avec le même identifiant se déconnectent mutuellement.

**13. Notre logiciel de navigation ne parle pas MQTT. Comment voir la flotte ?**
Branchez-le sur le flux **NMEA 0183** (`10.20.0.10:10110`) : les bateaux apparaissent comme des cibles AIS et les bouées comme des aides à la navigation. Voir [connecteurs.md](connecteurs.md#c-nmea-0183-sur-tcp--pour-les-logiciels-de-navigation).

**14. Pouvons-nous tester avec de vraies données avant mai ?**
Oui : les manches d’essai d’avril et la régate blanche sont enregistrées et publiées en fichiers de rejeu (JSON Lines et Parquet), rejouables sur le bac à sable.
