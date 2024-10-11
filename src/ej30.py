def main():
    inicio = int(input('Introduce un inicio: '))
    incremento = int(input('Introduce un incremento: '))
    total = int(input('Introduce un total: '))
    comprobante(incremento,total)
    print(pantalla(inicio,incremento,total))


def pantalla(inicio,incremento,total):
    cadena = intermedio(inicio,incremento,total)
    resultado = ""
    for i, numero in enumerate(cadena):
        if i == 0:
            resultado += str(numero)
        elif i == 1:
            resultado += "-" + str(numero)
        elif i == len(cadena) - 1:
           resultado += "-" + str(numero)
        else:
            resultado += ".." + str(numero)
    return resultado


def intermedio(inicio,incremento,total):
    serie = []
    while(total != 0):
            total = total - 1
            serie.append(inicio)
            inicio += incremento
    return serie


def comprobante(incremento,total):
    if(incremento == 0):
        while(incremento == 0):
            incremento = int(input('Introduce un nuevo número: '))
    if(total == 0):
            while(total == 0):
                total = int(input('Introduce un nuevo número: '))


if __name__ == '__main__':
    main()