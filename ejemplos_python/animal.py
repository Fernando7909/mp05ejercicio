class Animal:
    """
    Aquesta classe representa un animal.
    """
    def __init__(self, nom, especie, so, edad):
        """
        Constructor de la classe Animal.

        Args:
            nom: El nom de l'animal.
            especie: L'espècie de l'animal.
            so: El so que fa l'animal.
            edad: L'edat de l'animal.
        """
        self.nom = nom
        self.especie = especie
        self.so = so
        self.edad = edad

    def fer_so(self):
        """
        Fa que l'animal emeti el seu so característic.
        """
        return f"El {self.especie} {self.nom} fa {self.so} i té {self.edad} anys."

    def presentarse(self):
        """
        Presenta l'animal.
        """
        return f"Hola, sóc {self.nom} i sóc un {self.especie}."

    def modificar_edad(self, nueva_edad):
        """
        Modifica l'edat de l'animal si és més gran de 15 anys.

        Args:
            nueva_edad: La nova edat que se li vol assignar.
        """
        if self.edad > 15:
            self.nueva_edad = self.edad - 5
            return f"La nova edat del {self.nom} és {self.edad}."
        else:
            return f"{self.nom} tiene {self.edad} anys,no se ha modificado."

# Exemple d'ús
gat = Animal("Michi", "gat", "miau", 18)
gos = Animal("Max", "gos", "guau", 20)
vaca = Animal("Mu", "vaca", "muuu", 7)
pajaro = Animal("Pepe", "gorrio", "pio", 5)

print(gat.fer_so())  # Imprimeix "El gat Michi fa miau"
print(gos.fer_so())  # Imprimeix "El gos Max fa guau"
print(vaca.fer_so())  # Imprimeix "La vaca Mu fa muuu"
print(pajaro.fer_so())  # Imprimeix "El gorrio Pepe fa pio"

print(gat.presentarse())
print(gos.presentarse())
print(vaca.presentarse())
print(pajaro.presentarse())

# Exemple de modificació de l'edat
print(gat.modificar_edad())  # Canvia l'edat
print(vaca.modificar_edad())  # No canvia l'edat
