"""
CardTide — point d'entrée principal.

Ce script est conçu pour être lancé automatiquement par GitHub Actions
(voir .github/workflows/check_prices.yml), mais fonctionne aussi en local
pour tester (voir README, section "Tester en local").

Ce qu'il fait, dans l'ordre :
1. Charge la configuration (variables d'environnement)
2. Charge le watchlist et l'historique des prix
3. Pour chaque carte : récupère le prix, évalue s'il faut alerter
4. Envoie les alertes déclenchées sur Telegram
5. Sauvegarde le nouvel historique (GitHub Actions se charge ensuite de le commit)
"""

import os
import sys

from dotenv import load_dotenv

from src.alert_engine import evaluate_card
from src.data_store import append_price_point, load_history, load_watchlist, save_history
from src.logger_setup import get_logger
from src.notifier_telegram import send_alerts
from src.price_fetcher import fetch_card_price

logger = get_logger(__name__)

WATCHLIST_PATH = "data/watchlist.csv"
HISTORY_PATH = "data/price_history.json"


def load_config() -> dict:
    """Charge et valide la configuration depuis les variables d'environnement."""
    load_dotenv()  # ne fait rien en CI : les secrets GitHub sont déjà dans l'environnement

    required = [
        "TELEGRAM_BOT_TOKEN",
        "TELEGRAM_FREE_CHAT_ID",
        "TELEGRAM_PREMIUM_CHAT_ID",
        "PRICE_API_KEY",
        "PRICE_API_BASE_URL",
    ]
    missing = [key for key in required if not os.getenv(key)]
    if missing:
        logger.error("Variables d'environnement manquantes : %s", ", ".join(missing))
        logger.error("Vérifie ton fichier .env (en local) ou tes secrets GitHub (en CI).")
        sys.exit(1)

    return {
        "telegram_bot_token": os.environ["TELEGRAM_BOT_TOKEN"],
        "telegram_free_chat_id": os.environ["TELEGRAM_FREE_CHAT_ID"],
        "telegram_premium_chat_id": os.environ["TELEGRAM_PREMIUM_CHAT_ID"],
        "price_api_key": os.environ["PRICE_API_KEY"],
        "price_api_base_url": os.environ["PRICE_API_BASE_URL"],
        "threshold_24h": float(os.getenv("ALERT_THRESHOLD_24H", "15")),
        "threshold_7d": float(os.getenv("ALERT_THRESHOLD_7D", "25")),
        "threshold_bargain": float(os.getenv("ALERT_THRESHOLD_BARGAIN", "20")),
    }


def main() -> None:
    config = load_config()
    logger.info("=== Démarrage du run CardTide ===")

    watchlist = load_watchlist(WATCHLIST_PATH)
    history = load_history(HISTORY_PATH)

    triggered_alerts = []
    failures = 0

    for card in watchlist:
        card_id = card["cardmarket_id"]
        card_name = card["name"]

        result = fetch_card_price(config["price_api_base_url"], config["price_api_key"], card_id)
        if result is None:
            failures += 1
            continue

        current_price = result["price"]
        card_history = history.get(card_id, [])

        alert = evaluate_card(
            card_id=card_id,
            card_name=card_name,
            current_price=current_price,
            history_points=card_history,
            threshold_24h_pct=config["threshold_24h"],
            threshold_7d_pct=config["threshold_7d"],
            threshold_bargain_pct=config["threshold_bargain"],
        )
        if alert:
            triggered_alerts.append(alert)

        append_price_point(history, card_id, current_price)

    logger.info(
        "Traitement terminé : %d carte(s), %d échec(s), %d alerte(s) déclenchée(s)",
        len(watchlist), failures, len(triggered_alerts),
    )

    if watchlist and failures == len(watchlist):
        # Toutes les cartes ont échoué : c'est presque toujours le signe d'une
        # mauvaise clé API ou d'une mauvaise URL, pas d'un simple aléa réseau.
        # On sauvegarde quand même l'historique (rien n'a changé) puis on sort
        # en erreur pour que le run GitHub Actions s'affiche en rouge et
        # attire l'attention, plutôt qu'un ✅ vert trompeur.
        save_history(HISTORY_PATH, history)
        logger.error("Toutes les cartes ont échoué : vérifie PRICE_API_KEY et PRICE_API_BASE_URL.")
        sys.exit(1)

    if triggered_alerts:
        send_alerts(
            triggered_alerts,
            bot_token=config["telegram_bot_token"],
            free_chat_id=config["telegram_free_chat_id"],
            premium_chat_id=config["telegram_premium_chat_id"],
        )

    save_history(HISTORY_PATH, history)
    logger.info("=== Fin du run CardTide ===")


if __name__ == "__main__":
    main()
