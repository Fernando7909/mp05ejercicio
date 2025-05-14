class Llibre:
    def __init__(self, titol, autor, any_publicacio):
        self.titol = titol
        self.autor = autor
        self.any_publicacio = any_publicacio
        self.estat = "disponible"  # l'estat pot ser 'disponible' o 'prestat'



class Membre:
    def __init__(self, nom, id_membre):
        self.nom = nom
        self.id_membre = id_membre
        self.llibres_prestats = []  # Una llista per als llibres prestats
        self.historial_prestecs = []  # Una llista per a l'historial de préstecs



class Biblioteca:
    def __init__(self, nom, adreca):
        self.nom = nom
        self.adreca = adreca
        self.llibres = []  # Llista per a tots els llibres de la biblioteca
        self.membres = []  # Llista per a tots els membres registrats

    def afegir_llibre(self, llibre):
        self.llibres.append(llibre)

    def afegir_membre(self, membre):
        self.membres.append(membre)


llibre1=Llibre('Don Quijote de la Mancha', 'Cervantes', '1492')
membre1=Membre('Pepe', '11111')

biblioteca1=Biblioteca('Biblioteca Prat', 'Roger de Llurio 28')
biblioteca1.afegir_membre(membre1)
biblioteca1.afegir_llibre(llibre1)


