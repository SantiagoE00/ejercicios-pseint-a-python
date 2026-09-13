numeros = [0] * 5

for i in range(0, 5):
    numeros[i] = int(input("Ingrese un numero: "))

for i in range(0, 4):
    for j in range(i + 1, 5):
        if numeros[i] > numeros[j]:
            aux = numeros[i]
            numeros[i] = numeros[j]
            numeros[j] = aux

print("Numeros ordenados:")

for i in range(0, 5):
    print(numeros[i])
