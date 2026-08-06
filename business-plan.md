# CardTide — Intelligence de marché pour cartes à collectionner
### Plan d'affaires complet — MVP en 7 jours, budget 0€

> **Cadrage retenu** : débutant total en code, 0€ de budget, aucune cible client imposée (B2B/B2C), aucun secteur imposé si ce n'est une appétence pour jeux vidéo / anime / One Piece / animaux / immobilier / bébé, tolérance au risque élevée ("viser le max, pivoter si ça ne marche pas"), accès web utilisé pour valider chaque hypothèse de marché ci-dessous.
>
> **Niveau de confiance** : les chiffres de marché (croissance, indices) viennent de sources publiques récentes (citées par nom dans le texte) et sont fiables à haute confiance. Les estimations SAM/SOM et les prévisions financières sont des **hypothèses raisonnées, pas des garanties** — elles sont signalées comme telles.

---

## 1. Résumé exécutif

**CardTide** est un outil d'alerte et d'intelligence de marché pour les cartes à collectionner (Trading Card Games), lancé sur un premier terrain de jeu en pleine explosion : le marché secondaire du **One Piece Card Game (OPCG)**. Début 2026, l'indice Card Ladder de l'OPCG affiche +119 % sur 6 mois et +61,4 % sur 3 mois ; certains produits scellés (booster box OP01) ont pris +299 % sur 2025 ; le jeu pèse 300-400 M$ de revenus annuels avec plus de 50 % de croissance.

**Client** : le collectionneur/investisseur francophone actif sur le marché secondaire (Cardmarket, boutiques spécialisées), qui doit aujourd'hui surveiller les prix manuellement, en anglais, sur des outils pensés pour le marché américain en dollars.

**Problème** : aucun outil identifié ne combine alertes de **valeur** (pas de stock) + **français** + **euros/Cardmarket**. Un serveur Discord français existant couvre uniquement les alertes de réassort en boutique (produit différent, marché "rouge") — le marché secondaire francophone est un vide ("océan bleu").

**Solution** : alertes personnalisées par carte suivie, livrées sur Telegram, + rapport de marché hebdomadaire gratuit qui construit l'audience et le SEO.

**Revenus** : freemium — gratuit (5 cartes, alertes différées) / Premium 6,99€/mois (suivi illimité, temps réel) / Pro 29€/mois (boutiques, API). Revenus complémentaires par affiliation marketplace.

**Potentiel** : coût d'infrastructure quasi nul (automatisation gratuite), donc rentabilité atteignable dès les premiers abonnés. Trois leviers de croissance : extension multi-jeux (Pokémon, Dragon Ball Super, Magic), extension géographique (Cardmarket couvre déjà DE/ES/IT), offre B2B pour boutiques et revendeurs. MVP réalisable en **7 jours**, sans compétence technique préalable, avec du code livré prêt à l'emploi.

---

## 2. Analyse complète du marché

### 2.1 TAM / SAM / SOM

| Niveau | Estimation | Source / confiance |
|---|---|---|
| **TAM** (marché mondial cartes à collectionner physiques) | ~7,5 à 8,5 Md$ en 2025 (hors sport/digital pur ; 13-15 Md$ en les incluant) | Consensus Mordor Intelligence / BCC Research / Global Market Insights, cité dans l'analyse macro OPTCG 2026 — **haute confiance** |
| **TAM spécifique OPCG** | 300-400 M$/an, +50 %/an | OPTCG Macro Market Analysis 2026 — **haute confiance** |
| **SAM** (collectionneurs francophones actifs sur le marché secondaire) | Quelques dizaines de milliers de personnes (estimation croisée : boutique officielle Bandai à Paris, réseau de boutiques FR type LorenZone/carteonepiece.fr, tournois régionaux à Bonn/Lille, communauté Discord FR dédiée existante) | **Confiance modérée** — aucune donnée chiffrée officielle FR trouvée ; à valider par la taille réelle du canal Telegram dès le lancement |
| **SOM** (An 1, atteignable) | Quelques centaines à quelques milliers d'utilisateurs gratuits, quelques dizaines à ~250 payants fin d'année 1 | **Hypothèse de planification**, voir prévisions financières §11 |

### 2.2 Barrières à l'entrée, Moat, Effets de réseau, Scalabilité

- **Barrières à l'entrée** : techniques quasi nulles (n'importe qui peut copier le code) → la vraie barrière est la **confiance communautaire** et l'**historique de données** accumulé, qui prennent du temps à construire.
- **Moat** : dataset propriétaire de prix qui grossit chaque jour (avantage qui se compose), marque de confiance dans une niche passionnée, et spécialisation FR/EUR qu'un acteur US n'a pas d'incitation immédiate à répliquer.
- **Effets de réseau** : faibles au tout début (V1 = outil individuel), mais activables vite : classement communautaire des meilleurs "spotters" de deals, portefeuilles partageables, contenu généré par les utilisateurs → chaque nouvel utilisateur actif enrichit l'expérience des autres.
- **Scalabilité** : très forte — le coût marginal par utilisateur supplémentaire est proche de zéro (automatisation, pas de main-d'œuvre par client), et l'architecture se réplique telle quelle sur chaque nouveau jeu de cartes ou pays.

### 2.3 SWOT

| | Aide | Nuit |
|---|---|---|
| **Interne** | **Forces** : passion réelle du fondateur pour le sujet (accélère la création de contenu authentique), coût de départ quasi nul, mise en ligne en 7 jours, marché en forte hausse au moment du lancement | **Faiblesses** : fondateur non technique (dépendance au code livré et à la documentation), pas de relation officielle établie avec un fournisseur de données au départ, marque et audience à construire de zéro |
| **Externe** | **Opportunités** : sortie mondiale désormais synchronisée JP/Occident dès l'OP16-OP17 2026 (calendrier d'événements prévisible = pics d'attention exploitables pour le contenu), extension multi-jeux et multi-pays, offre B2B boutiques | **Menaces** : cycle de hype qui pourrait ralentir (la croissance du marché est qualifiée d'"if considérable" par l'analyse macro elle-même), dépendance à un fournisseur de données tiers, un acteur établi (Card Ladder, TCGplayer) pourrait localiser son offre en français |

### 2.4 PESTEL

| Facteur | Constat |
|---|---|
| **Politique** | Aucune régulation spécifique du commerce de cartes à collectionner en France |
| **Économique** | Statut micro-entreprise très adapté au démarrage ; franchise en base de TVA jusqu'à 37 500€ de CA services en 2026 |
| **Socioculturel** | Essor de la "culture collector" (anime, TCG, sneakers) chez les 18-35 ans ; l'adaptation Netflix de One Piece est citée comme catalyseur de la demande |
| **Technologique** | APIs de données de prix disponibles (officielles et tierces), automatisation et messagerie gratuites (GitHub Actions, Telegram) |
| **Environnemental** | Non significatif — produit 100 % numérique |
| **Légal** | CGU des marketplaces à respecter pour la réutilisation commerciale de données ; RGPD sur la gestion des abonnés ; statut auto-entrepreneur pour facturer légalement ; facturation électronique obligatoire en cours de déploiement 2026-2027 |

### 2.5 Porter — 5 forces

| Force | Niveau | Commentaire |
|---|---|---|
| Nouveaux entrants | Moyen-élevé | Barrière technique faible, mais barrière de confiance/communauté élevée |
| Pouvoir fournisseurs (données prix) | Moyen-élevé au départ | Dépendance à une API tierce → à réduire en migrant vers l'accès officiel Cardmarket + multi-sources |
| Pouvoir clients | Élevé au départ | Alternatives gratuites nombreuses (veille manuelle, Discord) → CardTide doit gagner par la spécificité FR et un niveau gratuit généreux |
| Substituts | Veille manuelle, outils US non localisés, Discord de restock (produit différent) | |
| Rivalité | Modérée | Acteurs établis anglophones/USD ; aucun positionné FR/EUR sur le marché secondaire à ce jour |

### 2.6 Océan Bleu vs Océan Rouge

- **Rouge (saturé)** : alertes de réassort générique, outils de suivi de prix anglophones/USD déjà matures (TCGSniper, Card Ladder, TCGIndex, PokeTrace, CardPulse, Hall of Cards, SNKRDUNK).
- **Bleu (à créer)** : intelligence de marché secondaire + contenu communautaire **en français, en euros, sur Cardmarket**, avec alertes personnalisées et rapport hebdomadaire — combinaison non occupée d'après la recherche menée.

---

## 3. Analyse concurrentielle

| Concurrent | Marché / langue | Prix | Forces | Faiblesses | Comment le dépasser |
|---|---|---|---|---|---|
| **TCGSniper** | US, EN/USD (TCGplayer, Card Kingdom) | Gratuit (15 alertes) + Plus payant | UX simple, alertes DM ciblées, modèle freemium **validé sur le marché** | Aucune couverture Cardmarket/EUR, zéro contenu FR | Répliquer le modèle freemium mais sur Cardmarket + EUR + FR, ajouter le contenu communautaire qu'ils n'ont pas |
| **Card Ladder / TCGIndex** | Global, EN/USD | Payant (analytics) | Données historiques riches, crédibilité "investisseur" | Complexe pour un collectionneur casual, cher, pas d'alertes actionnables simples, aucun FR | Simplicité + alertes actionnables + niveau gratuit généreux |
| **CardPulse / Hall of Cards / SNKRDUNK** | Global, EN | Gratuit (contenu éditorial) | Bon SEO, contenu de qualité | Statique, pas d'alertes temps réel personnalisées, aucun FR | Alertes en temps réel + personnalisation par carte suivie |
| **Discord FR "alertes restock OPCG"** | France, FR | Gratuit | Communauté FR déjà engagée — **prouve la demande d'alertes en France** | Couvre uniquement le stock neuf en boutique, pas la valeur du marché secondaire | Se positionner en **complément**, pas en concurrent : angle différent (investissement vs achat au prix boutique), partenariat envisageable plutôt que confrontation |

---

## 4. Pourquoi cette idée peut devenir très rentable

- **Pourquoi les clients paieront** : sur un marché où une carte ou un produit scellé peut prendre +50 à +300 % en quelques mois (cas de l'OP01 booster box, +299 % sur 2025), rater un mouvement coûte objectivement plus cher que 6,99€/mois. Le calcul est facile pour un collectionneur sérieux.
- **Pourquoi ils resteront** : une watchlist personnalisée et un historique accumulé créent un coût de changement (switching cost) ; le rapport hebdomadaire crée un rendez-vous récurrent.
- **Pourquoi ils recommanderont** : la communauté collector est très sociale (Discord, TikTok, forums) — "j'ai vu passer l'alerte à temps" est un contenu naturellement partagé ; un programme de parrainage simple (1 mois offert) amplifie l'effet.
- **Pourquoi les concurrents auront du mal à copier** : pas la technique (copiable en un week-end), mais l'audience, la confiance accumulée et le dataset historique propriétaire — un avantage qui se compose avec le temps, pas un avantage qu'on rattrape en un sprint.

---

## 5. Business Model

### 5.1 Grille tarifaire

| Offre | Cible | Prix | Contenu |
|---|---|---|---|
| **Gratuit** | Découverte | 0€ | 5 cartes suivies, alertes différées 24h, rapport hebdo public |
| **Premium** | Collectionneur actif | 6,99€/mois ou 59€/an | Watchlist illimitée, alertes temps réel, historique complet, export CSV |
| **Pro** | Boutiques & revendeurs | 29€/mois | Accès API, alertes multi-comptes, données brutes, support prioritaire |
| **Affiliation** | Tous | — | Commission sur les clics vers Cardmarket et marketplaces partenaires |

**Upsells / cross-sell** : rapport PDF hebdo détaillé, alertes SMS en option, badge "vérifié" communautaire.
**White-label** : envisageable à terme — bot d'alertes en marque blanche pour des boutiques partenaires.
**Licence / offre entreprise** : accès données brutes en marque blanche pour sites tiers (phase 2).

### 5.2 Économie unitaire

| Poste | Montant |
|---|---|
| Coût serveur/infra | ~0€ (GitHub Actions gratuit, Telegram API gratuite, hébergement statique gratuit) |
| Coût variable principal | API de données de prix au-delà du quota gratuit : quelques € à quelques dizaines d'€/mois selon volume |
| Marge brute en régime établi | >90 % |
| Seuil de rentabilité | Quasiment atteint dès le 1er abonné payant, coûts fixes proches de zéro |

---

## 6. MVP — Plan en 7 jours

| Jour | Objectif | Détail | Temps estimé | Priorité |
|---|---|---|---|---|
| **J1** | Fondations | Compte GitHub, bot Telegram via @BotFather, sélection des 20-30 cartes du watchlist initial (cartes les plus suivies/volatiles — cf. Top 50 SNKRDUNK et série OP01), positionnement de la marque | 3-4h | Critique |
| **J2** | Connexion aux données | Inscription à un fournisseur de prix (essai/quota gratuit), test manuel de 5 appels, validation du format | 3h | Critique |
| **J3** | Récupération + détection | Implémenter `price_fetcher.py` et `alert_engine.py`, tests en local sur le watchlist | 4h | Critique |
| **J4** | Notification + stockage | `notifier_telegram.py` et `data_store.py`, premier message de test reçu | 3h | Critique |
| **J5** | Automatisation | GitHub Actions configuré (secrets, planification 4x/jour), premier run automatique réussi | 3h | Critique |
| **J6** | Landing + visibilité | Mise en ligne de la landing page (hébergement gratuit), lien Telegram public, premiers posts dans 2-3 communautés (en respectant leurs règles) | 4h | Haute |
| **J7** | Lancement | Envoi du 1er rapport hebdo, ouverture publique du canal gratuit, lien de paiement Premium actif (Stripe Payment Link) | 3h | Haute |

**Total : ~23-24h sur 7 jours** — compatible avec une disponibilité flexible.

---

## 7. Architecture technique

### 7.1 Schéma

```
┌──────────────────┐     ┌───────────────────┐     ┌─────────────────────┐
│  GitHub Actions   │────▶│     main.py        │────▶│  API prix cartes     │
│  (cron, 4x/jour)  │     │  (orchestrateur)   │◀────│  (données Cardmarket)│
└──────────────────┘     └─────────┬──────────┘     └─────────────────────┘
                                    │
                 ┌──────────────────┼──────────────────┐
                 ▼                  ▼                   ▼
       ┌──────────────────┐ ┌───────────────┐  ┌────────────────────┐
       │ alert_engine.py   │ │ data_store.py │  │ notifier_telegram.py│
       │ (détection des    │ │ (watchlist +  │  │ (envoi des alertes) │
       │  mouvements)      │ │ historique en │  └──────────┬──────────┘
       └───────────────────┘ │ JSON, commité │             │
                              │ dans le repo) │             ▼
                              └───────────────┘   ┌───────────────────┐
                                                   │   Bot Telegram     │
                                                   │ (canal gratuit +   │
                                                   │  alertes premium)  │
                                                   └───────────────────┘
```

### 7.2 Justification de chaque choix

| Composant | Choix | Pourquoi |
|---|---|---|
| Orchestration/planification | GitHub Actions (repo public) | Gratuit et **illimité** sur dépôt public, aucun serveur à gérer, aucune carte bancaire requise |
| Base de données | Fichiers `CSV`/`JSON` **dans le dépôt**, mis à jour par un commit automatique de l'Action | Zéro service externe à configurer (pas de compte cloud, pas de clé de service compliquée) — le plus simple possible pour un profil débutant ; migration vers une vraie base (SQLite puis Postgres) prévue en §14 quand le volume grandira |
| Watchlist éditable | `data/watchlist.csv` | Éditable directement depuis l'interface web de GitHub (formulaire simple), pas besoin de savoir coder |
| Notifications | API Telegram Bot (gratuite) | Mise en place en 5 minutes via @BotFather, pas de vérification d'app, gratuite sans limite pratique à cette échelle |
| Données de prix | API tierce (quota gratuit/essai au départ) + piste API officielle Cardmarket (App Key) à moyen terme | Voir §13 (risques) — architecture volontairement **modulaire** pour changer de fournisseur sans réécrire le reste du code |
| Landing page | HTML/CSS statique, hébergement gratuit (GitHub Pages ou équivalent) | Aucun besoin de backend, chargement instantané, coût nul |
| Paiement | Lien de paiement Stripe (aucune ligne de code requise) | Le seul point qui touche à de l'argent réel doit être fiable et éprouvé — Stripe gère la conformité à la place du fondateur |
| Docker | **Non utilisé en V1** | Pas de serveur permanent à conteneuriser (tout tourne en jobs GitHub Actions courts) ; redevient pertinent quand une vraie API/backend sera construite (§14) |

### 7.3 Pseudo-code de la logique centrale

```
POUR chaque carte DANS watchlist:
    prix_actuel = appeler_api_prix(carte.id)
    historique = lire_historique(carte.id)  # depuis data/price_history.json

    variation_24h = calculer_variation(prix_actuel, historique, fenetre=24h)
    variation_7j  = calculer_variation(prix_actuel, historique, fenetre=7j)

    SI abs(variation_24h) >= seuil_alerte_rapide
       OU abs(variation_7j) >= seuil_alerte_tendance
       OU prix_actuel <= moyenne_7j * (1 - seuil_bonne_affaire):
        construire_message(carte, prix_actuel, variation_24h, variation_7j)
        envoyer_telegram(message, audience=deduire_audience(carte))  # gratuit (différé) vs premium (temps réel)

    enregistrer_historique(carte.id, prix_actuel, horodatage)

commit_et_push(data/price_history.json)  # fait par l'étape finale du workflow GitHub Actions
```

Le code complet, documenté et testé, correspondant à ce pseudo-code est livré séparément (voir fichiers du projet).

---

## 8. Génération du code

Le code intégral du MVP est livré dans le fichier **`cardtide-mvp.zip`** partagé avec ce plan. Il est documenté, modulaire (un fichier = une responsabilité), commenté, testé (tests unitaires sur la logique de détection), avec gestion des erreurs et journalisation. Contenu : arborescence complète, `README.md` d'installation pas-à-pas pour non-développeur, variables d'environnement (`.env.example`), dépendances (`requirements.txt`), scripts d'installation/lancement, workflow GitHub Actions clé en main. Voir le README du projet pour la marche à suivre complète.

---

## 9. Acquisition clients

| Canal | Action concrète |
|---|---|
| **Reddit** | Poster le rapport hebdo (valeur d'abord, lien ensuite) sur r/OnePieceTCG et communautés francophones, en respectant les règles anti-pub de chaque subreddit |
| **Discord** | Rejoindre les serveurs FR existants (dont le serveur d'alertes restock identifié) et proposer un **partenariat de complémentarité** plutôt qu'une promo froide |
| **TikTok / Instagram Reels** | Format natif court : "cette carte a pris +X % cette semaine" — faible effort de production, fort potentiel de partage dans une communauté déjà habituée à ce format |
| **Partenariats** | Boutiques et créateurs FR spécialisés (type LorenZone, carteonepiece.fr) — proposer l'outil comme valeur ajoutée à leur communauté plutôt que comme concurrent |
| **SEO / contenu** | Rapport de marché hebdomadaire publié en article de blog — cible les recherches longue traîne ("prix carte one piece OP01", etc.) |
| **Lead magnet** | Le canal Telegram gratuit **est** le lead magnet — accès immédiat, valeur immédiate, conversion Premium en second temps |
| **Cold DM / Email** | Non prioritaire en V1 — l'acquisition communautaire organique est plus cohérente avec le budget et le sujet |
| **Tunnel de vente** | Canal gratuit → habitude (alertes + rapport hebdo) → friction ressentie sur les limites du gratuit → upgrade Premium via lien Stripe en un clic |

---

## 10. Automatisation

| Ce qui est automatisé | Comment | Outils | Économie réalisée |
|---|---|---|---|
| Récupération des prix | Script planifié | GitHub Actions (cron) + API prix | Remplace une veille manuelle de plusieurs heures/semaine |
| Détection des mouvements | Calcul de variations sur seuils configurables | `alert_engine.py` | Aucun oubli, réactivité en minutes plutôt qu'en jours |
| Envoi des alertes | Appel API direct | Telegram Bot API | Zéro intervention humaine par alerte |
| Mise à jour de l'historique | Commit automatique du fichier de données | GitHub Actions + `git-auto-commit` | Pas de base de données à administrer |
| Rapport hebdomadaire | Données agrégées automatiquement, commentaire rédigé par le fondateur (10 min) | Script + intervention humaine courte | Le contenu reste authentique tout en réduisant le temps de préparation |

---

## 11. Prévisions financières

> Hypothèses de planification, pas des garanties — construites à partir d'un entonnoir freemium standard et des tarifs indiqués en §5. Trois scénarios par échéance.

| Échéance | Scénario | Abonnés gratuits | Abonnés payants | MRR estimé | Dépenses/mois | Marge |
|---|---|---|---|---|---|---|
| **3 mois** | Prudent | 100 | 3 | ~20€ | 0-15€ | Faible |
| | Central | 200 | 10 | ~70€ | 0-15€ | Correcte |
| | Optimiste | 350 | 20 | ~140€ | 15€ | Bonne |
| **6 mois** | Prudent | 350 | 15 | ~105€ | 20€ | Correcte |
| | Central | 650 | 35 | ~245€ | 25€ | Bonne |
| | Optimiste | 1000 | 60 | ~420€ | 35€ | Très bonne |
| **12 mois** | Prudent | 1200 | 80 | ~560€ | 60€ | Bonne |
| | Central | 2500 | 160 | ~1120€ | 100€ | Très bonne |
| | Optimiste | 4000 | 280 | ~1960€ | 150€ | Excellente |
| **24 mois** (multi-jeux) | Prudent | 3000 | 300 | ~2100€ | 250€ | Excellente |
| | Central | 6000 | 700 | ~4900€ | 400€ | Excellente |
| | Optimiste | 12000 | 1500 | ~10 500€ | 700€ | Excellente |

**Lecture honnête** : l'objectif "sans plafond" évoqué au départ est réaliste **uniquement** dans le scénario optimiste à 24 mois et au-delà, et seulement si l'expansion multi-jeux et B2B réussit. Le scénario central à 12 mois (~1100€/mois) est déjà un résultat solide pour un projet à 0€ de budget de départ — et conforme à l'idée que "10k€/mois ce n'est pas grave, on ajuste" évoquée dans le cadrage. Cash-flow : dépenses proches de zéro à chaque étape → pas de risque de trésorerie négative, le seul coût réel est le temps investi.

---

## 12. Plan d'exécution

### Semaine 1 — Jour par jour
Voir §6 (MVP 7 jours) — checklist de lancement :

- [ ] J1 — Comptes créés (GitHub, Telegram), watchlist initiale choisie
- [ ] J2 — Fournisseur de données choisi et testé
- [ ] J3 — Récupération + détection fonctionnelles en local
- [ ] J4 — Premières alertes reçues sur Telegram
- [ ] J5 — Automatisation GitHub Actions opérationnelle
- [ ] J6 — Landing en ligne, premiers posts communautaires
- [ ] J7 — Lancement public, lien de paiement actif

### Semaines 2-4 — Consolidation
- Semaine 2 : élargir le watchlist (30 → 60 cartes), premiers retours utilisateurs, ajuster les seuils d'alerte
- Semaine 3 : régulariser le rapport hebdomadaire, lancer 1-2 partenariats communautaires
- Semaine 4 : bilan du mois 1, décision d'inscription au statut auto-entrepreneur si des paiements récurrents arrivent

### Mois 2-6 — Traction
- Mois 2-3 : montée en audience organique, premiers abonnés Pro (boutiques), diversification des canaux
- Mois 4-6 : introduction d'un second jeu (Pokémon ou Dragon Ball Super) si la base One Piece est stable

### Mois 6-12 — Structuration
- Mise en place progressive d'une vraie base de données si le volume le justifie
- Négociation d'un accès officiel Cardmarket (App Key) si le volume d'appels le justifie économiquement
- Premiers tests d'offre marque blanche pour boutiques partenaires

### Mois 12-24 — Extension
- Multi-jeux consolidé (3-4 jeux), premiers pas à l'international (DE/ES/IT via les données déjà disponibles sur Cardmarket)
- Dashboard web complet (évolution SaaS, voir §14)

---

## 13. Risques

| Risque | Catégorie | Probabilité | Impact | Mitigation |
|---|---|---|---|---|
| Dépendance à une API de données tierce (panne, changement de tarif) | Technique | Moyenne | Moyen | Architecture modulaire dès le départ (voir §7), watchlist volontairement limitée au lancement |
| Conditions d'utilisation des marketplaces sur la réutilisation commerciale de données | Juridique | Moyenne | Moyen-élevé | Démarrer petit, lire les CGU du fournisseur choisi, viser un accès officiel ("App Key" Cardmarket) dès que la traction le justifie, ne jamais republier de données personnelles d'autres utilisateurs |
| Audience de niche, dépendance à 1-2 communautés de lancement | Marketing | Moyenne | Moyen | Diversifier les canaux dès le mois 2, construire du contenu evergreen (SEO) en parallèle du contenu "chaud" |
| Un acteur établi ajoute une offre FR/EUR | Concurrence | Faible-moyenne | Élevé si ça arrive | Construire l'audience et la confiance vite ; miser sur la relation communautaire, difficile à répliquer rapidement |
| Revenus lents à démarrer | Financier | Moyenne | Faible (coûts fixes ~0) | Aucune pression de trésorerie ; patience soutenable tant que le temps investi reste acceptable |
| Cycle de hype qui redescend (bulle spéculative sur le marché des cartes) | Marché | Moyenne | Moyen-élevé | Diversification multi-jeux dès que la base est stable, ne jamais dépendre à 100 % d'un seul jeu |
| Facturer sans statut légal | Légal/fiscal | Faible si anticipé | Moyen | Inscription **auto-entrepreneur** dès les premiers paiements récurrents (démarche gratuite en ligne via le Guichet unique), rester sous le seuil de franchise TVA (37 500€ pour les prestations de services en 2026) tant que pertinent |

---

## 14. Optimisations futures

- **Vers le SaaS** : dashboard web complet (portefeuille de cartes, valorisation en temps réel, graphiques interactifs) une fois l'audience et les revenus validés.
- **Intégration multi-IA** : résumé automatique du rapport hebdomadaire par LLM, détection d'anomalies de prix par apprentissage automatique, futur estimateur d'état/grade de carte par reconnaissance d'image.
- **Effet de réseau** : portefeuilles publics partageables, classement communautaire des meilleurs "spotters" de bonnes affaires, contenu généré par les utilisateurs.
- **Marque forte** : devenir LA référence francophone du marché secondaire des TCG, au-delà de One Piece.
- **Internationalisation** : Cardmarket couvre déjà l'Allemagne, l'Espagne et l'Italie — dupliquer la couche linguistique une fois le modèle FR validé, sans réécrire le cœur technique.
- **Chemin vers 1 M€/an** : la combinaison **multi-jeux + offre B2B (API boutiques/revendeurs) + international** est le scénario le plus crédible, sur un horizon réaliste de 3 à 5 ans plutôt qu'immédiat — à traiter comme un objectif directionnel, pas une échéance garantie.

---

## Sources principales consultées

Card Ladder (indice de marché OPCG), SNKRDUNK Magazine (Top 50 cartes échangées 2026), OPTCG.com (analyse macro investisseur 2026), Athlon Sports (guide investissement OPCG 2026), TCGIndex (état du marché OPCG 2026), JapHunter, Hall of Cards, CardPulse, TCGSniper (modèle freemium), Cardmarket (CGU et documentation API officielle), sites tiers d'API de prix (tcgapis.com, cardmarketapi.com, poketrace.com), GitHub Docs (tarification Actions 2026), sources fiscales françaises (LégiFiscal, Solo.fr, Portail Auto-Entrepreneur — seuils TVA micro-entreprise 2026), sites communautaires FR du OPCG (LorenZone, carte-onepiece.fr, universtcg.fr).
