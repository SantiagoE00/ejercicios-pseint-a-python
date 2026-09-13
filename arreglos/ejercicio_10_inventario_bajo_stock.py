stock = [0] * 5

for i in range(0, 5):
    stock[i] = int(input("Ingrese el stock del producto " + str(i + 1) + ": "))

print("Productos con bajo stock:")

for i in range(0, 5):
    if stock[i] < 10:
        print("Producto", i + 1, "tiene bajo stock.")
