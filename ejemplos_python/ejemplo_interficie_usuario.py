import tkinter as tk
from tkinter import*

# Finestra amb botons, menú desplegable i barra de menús
root = tk.Tk()
root.title("Interfície completa")
root.geometry("900x600")


# Botó
def on_button_click():
    print("Botó clicat!")


button = tk.Button(root, text="Clica'm!", command=on_button_click)
button.pack(pady=10)


# Menú desplegable
def selecciona_opcio(value):
    print(f"Opció seleccionada: {value}")


options = ["Opció 1", "Opció 2", "Opció 3"]
selected_option = tk.StringVar()
selected_option.set(options[0])

dropdown = tk.OptionMenu(root, selected_option, *options, command=selecciona_opcio)
dropdown.pack(pady=10)

# Barra de menús
menubar = tk.Menu(root)

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Nou", command=lambda: print("Nou arxiu"))
file_menu.add_command(label="Obre", command=lambda: print("Obre arxiu"))
file_menu.add_separator()
file_menu.add_command(label="Surt", command=root.quit)

menubar.add_cascade(label="Arxiu", menu=file_menu)
root.config(menu=menubar)

# Canvas

w = Canvas(width=200, height=100)
w.pack()
w.create_line(0, 0, 200, 100)
w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
w.create_rectangle(50, 25, 150, 75, fill="blue")

root.mainloop()

