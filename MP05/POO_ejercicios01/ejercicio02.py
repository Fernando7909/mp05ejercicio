import json


class Personaje:
    def __init__(self, nombre, nivel, experiencia, inventario):
        # Inicializamos los datos básicos del personaje (atributos)
        self.nombre = nombre
        self.nivel = nivel
        self.experiencia = experiencia
        self.inventario = inventario



    def guardar_json(self, archivo):
        # Intentamos abrir el archivo para cargar los personajes existentes
        try:
            with open(archivo, 'r') as f:
                personajes = json.load(f)
        except FileNotFoundError:
            personajes = []

        # Añadimos este personaje a la lista de personajes
        personajes.append(self.__dict__)

        # Guardamos la lista actualizada en el archivo
        with open(archivo, 'w') as f:
            json.dump(personajes, f, indent=4)


    # Leemos el archivo y devolvemos un personaje creado a partir de los datos
    def cargar_json(self, archivo):

        with open(archivo, 'r') as f:
            datos = json.load(f)
        return Personaje(**datos)  # Usamos los datos para crear un objeto Personaje


    def agregar_personaje_desde_terminal(self, archivo):
        print("Vamos a crear un nuevo personaje.")
        nombre = input("¿Cómo se llama tu personaje? ")
        nivel = int(input("¿En qué nivel está? "))
        experiencia = int(input("¿Cuánta experiencia tiene? "))
        inventario = input("¿Qué lleva en el inventario? (sepáralo por comas): ").split(',')

        # Limpiamos los espacios extra en cada elemento del inventario
        inventario = [item.strip() for item in inventario]

        # Creamos el personaje lo guardamos
        personaje = Personaje(nombre, nivel, experiencia, inventario)
        personaje.guardar_json (archivo)

        print(f"¡Personaje '{nombre}' guardado con éxito!")



    def mostrar_personajes(self, archivo):
        # Intentamos leer el archivo para mostrar los personajes guardados
            with open(archivo, 'r') as f:
                personajes = json.load(f)

            if not personajes:
                print("No hay ningún personaje guardado todavía.")
                return

            print("Lista de personajes guardados:")
            for p in personajes:
                print(f"- Nombre: {p['nombre']}, Nivel: {p['nivel']}, "
                      f"Experiencia: {p['experiencia']}, Inventario: {', '.join(p['inventario'])}")



# Menú principal para interactuar con el programa
def menu():
    archivo_json = "personajes.json"  # Archivo donde guardaremos los personajes

    while True:
        print("\n--- Menú principal ---")
        print("1. Añadir un nuevo personaje")
        print("2. Ver todos los personajes guardados")
        print("3. Salir del programa")

        opcion = input("Elige una opción (1, 2 o3): ")

        if opcion =="1":
            # Creamos un objeto vacío solopara usar sus métodos
            personaje = Personaje("", 0, 0, [])
            personaje.agregar_personaje_desde_terminal(archivo_json)

        elif opcion  == "2":
            personaje = Personaje("", 0, 0, [])
            personaje.mostrar_personajes (archivo_json)

        elif opcion == "3":
            print("Hasta luego máquina.")
            break
        else:
            print("Por favor, elige una opción válida (1, 2 o 3).")


# menú principal al iniciar el programa
menu()
