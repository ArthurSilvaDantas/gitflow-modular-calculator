# calc_basico.py
# Module A - Basic Operations
# Author: Leonardo Simões
# Branch: feature/module-basic

def somar(a, b):
    """
    Returns the sum of a and b.

    Args:
        a (int, float): The first value.
        b (int, float): The second value.

    Returns:
        int, float: The sum result.
    """
    return a + b

def subtrair(a, b):
    """
    Returns the difference between a and b.

    Args:
        a (int, float): The base value.
        b (int, float): The value to subtract.

    Returns:
        int, float: The subtraction result.
    """
    return a - b

def multiplicar(a, b):
    """
    Returns the product of a and b.

    Args:
        a (int, float): The first factor.
        b (int, float): The second factor.

    Returns:
        int, float: The multiplication result.
    """
    return a * b

def dividir(a, b):
    """
    Returns the division of a by b.

    Args:
        a (int, float): The dividend.
        b (int, float): The divisor.

    Returns:
        float: The division result.

    Raises:
        ValueError: If the divisor (b) is zero.
    """
    if b == 0:
        raise ValueError("Error: Division by zero is not allowed.")
    return a / b