# calc_conversao.py
# Módulo E — Operações de conversão
# Autor: Louise Mayumi Takigawa Pereira
# Branch: feature/modulo-conversao


def celsius_to_fahrenheit(celsius):
    """
    Converts a value from Celsius to Fahrenheit.
    
    Args:
        celsius (float | int): Temperature in degrees Celsius.
        
    Returns:
        float: Temperature converted to Fahrenheit.
    
    Note:
        Absolute zero corresponds to -273.15 °C.
        
    Example:
        >>> celsius_to_fahrenheit(-40)
        -40.0
    """
    
    return (celsius * 9/5) + 32



def km_to_miles(km):
    """
    Converts a distance in kilometers to miles.
    
    Args:
        km (float | int): Distance in kilometers.
        
    Returns:
        float: Distance converted to miles.
        
    Raises:
        ValueError: If the km value is negative.
        
    Example:
        >>> km_to_miles(0)
        0.0
    """
    if km < 0:
        raise ValueError("km cannot be negative")
    return km * 0.621371


def kg_to_pounds(kg):
    """
    Converts a value in kilograms to pounds.
    
    Args:
        kg (float | int): Mass in kilograms.
        
    Returns:
        float: Mass converted to pounds.
        
    Raises:
        ValueError: If the kg value is negative.
        
    Example:
        >>> kg_to_pounds(1)
        2.20462
    """
    if kg < 0:
        raise ValueError("kg cannot be negative")
    return kg * 2.20462
