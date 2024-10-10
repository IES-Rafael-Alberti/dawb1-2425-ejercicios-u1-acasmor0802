def cualidades(nombre, edad):
    if not nombre:
        print('Desconocido')

    if (edad < 0 or edad > 125):
        while(edad < 0 or edad > 125):
            edad = int(input('Introduce una edad de nuevo: '))
        
    return print(f'Te llamas {nombre} y tienes {edad} años, te quedan aún {años_restantes(edad)} años por cumplir')


def años_restantes(edad):
    años_faltantes = 125 - edad
    return años_faltantes


def main():
    nombre = input('Introduce un nombre: ')
    edad = int(input('Introduce una edad: '))
    cualidades(nombre, edad)


if __name__ == "__main__":
    main()