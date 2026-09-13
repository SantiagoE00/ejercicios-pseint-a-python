sumaHombres = 0
sumaMujeres = 0
sumaTotal = 0

contHombres = 0
contMujeres = 0

n = int(input("Cantidad de alumnos: "))

for i in range(1, n + 1):
    sexo = input("Digite sexo (H/M): ")
    edad = int(input("Digite edad: "))

    sumaTotal = sumaTotal + edad

    if sexo == "H":
        sumaHombres = sumaHombres + edad
        contHombres = contHombres + 1
    else:
        sumaMujeres = sumaMujeres + edad
        contMujeres = contMujeres + 1

if contHombres > 0:
    promHombres = sumaHombres / contHombres
else:
    promHombres = 0

if contMujeres > 0:
    promMujeres = sumaMujeres / contMujeres
else:
    promMujeres = 0

promTotal = sumaTotal / n

print("Promedio hombres:", promHombres)
print("Promedio mujeres:", promMujeres)
print("Promedio total:", promTotal)
