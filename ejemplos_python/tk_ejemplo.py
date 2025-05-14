import tkinter as tk


def saludar():
    print("¡Hola, mundo!")

# Crear una ventana raíz
root = tk.Tk()
root.title("Mi Segunda Ventana")
root.geometry("400x200")

# Añadir una etiqueta
etiqueta = tk.Label(root, text="¡Bienvenido a Tkinter!")
etiqueta.pack()

# Añadir un botón
boton = tk.Button(root, text="Saludar¡", command=saludar)
boton.pack()

# Iniciar el bucle de eventos
root.mainloop()


