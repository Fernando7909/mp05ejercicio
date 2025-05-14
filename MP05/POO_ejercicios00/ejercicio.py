# Ejercicio 1: Clases y Objetos
# 1. Clase Personaje con los atributos nombre y nivel
class Personaje:
    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel

    # 2. Método saludar que imprime un saludo con el nombre y nivel del personaje
    def saludar(self):
        print(f"¡Hola! Soy {self.nombre} y tengo el nivel {self.nivel}.")

# Creamos dos objetos Personaje y llamamos al método saludar
personaje1 = Personaje("Gandalf", 99)
personaje2 = Personaje("Frodo", 15)
personaje1.saludar()  # ¡Hola! Soy Gandalf y tengo el nivel 99.
personaje2.saludar()  # ¡Hola! Soy Frodo y tengo el nivel 15.


# Ejercicio 2: Atributos y Métodos
# 1. Clase Arma con los atributos nombre, daño y tipo
class Arma:
    def __init__(self, nombre, daño, tipo):
        self.nombre = nombre
        self.daño = daño
        self.tipo = tipo

    # 2. Método mostrar_info que devuelve la información del arma
    def mostrar_info(self):
        return f"Arma: {self.nombre}, Daño: {self.daño}, Tipo: {self.tipo}"

    # Ejercicio 3: Métodos adicionales
    # 1. Método usar que imprime "Usando el arma"
    def usar(self):
        print("Usando el arma.")

    # 2. Método guardar que imprime "Guardando el arma"
    def guardar(self):
        print("Guardando el arma.")

    # Ejercicio 4: Atributos de clase
    # 1. Atributo de clase durabilidad con valor 100
    durabilidad = 100


# 3. Creamos un objeto de la clase Arma y mostramos su información
mi_arma = Arma("Espada del Rey", 35, "Cuerpo a cuerpo")
print(mi_arma.mostrar_info())  # Arma: Espada del Rey, Daño: 35, Tipo: Cuerpo a cuerpo


# Llamamos a los métodos usar y guardar
mi_arma.usar()  # Usando el arma.
mi_arma.guardar()  # Guardando el arma.


# 4. Creamos un segundo objeto de la clase Arma y mostramos el atributo durabilidad
mi_arma2 = Arma("Arco Elfo", 25, "A distancia")
print(f"Durabilidad del arma 1: {mi_arma.durabilidad}")  # Durabilidad del arma 1: 100
print(f"Durabilidad del arma 2: {mi_arma2.durabilidad}")  # Durabilidad del arma 2: 100
