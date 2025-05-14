import random

# Definimos la clase personaje y las subclases que heredan de ella (los 3 personajes)
# Cada personaje tiene una vida y una furza de ataque. Tambien una habilidad especial de ataque
class Personaje:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque

    def atacar(self):
        print(f"{self.nombre} ataca con {self.ataque} de daño.")
        return self.ataque

    def habilidad_especial(self):
        pass


class Guerrero_Aragorn(Personaje):
    def __init__(self):
        super().__init__("Guerrero", vida=120, ataque=20)

    def habilidad_especial(self):
        print(f"{self.nombre} golpea con fuerza .")
        return self.ataque * 2


class Mago_Gandalf(Personaje):
    def __init__(self):
        super().__init__("Mago", vida=80, ataque=15)

    def habilidad_especial(self):
        print(f"{self.nombre} lanza una Bola de Fuego")
        return 30



class Arquero_Legolas(Personaje):
    def __init__(self):
        super().__init__("Arquero", vida=90, ataque=18)



    def habilidad_especial(self):
        print(f"{self.nombre} dispara una lluvia de flechas. ¡Es un acierto múltiple!")
        return 25

# En esta funcion elegimos el personaje para la pelea en el juego

def sistema_turnos():
    print("¡Bienvenido a la batalla!")
    print("Elige tu personaje:\n1. Guerrero \n2. Mago \n3. Arquero")

    eleccion = input("Escribe 1, 2 o 3: ")

    if eleccion == "1":
        jugador = Guerrero_Aragorn()
    elif eleccion == "2":
        jugador = Mago_Gandalf()
    elif eleccion == "3":
        jugador = Arquero_Legolas()
    else:
        print("Opción inválida.")


# Entre ortras cosas, el random te selecciona a tu enemigo aleatoriamente para ta batalla

    enemigo = random.choice([Guerrero_Aragorn(), Mago_Gandalf(), Arquero_Legolas()])
    print(f"\nTe enfrentarás a un {enemigo.nombre} enemigo. ¡Buena suerte!\n")

    turno = 1
    while jugador.vida >  0 and enemigo.vida > 0:
        print(f"\n###### Turno {turno} #####")
        print(f"{jugador.nombre} (Vida: {jugador.vida})")
        print(f"{enemigo.nombre} (Vida: {enemigo.vida})")

        # Turno del jugador
        print("\n¿Qué harás? elije una de las opciones")
        print("1. Atacar")
        print("2. Usar habilidad especial de ataque")

        opcion = input("Elige(1 o 2): ")

        if opcion == "1":
            daño = jugador.atacar()
        elif opcion == "2":
            daño = jugador.habilidad_especial()
        else:
            print("perdite el turno por dudar.")
            daño = 0

        enemigo.vida -= daño

        # Turno del enemigo
        if enemigo.vida > 0:
            print(f"\n{enemigo.nombre} se prepara para atacar...")
            if random.random() < 0.3:
                daño = enemigo.habilidad_especial()
            else:
                daño = enemigo.atacar()

            jugador.vida -= daño
        turno += 1

    # Resultado final de la batalla
    if jugador.vida > 0:
        print(f"\n{jugador.nombre} ha ganado la batalla!")
    else:
        print(f"\n {jugador.nombre} ha sido derrotado. El {enemigo.nombre} enemigo ha ganado.")


# Iniciar el juego
sistema_turnos()
