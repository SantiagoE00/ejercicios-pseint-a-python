numeros = [0] * 5
suma = 0

for i in range(0, 5):
    numeros[i] = int(input("Ingrese un numero: "))
    suma = suma + numeros[i]

print("La suma es:", suma)
