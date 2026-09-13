numeros = [0] * 5

for i in range(0, 5):
    numeros[i] = int(input("Ingrese un numero: "))

mayor = numeros[0]

for i in range(1, 5):
    if numeros[i] > mayor:
        mayor = numeros[i]

print("El numero mayor es:", mayor)
