from typing import List, Optional

class Persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat

    def parlar(self):
        print(f"{self.nom} està parlant.")

class Estudiant(Persona):
    def __init__(self, nom, edat, estudi):
        super().__init__(nom, edat)
        self.estudi = estudi

    def estudiar(self):
        print(f"{self.nom} està estudiant {self.estudi}.")

class Grup:
    def __init__(self):
        self.estudiants = []

    def afegir_estudiant(self, estudiant):
        self.estudiants.append(estudiant)

    def llistar_estudiants(self):
        for estudiant in self.estudiants:
            print(estudiant.nom)

class Llibre:
    def __init__(self, titol: str, autor: str, any_publicacio: int, isbn: str):
        self.titol = titol
        self.autor = autor
        self.any_publicacio = any_publicacio
        self.isbn = isbn
        self.estat = "disponible"  # l'estat pot ser 'disponible' o 'prestat'

    def prestar(self):
        if self.estat == "disponible":
            self.estat = "prestat"
            return True
        else:
            return False

    def retornar_llibres(self):
        if self.estat == "prestat":
            self.estat = "disponible"
            return True
        else:
            return False

class Membre:
    def __init__(self, nom, id_membre):
        self.nom = nom
        self.id_membre = id_membre
        self.llibres_prestats = []  # Una llista per als llibres prestats
        self.historial_prestecs = []  # Una llista per a l'historial de préstecs

    def demanar_llibres(self, llibre):
        if len(self.llibres_prestats) < 5 and llibre.prestar():
            self.llibres_prestats.append(llibre)
            self.historial_prestecs.append(llibre)
            return True
        else:
            print(f"{self.nom} no pot demanar més llibres.")
            return False

    def retornar_llibres(self, llibre):
        if llibre in self.llibres_prestats and llibre.retornar_llibres():
            self.llibres_prestats.remove(llibre)
            return True
        else:
            print(f"{llibre.titol} no es troba entre els llibres prestats per {self.nom}.")
            return False

class Biblioteca:
    def __init__(self, nom: str, adreca: str):
        self.nom = nom
        self.adreca = adreca
        self.llibres: List[Llibre] = []
        self.membres: List[Membre] = []

    def afegir_llibre(self, llibre: Llibre):
        self.llibres.append(llibre)

    def eliminar_llibres(self, isbn: str):
        self.llibres = [llibre for llibre in self.llibres if llibre.isbn != isbn]

    def cercar_llibres(self, isbn: str) -> Optional[Llibre]:
        for llibre in self.llibres:
            if llibre.isbn == isbn:
                return llibre
        return None

    def registrar_préstec(self, membre: Membre, isbn: str):
        llibre = self.cercar_llibres(isbn)
        if llibre and membre.demanar_llibres(llibre):
            self.eliminar_llibres(isbn)

    def registrar_devolució(self, membre: Membre, isbn: str):
        llibre = next((l for l in membre.llibres_prestats if l.isbn == isbn), None)
        if llibre:
            self.afegir_llibre(llibre)
            membre.retornar_llibres(llibre)

    def afegir_membre(self, membre: Membre):
        self.membres.append(membre)

    def cercar_llibre(self, titol: str) -> Optional[Llibre]:
        for llibre in self.llibres:
            if llibre.titol.lower() == titol.lower():
                return llibre
        print("Llibre no trobat.")
        return None

    def prestar_llibre(self, membre: Membre, titol_llibre: str):
        llibre = self.cercar_llibre(titol_llibre)
        if llibre and membre.demanar_llibres(llibre):
            return True
        elif llibre:
            print(f"{llibre.titol} està actualment prestat.")
            return False
        return False

    def retornar_llibre(self, membre: Membre, titol_llibre: str):
        llibre = self.cercar_llibre(titol_llibre)
        if llibre and membre.retornar_llibres(llibre):
            return True
        return False

# Crear la biblioteca
biblioteca = Biblioteca("Biblioteca Central", "Carrer de les Lletres, 123")

# Crear alguns llibres i afegir-los a la biblioteca
llibre1 = Llibre("Programació en Python", "Autor A", 2020, "ISBN001")
llibre2 = Llibre("Essencials de Ciència de Dades", "Autor B", 2021, "ISBN002")
biblioteca.afegir_llibre(llibre1)
biblioteca.afegir_llibre(llibre2)

# Crear un membre i afegir-lo a la biblioteca
membre1 = Membre("Alícia", "M001")
biblioteca.afegir_membre(membre1)

# Demanar un llibre
biblioteca.prestar_llibre(membre1, "Programació en Python")

# Retornar el llibre
biblioteca.retornar_llibre(membre1, "Programació en Python")
