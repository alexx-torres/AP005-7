# PROGRAMACIÓN APLICADA
# ACTIVIDAD: ANÁLISIS DE Fruits.csv
# Alexander Alberto Torres Lugo - 20251005063

import sys
import pandas as pd

# Intentamos abrir el archivo Fruits.csv.
try:
    datos = pd.read_csv("Fruits.csv")
    print("\nArchivo Fruits.csv cargado correctamente.")

except FileNotFoundError:
    print("\nERROR: No se encontró el archivo Fruits.csv.")
    print("Coloca Fruits.csv en la misma carpeta del programa.")
    sys.exit()

# ESTRUCTURAS DE DATOS AUXILIARES
opciones_menu = [
    "Información general",
    "Buscar una fruta",
    "Buscar por color",
    "Filtrar por precio",
    "Precio máximo y mínimo",
    "Estadísticas",
    "Tipos de frutas",
    "Colores",
    "Ordenar por precio",
    "Categorías de precio",
    "Columnas principales",
    "Salir"
]

columnas_principales = (
    "type",
    "color",
    "price usd"
)

categorias_precio = {
    "Bajo": "Menor o igual a 2 dólares",
    "Medio": "Mayor a 2 y menor o igual a 3 dólares",
    "Alto": "Mayor a 3 dólares"
}


def clasificar_precio(precio):
    if precio <= 2:
        return "Bajo"
    elif precio <= 3:
        return "Medio"
    else:
        return "Alto"


# Clasificación de precios
datos["categoria_precio"] = datos["price usd"].apply(clasificar_precio)


def titulo(texto):
    print("\n" + "=" * 60)
    print(texto.center(60))
    print("=" * 60)


def informacion_general():
    titulo("INFORMACIÓN GENERAL")
    print("\nPrimeros registros:")
    print(datos.head())

    print("\nCantidad de registros:")
    print(len(datos))

    print("\nCantidad de columnas:")
    print(len(datos.columns))

    print("\nColumnas del archivo:")
    for columna in datos.columns:
        print("-", columna)

    print("\nTipos de datos:")
    print(datos.dtypes)

    print("\nEstadísticas de los precios:")
    print(datos["price usd"].describe())


def buscar_fruta():
    titulo("BUSCAR UNA FRUTA")
    fruta = input("Escribe el nombre de la fruta: ").strip()
    resultado = datos[datos["type"].str.lower() == fruta.lower()]

    if resultado.empty:
        print("\nNo se encontró esa fruta.")
    else:
        print("\nRegistros encontrados:")
        print(resultado.to_string(index=False))
        print("\nCantidad de registros encontrados:", len(resultado))


def buscar_color():
    titulo("BUSCAR POR COLOR")
    color = input("Escribe el color: ").strip()
    resultado = datos[datos["color"].str.lower() == color.lower()]

    if resultado.empty:
        print("\nNo se encontraron frutas de ese color.")
    else:
        print("\nFrutas encontradas:")
        print(resultado.to_string(index=False))
        print("\nCantidad de registros encontrados:", len(resultado))


def filtrar_precio():
    titulo("FILTRAR POR RANGO DE PRECIOS")
    try:
        minimo = float(input("Precio mínimo: "))
        maximo = float(input("Precio máximo: "))

        if minimo > maximo:
            print("\nEl precio mínimo no puede ser mayor que el máximo.")
            return

        resultado = datos[
            (datos["price usd"] >= minimo) &
            (datos["price usd"] <= maximo)
        ]

        if resultado.empty:
            print("\nNo existen frutas dentro de ese rango.")
        else:
            print("\nFrutas encontradas:")
            print(resultado.to_string(index=False))
            print("\nCantidad de resultados:", len(resultado))

    except ValueError:
        print("\nDebes introducir valores numéricos.")


def precio_maximo_minimo():
    titulo("PRECIO MÁXIMO Y MÍNIMO")
    precio_maximo = datos["price usd"].max()
    precio_minimo = datos["price usd"].min()

    fruta_maxima = datos[datos["price usd"] == precio_maximo]
    fruta_minima = datos[datos["price usd"] == precio_minimo]

    print("\nPrecio más alto:")
    print(fruta_maxima.to_string(index=False))

    print("\nPrecio más bajo:")
    print(fruta_minima.to_string(index=False))


def estadisticas():
    while True:
        titulo("ESTADÍSTICAS")
        print("1. Precio promedio general")
        print("2. Estadísticas de una fruta")
        print("3. Estadísticas de un color")
        print("4. Volver al menú principal")

        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            promedio = datos["price usd"].mean()
            print(f"\nEl precio promedio es: ${promedio:.2f}")

        elif opcion == "2":
            fruta = input("\nEscribe el nombre de la fruta: ").strip()
            resultado = datos[datos["type"].str.lower() == fruta.lower()]

            if resultado.empty:
                print("\nNo se encontró esa fruta.")
            else:
                print("\nEstadísticas de:", fruta)
                print(resultado["price usd"].describe())

        elif opcion == "3":
            color = input("\nEscribe el color: ").strip()
            resultado = datos[datos["color"].str.lower() == color.lower()]

            if resultado.empty:
                print("\nNo se encontró ese color.")
            else:
                print("\nEstadísticas del color:", color)
                print(resultado["price usd"].describe())

        elif opcion == "4":
            break
        else:
            print("\nOpción no válida.")


def mostrar_tipos_frutas():
    titulo("TIPOS DE FRUTAS")
    frutas = datos["type"].unique()

    print("\nTipos de frutas:")
    for numero, fruta in enumerate(frutas, start=1):
        print(f"{numero}. {fruta}")

    print("\nCantidad de tipos de frutas:", len(frutas))


def mostrar_colores():
    titulo("COLORES DISPONIBLES")
    colores = datos["color"].unique()

    print("\nColores diferentes:")
    for numero, color in enumerate(colores, start=1):
        print(f"{numero}. {color}")

    print("\nCantidad de colores:", len(colores))


def ordenar_precio():
    titulo("ORDENAR POR PRECIO")
    print("1. De menor a mayor")
    print("2. De mayor a menor")

    opcion = input("\nSelecciona una opción: ")

    if opcion == "1":
        resultado = datos.sort_values(by="price usd", ascending=True)
        print("\nDatos ordenados de menor a mayor:")
        print(resultado.to_string(index=False))

    elif opcion == "2":
        resultado = datos.sort_values(by="price usd", ascending=False)
        print("\nDatos ordenados de mayor a menor:")
        print(resultado.to_string(index=False))

    else:
        print("\nOpción no válida.")


def mostrar_categorias():
    titulo("CATEGORÍAS DE PRECIO")
    print("\nCategorías utilizadas:")
    for categoria, descripcion in categorias_precio.items():
        print(f"{categoria}: {descripcion}")

    print("\nCantidad de frutas por categoría:")
    cantidades = datos["categoria_precio"].value_counts()
    for categoria, cantidad in cantidades.items():
        print(f"{categoria}: {cantidad}")


def mostrar_columnas():
    titulo("COLUMNAS PRINCIPALES")
    print("\nColumnas principales del archivo:")
    for columna in columnas_principales:
        print("-", columna)


# MENÚ PRINCIPAL

while True:
    titulo("PROGRAMA DE ANÁLISIS DE Fruits.csv")

    for idx, opcion in enumerate(opciones_menu, start=1):
        print(f"{idx}. {opcion}")

    opcion = input("\nSelecciona una opción: ")

    if opcion == "1":
        informacion_general()
    elif opcion == "2":
        buscar_fruta()
    elif opcion == "3":
        buscar_color()
    elif opcion == "4":
        filtrar_precio()
    elif opcion == "5":
        precio_maximo_minimo()
    elif opcion == "6":
        estadisticas()
    elif opcion == "7":
        mostrar_tipos_frutas()
    elif opcion == "8":
        mostrar_colores()
    elif opcion == "9":
        ordenar_precio()
    elif opcion == "10":
        mostrar_categorias()
    elif opcion == "11":
        mostrar_columnas()
    elif opcion == "12":
        print("\nPrograma finalizado.")
        print("Gracias por utilizar el programa.")
        break
    else:
        print("\nOpción no válida. Intenta nuevamente.")

    input("\nPresiona ENTER para continuar...")
