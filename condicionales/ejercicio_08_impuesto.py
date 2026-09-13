salario = float(input("Ingrese el salario: "))

if salario > 2000000:
    impuesto = salario * 0.10
else:
    impuesto = 0

print("Impuesto:", impuesto)
