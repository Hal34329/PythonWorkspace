# Find PI to the Nth Digit
# Enter a number and have the program generate PI up to that many decimal places. 
# Keep a limit to how far the program will go.

# Inputs
n = int(input("Introduzca el número de digitos de Pi que quiere mostrar:"))

for i in range(n):
    R = R + 1/(n+2)

val = 4 * (1 - R)

print("El valor de Pi es: %d" %(val))