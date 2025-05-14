import random


class Personaje:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque

    def atacar(self, objetivo):
        danio = random.randint(self.ataque // 2, self.ataque)
        objetivo.vida -= danio
        print(f"{self.nombre} ataca a {objetivo.nombre} y le causa {danio} de daño!")
        if objetivo.vida <= 0:
            print(f"¡{objetivo.nombre} ha sido derrotado!")


def combate(jugador, enemigo):
    print("\n¡Comienza el combate!")
    print(f"{jugador.nombre} (Vida: {jugador.vida}) vs {enemigo.nombre} (Vida: {enemigo.vida})")

    turno = 0
    while jugador.vida > 0 and enemigo.vida > 0:
        turno += 1
        print(f"\nTurno {turno}")

        # Turno del jugador
        jugador.atacar(enemigo)
        if enemigo.vida <= 0:
            break

        # Turno del enemigo
        enemigo.atacar(jugador)

    print("\n¡Combate terminado!")
    if jugador.vida > 0:
        print(f"¡{jugador.nombre} gana!")
    else:
        print(f"¡{enemigo.nombre} gana!")


# Creacion de los personajes
jugador = Personaje("Héroe", 100, 20)
enemigo = Personaje("Orco", 80, 15)

# Iniciar combate
combate(jugador, enemigo)