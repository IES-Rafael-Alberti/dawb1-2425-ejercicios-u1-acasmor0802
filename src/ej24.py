precio = input("Introduzca el precio del producto en euros con dos decimales: ")
print(precio[:precio.find(".")],"euros y",precio[precio.find(".")+1:],"centimos.")