"""
Tests unitaires de la logique de détection (src/alert_engine.py).

Lancer les tests :
    pytest

Ces tests ne font AUCUN appel réseau : ils vérifient uniquement les
fonctions de calcul pur, ce qui les rend rapides et fiables. C'est aussi
un bon exemple à suivre si tu veux ajouter tes propres tests plus tard.
"""

from datetime import datetime, timedelta, timezone

from src.alert_engine import compute_change_pct, evaluate_card, price_at_or_before


def iso(hours_ago: float) -> str:
    """Fabrique un horodatage ISO 8601 situé `hours_ago` heures dans le passé."""
    return (datetime.now(timezone.utc) - timedelta(hours=hours_ago)).isoformat()


def test_compute_change_pct_basic():
    assert compute_change_pct(110, 100) == 10.0
    assert compute_change_pct(90, 100) == -10.0


def test_compute_change_pct_handles_zero_past_price():
    assert compute_change_pct(50, 0) == 0.0


def test_price_at_or_before_returns_closest_past_point():
    # Trié du plus ancien au plus récent, comme le produit data_store en usage réel
    history = [
        {"price": 10.0, "timestamp": iso(48)},
        {"price": 12.0, "timestamp": iso(30)},
        {"price": 15.0, "timestamp": iso(2)},
    ]
    assert price_at_or_before(history, hours_ago=24) == 12.0


def test_price_at_or_before_returns_none_when_no_old_enough_point():
    history = [{"price": 10.0, "timestamp": iso(1)}]
    assert price_at_or_before(history, hours_ago=24) is None


def test_evaluate_card_triggers_on_sharp_24h_move():
    history = [{"price": 100.0, "timestamp": iso(25)}]
    alert = evaluate_card(
        card_id="123", card_name="Carte de test", current_price=120.0,
        history_points=history,
        threshold_24h_pct=15, threshold_7d_pct=25, threshold_bargain_pct=20,
    )
    assert alert is not None
    assert "24h" in alert.reason


def test_evaluate_card_returns_none_when_stable():
    history = [{"price": 100.0, "timestamp": iso(25)}]
    alert = evaluate_card(
        card_id="123", card_name="Carte de test", current_price=101.0,
        history_points=history,
        threshold_24h_pct=15, threshold_7d_pct=25, threshold_bargain_pct=20,
    )
    assert alert is None


def test_evaluate_card_detects_bargain():
    # Historique stable autour de 100 sur ~2 jours (du plus ancien au plus
    # récent), mais le prix courant est très bas -> alerte "bonne affaire",
    # même sans mouvement brutal sur 24h ou 7j.
    hours_ago_oldest_first = sorted(range(1, 48, 6), reverse=True)
    history = [{"price": 100.0, "timestamp": iso(h)} for h in hours_ago_oldest_first]

    alert = evaluate_card(
        card_id="123", card_name="Carte de test", current_price=70.0,
        history_points=history,
        threshold_24h_pct=999, threshold_7d_pct=999, threshold_bargain_pct=20,
    )
    assert alert is not None
    assert alert.is_bargain is True
