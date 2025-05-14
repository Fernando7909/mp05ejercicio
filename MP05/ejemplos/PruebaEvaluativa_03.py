class Cola_LIFO:
    def __init__(self):
        self.pila = []

    def afegir(self, element):
        self.pila.append(element)

    def extreure(self):
        if self.buit():
            raise IndexError("No se puede extraer, la pila está vacía.")
        return self.pila.pop()

    def veure_darrer(self):
        if self.buit():
            raise IndexError("No hay ningún elemento para ver, la pila está vacía.")
        return self.pila[-1]

    def buit(self):
        return len(self.pila) == 0

    def longitud(self):
        return len(self.pila)

pila = Cola_LIFO()
pila.afegir("A")
pila.afegir("B")
pila.afegir("C")

print(pila.veure_darrer()) 
print(pila.extreure())
print(pila.veure_darrer())
print(pila.longitud())
print(pila.buit())
pila.extreure()
pila.extreure()
print(pila.buit())