class Persona:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def presentarse(self):
        return f"Hola, mi nombre es {self.nombre} y mi email es {self.email}."


class Curso:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def info_curso(self):
        return f"{self.codigo}: {self.nombre}"


class Estudiante(Persona):
    def __init__(self, nombre, email, matricula):
        super().__init__(nombre, email)
        self.matricula = matricula
        self.cursos = []

    def agregar_curso(self, curso):
        self.cursos.append(curso)

    def listar_cursos(self):
        return [curso.info_curso() for curso in self.cursos]


if __name__ == "__main__":
    estudiante = Estudiante("Fernando Hernandez", "fernando@gmail.com", "1151KVT")
    curso1 = Curso("Matemáticas", "MAT101")
    curso2 = Curso("Programación", "PROG202")

    estudiante.agregar_curso(curso1)
    estudiante.agregar_curso(curso2)

    print(estudiante.presentarse())
    print("Cursos inscritos:")
    for curso in estudiante.listar_cursos():
        print("-", curso)
