# Complementario 7
# Calcule las raíces reales de una ecuación de segundo grado.
# La forma de una ecuación de segundo grado es Ax^2 + Bx + C,
# para este caso se debe tener presente el valor de la
# discriminante. PAra el algoritmo se procede a calcular las
# raíces solo si la discriminante es mayor a CERO.

# Entradas
print("-----------------")
print("Complementario 7")
print("-----------------")
print("Para la ecuación de segundo grado de forma Ax^2 + Bx + C")
A = int(input("-> Ingrese A:"))
B = int(input("-> Ingrese B:"))
C = int(input("-> Ingrese C:"))

# Procedimiento
d = (B**2 - 4*A*C)**0.5
X1 = (-B + d) / 2*A
X2 = (-B - d) / 2*A

# Salidas
print("\nLos valores de la raíz de X son: X1 = %d, X2 = %d\n" %(X1, X2))
