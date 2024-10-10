def main():
    inicio = int(input('Introduce un inicio: '))
    incremento = int(input('Introduce un incremento: '))
    total = int(input('Introduce un total: '))
    comprobante(incremento,total)
    intermedio(inicio,incremento,total)


def intermedio(inicio,incremento,total):
     while(total != 0):
          total = total - 1
          list().append(inicio)
          inicio += incremento
    print(list)

def comprobante(incremento,total):
    if(incremento == 0):
        while(incremento == 0):
            incremento = int(input('Introduce un nuevo número: '))
    if(total == 0):
            while(total == 0):
                total = int(input('Introduce un nuevo número: '))


if __name__ == '__main__':
    main()