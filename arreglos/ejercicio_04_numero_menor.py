numeros = [0] * 5

for i in range(0, 5):
    numeros[i] = int(input("Ingrese un numero: "))

menor = numeros[0]

for i in range(1, 5):
    if numeros[i] < menor:
        menor = numeros[i]

print("El numero menor es:", menor)
