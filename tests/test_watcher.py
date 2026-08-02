import pytest
from cryptobot.engine.watcher import calculate_price_impact

def test_price_impact_calc():
    # simple case
    res = calculate_price_impact(100, 110)
    assert res == 10.0

def test_zero_price_handling():
    with pytest.raises(ValueError):
        calculate_price_impact(0, 100)

def test_negative_swing():
    res = calculate_price_impact(100, 90)
    assert res == -10.0
