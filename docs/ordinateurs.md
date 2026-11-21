# AI Regatta — Cahier des charges des ordinateurs

> Des machines existantes, Mac ou PC, conviennent pour presque tous les rôles, à condition d’être stables, bien réglées et recettées avant l’événement.

## Serveurs du PC course

**Quantité :** 2, idéalement identiques (principal et secours)

Font tourner Mosquitto, le moteur de course, le moteur vent, l’enregistreur et la supervision.

| Critère | Exigence |
|---|---|
| Type | Mini-PC, PC de bureau ou Mac mini ; un portable est acceptable s’il reste branché |
| Âge | Moins de 6 à 7 ans |
| Processeur | 4 cœurs ou plus (Intel Core i5, AMD Ryzen 5, Apple M1 ou plus récents) |
| Mémoire | 16 Go (8 Go minimum) |
| Stockage | SSD de 256 Go minimum, 500 Go conseillés pour les enregistrements et les replays |
| Réseau | Port Ethernet Gigabit obligatoire, ou adaptateur USB-C vers Ethernet de bonne qualité ; pas de Wi-Fi |
| Ports USB | 3 libres : base RTK et deux récepteurs radio ; petit hub USB alimenté accepté |
| Système | Linux (Ubuntu LTS) de préférence ; macOS possible ; Windows à éviter pour les serveurs |
| Alimentation | Branchés sur la batterie de secours |

**Réglages obligatoires**

- Mise en veille et économies d’énergie désactivées
- Mises à jour automatiques suspendues pendant l’événement
- Démarrage automatique des services après une coupure de courant
- Heure calée sur la base RTK (heure GPS) pour le principal, sur le principal pour le secours
- Aucun autre logiciel ouvert, session dédiée à la régate

**Recette avant l’événement**

- 24 h de fonctionnement continu sur le simulateur, sans erreur
- Bascule : on débranche le principal en pleine manche simulée, le secours reprend en moins de 10 s
- Coupure de courant simulée : relais par la batterie de secours

## Régie vidéo

**Quantité :** 1

Fait tourner OBS, qui lit la caméra par le réseau, les incrustations et la diffusion vers YouTube. Prévu : un mini-PC ASUS NUC 14 Pro, comme les serveurs. Il remplace le mélangeur ATEM, qui n’accepte pas la vidéo par le réseau.

| Critère | Exigence |
|---|---|
| Type | PC ou Mac de moins de 5 ans |
| Processeur | 6 cœurs ou plus, ou Apple M1 Pro, M2 et plus récents |
| Carte graphique | Avec encodage vidéo matériel : NVIDIA GTX 1660 ou plus récente, puce Apple Silicon, Intel Quick Sync récent |
| Mémoire | 16 Go |
| Ports | HDMI ou USB-C vidéo, USB 3 pour le boîtier d’acquisition vidéo, Ethernet |
| Écrans | 2 conseillés : régie et contrôle |

**Réglages obligatoires**

- Veille désactivée, notifications coupées
- Heure synchronisée sur le PC course

**Recette avant l’événement**

- 3 h de diffusion continue en 1080p sans saccade
- Incrustations recalées sur l’image

## Consoles du comité

**Quantité :** 3 à 4 (direction de course, arbitrage, sécurité)

Pages web : direction de course, arbitrage, sécurité.

| Critère | Exigence |
|---|---|
| Type | N’importe quel portable ou PC de moins de 7 à 8 ans, Mac ou Windows |
| Logiciel | Navigateur récent : Chrome, Edge, Firefox ou Safari à jour |
| Mémoire | 8 Go |
| Réseau | Ethernet de préférence ; Wi-Fi de l’organisation accepté |
| Écran | 24 à 27 pouces pour la direction de course et l’arbitrage ; écran de portable suffisant pour la sécurité |
| Tablette de l’arbitre | iPad ou tablette Android récente, navigateur à jour, Wi-Fi de l’organisation |

**Réglages obligatoires**

- Veille désactivée
- Mode plein écran, notifications coupées

**Recette avant l’événement**

- Une manche simulée complète suivie sur chaque console
- Écart d’horloge affiché inférieur à 5 ms

## Poste de contrôle

**Quantité :** 1

Recette des balises chaque matin et vérification des fréquences.

| Critère | Exigence |
|---|---|
| Type | Portable, Mac ou PC |
| Ports | 2 USB : balise à tester et analyseur de fréquences TinySA |
| Logiciel | Navigateur et outil de recette fourni (S11) |
| Autonomie | Batterie correcte, pour circuler entre les bateaux |

**Réglages obligatoires**

- Heure synchronisée sur le PC course

**Recette avant l’événement**

- Recette complète d’une balise en moins de 10 min

## Tablette du commentateur

**Quantité :** 1

Souffleur : moments forts, fiches, chrono.

| Critère | Exigence |
|---|---|
| Type | Tablette ou portable léger |
| Logiciel | Navigateur récent |
| Réseau | Wi-Fi de l’organisation |
| Autonomie | Une journée, ou un chargeur à portée |

**Réglages obligatoires**

- Veille désactivée pendant les manches

**Recette avant l’événement**

- Une manche simulée commentée avec le souffleur

## Machines des équipes (conseils)

**Quantité :** Celles des équipes

Recommandations à inscrire dans l’avis de course ; ce ne sont pas des obligations.

| Critère | Exigence |
|---|---|
| Réseau | Port Ethernet ou adaptateur, pour la prise de la zone des équipes |
| Heure | Réglée sur le serveur de temps du PC course (adresse fournie) |
| Logiciel | Un client MQTT dans leur programme ; exemples Python et JavaScript fournis |
| Énergie | Batterie ou rallonge : prises en nombre limité dans la zone |

**Réglages obligatoires**

- Veille désactivée pendant les manches

**Recette avant l’événement**

- Connexion au simulateur avant le 15 mars

## La synchronisation, quel que soit l’ordinateur

Les consoles, la régie et la tablette mesurent elles-mêmes leur écart avec l’horloge du PC course, en échangeant régulièrement de petits messages. Le chrono et l’heure des événements restent justes, même sur une machine mal réglée. La supervision signale toute machine dont l’horloge s’écarte de plus de 5 ms.

## Économie possible

Avec deux machines conformes pour les serveurs et des écrans existants : jusqu’à ≈ 2 250 € de moins sur le budget matériel.
