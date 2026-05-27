import pytest

from calc_percentual import acrescimo, desconto, percentual


def test_percentual_calculates_percentage_for_integers_and_floats():
    assert percentual(200, 10) == pytest.approx(20.0)
    assert percentual(99.9, 10) == pytest.approx(9.99)
    assert percentual(0, 10) == pytest.approx(0.0)


def test_acrescimo_applies_percentage_increase():
    assert acrescimo(200, 10) == pytest.approx(220.0)
    assert acrescimo(100, 0) == pytest.approx(100.0)


def test_desconto_applies_percentage_discount():
    assert desconto(200, 10) == pytest.approx(180.0)
    assert desconto(200, 100) == pytest.approx(0.0)


def test_percentual_functions_reject_negative_percentage():
    with pytest.raises(ValueError):
        percentual(200, -5)
    with pytest.raises(ValueError):
        acrescimo(200, -5)
    with pytest.raises(ValueError):
        desconto(200, -5)
