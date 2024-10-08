def calculo(num1,num2):
    if(num1 == num2):
        print('Los números son iguales')
    else:
        if(num1 < num2):
            calcular1(num1,num2)
        else:
            calcular2(num1,num2)
        

def calcular2(num1,num2):
    num3 = len(range(num2 +1,num1))
    print(num3)


def calcular1(num1, num2):
    num3 = len(range(num1 +1,num2))
    print(num3)


def main():
    numero = (input('Introduce 2 números: ').split(','))
    num1 = int(numero[0].strip())
    num2 = int(numero[1].strip())
    calculo(num1, num2)

    
if __name__ == "__main__":
    main()