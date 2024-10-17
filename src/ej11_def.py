def calculo(n):
    suma = (n*(n+1))/2
    return suma


def main():
    n = int (input("Introduzca un número entero: "))
    return print(f"La suma de todos los enteros desde 1 hazsta el número introducido es: {calculo(n)}.")


if __name__ == "__main__":
    main()