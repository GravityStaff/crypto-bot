import pytest
from cryptobot.engine.watcher import calculate_price_impact

def test_price_impact_calc():
    # simple case
    res = calculate_price_impact(100, 110)
    assert res == 10.0

