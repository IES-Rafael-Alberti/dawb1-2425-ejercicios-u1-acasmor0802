

def convertir_a_binario(valor, base):
    base = 2
    cociente = valor
    resultado = ""

    while cociente >= base:
        resto = cociente % base
        resultado += str(resto)
        cociente = cociente // base

    resultado += str(cociente)
    resultado = resultado[::-1]
    return resultado


def main():
    valor = int(input("Introduzca un número: "))
    print(convertir_a_binario)


if __name__ == "__main__":
    main()