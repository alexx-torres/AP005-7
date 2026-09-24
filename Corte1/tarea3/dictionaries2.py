# Obtener una clave (Get A Key)
# Puedes acceder a los valores de un diccionario proporcionando su clave:
# Crea un diccionario con las alturas de los edificios en metros
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
# Accede e imprime el valor asociado a "Burj Khalifa"
print(building_heights["Burj Khalifa"]) # Imprime 828
# Accede e imprime el valor asociado a "Ping An"
print(building_heights["Ping An"]) # Imprime 599
# Crea un diccionario que relaciona elementos del zodiaco con listas de signos
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
# Accede e imprime la lista de signos de tierra
print(zodiac_elements["earth"])
# Accede e imprime la lista de signos de fuego
print(zodiac_elements["fire"])
# Obtener una clave no válida (Get an Invalid Key)
# Reorganiza/declara el diccionario de alturas de edificios
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
# Intentar acceder a una clave que no existe lanza un error KeyError:
# print(building_heights["Landmark 81"])
# Una forma de evitar este error es verificar primero si la clave existe en el diccionario:
key_to_check = "Landmark 81"
# Imprime el valor de forma segura solo si la clave existe en el diccionario
if key_to_check in building_heights:
  print(building_heights["Landmark 81"])
# Redeclara el diccionario de elementos del zodiaco
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
# Agrega un nuevo par clave-valor al diccionario
zodiac_elements["energy"] = "Not a Zodiac element"
# Verifica si la clave "energy" existe antes de intentar acceder a ella
if "energy" in zodiac_elements:
   print(zodiac_elements["energy"])
# Obtener una clave de forma segura (Safely Get a Key)
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
# Esta línea devolverá 632:
building_heights.get("Shanghai Tower")
# Esta línea devolverá None porque la clave no existe:
building_heights.get("My House")
# Diccionario de IDs de usuario que relaciona nombres de usuario con números de ID
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
# Obtiene el ID para "teraCoder" de forma segura usando .get()
user_ids.get("teraCoder")
# Comprueba si el ID devuelto es None; si es así, asigna un ID por defecto, de lo contrario obtiene el ID real
if user_ids.get("teraCoder") == None:
   tc_id = 1000
else:
   tc_id = user_ids.get("teraCoder")
# Imprime el ID obtenido para "teraCoder"
print(tc_id)
# Comprueba si "superStackSmash" existe; si no, establece un valor de ID por defecto
if user_ids.get("superStackSmash") == None:
    stack_id = 100000
# Imprime el ID por defecto asignado
print(stack_id)
# Eliminar una clave (Delete a Key)
# .pop() sirve para eliminar elementos de un diccionario cuando conoces el valor de la clave.
raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}
# Elimina la clave 320291 y devuelve su valor ("Gift Basket"); devuelve "No Prize" si la clave no se encuentra
print(raffle.pop(320291, "No Prize"))
# Imprime "Gift Basket"
# Imprime el diccionario después de eliminar la clave 320291
print(raffle)
# Imprime {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}
# Intenta hacer pop de la clave 100000 que no existe; devuelve el valor por defecto "No Prize"
print(raffle.pop(100000, "No Prize"))
# Imprime "No Prize"
# El diccionario permanece sin cambios
print(raffle)
# Imprime {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}
# Elimina la clave 872921 y devuelve su valor ("Concert Tickets")
print(raffle.pop(872921, "No Prize"))
# Imprime "Concert Tickets"
# Imprime el diccionario después de eliminar la clave 872921
print(raffle)
# Imprime {223842: "Teddy Bear", 412123: "Necklace", 298787: "Pasta Maker"}
# Inventario de objetos disponibles y sus puntos de salud
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
# Puntos de salud iniciales
health_points = 20
# Elimina "stamina grains" del inventario y suma su valor (15) a los puntos de salud
health_points += available_items.pop("stamina grains", 0)
# Elimina "power stew" del inventario y suma su valor (30) a los puntos de salud
health_points += available_items.pop("power stew", 0)
# Intenta eliminar "mystic bread"; al no existir, suma el valor por defecto 0
health_points += available_items.pop("mystic bread", 0)
# Imprime los objetos restantes en el inventario
print(available_items)
# Imprime el total de puntos de salud acumulados
print(health_points)
# Obtener todas las claves (Get All Keys)
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
# Convertir un diccionario directamente a lista devuelve todas sus claves
print(list(test_scores))
# Imprime ["Grace", "Jeffrey", "Sylvia", "Pedro", "Martin", "Dina"]
# Itera a través de cada clave utilizando el método .keys()
for student in test_scores.keys():
  print(student)
# Diccionario de IDs de usuario
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
# Diccionario con la cantidad de ejercicios por lección
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
# Obtiene un objeto dict_keys con todas las claves de user_ids
users = user_ids.keys()
# Obtiene un objeto dict_keys con todas las claves de num_exercises
lessons = num_exercises.keys()
# Imprime la vista de claves para los IDs de usuario
print(users)
# Imprime la vista de claves para los nombres de las lecciones
print(lessons)
# Obtener todos los valores (Get All Values)
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
# Itera a través de todos los valores del diccionario (listas de puntuaciones)
for score_list in test_scores.values():
  print(score_list)
# Diccionario que relaciona temas con la cantidad de ejercicios
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
# Variable acumuladora para el total de ejercicios
total_exercises = 0
# Itera a través de cada valor numérico en el diccionario y lo suma a total_exercises
for exercises in num_exercises.values():
   total_exercises += exercises
# Imprime la suma total de ejercicios
print(total_exercises)
# Obtener todos los elementos (Get All Items)
biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}
# Itera sobre los pares clave-valor simultáneamente usando .items()
for company, value in biggest_brands.items():
  print(company + " has a value of " + str(value) + " billion dollars. ")
# Diccionario que relaciona profesiones con el porcentaje de mujeres
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}
# Itera a través de cada profesión y su porcentaje asociado
for occupation, percentage in pct_women_in_occupation.items():
   print("Women make up " + str(percentage) + " percent of " + occupation + "s.")
