numeros = [0] * 5
suma = 0

for i in range(0, 5):
    numeros[i] = int(input("Ingrese un numero: "))
    suma = suma + numeros[i]

promedio = suma / 5

print("El promedio es:", promedio)
