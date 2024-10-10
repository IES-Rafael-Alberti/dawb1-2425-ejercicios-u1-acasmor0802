barras = int(input("Introduce el número de barras vendidas que no son del día: "))
precio = 3.49
descuento = 0.6
coste = barras * precio * (1-descuento)
print(f"Precio por una barra de pan de dia: {precio} €.")
print(f"Descuento por barra por no se fresca es del {descuento*100} %.")
print(f"Precio total de {barras} barra no frescas: {round(coste,2)} €.")