precio = int(input("ingrese un numero"))

if precio <= 1000:
    print("barato")
elif precio > 1000 and precio <= 2000:
    print("medianamente barato")
elif precio > 2000 and precio <= 3000:
    print("medianamente caro")
else: 
    print("caro")
