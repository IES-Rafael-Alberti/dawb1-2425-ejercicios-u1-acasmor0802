precio = float(input('Introduzca el importe sin IVA: '))
iva = float(input('Introduzca el IVA a aplicar: '))

ivatotal = iva / 100 + 1

preciofinal = precio * ivatotal

preciofinal = round(preciofinal, 2)
print(f'El importe será de:{preciofinal}')