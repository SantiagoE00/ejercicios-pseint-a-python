positivos = 0
negativos = 0
neutros = 0

for i in range(1, 21):
    num = int(input("Digite un numero: "))

    if num > 0:
        positivos = positivos + 1
    else:
        if num < 0:
            negativos = negativos + 1
        else:
            neutros = neutros + 1

print("Positivos:", positivos)
print("Negativos:", negativos)
print("Neutros:", neutros)
