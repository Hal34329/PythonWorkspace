# Complementario 8

# Algoritmo que permita efectual el cálculo del área de un
# círculo o un triángulo equilátero según la opción seleccionada
# por el usuario a través de un mneú, además se deben ingresar
# los datos adicionales que se requieran para el cálculo del área.

print("-----------------")
print("Complementario 8")
print("-----------------")

pi = 3.1416

print("Elija la operación a realizar")
print("1. Cálculo del área de un círculo")
print("2. Cálculo del área de un triángulo equilátero")

# Entradas
opc = int(input("\nOpción: "))
# print("Resultado elegido %d" %(opc))

# Procedimiento

# Salidas
if opc == 1:
    r = int(input("Ingrese el valor del radio:"))
    result = pi * r**2
    print("El área del círculo es: %f" %(result))
elif opc == 2:
    #print("Not yet")
    b = int(input("Ingrese el valor de la base del triangulo:"))
    h = int(input("Ingrese el valor de la altura del triangulo:"))
    result = (b * h) / 2
    print("El área del triángulo es: %f" %(result))
    
else:
    print("\nError")

