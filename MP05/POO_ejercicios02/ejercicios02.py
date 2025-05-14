import random


# Función para generar un mapa aleatorio
def generar_mapa(filas, columnas):
    mapa = []

    # Creamos un mapa vacío con suelo (.)
    for i in range(filas):
        fila = []
        for j in range(columnas):
            if random.random() < 0.2:  # 20% de probabilidad de poner una pared (#)
                fila.append('#')
            else:
                fila.append('.')
        mapa.append(fila)

    # Colocar el personaje (P) en una posición aleatoria
    personaje_colocado = False
    while not personaje_colocado:
        fila_personaje = random.randint(0, filas - 1)
        col_personaje = random.randint(0, columnas - 1)

        # Asegurarse de que el personaje no se coloque en una pared
        if mapa[fila_personaje][col_personaje] == '.':
            mapa[fila_personaje][col_personaje] = 'P'
            personaje_colocado = True

    return mapa


# Función para mostrar el mapa en pantalla
def mostrar_mapa(mapa):
    for fila in mapa:
        print(" ".join(fila))


# Tamaño del mapa
filas = 10
columnas = 10


# Generar y mostrar el mapa
mapa = generar_mapa(filas, columnas)
mostrar_mapa(mapa)
