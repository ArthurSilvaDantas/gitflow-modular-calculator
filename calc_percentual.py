# calc_percentual.py
# Module C - Percentage calculations
# Author: Guilherme Facco Silva
# Branch: feature/modulo-percentual


def _validate_percentage(pct):
    if pct < 0:
        raise ValueError("Percentage cannot be negative.")


def percentual(valor, pct):
    """
    Calculate how much a percentage represents from a base value.

    Args:
        valor (int | float): Base value.
        pct (int | float): Percentage to calculate.

    Returns:
        float: The percentage amount from the base value.

    Raises:
        ValueError: If pct is negative.

    Examples:
        >>> percentual(200, 10)
        20.0
    """
    _validate_percentage(pct)
    return valor * pct / 100


def acrescimo(valor, pct):
    """
    Apply a percentage increase to a base value.

    Args:
        valor (int | float): Base value.
        pct (int | float): Percentage increase to apply.

    Returns:
        float: The value after the percentage increase.

    Raises:
        ValueError: If pct is negative.

    Examples:
        >>> acrescimo(200, 10)
        220.0
    """
    _validate_percentage(pct)
    return valor + percentual(valor, pct)


def desconto(valor, pct):
    """
    Apply a percentage discount to a base value.

    Args:
        valor (int | float): Base value.
        pct (int | float): Percentage discount to apply.

    Returns:
        float: The value after the percentage discount.

    Raises:
        ValueError: If pct is negative.

    Examples:
        >>> desconto(200, 10)
        180.0
    """
    _validate_percentage(pct)
    return valor - percentual(valor, pct)
