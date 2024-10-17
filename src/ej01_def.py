def texto(nombre):
    if nombre == 'Pedro':
        return f"Hola {nombre}."


def main():
    nombre = input("Introduce tu nombre: ")
    print(texto(nombre))


if __name__ == "__main__":
    main()