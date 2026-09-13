sumaNinos = 0
sumaJovenes = 0
sumaAdultos = 0
sumaAncianos = 0

contNinos = 0
contJovenes = 0
contAdultos = 0
contAncianos = 0

for i in range(1, 51):
    edad = int(input("Digite edad: "))
    peso = float(input("Digite peso: "))

    if edad >= 0 and edad <= 12:
        sumaNinos = sumaNinos + peso
        contNinos = contNinos + 1
    else:
        if edad <= 29:
            sumaJovenes = sumaJovenes + peso
            contJovenes = contJovenes + 1
        else:
            if edad <= 59:
                sumaAdultos = sumaAdultos + peso
                contAdultos = contAdultos + 1
            else:
                sumaAncianos = sumaAncianos + peso
                contAncianos = contAncianos + 1

if contNinos > 0:
    promNinos = sumaNinos / contNinos
else:
    promNinos = 0

if contJovenes > 0:
    promJovenes = sumaJovenes / contJovenes
else:
    promJovenes = 0

if contAdultos > 0:
    promAdultos = sumaAdultos / contAdultos
else:
    promAdultos = 0

if contAncianos > 0:
    promAncianos = sumaAncianos / contAncianos
else:
    promAncianos = 0

print("Promedio niños:", promNinos)
print("Promedio jovenes:", promJovenes)
print("Promedio adultos:", promAdultos)
print("Promedio ancianos:", promAncianos)
