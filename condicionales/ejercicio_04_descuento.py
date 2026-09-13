compra = float(input("Ingrese el valor de la compra: "))

if compra > 100000:
    total = compra - (compra * 0.10)
else:
    total = compra

print("Total a pagar:", total)
