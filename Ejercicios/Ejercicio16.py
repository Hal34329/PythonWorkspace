# -*- coding: utf-8 -*-
# Pág. 124
print("Ejercicio 16")

#Entradas
A = int(input("Ingrese A:"))
B = int(input("Ingrese B:"))
C = int(input("Ingrese C:"))

print("\nSalida:")

#Proceso
if A > B:
    if A > C:
        if(B > C):
            print(A, B, C)
        else:
            print(A, C, B)
    else:
        print(C, A, B)
else:
    if B > C:
        if A > C:
            print(B, A, C)
        else:
            print(B, C, A)
    else:
        print(C, B, A)
        

