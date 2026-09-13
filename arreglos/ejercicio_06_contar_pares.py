numeros = [0] * 5
contador = 0

for i in range(0, 5):
    numeros[i] = int(input("Ingrese un numero: "))

    if numeros[i] % 2 == 0:
        contador = contador + 1

print("Cantidad de numeros pares:", contador)
