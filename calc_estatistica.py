# calc_estatistica.py
# Module D - Descriptive statistics
# Author: Guilherme Facco Silva
# Branch: feature/modulo-estatistica

from math import sqrt


def _validate_data(data):
    if len(data) == 0:
        raise ValueError("Data list cannot be empty.")


def mean(data):
    """
    Calculate the arithmetic mean of a list of numbers.

    Args:
        data (list[int | float]): List of numeric values.

    Returns:
        float: The arithmetic mean.

    Raises:
        ValueError: If data is empty.

    Examples:
        >>> mean([1, 2, 3])
        2.0
    """
    _validate_data(data)
    return sum(data) / len(data)


def median(data):
    """
    Calculate the median of a list of numbers without changing the original list.

    Args:
        data (list[int | float]): List of numeric values.

    Returns:
        int | float: The median value.

    Raises:
        ValueError: If data is empty.

    Examples:
        >>> median([3, 1, 2])
        2
    """
    _validate_data(data)
    sorted_values = sorted(data)
    middle_index = len(sorted_values) // 2

    if len(sorted_values) % 2 == 1:
        return sorted_values[middle_index]

    return (sorted_values[middle_index - 1] + sorted_values[middle_index]) / 2


def standard_deviation(data):
    """
    Calculate the population standard deviation of a list of numbers.

    Args:
        data (list[int | float]): List of numeric values.

    Returns:
        float: The population standard deviation.

    Raises:
        ValueError: If data is empty.

    Examples:
        >>> standard_deviation([2, 2, 2])
        0.0
    """
    _validate_data(data)
    mean_value = mean(data)
    variance = sum((value - mean_value) ** 2 for value in data) / len(data)
    return sqrt(variance)
