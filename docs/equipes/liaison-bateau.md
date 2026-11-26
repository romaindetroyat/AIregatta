# AI Regatta — Piloter votre bateau depuis l’ordinateur

> Version 2.0-draft, 26 novembre 2026. Remplace la version du 20 novembre. Concerne la liaison entre l’ordinateur de l’équipe, à terre, et son bateau.
> Trois montages sont proposés. Aucun n’est encore validé sur l’eau : un kit d’essai de chacun doit être testé avant le choix définitif. Fiches de présentation : [fiche-liaison-ordinateur.pdf](fiche-liaison-ordinateur.pdf).

## 1. Qui fait quoi

| | Organisation | Meridia | Équipe |
|---|---|---|---|
| Position officielle du bateau | Balise officielle, scellée, autonome | Traite ses données | Implante la balise |
| Flux de course (positions, vent, chrono…) | Le fournit à toutes les équipes | Le diffuse | Le reçoit sur son ordinateur |
| **Liaison ordinateur → bateau** | Recommande trois montages (A, B, C) et fixe les règles radio | Fournit le **programme de liaison**, sur Mac et PC | Achète, installe et règle son matériel |
| Tactique | Aucun assistant fourni | — | C’est son travail : son IA, sur son ordinateur |
| Sécurité sur l’eau | Bateaux d’assistance | — | Déclare le comportement du bateau en cas de coupure |

**La balise officielle n’a aucun lien avec votre électronique** : elle a sa propre batterie et ne reçoit rien de votre bateau. Votre bateau reste suivi et classé même si toute votre électronique tombe en panne.

## 2. Les trois montages

Dans les trois cas :
- l’IA de l’équipe, à terre, décide et envoie des ordres de tacticien (§4) ;
- le **programme de liaison** fourni par Meridia transmet ces ordres au bateau ;
- la radio est de l’**ExpressLRS en 2,4 GHz**, le système des drones de course ;
- les **servos du bateau** (safran, treuil d’écoute) ne changent pas.

### A. Radio imposée avec prise écolage + petit boîtier

```
Ordinateur ── USB ── petit boîtier ── jack ── radio imposée  ))) radio )))  récepteur ER4 → safran + écoute
```

- **Principe** : la prise écolage sert normalement aux cours de pilotage. Le boîtier fait semblant d’être la radio de l’élève ; la radio obéit à l’ordinateur. Un interrupteur de la radio choisit qui pilote : l’ordinateur ou un humain.
- **Radio imposée** : RadioMaster Pocket ou TX12 MKII, version ExpressLRS.
- **Le boîtier** : aucun boîtier tout fait n’existe. Il est fabriqué par un partenaire ou un fablab : une petite carte électronique, un câble jack, un câble USB, un boîtier étanche, environ 20 € de pièces. Liste d’achat : page « Pièces du boîtier écolage ».
- **La barre** : l’ordinateur commande directement le safran et l’écoute. Il barre à partir du cap donné par la balise officielle.
- **Coût par équipe** : ≈ 100 à 170 € (radio 65 à 130 €, récepteur ≈ 18 €, boîtier ≈ 20 €).
- **Fiabilité** : la prise écolage est une technique ancienne, avec de nombreux retours positifs. Le boîtier reste à mettre au point.
- **Ce que ça impose** : acheter la radio imposée, changer le récepteur du bateau, régler la radio une fois.

### B. ExpressLRS complet, sans radio

```
Ordinateur ── USB-C ── émetteur Ranger Micro  ))) radio )))  récepteur ER4 → safran + écoute
```

- **Principe** : l’ordinateur pilote directement un petit émetteur du commerce. Pas de radio, rien à fabriquer.
- **La barre** : comme en A, l’ordinateur commande directement le safran et l’écoute, à partir du cap de la balise officielle.
- **Coût par équipe** : ≈ 60 à 90 € (émetteur et câble ≈ 43 €, récepteur ≈ 18 €, batterie et adaptateur si besoin). Liste d’achat : page « Pièces de la liaison ExpressLRS ».
- **Fiabilité** : la radio vers le bateau est très éprouvée. Le lien entre l’ordinateur et l’émetteur reste à valider : les témoignages sont mitigés.
- **Ce que ça impose** : changer le récepteur du bateau, régler l’émetteur une fois depuis un téléphone.

### C. Le système des drones : pilote automatique à bord

```
Ordinateur ── USB-C ── émetteur Ranger Micro  ))) radio, dans les deux sens )))  récepteur RP2 → pilote automatique → safran + écoute
                                                                                         ↑ GPS, compas, girouette
```

- **Principe** : on reprend le montage complet d’un drone. À bord, une carte de pilote automatique (Matek H743-WING avec le logiciel libre ArduPilot, en mode voilier) barre et règle l’écoute toute seule. L’ordinateur envoie des ordres de tacticien : « cap 45° », « vire », « va à la bouée ». En retour, il reçoit le cap, la vitesse et l’état du bateau.
- **La liaison** : le même émetteur qu’en B, réglé pour transporter les ordres et les retours du bateau dans les deux sens. Ce branchement en USB entre l’ordinateur et l’émetteur est **documenté officiellement** par ExpressLRS ; il utilise le langage standard des drones pour parler à un ordinateur (MAVLink).
- **Coût par équipe** : ≈ 290 à 390 € (carte ≈ 110 €, GPS et compas ≈ 45 €, girouette 50 à 150 €, émetteur et câble ≈ 43 €, récepteur ≈ 22 €, batterie 3S ≈ 20 €). Liste d’achat : page « Pièces du pilote automatique ».
- **Fiabilité** : la liaison et le logiciel sont éprouvés sur des milliers de drones et de bateaux autonomes. Le mode voilier existe mais il faut l’apprendre au bateau : réglages et essais sur l’eau.
- **Ce que ça impose** : installer la carte, le GPS, la girouette et une batterie 3S (la carte demande 8 V au moins) ; changer le récepteur ; plusieurs sorties d’essai pour régler le pilote.
- **Atout** : le bateau barre seul. Le délai de la liaison ne le gêne pas, et les ordres correspondent au métier de tacticien.

### Comparaison

| | A. Écolage + boîtier | B. ExpressLRS sans radio | C. Pilote à bord |
|---|---|---|---|
| Coût par équipe | ≈ 100 à 170 € | ≈ 60 à 90 € | ≈ 290 à 390 € |
| Ce qui change dans le bateau | Le récepteur | Le récepteur | Récepteur, carte, GPS, girouette, batterie 3S |
| Qui barre | L’ordinateur, à terre | L’ordinateur, à terre | Le pilote, à bord |
| Rien à fabriquer | Non : le boîtier | Oui | Oui |
| Reprise en main par un humain | Interrupteur de la radio | Avec une radio ExpressLRS en plus | Avec une radio ExpressLRS en plus |
| Point à valider | Le boîtier | Le lien ordinateur-émetteur | Les réglages du pilote sur l’eau |

### Les essais avant de choisir

Un kit d’essai par montage, testé dans le même ordre :
1. **Sur la table** : l’ordinateur fait bouger le safran et l’écoute dans le bon sens.
2. **Endurance** : plusieurs heures d’affilée, sur Mac et sur PC, en comptant les coupures.
3. **À l’eau** : portée jusqu’au point le plus loin du parcours, mise en sécurité quand on coupe l’ordinateur. Pour C, cap tenu et virements automatiques.

Budget indicatif : ≈ 200 € pour A et B, ≈ 350 € de plus pour C ; 3 à 4 jours de travail pour A et B, une semaine de plus pour C (réglages sur l’eau).

## 3. Les règles radio

| Bande | Usage | Règle |
|---|---|---|
| **2 400–2 483,5 MHz** | Liaison de l’équipe (ExpressLRS), radio de secours | **100 mW au plus**, antenne comprise. Les émetteurs proposés sont réglés à 100 mW d’usine : ne pas augmenter |
| 869,4–869,65 MHz | Radio de secours des balises officielles | **Interdite aux équipes** |
| 5 GHz (Wi-Fi) | Réseau de l’organisation sur le site | Interdit aux équipes sans accord |

**Déclaration à l’inscription** : chaque émetteur (type, puissance réglée, antenne, usage). Tout changement est déclaré avant d’être utilisé. L’organisation peut vérifier les réglages au contrôle.

**Une version logicielle figée** : ExpressLRS change souvent. L’organisation fixe une version, la même pour toutes les équipes, jusqu’à la régate (version 3.5 au moins pour le montage C).

**Antenne du récepteur** : le signal passe moins bien au ras de l’eau et à travers une coque en carbone. Placer l’antenne haut, hors de la coque si possible.

## 4. Les ordres de tacticien

### 4.1 La liste des ordres

L’IA de l’équipe envoie au programme de liaison des ordres simples. En A et B, le programme les traduit en mouvements de safran et d’écoute ; en C, il les transmet au pilote automatique, qui les exécute. Les ordres se rangent en deux familles : les **manœuvres**, ponctuelles, et les **modes**, qui restent actifs jusqu’à l’ordre suivant. Cette liste est la référence commune ; elle pourra être complétée avant le gel du 15 mars 2027.

**Manœuvres**

| Ordre | Code proposé | Effet attendu | Paramètre facultatif |
|---|---|---|---|
| Vire | `tack` | Virement de bord (l’avant du bateau passe face au vent) | — |
| Empanne | `gybe` | Empannage (l’arrière du bateau passe face au vent) | — |
| Abats | `bear_away` | Contournement de la **bouée au vent** : une fois la bouée passée, le bateau s’écarte du vent pour partir au portant | `mark_id`, `side` (côté de passage) |
| Loffe | `head_up` | Contournement de la **bouée sous le vent** (ou de la porte) : une fois la bouée passée, le bateau remonte vers le vent | `mark_id`, `side` |
| Face au vent | `head_to_wind` | Le bateau se met bout au vent et s’arrête, voiles qui faseyent | `duration_s` |

**Modes**

| Ordre | Code proposé | Effet attendu | Paramètre facultatif |
|---|---|---|---|
| Mode près | `mode_upwind` | Navigation vers le vent, au plus près efficace | `twa_deg` : angle au vent vrai visé |
| Mode portant | `mode_downwind` | Navigation vent arrière ou grand largue | `twa_deg` |
| Mode VMG | `mode_vmg` | Le bateau cherche la meilleure vitesse utile vers la bouée | `twa_deg` |
| Mode haut | `mode_high` | Le bateau serre le vent (plus près, moins vite) | `twa_deg` |
| Mode bas | `mode_low` | Le bateau s’écarte du vent (plus loin, plus vite) | `twa_deg` |
| Cap | `heading` | Tenir un cap fixe | `heading_deg` (degrés vrais) |

**Réglages**

| Ordre | Code proposé | Effet | Paramètre |
|---|---|---|---|
| Choque | `ease` | Relâcher l’écoute | `amount_pct` |
| Borde | `trim` | Reprendre l’écoute | `amount_pct` |

**VMG** (*velocity made good*) : la vitesse à laquelle on se rapproche réellement de la bouée. **TWA** (*true wind angle*) : l’angle entre l’axe du bateau et le vent vrai.

### 4.2 Format des ordres

Le programme de liaison reçoit les ordres dans un format commun :

```json
{
  "v": 1,
  "kind": "order",
  "boat_id": "FRA-07",
  "order_id": 1842,
  "t_gps_ms": 1494421447200,
  "cmd": "mode_high",
  "param": {"twa_deg": 38},
  "ttl_ms": 2000
}
```

Il répond par un accusé de réception (`"kind": "ack"`, `status` : `accepted`, `rejected`, `expired`), puis par un compte rendu (`"kind": "report"`, `status` : `started`, `done`, `failed`, `aborted`).

| Champ | Description |
|---|---|
| `boat_id` | Bateau visé |
| `order_id` | Numéro croissant ; un ordre déjà reçu n’est pas exécuté deux fois |
| `t_gps_ms` | Instant d’émission, même convention que le contrat d’interface |
| `cmd`, `param` | L’ordre et ses paramètres (§4.1) |
| `ttl_ms` | Durée de validité : un ordre arrivé trop tard est refusé, pour ne pas virer au mauvais moment |

Le programme tient le **journal des ordres**, fourni au jury en cas de réclamation.

### 4.3 Ce qui est tranché

Décisions du 20 et du 21 novembre 2026 :
- l’IA peut commander directement le safran et l’écoute ; aucun humain ne barre en course, sauf arrêt de sécurité ;
- les paramètres des ordres sont libres (angles, points de passage) ;
- les données officielles peuvent être utilisées à bord comme à terre ;
- le journal des ordres est fourni au jury en cas de réclamation.

À trancher : l’usage de l’interrupteur de reprise en main pendant la course (sécurité seulement, ou pénalité).

## 5. Perte de liaison et sécurité

Chaque équipe déclare à l’inscription ce que fait son bateau quand il ne reçoit plus rien, et le démontre au contrôle.

- **Montages A et B** : le récepteur met le bateau dans une position réglée à l’avance : **safran droit, écoute choquée**. Le bateau ralentit et dérive.
- **Montage C** : le pilote garde le cap quelques secondes, puis rejoint un point de sécurité déclaré ou se met face au vent.

Les témoignages montrent que ce comportement ne va pas de soi (délai caché, bateau qui accélère) : il se teste sur l’eau, en coupant l’ordinateur.

- La sécurité sur l’eau est assurée par les **bateaux d’assistance** de l’organisation, qui peuvent récupérer un bateau à tout moment.
- La reprise en main par un humain n’est autorisée en course que pour la sécurité ; elle vaut abandon et se signale au comité (`retire`, `safety`).
- Un bateau qui a perdu sa liaison reste suivi et classé par sa balise officielle. L’équipe prévient le comité (`technical_issue`, ou `assistance_request` si le bateau devient dangereux).
