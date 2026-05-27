import math

# calc_potencia.py
# Module B - Power and Roots
# Author: Leonardo Simões
# Branch: feature/module-power

def potencia(base, exponent):
    """
    Raises the base to the given exponent.

    Args:
        base (int, float): The base number.
        exponent (int, float): The exponent (can be positive, negative, or zero).

    Returns:
        float: The exponentiation result.
    """
    return math.pow(base, exponent)

def raiz_quadrada(n):
    """
    Calculates the square root of n.

    Args:
        n (int, float): The number to extract the square root from.

    Returns:
        float: The square root of the number.

    Raises:
        ValueError: If n is less than zero.
    """
    if n < 0:
        raise ValueError("Error: Square root of a negative number is not real.")
    return math.sqrt(n)

def raiz_cubica(n):
    """
    Calculates the cube root of n.

    Args:
        n (int, float): The number to extract the cube root from (positive or negative).

    Returns:
        float: The cube root of the number.
    """
    if n < 0:
        return -math.pow(-n, 1.0 / 3.0)
    return math.pow(n, 1.0 / 3.0)