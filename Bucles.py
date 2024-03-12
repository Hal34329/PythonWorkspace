# Ejemplo de uso de bucles

# While
i = 1
while i<10:
    print(i)
    i = i + 1


# Foreach
lista = [1, 3, 5, 2, 4, 7, 8, 6, 9]

for elemento in lista:
    print(elemento)

print("\n\n")
# Rango
range(10) # Crea una lista de 0 hasta 9
range (1, 10) # Crea una lista desde 1 hasta 9
range (1, 10, 2) # Crea una lista desde 1 hasta 9 de 2 en 2

for i in range(1, 10, 2):
    print(i)