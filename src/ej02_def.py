def calculo(hora, precio):
    return f"El importe total es de {hora * precio}."


def introducir(valor):
    return float(input(valor))


def main():
    precio = introducir("Introduce un coste: ")
    hora = introducir("introduce una cantidad de horas: ")

    print(calculo(hora, precio))

if __name__ == "__main__":
    main()