preciototal = float(input('Introduce el precio del articulo:'))

preciosiniva = preciototal/1.10
iva = preciosiniva * 0.10
preciosiniva = round(preciosiniva, 2)
iva = round(iva, 2)
print(f'El precio del articulo sin IVA es: {preciosiniva} y el IVA pagado es: {iva}')