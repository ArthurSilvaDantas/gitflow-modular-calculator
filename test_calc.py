# test_calc_conversao.py
import pytest

from calc_conversao import (
    celsius_para_fahrenheit,
    km_para_milhas,
    kg_para_libras
)

def test_celsius_para_fahrenheit():
    assert celsius_para_fahrenheit(0) == pytest.approx(32.0)
    assert celsius_para_fahrenheit(100) == pytest.approx(212.0)
    assert celsius_para_fahrenheit(-40) == pytest.approx(-40.0)

def test_km_para_milhas():
    assert km_para_milhas(1) == pytest.approx(0.621371, rel=1e-5)
    assert km_para_milhas(0) == pytest.approx(0.0)
    with pytest.raises(ValueError):
        km_para_milhas(-1)

def test_kg_para_libras():
    assert kg_para_libras(1) == pytest.approx(2.20462, rel=1e-5)
    assert kg_para_libras(0) == pytest.approx(0.0)
    with pytest.raises(ValueError):
        kg_para_libras(-1)