import pytest

from calc_percentual import discount, increase, percentage


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
