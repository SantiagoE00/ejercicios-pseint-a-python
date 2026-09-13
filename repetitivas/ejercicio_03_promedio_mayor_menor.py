suma = 0
mayor = 0
menor = 0

for i in range(1, 21):
    nota = float(input("Digite la nota: "))

    suma = suma + nota

    if i == 1:
        mayor = nota
        menor = nota
    else:
        if nota > mayor:
            mayor = nota

        if nota < menor:
            menor = nota

promedio = suma / 20

print("Promedio:", promedio)
print("Mayor:", mayor)
print("Menor:", menor)
