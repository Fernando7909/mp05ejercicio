class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

class Coche(Vehiculo):
    def __init__(self, marca, modelo, motor: Motor):
        super().__init__(marca)
        self.modelo = modelo
        self.motor = motor

class Camion(Vehiculo):
    def __init__(self, marca, carga):
        super().__init__(marca)
        self.carga = carga



if __name__ == "__main__":
    motor_gasolina = Motor("Gasolina")
    mi_coche = Coche("Toyota", "Corolla", motor_gasolina)
    mi_camion = Camion("Volvo", 12.5)

    print("🚗 Coche:")
    print(f"Marca: {mi_coche.marca}")
    print(f"Modelo: {mi_coche.modelo}")
    print(f"Motor: {mi_coche.motor.tipo}")

    print("\nCamion:")
    print(f"Marca: {mi_camion.marca}")
    print(f"Capacidad de carga: {mi_camion.carga} toneladas")
