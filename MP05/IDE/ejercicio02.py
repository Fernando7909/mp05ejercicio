from datetime import date, time

class Sala:
    def __init__(self, nombre: str, capacidad: int):
        self.nombre = nombre
        self.capacidad = capacidad

    def info_sala(self):
        return f"Sala: {self.nombre}, Capacidad: {self.capacidad}"


class Usuario:
    def __init__(self, nombre: str, correo: str):
        self.nombre = nombre
        self.correo = correo
        self.reservas = []

    def reservar(self, sala, fecha: date, hora_inicio: time, hora_fin: time):
        nueva_reserva = Reserva(fecha, hora_inicio, hora_fin, sala, self)
        self.reservas.append(nueva_reserva)
        return nueva_reserva

    def listar_reservas(self):
        return [r.detalle() for r in self.reservas]


class Reserva:
    def __init__(self, fecha: date, hora_inicio: time, hora_fin: time, sala: Sala, usuario: Usuario):
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.sala = sala
        self.usuario = usuario

    def detalle(self):
        return (f"Reserva de {self.usuario.nombre} en sala {self.sala.nombre} "
                f"el {self.fecha} de {self.hora_inicio} a {self.hora_fin}")


if __name__ == "__main__":
    sala1 = Sala("Aula 100", 30)
    usuario1 = Usuario("Fernando Hdez", "fernando@example.com")

    reserva1 = usuario1.reservar(
        sala=sala1,
        fecha=date(2025, 5, 15),
        hora_inicio=time(10, 0),
        hora_fin=time(12, 0)
    )

    print("Reserva creada:")
    for detalle in usuario1.listar_reservas():
        print("-", detalle)
