# complementario 6
# Leer tres números enteros y, si el primero de ellos es negativo,
# calcular el producto de los tres, en caso contrario calcular la
# suma de ellos.

# Entradas
print("-----------------")
print("Complementario 6")
print("-----------------")
print("Ingrese 3 números")
a = int(input("-> Ingrese el primer número:"))
b = int(input("-> Ingrese el segundo número:"))
c = int(input("-> Ingrese el tercer número:"))

# Procedimiento
if a < 0:
    result = a * b * c
else:
    result = a + b + c

# Salida
print("El resultado es: %d" %(result))
