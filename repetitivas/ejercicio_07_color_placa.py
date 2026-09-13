amarilla = 0
rosa = 0
roja = 0
verde = 0
azul = 0

n = int(input("Cantidad de autos: "))

for i in range(1, n + 1):
    placa = int(input("Digite ultimo digito de la placa: "))

    if placa == 1 or placa == 2:
        amarilla = amarilla + 1
    elif placa == 3 or placa == 4:
        rosa = rosa + 1
    elif placa == 5 or placa == 6:
        roja = roja + 1
    elif placa == 7 or placa == 8:
        verde = verde + 1
    elif placa == 9 or placa == 0:
        azul = azul + 1

print("Amarilla:", amarilla)
print("Rosa:", rosa)
print("Roja:", roja)
print("Verde:", verde)
print("Azul:", azul)
