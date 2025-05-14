import random


class GeneradorMazmorras:
    def __init__(self, ancho=20, alto=20, densidad_paredes=0.4):
        self.ancho = ancho
        self.alto = alto
        self.densidad_paredes = densidad_paredes
        self.mapa = []
        self.posicion_jugador = (0, 0)

    def generar_mapa(self):
        """Genera un mapa aleatorio básico con paredes y espacios vacíos"""
        # Crear mapa vacío con bordes de paredes
        self.mapa = [['#' if x == 0 or y == 0 or x == self.ancho - 1 or y == self.alto - 1
                      else '.' for x in range(self.ancho)] for y in range(self.alto)]

        # Añadir paredes aleatorias
        for y in range(1, self.alto - 1):
            for x in range(1, self.ancho - 1):
                if random.random() < self.densidad_paredes:
                    self.mapa[y][x] = '#'

        # Colocar al jugador en posición aleatoria vacía
        self.colocar_jugador()

    def colocar_jugador(self):
        """Coloca al jugador en una celda vacía aleatoria"""
        celdas_vacias = [(x, y) for y in range(1, self.alto - 1)
                         for x in range(1, self.ancho - 1) if self.mapa[y][x] == '.']

        if celdas_vacias:
            x, y = random.choice(celdas_vacias)
            self.posicion_jugador = (x, y)
            self.mapa[y][x] = 'P'

    def imprimir_mapa(self):
        """Muestra el mapa en la consola"""
        for fila in self.mapa:
            print(' '.join(fila))


def main():
    # Crear y generar mapa
    generador = GeneradorMazmorras(ancho=15, alto=15, densidad_paredes=0.3)
    generador.generar_mapa()

    # Mostrar resultados
    generador.imprimir_mapa()
    print(f"\nPosición del jugador: {generador.posicion_jugador}")


if __name__ == "__main__":
    main()