# Bucle_ejercicio 1

# Se coloca una capital C, a un interés I (que oscila entre 0 y 
# 100), durante M años y se desea saber en cuanto se habrá
# convertido ese capital en "M" años, sabiendo que es
# acumulativo.

print("Ejercicio interés")

# Inicialización
C = -1
I = 0
M = 0

# Entradas
while(C < 0) or (I <= 0) or (I >= 100) or (M <= 0):
    print("Introduce el capital, el interés y el tiempo apropiados")
    C = int(input("Capital:"))
    I = int(input("Interés:"))
    M = int(input("Tiempo en años:"))

# Proceso
for i in range(M):
    C = C * (1 + I / 100)

# Salida
print("\nSalida")
print("Tienes %f soles" %C)
