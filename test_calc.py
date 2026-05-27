import pytest
from calc_potencia import potencia, raiz_quadrada, raiz_cubica

# ==============================================================================
# TESTS - MODULE B
# ==============================================================================

def test_potencia():
    assert potencia(2, 0) == 1.0
    assert potencia(2, -1) == 0.5

def test_raiz_quadrada():
    assert raiz_quadrada(0) == 0.0

def test_raiz_quadrada_negativa():
    with pytest.raises(ValueError):
        raiz_quadrada(-1)

def test_raiz_cubica():
    assert raiz_cubica(-8) == pytest.approx(-2.0)