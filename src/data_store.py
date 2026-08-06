"""
Stockage des données : la "base de données" de CardTide tient dans deux
fichiers versionnés avec le code, pour rester à budget 0€ et sans service
externe à configurer :

- data/watchlist.csv      : la liste des cartes à suivre (modifiable à la
                             main, y compris directement depuis l'interface
                             web de GitHub, sans rien installer)
- data/price_history.json : l'historique des prix relevés, mis à jour et
                             recommité automatiquement à chaque exécution
                             par le workflow GitHub Actions.

Cette approche est volontairement simple pour démarrer sans compétence
technique. Voir le plan d'affaires (section 14, "Optimisations futures")
pour la migration vers une vraie base de données une fois le volume
d'utilisateurs plus important.
"""

import csv
import json
import os
from datetime import datetime, timezone
from typing import Any

from src.logger_setup import get_logger

logger = get_logger(__name__)


def load_watchlist(path: str) -> list[dict[str, str]]:
    """
    Charge la liste des cartes à suivre depuis un fichier CSV.
    Colonnes attendues : name, cardmarket_id, category.
    Ignore silencieusement les lignes sans identifiant (ex: lignes vides).
    """
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Watchlist introuvable : {path}. "
            "Vérifie que data/watchlist.csv existe bien à la racine du projet."
        )

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        watchlist = [row for row in reader if row.get("cardmarket_id")]

    logger.info("Watchlist chargée : %d carte(s)", len(watchlist))
    return watchlist


def load_history(path: str) -> dict[str, list[dict[str, Any]]]:
    """
    Charge l'historique des prix. Retourne un dict vide si le fichier
    n'existe pas encore (cas du tout premier lancement).

    Format : { "<cardmarket_id>": [ {"price": 12.5, "timestamp": "..."}, ... ] }
    """
    if not os.path.exists(path):
        logger.info("Aucun historique existant, démarrage à vide (%s)", path)
        return {}

    with open(path, encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            logger.warning("Historique illisible, redémarrage à vide (%s)", path)
            return {}


def save_history(path: str, history: dict[str, list[dict[str, Any]]]) -> None:
    """Sauvegarde l'historique complet sur disque (JSON lisible, indenté)."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)
    logger.info("Historique sauvegardé (%s)", path)


def append_price_point(
    history: dict[str, list[dict[str, Any]]],
    card_id: str,
    price: float,
    max_points_per_card: int = 500,
) -> None:
    """
    Ajoute un relevé de prix pour une carte, avec horodatage UTC.

    Garde un nombre borné de points par carte pour éviter un fichier qui
    grossit indéfiniment (voir §14 du plan d'affaires pour la migration
    vers une vraie base de données quand ce plafond devient limitant).
    """
    history.setdefault(card_id, [])
    history[card_id].append(
        {
            "price": price,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
    )
    if len(history[card_id]) > max_points_per_card:
        history[card_id] = history[card_id][-max_points_per_card:]
