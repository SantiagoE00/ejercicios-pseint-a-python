hombres = 0
mujeres = 0
mayores170 = 0
menores150 = 0
sumaAltura = 0
total = 0

edad = int(input("Digite edad (0 para terminar): "))

while edad != 0:
    sexo = input("Digite sexo (H/M): ")
    altura = float(input("Digite altura: "))

    total = total + 1

    sumaAltura = sumaAltura + altura

    if sexo == "H":
        hombres = hombres + 1
    else:
        mujeres = mujeres + 1

    if altura > 1.70:
        mayores170 = mayores170 + 1

    if altura <= 1.50:
        menores150 = menores150 + 1

    edad = int(input("Digite edad (0 para terminar): "))

promedio = sumaAltura / total

print("Hombres:", hombres)
print("Mujeres:", mujeres)
print("Promedio altura:", promedio)
print("Mayores a 1.70:", mayores170)
print("Menores o iguales a 1.50:", menores150)
