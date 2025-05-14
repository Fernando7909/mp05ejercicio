import os

# Tamaño del mapa
ANCHO = 15
ALTO = 15

# Mapa inicial
mapa = [['.' for _ in range(ANCHO)] for _ in range(ALTO)]

# Posición inicial del personaje
posicion_personaje = [ALTO // 2, ANCHO // 2]


# Función para mostrar el mapa
def mostrar_mapa():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la consola (Windows o Unix)
    for y in range(ALTO):
        for x in range(ANCHO):
            if [y, x] == posicion_personaje:
                print('P', end=' ')  # Imprimir al personaje en su posición
            else:
                print(mapa[y][x], end=' ')  # Imprimir el suelo
        print()


# Función para mover al personaje con las teclas
def mover_personaje(tecla):
    if tecla == 'w' and posicion_personaje[0] > 0:  # Mover arriba
        posicion_personaje[0] -= 1
    elif tecla == 's' and posicion_personaje[0] < ALTO - 1:  # Mover abajo
        posicion_personaje[0] += 1
    elif tecla == 'a' and posicion_personaje[1] > 0:  # Mover izquierda
        posicion_personaje[1] -= 1
    elif tecla == 'd' and posicion_personaje[1] < ANCHO - 1:  # Mover derecha
        posicion_personaje[1] += 1


# Función principal que ejecuta el juego
def main():
    while True:
        mostrar_mapa()
        movimiento = input("Usa WASD para mover el personaje (q para salir): ").lower()

        if movimiento == 'q':  # Salir del juego
            print("¡Saliendo del juego!")
            break

        if movimiento in ['w', 'a', 's', 'd']:
            mover_personaje(movimiento)
        else:
            print("Tecla no válida, usa W, A, S o D para mover o Q para salir.")


if __name__ == "__main__":
    main()
