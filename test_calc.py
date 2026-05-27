# test_calc_conversao.py
import pytest

from calc_conversao import (
    celsius_to_fahrenheit,
    km_to_miles,
    kg_to_pounds
)

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == pytest.approx(32.0)
    assert celsius_to_fahrenheit(100) == pytest.approx(212.0)
    assert celsius_to_fahrenheit(-40) == pytest.approx(-40.0)

def test_km_to_miles():
    assert km_to_miles(1) == pytest.approx(0.621371, rel=1e-5)
    assert km_to_miles(0) == pytest.approx(0.0)
    with pytest.raises(ValueError):
        km_to_miles(-1)

def test_kg_to_pounds():
    assert kg_to_pounds(1) == pytest.approx(2.20462, rel=1e-5)
    assert kg_to_pounds(0) == pytest.approx(0.0)
    with pytest.raises(ValueError):
        kg_to_pounds(-1)
