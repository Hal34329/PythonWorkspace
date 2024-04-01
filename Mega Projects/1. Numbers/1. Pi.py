# Find PI to the Nth Digit
# Enter a number and have the program generate PI up to that many decimal places. 
# Keep a limit to how far the program will go.


n = 1000000 # Número de términos en la serie de Leibniz
pi_aprox = 0 # La variable que va a almacenar el valor de pi
sign = 1 # Valor del signo para ir alternando

# for i in range(inicio, fin [se suma el 1 para contener el valor de n*2], pasos de 2 en 2)
for i in range(1, n * 2 + 1, 2):
    pi_aprox += sign * 4 / i
    sign *= -1

print(pi_aprox)
