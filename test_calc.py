import pytest

from calc_conversao import (
    celsius_to_fahrenheit,
    km_to_miles,
    kg_to_pounds
)
from calc_basico import dividir, multiplicar, somar, subtrair
from calc_estatistica import mean, median, standard_deviation
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

        
# ==============================================================================
# TESTS - MODULE E
# ==============================================================================   
        
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
