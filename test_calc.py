import pytest

from calc_basico import dividir, multiplicar, somar, subtrair
from calc_estatistica import mean, median, standard_deviation
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
# TESTS - MODULE D
# ==============================================================================

def test_mean_calculates_arithmetic_mean():
    assert mean([1, 2, 3, 4]) == pytest.approx(2.5)
    assert mean([10]) == pytest.approx(10.0)


def test_median_calculates_odd_and_even_lists_without_mutating_original():
    odd_values = [3, 1, 2]
    even_values = [1, 2, 3, 4]

    assert median(odd_values) == 2
    assert median(even_values) == pytest.approx(2.5)
    assert odd_values == [3, 1, 2]


def test_standard_deviation_calculates_population_standard_deviation():
    assert standard_deviation([2, 4, 4, 4, 5, 5, 7, 9]) == pytest.approx(2.0)
    assert standard_deviation([2, 2, 2]) == pytest.approx(0.0)
    assert standard_deviation([10]) == pytest.approx(0.0)


def test_statistical_functions_reject_empty_lists():
    with pytest.raises(ValueError):
        mean([])
    with pytest.raises(ValueError):
        median([])
    with pytest.raises(ValueError):
        standard_deviation([])
