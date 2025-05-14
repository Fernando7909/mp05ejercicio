class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

    def encender(self):
        print(f"Motor {self.tipo} de {self.potencia} Caballos (HP) encendido")


class Coche:
    def __init__(self, marca, modelo, año, tipo_motor, potencia_motor):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.motor = Motor(tipo_motor, potencia_motor)

    def arrancar(self):
        print(f"{self.marca} {self.modelo} ({self.año}) arrancando...")
        self.motor.encender()

    def detener(self):
        print(f"{self.marca} {self.modelo} ({self.año}) detenido")



if __name__ == "__main__":
    mi_coche = Coche("Toyota", "Corolla", 2022, "4 cilindros", 180)

    mi_coche.arrancar()
    mi_coche.detener()

    print(f"\nDetalles del coche:")
    print(f"Marca: {mi_coche.marca}")
    print(f"Modelo: {mi_coche.modelo}")
    print(f"Año: {mi_coche.año}")
    print(f"Tipo de motor: {mi_coche.motor.tipo}")
    print(f"Potencia: {mi_coche.motor.potencia} HP")