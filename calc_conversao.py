# calc_conversao.py
# Módulo E — Operações de conversão
# Autor: Louise Mayumi Takigawa Pereira
# Branch: feature/modulo-conversao


def celsius_para_fahrenheit(celsius):
    """
    Converte um valor em celsius para fahrenheit.

    Args:
        celsius (float | int): Temperatura em graus Celsius.

    Returns:
        float: Temperatura convertida para Fahrenheit.
    
    Note:
        O zero absoluto corresponde a -273.15 °C.

    Example:
        >>> celsius_para_fahrenheit(-40)
        -40.0
    """
    
    return (celsius * 9/5) + 32



def km_para_milhas(km):
    """
    Converte uma distância em quilômetros para milhas.

    Args:
        km (float | int): Distância em quilômetros.

    Returns:
        float: Distância convertida para milhas.

    Raises:
        ValueError: Se o valor de km for negativo.

    Example:
        >>> km_para_milhas(0)
        0.0
    """
    if km < 0:
        raise ValueError("O km não pode ser negativo")

    return km * 0.621371



def kg_para_libras(kg):
    """
    Converte um valor em quilogramas para libras.

    Args:
        kg (float | int): Massa em quilogramas.

    Returns:
        float: Massa convertida para libras.

    Raises:
        ValueError: Se o valor de kg for negativo.

    Example:
        >>> kg_para_libras(1)
        2.20462
    """
    if kg < 0:
        raise ValueError("O kg não pode ser negativo")

    return kg * 2.20462