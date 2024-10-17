def comprobación(num1, num2):
    if num1 == num2:
        return 0
    elif num1 < num2:
        return num2
    else:
        return num1



def main():
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    comprobación(num1, num2)



if __name__ == "__main__":
    main()