import pytest
from calc_basico import somar, subtrair, multiplicar, dividir
from calc_potencia import potencia, raiz_quadrada, raiz_cubica

# ==============================================================================
# TESTS - MODULE A
# ==============================================================================

def test_somar():
    assert somar(-5, -3) == -8

def test_subtrair():
    assert subtrair(10.5, 5.2) == pytest.approx(5.3)

def test_multiplicar():
    assert multiplicar(5, 0) == 0

def test_dividir():
    assert dividir(10, 2) == 5.0

def test_divisao_por_zero():
    with pytest.raises(ValueError):
        dividir(5, 0)

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
