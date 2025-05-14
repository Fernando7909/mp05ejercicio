# En este juego vamos a empezar definiendo las clases que se explican en el enunciado
# Clase Preguntta con los atributos correcpondientes

class Pregunta:
# metodo constructor
    def __init__(self, pregunta, opciones, respuesta_correcta):
        self.pregunta = pregunta
        self.opciones = opciones
        self.respuesta_correcta = respuesta_correcta

# Clase JuegoTrivial donde definimos las preguntas con las opcoines de respuesta y la respuesta correcta

class Juego_Trivial:
    def __init__(self):
        self.puntuacion =0
        self.preguntas =[
            Pregunta("¿Cual de estas es una marca española de coches?",
                     ["Seat", "Mazda", "Ferrari", "Peugeot"],
                     "Seat"),

            Pregunta("¿Quien fue el creador de Ferrari?",
                     ["PAco", "Picasso", "Enzo", "Antonio"],
                     "Enzo"),

            Pregunta("¿Qué tipo de coche es mas apropiado para ir por la montaña?",
                     ["Berlina", "Todoterreno", "deportivo", "suv"],
                     "Todoterreno")
        ]


# Aqui definimos la funcion iniciar_juego donde creamos a logica para que el usuario, en funcion de su respuesta
# sume puntos o no

    def iniciar_juego (self):
        print(" Juego de preguntas: TRIVIAL ")
        print("Responde con el número de la opción correcta\n")

        for pregunta in self.preguntas:
            print(pregunta.pregunta)
            for i, opcion in enumerate(pregunta.opciones,  1):
                print(f"{i}. {opcion}")

            respuesta = input("\nRespuesta: ")

            if pregunta.opciones[int(respuesta) - 1] == pregunta.respuesta_correcta:
                print("Correcto!!!!")
                self.puntuacion +=1
            else:
                print(f"Incorrecto. La respuesta correcta es: {pregunta.respuesta_correcta}")

            print(f"Puntuación: {self.puntuacion} \n")

        print(" FIN DEL JUEGO ")
        print(f"Puntuación final: {self.puntuacion} ")


# Inicio del juego
juego = Juego_Trivial()
juego.iniciar_juego()