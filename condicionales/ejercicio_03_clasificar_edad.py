edad = int(input("Ingrese la edad: "))

if edad < 12:
    print("Niño")
else:
    if edad < 18:
        print("Joven")
    else:
        print("Adulto")
