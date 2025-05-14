class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hablar(self, mensaje):
        print(f"{self.nombre} dice: {mensaje}")

    def caminar(self, distancia):
        print(f"{self.nombre} está caminando {distancia} metros")

class Estudiante(Persona):
    def __init__(self, nombre, edad, matricula):
        super().__init__(nombre, edad)
        self.matricula = matricula

    def estudiar(self, materia):
        print(f"{self.nombre} con matrícula {self.matricula} está estudiando {materia}")




if __name__ == "__main__":
    persona1 = Persona("Juan", 30)
    persona1.hablar("Hola, ¿cómo estás?")
    persona1.caminar(50)

    print("\n")


    estudiante1 = Estudiante("María", 22, "1151KVT")
    estudiante1.hablar("Hola, voy a estudiar")
    estudiante1.caminar(20)
    estudiante1.estudiar("Matemáticas")