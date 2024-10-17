def pedir(var):
    return float(input(var))


def calcula_precio(importe: float, iva: float) -> str:
    if(iva >= 0 and iva <= 100):
        ivatotal = iva / 100 + 1
        preciofinal = importe * ivatotal
        return preciofinal
    else:
        preciofinal = importe * 1.21
        return preciofinal


def main():
    importe = pedir('Introduzca el importe sin IVA: ')
    iva = pedir('Introduzca el IVA a aplicar: ')

    print(f"El importe será de: {calcula_precio(iva, importe)}")


if __name__ == "__main__":
    main()