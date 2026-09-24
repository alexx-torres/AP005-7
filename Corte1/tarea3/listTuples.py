# Declaración de una lista inicial de colores
my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']
# Muestra en consola la lista completa
print(my_lista)
# Muestra el tipo de dato de la variable (devuelve <class 'list'>)
print(type(my_lista))
# Accede e imprime el elemento en el índice 2 ('Amarillo')
print(my_lista[2])
# Muestra el número total de elementos en la lista usando len()
print("my_lista size: ", len(my_lista))
# Obtiene un subconjunto de la lista desde el índice 0 hasta el 1 (el 2 no se incluye)
print(my_lista[0:2])
# Sintaxis equivalente a la anterior: al omitir el inicio, comienza desde el índice 0
print(my_lista[:2])
# Agrega un nuevo elemento ('Blanco') al final de la lista
my_lista.append('Blanco')
print(my_lista)
# Inserta el elemento 'Negro' en el índice 3, desplazando los demás hacia la derecha
my_lista.insert(3, 'Negro')
print(my_lista)
# Agrega múltiples elementos al final de la lista concatenando otra lista
my_lista.extend(['Marron', 'Gris'])
print(my_lista)
# Devuelve el índice en el que se encuentra por primera vez el elemento 'Azul'
print(my_lista.index('Azul'))
# Intento de eliminar un elemento no existente que lanzaría error:
# my_lista.remove('Magenta')
# Busca y elimina la primera aparición del elemento 'Marron' en la lista
my_lista.remove('Marron')
print(my_lista)
# Inserta el elemento 'Marron' en la posición del índice 8
my_lista.insert(8, 'Marron')
print(my_lista)
# Elimina y devuelve el último elemento de la lista
print(my_lista.pop())
# Obtiene la cantidad actual de elementos en la lista
size = len(my_lista)
print("size = ", size)
# Intento de hacer pop pasando el tamaño total como índice; lanzaría IndexError porque los índices van de 0 a size-1:
# print(my_lista.pop(size))
# Duplica y concatena la lista 3 veces creando una nueva lista más grande
my_lista_3 = my_lista*3
print("my_lista_3: ", my_lista_3)
print("Sort:")
print()
# .sort() ordena la lista en el sitio y devuelve None (por eso my_listaSort guarda None)
my_listaSort = my_lista.sort()
print(my_listaSort)
# Lista numérica desordenada
my_NumList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1]
print("Ordering my_NumList: ")
# Ordena la lista numérica de menor a mayor
my_NumList.sort()
print(my_NumList)
# Asignación comentada que también guardaría None:
# OrderedLList = my_NumList.sort()
# print(my_listaSort)
# Ordena la lista numérica en orden inverso (de mayor a menor)
my_NumList.sort(reverse = True)
print("De menor a mayor: ", my_NumList)
# Imprime líneas decorativas de separación
print("###########################")
print("###########################")
print("###########################")
print("############TUPLAS#########")
# Convierte la lista 'my_lista' en una tupla (estructura inmutable)
my_tupla = tuple(my_lista)
print()
print()
print("my_tuple: ", my_tupla)
# Accede e imprime el primer elemento de la tupla (índice 0)
print(my_tupla[0])
# Accede e imprime el tercer elemento de la tupla (índice 2)
print(my_tupla[2])
# Evalúa si la cadena 'Rojo' existe en la tupla y devuelve un booleano (True/False)
print('Rojo' in my_tupla)
# Cuenta cuántas veces aparece el elemento 'Rojo' dentro de la tupla
print(my_tupla.count('Rojo'))
# Declaración de una variable que contiene una cadena simple (sin coma no se crea una tupla)
my_tupla_unitaria = ('Blanco')
print(my_tupla_unitaria)
# Empaquetado de tupla: crea una tupla omitiendo los paréntesis explícitos
my_tupla = 'Gaspar', 5, 8, 1999
print(my_tupla)
# Desempaquetado de tupla: asigna cada valor de la tupla a las variables en orden
nombre, dia, mes, año = my_tupla
print(nombre)
print(dia)
print(mes)
print(año)
# Imprime los datos desempaquetados formateados con texto adicional
print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)
