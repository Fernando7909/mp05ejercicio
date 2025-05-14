
biblioteca = {
    1: {"titulo": "El Señor de los Anillos", "autor": "JRR Tolkien", "cantidad": 3},
    2: {"titulo": "Datos y Estructuras", "autor": "Anna Smith", "cantidad": 5},
    3: {"titulo": "Introducción a OOP", "autor": "Joan Costa", "cantidad": 2},
}


def agregar_libro():
    """Agregar un nuevo libro a la biblioteca."""
    try:
        id_libro = int(input("Introduce el ID del libro: "))
        titulo = input("Introduce el título del libro: ")
        autor = input("Introduce el autor del libro: ")
        cantidad = int(input("Introduce la cantidad de ejemplares disponibles: "))

        biblioteca[id_libro] = {"titulo": titulo, "autor": autor, "cantidad": cantidad}
        print(f"Libro '{titulo}' agregado con éxito.")
    except ValueError:
        print("Se ha producido un error con los datos introducidos. Asegúrate de que la cantidad y el ID sean números.")


def buscar_libro():
    """Buscar un libro por ID y mostrar su información."""
    try:
        id_libro = int(input("Introduce el ID del libro a buscar: "))
        if id_libro in biblioteca:
            libro = biblioteca[id_libro]
            print(f"Título: {libro['titulo']}\nAutor: {libro['autor']}\nCantidad: {libro['cantidad']}")
        else:
            print("Libro no encontrado.")
    except ValueError:
        print("Introduce un ID válido.")


def mostrar_libros():
    """Mostrar la información de todos los libros disponibles de manera ordenada por ID."""
    if biblioteca:
        for id_libro, info in sorted(biblioteca.items()):
            print(f"ID: {id_libro} - Título: {info['titulo']} - Autor: {info['autor']} - Cantidad: {info['cantidad']}")
    else:
        print("No hay libros en la biblioteca.")


def prestamo_libro():
    """Gestión del préstamo de un libro."""
    try:
        id_libro = int(input("Introduce el ID del libro que quieres tomar en préstamo: "))
        if id_libro in biblioteca:
            if biblioteca[id_libro]["cantidad"] > 0:
                biblioteca[id_libro]["cantidad"] -= 1
                print(f"Préstamo realizado con éxito del libro '{biblioteca[id_libro]['titulo']}'.")
            else:
                print("No hay libros disponibles para este préstamo.")
        else:
            print("Libro no encontrado.")
    except ValueError:
        print("Introduce un ID válido.")


def menu():
    while True:
        print("\nMenú:")
        print("1. Agregar un nuevo libro")
        print("2. Buscar un libro")
        print("3. Mostrar todos los libros")
        print("4. Préstamo de un libro")
        print("5. Salir")

        opcion = input("Selecciona una opción (1-5): ")

        if opcion == '1':
            agregar_libro()
        elif opcion == '2':
            buscar_libro()
        elif opcion == '3':
            mostrar_libros()
        elif opcion == '4':
            prestamo_libro()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")


# Iniciar el menú
menu()
