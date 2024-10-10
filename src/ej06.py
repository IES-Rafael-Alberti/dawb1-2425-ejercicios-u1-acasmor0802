preciototal = int(input('Introduce el precio del articulo:'))

preciosiniva = preciototal/1.10
iva = preciosiniva * 0.10

print('El precio del articulo sin IVA es:', preciosiniva, 'y el IVA pagado es:', iva)