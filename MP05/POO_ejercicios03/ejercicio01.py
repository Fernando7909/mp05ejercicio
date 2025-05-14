class Inventario:
    def __init__(self):
        # El inventario es un diccionario donde las claves son los nombres de los objetos
        # y los valores son las cantidades.
        self.items = {}

    def agregar_objeto(self, nombre, cantidad=1):
        """Agrega un objeto al inventario. Si ya existe, aumenta la cantidad."""
        if nombre in self.items:
            self.items[nombre] += cantidad
        else:
            self.items[nombre] = cantidad
        print(f"Se han agregado {cantidad} {nombre}(s) al inventario.")

    def eliminar_objeto(self, nombre, cantidad=1):
        """Elimina una cantidad de un objeto del inventario."""
        if nombre in self.items:
            if self.items[nombre] > cantidad:
                self.items[nombre] -= cantidad
                print(f"Se han eliminado {cantidad} {nombre}(s) del inventario.")
            elif self.items[nombre] == cantidad:
                del self.items[nombre]
                print(f"El objeto {nombre} ha sido eliminado del inventario.")
            else:
                print(f"No tienes suficientes {nombre} para eliminar.")
        else:
            print(f"No tienes {nombre} en tu inventario.")

    def listar_inventario(self):
        """Lista todos los objetos en el inventario con su cantidad."""
        if self.items:
            print("\nInventario actual:")
            for nombre, cantidad in self.items.items():
                print(f"{nombre}: {cantidad}")
        else:
            print("Tu inventario está vacío.")

# Clase Personaje
class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.inventario = Inventario()

    def mostrar_inventario(self):
        print(f"\nInventario de {self.nombre}:")
        self.inventario.listar_inventario()

# Función principal que simula la interacción con el usuario
def main():
    # Creación de un personaje
    personaje = Personaje("Aragorn")

    while True:
        print("\nMENU DEL INVENTARIO\n")
        print("1. Agregar objeto")
        print("2. Eliminar objeto")
        print("3. Listar objetos")
        print("4. Salir\n")

        opcion = input("Elige una opción (1-4): ")

        if opcion == "1":
            nombre_objeto = input("Nombre del objeto: ")
            cantidad = int(input("Cantidad: "))
            personaje.inventario.agregar_objeto(nombre_objeto, cantidad)

        elif opcion == "2":
            nombre_objeto = input("Nombre del objeto a eliminar: ")
            cantidad = int(input("Cantidad a eliminar: "))
            personaje.inventario.eliminar_objeto(nombre_objeto, cantidad)

        elif opcion == "3":
            personaje.mostrar_inventario()

        elif opcion == "4":
            print("Gracisa y adios!")
            break

        else:
            print("ERROR!!! Intenta de nuevo.")

if __name__ == "__main__":
    main()
