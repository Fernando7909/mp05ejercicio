"""Creamos un diccionario con diferentes nombres donde se muestra
el producto, la cantidad y su precio en €"""

comandas = {
    "Alex": [("Libro", 2, 10.0), ("Bolígrafo", 5, 1.5)],
    "Juan": [("Carpeta", 3, 4.5)],
    "Erika": [("Ordenador", 1, 800.0), ("Ratón", 2, 20.0)],
    "Pau": [("Camiseta", 2, 15.99), ("Pantalones", 1, 39.99)],
    "Margarida": [("Zapatos", 1, 59.95), ("Bolso", 1, 89.99)],
    "Jairon": [("Libro", 3, 12.50), ("Revista", 2, 4.99)]
}

"""En esta parte del codigo creamos las funciones que calculan el precio total de la comanda,
los clientes que han tenido un gasto superior a 100€ y la función que imprimelas comandas
de cada clkiente"""
def calcular_total_comanda(comandas, cliente):
    total = 0
    for producto, cantidad, precio in comandas[cliente]:
        total += cantidad * precio
    return total

def clientes_con_gasto_mayor_a_100(comandas):
    clientes_grandes_gastadores = []
    for cliente, compras in comandas.items():
        total = calcular_total_comanda(comandas, cliente)
        if total > 100:
            clientes_grandes_gastadores.append(cliente)
    return clientes_grandes_gastadores

def imprimir_comandas_cliente(comandas, cliente):
    if cliente in comandas:
        print(f"\nComandas de {cliente}:")
        for producto, cantidad, precio in comandas[cliente]:
            print(f"- {cantidad} {producto} a {precio} €")
    else:
        print(f"No se encontraron compras para {cliente}.")


"""En esta funcion del menu() se ejecuta el programa donde a través de la seleccion
de uno de los 4 menus, el programa te reporta la informacion, en función de lo que le solicites"""
def menu():
    while True:
        print("\nMenú:")
        print("1. Calcular el costo total de cada cliente.")
        print("2. Listado de clientes con gastos superiores a 100 euros.")
        print("3. Ver las compras de un cliente concreto.")
        print("4. Salir del programa.")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            for cliente, compras in comandas.items():
                total = calcular_total_comanda(comandas, cliente)
                print(f"El costo total de las compras de {cliente} es: {total:.2f} €")

        elif opcion == '2':
            grandes_gastadores = clientes_con_gasto_mayor_a_100(comandas)
            print("\nClientes con gastos superiores a 100 €:")
            if grandes_gastadores:
                for cliente in grandes_gastadores:
                    total = calcular_total_comanda(comandas, cliente)
                    print(f"{cliente}: {total:.2f} euros")  # .2f se utiliza para que muestre 2 decimales como máximo
            else:
                print("No hay clientes con gastos superiores a 100 €.")

        elif opcion == '3':
            cliente = input("Introduce el nombre del cliente: ").capitalize()
            imprimir_comandas_cliente(comandas, cliente)    # Aqui estamos llamando a la funcion de imprimir la comanda de cada cliente

        elif opcion == '4':
            print("Hasta la próxima!!!")
            break                                           # Añadiendo un break, forzamos al programa a salir del bucle

        else:
            print("ERROR!. Selecciona una de las 4 opciones.")

# Ejecutar el menú
menu()
