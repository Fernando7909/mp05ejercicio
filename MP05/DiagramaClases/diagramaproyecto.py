# En la clase proyecto, asi como en las clases restantes utilizamos el metodo __init__
# Este metodo es el constructor de las clases
# Dentro de cada clase tenemos los atributos correspondientes y los metodos
class Projecte:
    def __init__(self, nom, duracio, llenguatge):
        self.nom = nom
        self.duracio = duracio
        self.llenguatge = llenguatge

    def mostrar_informacio(self):
        return f"Projecte: {self.nom}, Duració: {self.duracio} mesos, Llenguatge: {self.llenguatge}"


# Las clases Proyecto interno y externo, heredan de "Proyecto"
class ProjecteIntern(Projecte):
    def __init__(self, nom, duracio, llenguatge, responsable, departament):
        super().__init__(nom, duracio, llenguatge)
        self.responsable = responsable
        self.departament = departament
        self.tasques = []  # Lista para almacenar tareas

    def mostrar_informacio(self):
        info_base = super().mostrar_informacio()
        return f"{info_base}, Responsable: {self.responsable}, Departament: {self.departament}"

    def afegir_tasca(self, tasca):
        self.tasques.append(tasca)

    def mostrar_tasques(self):
        return "\n".join([tasca.mostrar_informacio() for tasca in self.tasques])


class ProjecteExtern(Projecte):
    def __init__(self, nom, duracio, llenguatge, client, pressupost):
        super().__init__(nom, duracio, llenguatge)
        self.client = client
        self.pressupost = pressupost

    def mostrar_informacio(self):
        info_base = super().mostrar_informacio()
        return f"{info_base}, Client: {self.client}, Pressupost: {self.pressupost}K€"


class Membre:
    def __init__(self, nom, rol, experiencia):
        self.nom = nom
        self.rol = rol
        self.experiencia = experiencia

    def mostrar_informacio(self):
        return f"Membre: {self.nom}, Rol: {self.rol}, Experiència: {self.experiencia} anys"


class Equip:
    def __init__(self, nom):
        self.nom = nom
        self.membres = []

    def afegir_membre(self, membre):
        self.membres.append(membre)

    def mostrar_informacio(self):
        return f"Equip: {self.nom}, Membres: {len(self.membres)}"

    def mostrar_membres(self):
        return "\n".join([m.mostrar_informacio() for m in self.membres])



# Clase tasca con los correspondientes atributos y la funcion mostrar_informacio
class Tasca:
    def __init__(self, titol, estat, responsable):
        self.titol = titol
        self.estat = estat
        self.responsable = responsable

    def mostrar_informacio(self):
        return f"Tasca: {self.titol}, Estat: {self.estat}, Responsable: {self.responsable.nom}"


if __name__ == "__main__":
    # Crear un projecte intern
    projecte_intern = ProjecteIntern("Aplicació CRM Interna", 12, "Python", "Joan Rovira", "IT")

    # Crear un projecte extern
    projecte_extern = ProjecteExtern("Plataforma E-learning", 18, "Java", "Educorp", 300)

    # Crear un equip i membres
    equip = Equip("Equip Desenvolupament")
    membre1 = Membre("Anna", "Desenvolupadora", 3)
    membre2 = Membre("Marc", "Tester", 2)
    equip.afegir_membre(membre1)
    equip.afegir_membre(membre2)

    # Crear i afegir tasques al projecte intern
    tasca1 = Tasca("Definir requeriments", "pendent", membre1)
    tasca2 = Tasca("Provar funcionalitats", "pendent", membre2)
    projecte_intern.afegir_tasca(tasca1)
    projecte_intern.afegir_tasca(tasca2)

    # Mostrar informació del projecte intern
    print("\nInformació del projecte intern:")
    print(projecte_intern.mostrar_informacio())

    print("\nTasques del projecte intern:")
    print(projecte_intern.mostrar_tasques())

    # Mostrar informació de l'equip
    print("\nInformació de l'equip:")
    print(equip.mostrar_informacio())
    print(equip.mostrar_membres())

    # Mostrar informació del projecte extern
    print("\nInformació del projecte extern:")
    print(projecte_extern.mostrar_informacio())