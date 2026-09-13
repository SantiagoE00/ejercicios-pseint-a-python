hombres = 0
mujeres = 0

n = int(input("Cantidad de personas: "))

for i in range(1, n + 1):
    sexo = input("Digite sexo (H/M): ")

    if sexo == "H":
        hombres = hombres + 1
    else:
        mujeres = mujeres + 1

print("Hombres:", hombres)
print("Mujeres:", mujeres)
