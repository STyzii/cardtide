"""
Logique de détection des mouvements de prix dignes d'une alerte.

Ce module est délibérément composé de fonctions pures (pas d'appel réseau,
pas de lecture/écriture de fichier) pour rester facile à tester
unitairement — voir tests/test_alert_engine.py.
"""

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Any, Optional


@dataclass
class PriceAlert:
    card_id: str
    card_name: str
    current_price: float
    change_24h_pct: Optional[float]
    change_7d_pct: Optional[float]
    is_bargain: bool
    reason: str


def compute_change_pct(current_price: float, past_price: float) -> float:
    """Variation en pourcentage entre deux prix. Évite la division par zéro."""
    if past_price == 0:
        return 0.0
    return round((current_price - past_price) / past_price * 100, 2)


def price_at_or_before(history_points: list[dict[str, Any]], hours_ago: float) -> Optional[float]:
    """
    Retourne le prix le plus proche de "il y a `hours_ago` heures".

    IMPORTANT : `history_points` doit être trié par ordre chronologique
    croissant (le plus ancien en premier, le plus récent en dernier) —
    c'est l'ordre naturel produit par data_store.append_price_point, qui
    ajoute toujours le nouveau relevé à la fin de la liste.
    """
    if not history_points:
        return None

    target = datetime.now(timezone.utc) - timedelta(hours=hours_ago)
    candidates = [
        p for p in history_points
        if datetime.fromisoformat(p["timestamp"]) <= target
    ]
    if not candidates:
        return None
    return candidates[-1]["price"]


def evaluate_card(
    card_id: str,
    card_name: str,
    current_price: float,
    history_points: list[dict[str, Any]],
    threshold_24h_pct: float,
    threshold_7d_pct: float,
    threshold_bargain_pct: float,
) -> Optional[PriceAlert]:
    """
    Décide si une carte mérite une alerte, selon 3 règles :
    1. Variation brutale sur 24h
    2. Tendance marquée sur 7 jours
    3. "Bonne affaire" : prix courant nettement sous la moyenne des 7 derniers jours
    """
    price_24h_ago = price_at_or_before(history_points, hours_ago=24)
    price_7d_ago = price_at_or_before(history_points, hours_ago=24 * 7)

    change_24h = compute_change_pct(current_price, price_24h_ago) if price_24h_ago else None
    change_7d = compute_change_pct(current_price, price_7d_ago) if price_7d_ago else None

    recent_prices = [p["price"] for p in history_points[-28:]] or [current_price]
    avg_7d = sum(recent_prices) / len(recent_prices)
    is_bargain = avg_7d > 0 and current_price <= avg_7d * (1 - threshold_bargain_pct / 100)

    triggered_reasons = []
    if change_24h is not None and abs(change_24h) >= threshold_24h_pct:
        triggered_reasons.append(f"variation 24h de {change_24h:+.1f}%")
    if change_7d is not None and abs(change_7d) >= threshold_7d_pct:
        triggered_reasons.append(f"tendance 7j de {change_7d:+.1f}%")
    if is_bargain:
        triggered_reasons.append(f"prix sous la moyenne 7j de plus de {threshold_bargain_pct:.0f}%")

    if not triggered_reasons:
        return None

    return PriceAlert(
        card_id=card_id,
        card_name=card_name,
        current_price=current_price,
        change_24h_pct=change_24h,
        change_7d_pct=change_7d,
        is_bargain=is_bargain,
        reason=" · ".join(triggered_reasons),
    )
