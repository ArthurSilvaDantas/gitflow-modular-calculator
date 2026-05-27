# calc_percentual.py
# Module C - Percentage calculations
# Author: Guilherme Facco Silva
# Branch: feature/modulo-percentual


def _validate_percentage(percentage_rate):
    if percentage_rate < 0:
        raise ValueError("Percentage cannot be negative.")


def percentage(value, percentage_rate):
    """
    Calculate how much a percentage represents from a base value.

    Args:
        value (int | float): Base value.
        percentage_rate (int | float): Percentage to calculate.

    Returns:
        float: The percentage amount from the base value.

    Raises:
        ValueError: If percentage_rate is negative.

    Examples:
        >>> percentage(200, 10)
        20.0
    """
    _validate_percentage(percentage_rate)
    return value * percentage_rate / 100


def increase(value, percentage_rate):
    """
    Apply a percentage increase to a base value.

    Args:
        value (int | float): Base value.
        percentage_rate (int | float): Percentage increase to apply.

    Returns:
        float: The value after the percentage increase.

    Raises:
        ValueError: If percentage_rate is negative.

    Examples:
        >>> increase(200, 10)
        220.0
    """
    _validate_percentage(percentage_rate)
    return value + percentage(value, percentage_rate)


def discount(value, percentage_rate):
    """
    Apply a percentage discount to a base value.

    Args:
        value (int | float): Base value.
        percentage_rate (int | float): Percentage discount to apply.

    Returns:
        float: The value after the percentage discount.

    Raises:
        ValueError: If percentage_rate is negative.

    Examples:
        >>> discount(200, 10)
        180.0
    """
    _validate_percentage(percentage_rate)
    return value - percentage(value, percentage_rate)
