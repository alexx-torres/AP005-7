# Crea un diccionario con la temperatura (o sensores) de cada habitación
sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
# Crea un diccionario con la cantidad de cámaras en distintas zonas
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}
# Imprime el contenido del diccionario 'sensors'
print(sensors)
# Imprime el contenido del diccionario 'num_cameras'
print(num_cameras)
# Crea un diccionario para traducir palabras del inglés a Élfico (Sindarin)
translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch" }
# Imprime el diccionario de traducciones
print(translations)
##Verifiying an error:
# En Python, las claves de un diccionario DEBEN ser de un tipo mutable (como enteros, cadenas o tuplas).
# Las listas '[1, 2, 4, 8, 16]' son mutables, por lo que esta línea lanza un error de tipo (TypeError):
# powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}
# # print(powers)
# Crea un diccionario donde los valores son listas de nombres (las listas SÍ pueden ser valores)
children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"] , "Corleone": ["Sonny", "Fredo", "Michael"]}
print(children) # Muestra el diccionario con familias y sus hijos
# Crea un diccionario totalmente vacío utilizando llaves sin elementos
my_empty_dictionary = {}
print(my_empty_dictionary) # Muestra: {}
#Crea un diccionario inicial de menú con sus respectivos precios
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print("Before: ", menu) # Muestra el menú original
# Añade un nuevo par clave-valor ("cheesecake" con valor 8) al diccionario
menu["cheesecake"] = 8
print("After", menu) # Muestra el menú actualizado con el cheesecake incluido
# Reasignación de variables:
animals_in_zoo = {"dinosaurs": 0} # Se crea el diccionario con "dinosaurs"
animals_in_zoo = {"dinosaurs": 0} # Se sobreescribe la variable exactamente con lo mismo
animals_in_zoo = {"horses": 2}    # Se sobreescribe la variable; el diccionario anterior se pierde
print(animals_in_zoo)            # Imprime únicamente: {'horses': 2}
##Add multiple keys
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
print("Before", sensors) # Imprime el estado inicial de los sensores
# El método .update() agrega múltiples pares clave-valor de un solo paso
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
print("After", sensors) # Muestra el diccionario combinando las zonas antiguas y las nuevas
###
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
print(user_ids) # Muestra los dos usuarios iniciales
# Agrega dos nuevos usuarios de una sola vez al diccionario
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids) # Muestra el diccionario con los cuatro usuarios
## Overwrite values ##
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print("Before: ", menu)
# Como la clave "oatmeal" ya existe, esta instrucción modifca su valor de 3 a 5
menu["oatmeal"] = 5
print("After", menu) # Muestra el menú con el valor actualizado de "oatmeal"
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
print("Before", oscar_winners) # Muestra los ganadores iniciales
print()                        # Imprime un salto de línea en blanco
# Agrega la nueva categoría "Supporting Actress" que no existía antes
oscar_winners.update({"Supporting Actress": "Viola Davis"})
print("After1", oscar_winners)
print()                        # Imprime otro salto de línea en blanco
# Corrige la clave "Best Picture", reemplazando "La La Land" por "Moonlight"
oscar_winners["Best Picture"] = "Moonlight"
print("After2", oscar_winners)
###Dict Comprehensions
#Let’s say we have two lists that we want to combine into a
#dictionary, like a list of students and a list of their heights,
#in inches:
# Lista 1: Nombres de estudiantes
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
# Lista 2: Alturas correspondientes para cada estudiante (en pulgadas)
heights = [61, 70, 67, 64]
zip(names, heights) empareja cada nombre con su altura respetando el orden
zipStudents = zip(names, heights)
print("zipStudents: ", zipStudents) # Muestra el objeto iterador zip en memoria
# Estructura de comprensión: crea un diccionario iterando sobre las parejas generadas por zip
students = {key:value for key, value in zip(names, heights)}
print(students) # Muestra: {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}
# Lista de bebidas
drinks = ["espresso", "chai", "decaf", "drip"]
#Lista de contenido de cafeína para cada bebida
caffeine = [64, 40, 0, 120]
# Empareja las bebidas con su cafeína
zipped_drinks = zip(drinks, caffeine)
print(zipped_drinks)
# Convierte las parejas emparejadas en un diccionario mediante comprensión
drinks_to_caffeine = {key:value for key, value in zipped_drinks}
print(drinks_to_caffeine)
# Lista con nombres de canciones
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
# Lista con la cantidad de reproducciones de cada canción
playcounts = [78, 29, 44, 21, 89, 5]
# Crea un diccionario uniendo las canciones (claves) con sus reproducciones (valores)
plays = {key:value for key, value in zip(songs, playcounts)}
# Imprime el diccionario 'plays' resultante
print(plays)
# Añade la canción "Purple Haze" con 1 reproducción
plays.update({"Purple Haze": 1})
# Actualiza las reproducciones de "Respect", cambiando su valor previo (89) por 94
plays.update({"Respect": 94})
# Imprime el diccionario 'plays' actualizado
print("After: ", plays)
# Crea un diccionario anidado (un diccionario dentro de otro)
#"The Best Songs" contiene el diccionario 'plays' completo
# "Sunday Feelings" se inicializa como un diccionario vacío
library = {"The Best Songs": plays, "Sunday Feelings": {}}
# Imprime la biblioteca completa
print(library)
