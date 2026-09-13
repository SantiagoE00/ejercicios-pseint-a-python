numeros = [0] * 5
encontrado = False

for i in range(0, 5):
    numeros[i] = int(input("Ingrese un numero: "))

buscar = int(input("Numero a buscar: "))

for i in range(0, 5):
    if numeros[i] == buscar:
        encontrado = True

if encontrado:
    print("Numero encontrado.")
else:
    print("Numero no encontrado.")
