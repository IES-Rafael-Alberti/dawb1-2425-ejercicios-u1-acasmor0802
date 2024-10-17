def texto(nombre):
    saludo = f"Hola {nombre}"
    return saludo


def main():
    nombre = input("Introduce tu nombre: ")
    print(texto(nombre))

if __name__ == "__main__":
    main()