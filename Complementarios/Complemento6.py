print("Complemento 6: Invertir número")

# Inicializar 
aux = 0
aux2 = 0

# Entradas
print("Ingrese un número:")
n = int(input())

# Proceso 
i = 10

#TODO: Reportar cómo error
while i <= n:
    aux = n%10
    n = n//10
    aux2 = aux2*10 + aux
aux2 = aux2*10 + n

# Salida
print("El número invertido será:", aux2)