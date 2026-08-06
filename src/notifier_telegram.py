"""
Envoi des messages d'alerte via l'API Telegram Bot (gratuite, sans limite
pratique à l'échelle d'un MVP).

Créer un bot : ouvrir Telegram, chercher "@BotFather", envoyer /newbot et
suivre les instructions. Voir le README (étape 2) pour le détail pas-à-pas.
"""

from typing import List

import requests

from src.alert_engine import PriceAlert
from src.logger_setup import get_logger

logger = get_logger(__name__)

TELEGRAM_API_BASE = "https://api.telegram.org"
REQUEST_TIMEOUT_SECONDS = 10


def format_alert_message(alert: PriceAlert) -> str:
    """Construit le texte du message envoyé pour une alerte donnée."""
    lines = [f"🔔 {alert.card_name}", f"Prix actuel : {alert.current_price:.2f} €"]
    if alert.change_24h_pct is not None:
        lines.append(f"Variation 24h : {alert.change_24h_pct:+.1f}%")
    if alert.change_7d_pct is not None:
        lines.append(f"Tendance 7j : {alert.change_7d_pct:+.1f}%")
    lines.append(f"Raison : {alert.reason}")
    return "\n".join(lines)


def send_telegram_message(bot_token: str, chat_id: str, text: str) -> bool:
    """
    Envoie un message Telegram. Retourne True/False plutôt que de lever
    une exception, pour que l'échec d'un envoi n'interrompe pas le
    traitement des autres alertes.
    """
    url = f"{TELEGRAM_API_BASE}/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}

    try:
        response = requests.post(url, json=payload, timeout=REQUEST_TIMEOUT_SECONDS)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as exc:
        logger.error("Échec d'envoi Telegram vers %s : %s", chat_id, exc)
        return False


def send_alerts(
    alerts: List[PriceAlert],
    bot_token: str,
    free_chat_id: str,
    premium_chat_id: str,
) -> None:
    """
    Envoie chaque alerte déclenchée.

    V1 volontairement simple : chaque alerte part vers les deux canaux
    (gratuit et premium). La différenciation "gratuit = différé 24h" se
    gère en amont, en ne publiant sur le canal gratuit qu'une fois par jour
    (voir README, section "Gérer gratuit vs premium"). Quand le nombre
    d'abonnés justifiera une vraie gestion par utilisateur individuel
    plutôt que par canal, c'est cette fonction qu'il faudra faire évoluer
    en premier (voir plan d'affaires, §14).
    """
    for alert in alerts:
        text = format_alert_message(alert)

        if send_telegram_message(bot_token, premium_chat_id, text):
            logger.info("Alerte envoyée (premium) : %s — %s", alert.card_name, alert.reason)

        if send_telegram_message(bot_token, free_chat_id, text):
            logger.info("Alerte envoyée (gratuit) : %s — %s", alert.card_name, alert.reason)
