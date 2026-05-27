# main.py — imports modules as they are merged into main
def menu():
    print("=== GCS Calculator ===\n")

    try:
        from calc_basico import somar, subtrair, multiplicar, dividir
        print("Basic Module loaded.")
        print("  2 + 3 =", somar(2, 3))
        print("  10 - 4 =", subtrair(10, 4))
        print("  3 * 5 =", multiplicar(3, 5))
        print("  10 / 2 =", dividir(10, 2))
    except ImportError:
        print("Basic Module not yet available.")

    try:
        from calc_potencia import potencia, raiz_quadrada, raiz_cubica
        print("\nPower Module loaded.")
        print("  2^10 =", potencia(2, 10))
        print("  sqrt(9) =", raiz_quadrada(9))
        print("  cbrt(27) =", raiz_cubica(27))
    except ImportError:
        print("Power Module not yet available.")

    try:
        from calc_percentual import percentage, increase, discount
        print("\nPercentage Module loaded.")
        print("  10% of 200 =", percentage(200, 10))
        print("  200 + 10% =", increase(200, 10))
        print("  200 - 10% =", discount(200, 10))
    except ImportError:
        print("Percentage Module not yet available.")

    try:
        from calc_estatistica import mean, median, standard_deviation
        print("\nStatistics Module loaded.")
        print("  mean of [1,2,3,4,5] =", mean([1, 2, 3, 4, 5]))
        print("  median of [3,1,2] =", median([3, 1, 2]))
        print("  std dev of [2,4,4,4,5,5,7,9] =", standard_deviation([2, 4, 4, 4, 5, 5, 7, 9]))
    except ImportError:
        print("Statistics Module not yet available.")

    try:
        from calc_conversao import celsius_to_fahrenheit, km_to_miles, kg_to_pounds
        print("\nConversion Module loaded.")
        print("  100°C in °F =", celsius_to_fahrenheit(100))
        print("  10 km in miles =", km_to_miles(10))
        print("  70 kg in pounds =", kg_to_pounds(70))
    except ImportError:
        print("Conversion Module not yet available.")


if __name__ == "__main__":
    menu()
