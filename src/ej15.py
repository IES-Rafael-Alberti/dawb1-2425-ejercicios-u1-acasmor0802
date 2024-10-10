interes = 4/100
deposito = float(input("Introduzca la cantidad de dinero de la cuenta: "))
ahorro1 = round(deposito * (1+(interes)),2)
ahorro2 = round(ahorro1 * (1+(interes)),2)
ahorro3 = round(ahorro2 * (1+(interes)),2)
print(f"Cantidad de dineros despues del primer años {ahorro1} €.")
print(f"Cantidad de dineros despues del primer años {ahorro2} €.")
print(f"Cantidad de dineros despues del primer años {ahorro3} €.")