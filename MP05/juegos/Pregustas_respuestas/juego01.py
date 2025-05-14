from datetime import datetime

# Empezamos definiendo la Clase Vehiculo en el codigo con sus respectivos atributoas
class Vehiculo:
    def __init__(self, matricula, marca, modelo, año_fabricacion, km):
        self._matricula = matricula
        self._marca = marca
        self._modelo = modelo
        self._año_fabricacion = año_fabricacion
        self._km = km

    def detalles_vehiculo(self):
        return (f"Matrícula: {self._matricula}, Marca: {self._marca}, Modelo: {self._modelo}, "
                f"Año: {self._año_fabricacion}, Km: {self._km} km")


# Defnimos la clase coche con sus respectivos atributos
class Coche(Vehiculo):
    def __init__(self, matricula, marca, modelo, año_fabricacion, km, num_puertas):
        super().__init__(matricula, marca, modelo, año_fabricacion, km)
        self._num_puertas = num_puertas

    def detalles_vehiculo(self):
        return f"Coche - {super().detalles_vehiculo()}, Puertas: {self._num_puertas}"



# Clase Moto
class Moto(Vehiculo):
    def __init__(self, matricula, marca, modelo, año_fabricacion, km, tipo):
        super().__init__(matricula, marca, modelo, año_fabricacion, km)
        self._tipo = tipo

    def detalles_vehiculo(self):
        return f"Moto - {super().detalles_vehiculo()}, Tipo: {self._tipo}"


# Clase Camión
class Camion(Vehiculo):
    def __init__(self, matricula, marca, modelo, año_fabricacion, km, capacidad_carga):
        super().__init__(matricula, marca, modelo, año_fabricacion, km)
        self._capacidad_carga = capacidad_carga

    def detalles_vehiculo(self):
        return f"Camión - {super().detalles_vehiculo()}, Capacidad de carga: {self._capacidad_carga} kg"





# Clase Taller, similar a un CRUD
class Taller:
    def  __init__(self):
        self._vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self._vehiculos.append(vehiculo)
        print(f"Vehículo con matrícula {vehiculo._matricula} agregado correctamente.")

    def mostrar_vehiculo(self, matricula):
        for vehiculo in self._vehiculos:
            if vehiculo._matricula == matricula:
                print(vehiculo.detalles_vehiculo())
                return
        print(f"No hay vehículos con matrícula{matricula}.")

    def mostrar_todos_vehiculos(self):
        if not self._vehiculos:
            print("No hay vehículos registrados.")
        else:
            for vehiculo in self._vehiculos:
                print(vehiculo.detalles_vehiculo())

    def actualizar_km(self, matricula, nuevos_kilometros):
        for vehiculo in self._vehiculos:
            if vehiculo._matricula == matricula:
                vehiculo._km = nuevos_kilometros
                print(f"Km actualizado para el vehículo {matricula}.")
                return
        print(f"No hay vehículos con matrícula {matricula}.")

    def eliminar_vehiculo(self, matricula):
        for vehiculo  in self._vehiculos:
            if vehiculo._matricula == matricula:
                self._vehiculos.remove(vehiculo)
                print(f"Vehículo con la matrícula {matricula} eliminado.")
                return
        print(f"No existen vehñiculos con la matrícula {matricula}.")

    def listar_vehiculos_por_año(self, año):
        encontrados = [v for v in self._vehiculos  if v._año_fabricacion < año]
        if not encontrados:
            print(f"No hay vehículos fabricados antes del año {año}.")
        else:
            for vehiculo in encontrados:
                print(vehiculo.detalles_vehiculo())

    def promedio_antiguedad(self):
        if not self._vehiculos:
            print("No hay vehículos para calcular la edad promedio.")
            return 0
        año_actual = datetime.now().year
        edades =  [año_actual - v._año_fabricacion for v in self._vehiculos]
        promedio = sum(edades) / len(edades)
        print(f"La edad promedio de los vehículos es {promedio:.2f} años.")
        return promedio

    def promocion_mantenimiento(self, tipo_vehiculo):
        tipos_clases = {"coche": Coche, "moto": Moto, "camion": Camion}
        if tipo_vehiculo not in tipos_clases:
            print("Tipo de vehículo no válido.")
            return

        año_actual =datetime.now().year
        elegibles = []

        # Determinar los vehículos según el tipo y los años
        for vehiculo in self._vehiculos:
            if isinstance(vehiculo, tipos_clases[tipo_vehiculo]):
                edad = año_actual - vehiculo._año_fabricacion
                descuento = 0


                if tipo_vehiculo == "coche" and edad >= 25:
                    descuento = 25
                elif tipo_vehiculo == "moto" and edad >= 20:
                    descuento = 20
                elif tipo_vehiculo == "camion" and edad >= 15:
                    descuento = 15

                if descuento > 0:
                    elegibles.append((vehiculo, descuento))

        # Mostrar los resultados
        if not elegibles:
            print(f"No hay {tipo_vehiculo}s elegibles para la promoción.")
        else:
            print(f"Vehículos {tipo_vehiculo}s elegibles para la promoción de mantenimiento:")
            for vehiculo, descuento in elegibles:
                print(f"{vehiculo.detalles_vehiculo()} - Descuento aplicadod del: {descuento}%")


# Función para agregar un vehículo en el programaa
def agregar_vehiculo(taller):
    tipo = input("Introduce el tipo de vehículo (coche, moto, camion): ").lower()
    matricula = input("Introduce la matrícula: ")
    marca = input("Introduce la marca: ")
    modelo = input("Introduce el modelo: ")
    año_fabricacion = int(input("Introduce el año de fabricación: "))
    km = int(input("Introduce el km: "))

    if tipo == "coche":
        num_puertas = int(input("Introduce el número de puertas: "))
        vehiculo = Coche(matricula, marca, modelo, año_fabricacion, km, num_puertas)
    elif tipo == "moto":
        tipo_moto = input("Introduce el tipo de moto (ej. scooter, custom, trail): ")
        vehiculo = Moto(matricula, marca, modelo, año_fabricacion, km, tipo_moto)
    elif tipo == "camion":
        capacidad_carga =int(input("Introduce la capacidad de carga (kg): "))
        vehiculo =Camion(matricula, marca, modelo, año_fabricacion, km, capacidad_carga)

    else:
        print("El Tipo de vehículo no es válido.")
        return

    taller.agregar_vehiculo(vehiculo)

def menu_taller():
    taller = Taller()
    while True:
        print("\n--- Menú del Taller Mecánico ---")
        print("1. Agregar vehículo")
        print("2. Mostrar información de un vehículo")
        print("3. Mostrar todos los vehículos")
        print("4. Actualizar km de un vehículo")
        print("5. Eliminar un vehículo")
        print("6. Listar vehículos por año")
        print("7. Calcular la edad promedio de los vehículos")
        print("8. Aplicar la promoción de mantenimiento")
        print("9. Salir")

        opcion = input("Selecciona una opción (1-9): ")

        if opcion == "1":
            agregar_vehiculo(taller)

        elif opcion == "2":
            matricula = input("Introduce la matrícula del vehículo: ")
            taller.mostrar_vehiculo(matricula)

        elif opcion == "3":
            taller.mostrar_todos_vehiculos()

        elif opcion == "4":
            matricula = input("Introduce la matrícula del vehículo: ")
            nuevos_kilometros = int(input("Introduce el nuevo km: "))
            taller.actualizar_km(matricula, nuevos_kilometros)

        elif opcion == "5":
            matricula = input("Introduce la matrícula del vehículo a eliminar: ")
            taller.eliminar_vehiculo(matricula)

        elif opcion == "6":
            año = int(input("Introduce el año para filtrar: "))
            taller.listar_vehiculos_por_año(año)

        elif opcion == "7":
            taller.promedio_antiguedad()
        elif opcion == "8":
            tipo = input("Introduce el tipo de vehículo (coche, moto, camion): ").lower()
            taller.promocion_mantenimiento(tipo)

        elif opcion == "9":
            print("¡Saliendo del programa. Gracias!")
            break

        else:
            print("ERROR!!, intentalo de nuevo.")


# Ejecutamos el programa indefinidamdente hasta que seleccionemos la opción de salir en el menu
if __name__ == "__main__":
    menu_taller()