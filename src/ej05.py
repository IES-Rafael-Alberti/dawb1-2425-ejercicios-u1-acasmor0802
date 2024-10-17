precio = int(input('Introduzca el importe sin IVA: '))
iva = int(input('Introduzca el IVA a aplicar: '))

ivatotal = iva / 100 + 1

preciofinal = precio * ivatotal

print('El importe será de:', preciofinal)