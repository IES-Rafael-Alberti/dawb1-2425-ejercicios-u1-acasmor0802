def pedir(var):
    return float(input(var))


def calculo(iva, precio):
    ivatotal = iva / 100 + 1
    preciofinal = precio * ivatotal
    return preciofinal

def main():
    precio = pedir('Introduzca el importe sin IVA: ')
    iva = pedir('Introduzca el IVA a aplicar: ')

    print(f"El importe será de: {calculo(iva, precio)}")


if __name__ == "__main__":
    main()