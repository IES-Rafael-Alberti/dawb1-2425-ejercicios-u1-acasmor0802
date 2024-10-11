def texto():
 print(texto_entrada())


def texto_entrada():
    f = float(input("Introduce una temperatura en Farenheit: "))
    c = (f - 32) * 5.0/9.0
    return f"{c}ºC({f}ºF)"


def main():
    texto()


if __name__ == "__main__":
    main()