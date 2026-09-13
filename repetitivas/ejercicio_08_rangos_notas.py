menor50 = 0
entre50y69 = 0
entre70y79 = 0
mayor80 = 0

for i in range(1, 24):
    nota = int(input("Digite nota: "))

    if nota < 50:
        menor50 = menor50 + 1
    else:
        if nota < 70:
            entre50y69 = entre50y69 + 1
        else:
            if nota < 80:
                entre70y79 = entre70y79 + 1
            else:
                mayor80 = mayor80 + 1

print("Menores de 50:", menor50)
print("Entre 50 y 69:", entre50y69)
print("Entre 70 y 79:", entre70y79)
print("80 o mas:", mayor80)
