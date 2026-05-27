import pytest

from calc_estatistica import mean, median, standard_deviation


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
