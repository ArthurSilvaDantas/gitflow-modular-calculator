import pytest

from calc_basico import dividir, multiplicar, somar, subtrair
from calc_percentual import discount, increase, percentage
from calc_potencia import potencia, raiz_cubica, raiz_quadrada


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


# ==============================================================================
# TESTS - MODULE C
# ==============================================================================

def test_percentage_calculates_percentage_for_integers_and_floats():
    assert percentage(200, 10) == pytest.approx(20.0)
    assert percentage(99.9, 10) == pytest.approx(9.99)
    assert percentage(0, 10) == pytest.approx(0.0)


def test_increase_applies_percentage_increase():
    assert increase(200, 10) == pytest.approx(220.0)
    assert increase(100, 0) == pytest.approx(100.0)


def test_discount_applies_percentage_discount():
    assert discount(200, 10) == pytest.approx(180.0)
    assert discount(200, 100) == pytest.approx(0.0)


def test_percentage_functions_reject_negative_percentage():
    with pytest.raises(ValueError):
        percentage(200, -5)
    with pytest.raises(ValueError):
        increase(200, -5)
    with pytest.raises(ValueError):
        discount(200, -5)
