import pytest

from calc_estatistica import desvio_padrao, media, mediana


def test_media_calculates_arithmetic_mean():
    assert media([1, 2, 3, 4]) == pytest.approx(2.5)
    assert media([10]) == pytest.approx(10.0)


def test_mediana_calculates_odd_and_even_lists_without_mutating_original():
    odd_values = [3, 1, 2]
    even_values = [1, 2, 3, 4]

    assert mediana(odd_values) == 2
    assert mediana(even_values) == pytest.approx(2.5)
    assert odd_values == [3, 1, 2]


def test_desvio_padrao_calculates_population_standard_deviation():
    assert desvio_padrao([2, 4, 4, 4, 5, 5, 7, 9]) == pytest.approx(2.0)
    assert desvio_padrao([2, 2, 2]) == pytest.approx(0.0)
    assert desvio_padrao([10]) == pytest.approx(0.0)


def test_statistical_functions_reject_empty_lists():
    with pytest.raises(ValueError):
        media([])
    with pytest.raises(ValueError):
        mediana([])
    with pytest.raises(ValueError):
        desvio_padrao([])
