def comprobar_entero(cadena: str):
    cadena = cadena.strip()
    return cadena.isdigit() or (cadena.startswith("-") and cadena[1:].isdigit())
    

def dame_entero():
    cadena = input('Escribe un número entero: ')
    while comprobar_entero(cadena) != True:
        cadena = input("**ERROR** Eso no es un entero!!!\n\nEscribe un número entero otra vez: ")

    return int(cadena)

def main():
    num = dame_entero()
    print(f"Has introducido el número {num}")


if __name__ == "__main__":
    main()