"""
Récupération des prix depuis un fournisseur de données externe.

Ce module est volontairement isolé du reste du code : pour changer de
fournisseur de données (voir README, étape 4, pour les options identifiées
lors de l'étude de marché), il suffit de modifier CE fichier, sans toucher
au reste du projet.

Implémentation de référence : une API au format "GET /card/{id}" avec un
en-tête X-API-Key (forme commune à plusieurs fournisseurs identifiés lors
de la recherche). Les conditions exactes des fournisseurs tiers changent
souvent : vérifie l'offre en cours avant de t'engager, et commence avec un
watchlist restreint pour rester dans un quota gratuit usuel (voir plan
d'affaires, §7 et §13).
"""

import time
from typing import Any, Optional

import requests

from src.logger_setup import get_logger

logger = get_logger(__name__)

REQUEST_TIMEOUT_SECONDS = 15
MAX_RETRIES = 2
RETRY_DELAY_SECONDS = 3


def fetch_card_price(base_url: str, api_key: str, card_id: str) -> Optional[dict[str, Any]]:
    """
    Récupère le prix courant d'une carte.

    Retourne un dict avec au minimum {"price": float} en cas de succès,
    ou None en cas d'échec — pour que main.py puisse continuer avec les
    autres cartes sans que tout le run échoue à cause d'une seule carte.
    """
    url = f"{base_url.rstrip('/')}/card/{card_id}"
    headers = {"X-API-Key": api_key}

    for attempt in range(1, MAX_RETRIES + 2):
        try:
            response = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT_SECONDS)
            response.raise_for_status()
            data = response.json()
            price = _extract_price(data)
            if price is None:
                logger.warning("Réponse reçue mais prix introuvable pour %s", card_id)
                return None
            return {"price": price, "raw": data}

        except requests.exceptions.RequestException as exc:
            logger.warning(
                "Échec appel API pour la carte %s (tentative %d/%d) : %s",
                card_id, attempt, MAX_RETRIES + 1, exc,
            )
            if attempt <= MAX_RETRIES:
                time.sleep(RETRY_DELAY_SECONDS)

    logger.error("Abandon pour la carte %s après %d tentatives", card_id, MAX_RETRIES + 1)
    return None


def _extract_price(data: dict[str, Any]) -> Optional[float]:
    """
    Isole la lecture du champ de prix dans la réponse de l'API.

    Adapte cette fonction si tu changes de fournisseur : c'est le SEUL
    endroit du projet qui a besoin de connaître la forme exacte de la
    réponse JSON de ton fournisseur.
    """
    prices = data.get("prices") or {}
    for key in ("from", "avg5", "avg", "trend"):
        if key in prices and prices[key] is not None:
            try:
                return float(prices[key])
            except (TypeError, ValueError):
                continue
    return None
