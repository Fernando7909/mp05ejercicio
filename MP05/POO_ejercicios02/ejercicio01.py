import random

#Creacion de la clase de Personaje con sus respectivas funciones de vida, ataque
class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = random.randint(80, 120)
        self.ataque = random.randint(10, 20)
        self.defensa =  random.randint(5, 15)

    def esta_vivo(self):
        return self.vida > 0

    def atacar(self, enemigo):
        daño = max(1, self.ataque - enemigo.defensa // 2)
        enemigo.vida -= daño
        print(f"{self.nombre} ataca a {enemigo.nombre} y causa {daño} de daño!")
        print(f"{enemigo.nombre}  ahora tiene {enemigo.vida} putos de vida.\n")

    def __str__(self):
        return f"{self.nombre} (Vida: {self.vida}, Ataque: {self.ataque}, Defensa: {self.defensa})"


#Funcion para crear a los personajes y almacenarlos
def crear_personaje():

    nombre = input("Nombre del personaje: ")
    return  Personaje(nombre)


# Funcion que muestra los personajes que has creado mediante un bucle que recorre a todos los personajes
def mostrar_personajes(personajes):
    print("\n Personajes:")
    i=1
    for personaje in personajes:
        print(f"{i}. {personaje}")
        i += 1


#Funcion que crea un menu iinteractivo con diferentes opciones
def batalla(jugador, enemigo):
    print(f" \n¡Comienza la batalla entre {jugador.nombre} y {enemigo.nombre}!")

    while jugador.esta_vivo() and enemigo.esta_vivo():
        print(f"\nTurno de {jugador.nombre}:")
        print("1. Atacar")
        print("2. Ver estadísticas")

        opcion = input("Elige una acción (1-2): ")

        if opcion  =="1":
            jugador.atacar(enemigo)

        elif opcion == "2":
            print(f"\n{jugador}\n{enemigo}")
            continue
        else:
            print("Opción no válida. Pierdes tu turno!")
        if not  enemigo.esta_vivo():
            break

        print(f"\nTurno de {enemigo.nombre}:")
        enemigo.atacar(jugador)

    if jugador.esta_vivo():
        print(f"\n¡{jugador.nombre} ha vencido la batalla!")
    else:
        print(f"\n¡{enemigo.nombre} ha ganado la batalla!")


def main():
    print("JUEGO DE BATALLA POR TURNOS")
    personajes = []

    while True:
        print("\nMENÚ PRINCIPAL")
        print("1. Crear personaje")
        print("2. Iniciar batalla")
        print("3. Salir")

        opcion = input("Elige una opción (1-3): ")

        if opcion =="1":
            personajes.append(crear_personaje())

        elif opcion == "2":
            if len(personajes) < 2:
                print("Necesitas al menos 2 personajes para batallar!")
                continue

            mostrar_personajes(personajes)

            try:
                p1= int(input("\nElige tu personaje (número): ")) - 1
                p2 = int(input("Elige el enemigo (número): ")) - 1

                if p1== p2:
                    print("No puedes elegir el mismo personaje!")
                    continue

                # vida para nueva batalla
                personajes[p1].vida = personajes[p1].vida + random.randint(10, 20)
                personajes[p2].vida = personajes[p2].vida + random.randint(10, 20)

                batalla(personajes[p1], personajes[p2])
            except (ValueError, IndexError):
                print("Selección inválida. Intenta nuevamente.")

        elif opcion == "3":
            print("¡Gracias por jugar!")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")


if __name__ == "__main__":
    main()