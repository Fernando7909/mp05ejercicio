class Coche:
    def __init__(self, marca, modelo, color):

        self.marca = marca
        self.modelo = modelo
        self.color = color

    def descripcion(self):

        return (f"Este coche es de la marca {self.marca}, del modelo {self.modelo} y de color {self.color}.")

mi_coche = Coche("seat", "ibiza", "rojo")

print(mi_coche.descripcion())