def texto_entrada(farenheit: float) -> float:
    farenheit = round(farenheit, 2)
    cad = grados_celsius(farenheit)
    return f"{cad}ºC({farenheit}ºF)"


def grados_celsius(farenheit: float) -> float:
    c = (farenheit - 32) * 5.0/9.0
    c = round(c, 2)
    return c

def main():
    farenheit = float(input("Introduce una temperatura en farenheit: "))
    print(texto_entrada(farenheit))


if __name__ == "__main__":
    main()