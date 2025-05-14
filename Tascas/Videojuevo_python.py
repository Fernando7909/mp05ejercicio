import tkinter as tk
from PIL import Image, ImageTk
import random

# Inicializa el número aleatorio y el contador de intentos
numero_aleatorio = random.randint(1, 100)
intentos = 10

# Función que verifica el número introducido por el usuario en pantalla
# He añadido una funcionalidad adicional en la que si tu numero esta a 5 cifras por encima o por debajo, te visa de que estas cerca deadivinarlo
def verificar_numero():
    global intentos
    try:
        numero_introducido = int(entry.get())

        if intentos > 1:
            if numero_introducido > 100 or numero_introducido < 1:
                resultado.set(f"El número que has introducido, esta fuera del rango. Te quedan {intentos - 1} intentos.")

            elif numero_introducido > numero_aleatorio:
                if numero_introducido <= numero_aleatorio + 5:
                    resultado.set(
                        f"El número es demasiado alto, pero estás muy cerca de adivinarlo. Te quedan {intentos - 1} intentos.")
                else:
                    resultado.set(f"Demasiado alto. Te quedan {intentos - 1} intentos.")

            elif numero_introducido < numero_aleatorio:
                if numero_introducido >= numero_aleatorio - 5:
                    resultado.set(
                        f"El número es demasiado bajo, pero estás muy cerca de adivinarlo. Te quedan {intentos - 1} intentos.")
                else:
                    resultado.set(f"Demasiado bajo. Te quedan {intentos - 1} intentos.")

            else:
                resultado.set("¡Felicidades! Adivinaste el número.")
                boton_verificar.config(state=tk.DISABLED)  # Desactiva el botón tras ganar

            intentos -= 1  # Disminuimos el contador de intentos
        else:
            resultado.set(f"Te quedaste sin intentos. El número era {numero_aleatorio}.")
            boton_verificar.config(state=tk.DISABLED)  # Desactiva el botón tras perder


    except ValueError:
        resultado.set("Por favor, introduce un número válido.")

# Función para reiniciar el juego
def reiniciar_juego():
    global numero_aleatorio, intentos
    # Regenerar el número aleatorio y restablecer los intentos
    numero_aleatorio = random.randint(1, 100)
    intentos = 10
    resultado.set(f"Introduce un número entre 1 y 100. Tienes {intentos} intentos.")
    entry.delete(0, tk.END)  # Limpiar la entrada
    boton_verificar.config(state=tk.NORMAL)  # Reactivar el botón

# Funcion para limpiar la celda al poner un numero
# He añadido un boton que resetea la celda donde se ponen los numeros
def limpiar_celda():
    entry.delete(0, tk.END)

# Inicializa la ventana de Tkinter
ventana = tk.Tk()
ventana.title("Adivina el número oculto")

# Tamaño de la ventana
ventana.geometry("900x600")

# Carga y coloca la imagen de fondo
imagen_fondo = Image.open("C:/Users/Propietario/Desktop/MP05/foto_numeros.jpg")
imagen_fondo = imagen_fondo.resize((900, 600))  # Ajusta el tamaño de la imagen al tamaño de la ventana
imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)

# Crear un Canvas y colocar la imagen de fondo
canvas = tk.Canvas(ventana, width=900, height=600)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=imagen_fondo_tk, anchor="nw")  # Posiciona la imagen en la esquina superior izquierda

# Crear las etiquetas y campos de entrada encima del canvas
label_instruccion = tk.Label(ventana, text="Adivina un número entre 1 y 100:", font=("Helvetica", 16), bg="white")
canvas.create_window(450, 100, window=label_instruccion)  # Coloca la etiqueta en el canvas

entry = tk.Entry(ventana, font=("Helvetica", 16))
canvas.create_window(450, 150, window=entry)  # Coloca la entrada en el canvas

resultado = tk.StringVar()
resultado.set(f"Introduce un número entre 1 y 100. Tienes {intentos} intentos.")
label_resultado = tk.Label(ventana, textvariable=resultado, font=("Helvetica", 14), bg="white")
canvas.create_window(450, 200, window=label_resultado)  # Coloca el resultado en el canvas

# Botón para verificar el número
boton_verificar = tk.Button(ventana, text="Verificar", command=verificar_numero)
canvas.create_window(450, 250, window=boton_verificar)  # Coloca el botón en el canvas

# Boton limpiar la pantalla
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_celda)
canvas.create_window(450, 300, window=boton_limpiar)  # Coloca el botón en el canvas

# Botón para reiniciar el juego
boton_reiniciar = tk.Button(ventana, text="Reiniciar juego", command=reiniciar_juego)
canvas.create_window(450, 350, window=boton_reiniciar)  # Coloca el botón en el canvas

# Inicia el bucle principal de la ventana
ventana.mainloop()
