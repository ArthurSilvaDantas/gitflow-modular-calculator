# calc_estatistica.py
# Module D - Descriptive statistics
# Author: Guilherme Facco Silva
# Branch: feature/modulo-estatistica

from math import sqrt


def _validate_data(dados):
    if len(dados) == 0:
        raise ValueError("Data list cannot be empty.")


def media(dados):
    """
    Calculate the arithmetic mean of a list of numbers.

    Args:
        dados (list[int | float]): List of numeric values.

    Returns:
        float: The arithmetic mean.

    Raises:
        ValueError: If dados is empty.

    Examples:
        >>> media([1, 2, 3])
        2.0
    """
    _validate_data(dados)
    return sum(dados) / len(dados)


def mediana(dados):
    """
    Calculate the median of a list of numbers without changing the original list.

    Args:
        dados (list[int | float]): List of numeric values.

    Returns:
        int | float: The median value.

    Raises:
        ValueError: If dados is empty.

    Examples:
        >>> mediana([3, 1, 2])
        2
    """
    _validate_data(dados)
    ordenados = sorted(dados)
    meio = len(ordenados) // 2

    if len(ordenados) % 2 == 1:
        return ordenados[meio]

    return (ordenados[meio - 1] + ordenados[meio]) / 2


def desvio_padrao(dados):
    """
    Calculate the population standard deviation of a list of numbers.

    Args:
        dados (list[int | float]): List of numeric values.

    Returns:
        float: The population standard deviation.

    Raises:
        ValueError: If dados is empty.

    Examples:
        >>> desvio_padrao([2, 2, 2])
        0.0
    """
    _validate_data(dados)
    valor_medio = media(dados)
    variancia = sum((valor - valor_medio) ** 2 for valor in dados) / len(dados)
    return sqrt(variancia)
