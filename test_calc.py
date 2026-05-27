import pytest
from calc_basico import somar, subtrair, multiplicar, dividir

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