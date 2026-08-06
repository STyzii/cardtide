# CardTide — Guide de démarrage (aucune compétence technique requise)

CardTide surveille le prix de tes cartes à collectionner et t'envoie une alerte sur Telegram dès qu'un prix bouge ou qu'une bonne affaire apparaît. Ce guide t'explique comment le mettre en ligne, étape par étape, même si tu n'as jamais codé. Compte environ 20-25h réparties sur 7 jours — voir le planning détaillé dans `business-plan.md`.

**Tu n'as besoin d'installer aucun logiciel.** Tout se fait dans ton navigateur et sur des services gratuits.

---

## Avant de commencer : les comptes gratuits dont tu auras besoin

- [ ] Un compte [GitHub](https://github.com) (gratuit) — héberge ton code et fait tourner le robot automatiquement
- [ ] L'application Telegram (gratuite) — pour créer ton bot et tes canaux d'alerte
- [ ] Un compte chez un fournisseur de données de prix (voir Étape 4)
- [ ] Un compte [Stripe](https://stripe.com) (gratuit à la création) — pour encaisser les abonnements Premium

---

## Étape 1 — Mettre le code sur GitHub

1. Crée un compte sur [github.com](https://github.com) si tu n'en as pas.
2. Clique sur **"New repository"** (bouton vert, ou le "+" en haut à droite → "New repository").
3. Donne-lui un nom, par exemple `cardtide`. Laisse-le en **Public** (c'est ce qui rend l'automatisation gratuite et illimitée). Ne coche aucune case d'initialisation. Clique sur **"Create repository"**.
4. Sur la page qui s'affiche, clique sur **"uploading an existing file"**.
5. Décompresse le fichier `cardtide-mvp.zip` que tu as reçu sur ton ordinateur.
6. Ouvre le dossier décompressé, sélectionne **tout son contenu** (fichiers ET dossiers : `main.py`, `src`, `tests`, `data`, `landing`, `.github`, `requirements.txt`, etc.) et fais un glisser-déposer dans la zone d'upload de GitHub.

   ⚠️ Important : glisse le **contenu** du dossier, pas le dossier lui-même — `main.py` doit apparaître directement à la racine de ton dépôt, pas dans un sous-dossier `cardtide-mvp/main.py`.
7. Clique sur **"Commit changes"** en bas de page.

Ton code est maintenant en ligne.

---

## Étape 2 — Créer ton bot Telegram

1. Ouvre Telegram, cherche le compte **@BotFather** (compte officiel, coché).
2. Envoie-lui `/newbot`.
3. Donne un nom (ex: "CardTide Alerts") puis un nom d'utilisateur qui doit finir par "bot" (ex: `cardtide_alerts_bot`).
4. BotFather te répond avec un **jeton (token)** — une longue chaîne du type `123456789:AAExxxxxxxxxxxxxxxxxxxxxxxxxxx`. Copie-le, tu en auras besoin à l'Étape 5. Ne le partage jamais publiquement.

---

## Étape 3 — Créer tes deux canaux Telegram

**Canal gratuit (public) :**
1. Dans Telegram, crée un nouveau canal (icône crayon → "New Channel").
2. Rends-le **public** et choisis un nom d'utilisateur, ex: `@cardtide_free`.
3. Ajoute ton bot comme administrateur du canal (Gérer le canal → Administrateurs → Ajouter → cherche ton bot).
4. Ton identifiant de chat est simplement `@cardtide_free` (avec le @). Note-le pour l'Étape 5.

**Canal ou groupe premium (privé) :**
1. Crée un second canal (ou groupe), cette fois **privé**.
2. Ajoute ton bot comme administrateur.
3. Pour récupérer son identifiant numérique (les canaux privés n'ont pas de @username) :
   - Envoie n'importe quel message dans ce canal.
   - Dans ton navigateur, va sur `https://api.telegram.org/bot<TON_TOKEN>/getUpdates` (remplace `<TON_TOKEN>` par le jeton de l'Étape 2).
   - Cherche `"chat":{"id":-100xxxxxxxxxx` dans le résultat — ce nombre (avec le `-`) est ton identifiant. Note-le pour l'Étape 5.

---

## Étape 4 — Choisir un fournisseur de données de prix

Ton robot a besoin d'une source pour connaître le prix des cartes. Plusieurs options ont été identifiées pendant l'étude de marché — **vérifie l'offre actuelle de chacune avant de choisir**, les conditions (quota gratuit, durée d'essai) changent souvent :

| Option | Type d'accès |
|---|---|
| Des API tierces packageant les données Cardmarket (ex: cardmarketapi.com, tcgapis.com, ou des API listées sur RapidAPI) | Essai gratuit ou quota gratuit mensuel selon le fournisseur — le plus rapide pour démarrer |
| Apify — "Cardmarket Trend Scraper" | Le plan gratuit d'Apify inclut un crédit mensuel qui peut suffire pour une petite watchlist |
| API officielle Cardmarket (compte développeur "App Key") | Chemin le plus légitime à moyen terme pour un usage commercial ; nécessite une inscription et une revue de la part de Cardmarket |

**Recommandation de démarrage** : commence avec une des API tierces ci-dessus sur un watchlist de 20-30 cartes maximum, vérifiées 2 à 4 fois par jour — cela reste dans la plupart des quotas gratuits usuels. Une fois inscrit, tu obtiens une **clé API** : note-la pour l'étape suivante, ainsi que l'URL de base de l'API (le début de l'adresse à laquelle le service répond).

---

## Étape 5 — Configurer les secrets sur GitHub

Sur ton dépôt GitHub : **Settings → Secrets and variables → Actions → New repository secret**. Crée ces 5 secrets un par un (nom exact à gauche, ta valeur à droite) :

| Nom du secret | Valeur |
|---|---|
| `TELEGRAM_BOT_TOKEN` | Le jeton obtenu à l'Étape 2 |
| `TELEGRAM_FREE_CHAT_ID` | Ex: `@cardtide_free` (Étape 3) |
| `TELEGRAM_PREMIUM_CHAT_ID` | L'identifiant numérique noté à l'Étape 3 |
| `PRICE_API_KEY` | Ta clé API (Étape 4) |
| `PRICE_API_BASE_URL` | L'URL de base de ton fournisseur (Étape 4) |

---

## Étape 6 — Personnaliser ta watchlist

1. Sur GitHub, ouvre `data/watchlist.csv` et clique sur l'icône crayon (Edit) pour l'éditer directement dans le navigateur.
2. Remplace les lignes d'exemple par de vraies cartes : un nom lisible, l'identifiant produit de ton fournisseur de données (c'est en général le numéro qui apparaît dans l'URL de la page de la carte sur Cardmarket ou sur le site de ton fournisseur), et une catégorie libre (`leader`, `secondaire`, etc.).
3. Commit les changements.

---

## Étape 7 — Activer et tester le workflow

1. Va dans l'onglet **"Actions"** de ton dépôt GitHub. Accepte l'activation des workflows si demandé.
2. Clique sur **"Vérification des prix CardTide"** dans la liste à gauche, puis sur **"Run workflow"** (bouton à droite) pour le lancer manuellement une première fois.
3. Attends 1-2 minutes, rafraîchis la page. Un ✅ vert signifie que tout fonctionne — tu devrais recevoir un message de test sur Telegram si une alerte s'est déclenchée (sinon, c'est normal : pas de mouvement de prix détecté au premier passage puisqu'il n'y a pas encore d'historique). Un ❌ rouge : clique dessus pour lire le message d'erreur, il t'indique précisément ce qui manque (souvent un secret mal orthographié).
4. Une fois que ça fonctionne, le workflow se relance **automatiquement toutes les 6 heures**, sans que tu aies à y retoucher.

---

## Étape 8 — Mettre en ligne la landing page

Le moyen le plus simple : **GitHub Pages**, gratuit et déjà dans ton dépôt.
1. Settings → Pages.
2. Source : "Deploy from a branch", branche `main`, dossier `/landing`... si l'option `/landing` n'apparaît pas, choisis `/ (root)` et renomme temporairement `landing/index.html` en `index.html` à la racine.
3. GitHub te donne une adresse du type `https://tonpseudo.github.io/cardtide/`.

Alternative tout aussi simple : dépose le dossier `landing` sur [Netlify Drop](https://app.netlify.com/drop) (glisser-déposer, aucun compte requis pour un premier test).

---

## Étape 9 — Mettre en place le paiement Premium

1. Crée ton compte Stripe, active-le pour ta zone (France).
2. Dans Stripe : **Produits → Ajouter un produit** → "CardTide Premium" → prix récurrent 6,99€/mois.
3. Crée un **Payment Link** pour ce produit (aucune ligne de code nécessaire) et mets ce lien sur ta landing page et dans ton canal gratuit.
4. **Au tout début**, gère l'accès au canal premium manuellement : quand Stripe t'envoie une notification de paiement, ajoute la personne à ton canal privé Telegram à la main. À ce volume, ça prend 30 secondes par personne — automatiser cette étape (webhook Stripe → invitation automatique) est une bonne tâche pour une V2, une fois que tu as tes 10-20 premiers abonnés.

---

## Gérer gratuit vs premium (bon à savoir)

Dans cette V1, le code envoie chaque alerte vers les **deux** canaux Telegram en même temps. La distinction "gratuit = différé 24h" n'est pas encore automatisée dans le code — le plus simple pour démarrer est de la gérer toi-même : republie manuellement (ou avec un simple rappel dans ton calendrier) les alertes du canal premium vers le canal gratuit, avec un jour de décalage. Ce n'est pas glamour, mais c'est exactement le genre de "faire à la main ce qui ne scale pas encore" qui permet de valider la demande avant d'investir du temps à automatiser. Voir le plan d'affaires (§14) pour l'évolution vers une gestion par utilisateur individuel.

---

## Tester en local (optionnel, pour les plus curieux)

Si tu as Python installé sur ton ordinateur (version 3.10 ou plus récente) :

```bash
bash install.sh          # installe les dépendances
cp .env.example .env      # puis remplis .env avec tes propres valeurs
bash run.sh                # lance CardTide une fois
python -m pytest           # lance les tests
```

Si cette section ne te parle pas, ignore-la sans problème : GitHub Actions fait tout à ta place.

---

## Structure du projet

```
cardtide/
├── README.md                        # ce guide
├── business-plan.md                 # le plan d'affaires complet
├── requirements.txt                 # dépendances Python
├── .env.example                     # modèle de configuration locale
├── .gitignore
├── install.sh / run.sh              # scripts optionnels pour tester en local
├── main.py                          # point d'entrée : orchestre tout le reste
├── src/
│   ├── price_fetcher.py             # récupère les prix depuis l'API choisie
│   ├── alert_engine.py              # décide si un mouvement mérite une alerte
│   ├── notifier_telegram.py         # envoie les messages Telegram
│   ├── data_store.py                # lit/écrit la watchlist et l'historique
│   └── logger_setup.py              # journalisation
├── tests/
│   └── test_alert_engine.py         # tests unitaires (aucun appel réseau)
├── data/
│   ├── watchlist.csv                # les cartes que tu suis (à personnaliser)
│   └── price_history.json           # généré et mis à jour automatiquement
├── landing/
│   └── index.html                   # ta page d'accueil publique
└── .github/workflows/
    └── check_prices.yml             # automatisation : planifie et exécute tout
```

---

## Dépannage — questions fréquentes

**Le workflow échoue avec une erreur "variables d'environnement manquantes"**
→ Un secret GitHub est mal orthographié ou manquant. Compare avec le tableau de l'Étape 5, les noms doivent correspondre exactement (majuscules comprises).

**Je ne reçois aucune alerte**
→ Normal au tout premier passage : il n'y a pas encore d'historique pour calculer une variation. Après 2-3 exécutions (donc 12-18h), le système a assez de données pour comparer.

**L'appel à l'API de prix échoue**
→ Vérifie ta clé API et l'URL de base dans les secrets. Vérifie aussi que tu n'as pas dépassé le quota gratuit de ton fournisseur (voir Étape 4).

**Je veux ajouter plus de cartes**
→ Modifie `data/watchlist.csv` directement sur GitHub (Étape 6). Reste raisonnable au départ pour ne pas dépasser ton quota d'API gratuit.

---

## Et après ?

Ce README couvre la mise en route technique. Pour la stratégie complète (marché, concurrence, acquisition, prévisions financières, feuille de route au-delà de la semaine 1), voir **`business-plan.md`**.
