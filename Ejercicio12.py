print("Ejercico 12")

# Entradas
SUE = float(input("Ingrese Sueldo:"))

#Proceso
if SUE < 1000:
    AUM = SUE * 0.15
    SUE = SUE + AUM

#Salida
print("\nSalida:")
print("El sueldo es:", SUE)

