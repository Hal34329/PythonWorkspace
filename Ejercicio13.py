print("Ejercicio 13")

#Entradas
year = int(input("Ingrese año:"))

#Salida
print("Salida:")
if(year%400 == 0) or (year%400 == 0) and (year%100 != 0):
    print("El año es bisiesto")
else:
    print("El año no es bisisesto")