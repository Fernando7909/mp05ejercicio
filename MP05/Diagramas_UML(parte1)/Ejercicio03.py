class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.encendido = False

    def arrancar(self):
        if not self.encendido:
            self.encendido = True
            print(f"{self.marca} {self.modelo} ha sido encendido")
        else:
            print(f"{self.marca} {self.modelo} ya estaba encendido")

    def detener(self):
        if self.encendido:
            self.encendido = False
            print(f"{self.marca} {self.modelo} ha sido apagado")
        else:
            print(f"{self.marca} {self.modelo} ya estaba apagado")

    def mostrar_info(self):
        estado = "Encendido" if self.encendido else "Apagado"
        print(f"\nInformación del vehículo:")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Estado: {estado}")


class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        super().__init__(marca, modelo, año)
        self.puertas = puertas

    def abrir_maletero(self):
        print(f"Maletero del {self.marca} {self.modelo} abierto")

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Puertas: {self.puertas}")
        print("Tipo: Coche")


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, cilindrada):
        super().__init__(marca, modelo, año)
        self.cilindrada = cilindrada

    def hacer_caballito(self):
        if self.encendido:
            print(f"¡{self.marca} {self.modelo} está haciendo un caballito!")
        else:
            print("No se puede hacer caballito con la moto apagada")

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Cilindrada: {self.cilindrada}cc")
        print("Tipo: Motocicleta")



if __name__ == "__main__":
    print("--- Ejemplo de Herencia de Vehículos ---")


    mi_coche = Coche("Toyota", "Corolla", 2022, 4)
    mi_moto = Motocicleta("Honda", "CBR600", 2021, 600)


    print("\n--- coche ---")
    mi_coche.mostrar_info()
    mi_coche.arrancar()
    mi_coche.abrir_maletero()
    mi_coche.detener()


    print("\n--- motocicleta ---")
    mi_moto.mostrar_info()
    mi_moto.arrancar()
    mi_moto.hacer_caballito()
    mi_moto.detener()
    mi_moto.hacer_caballito()