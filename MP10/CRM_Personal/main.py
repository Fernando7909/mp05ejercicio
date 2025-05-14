import tkinter as tk
from vendes import mostrar_seccio_vendes
from personal import mostrar_seccio_personal  # Importar Gestió de Personal
from clients import mostrar_gestio_clients  # Importar Gestió de Clients
from inventari import mostrar_seccio_inventari  # Importar Gestió d'Inventari
from datetime import datetime
from interficie_vendes import mostrar_seccio_Interficie_Vendes



# Configuració de la finestra principal
root = tk.Tk()
root.title("CRM/ERP - Gestió Empresarial")
root.geometry("1000x600")
root.configure(bg="#e0e0e0")

# Barra de navegació
sidebar = tk.Frame(root, width=200, bg="#343a40", relief="sunken", borderwidth=2)
sidebar.pack(expand=False, fill="y", side="left", anchor="nw")

# Botons de navegació
seccions = ["Inici", "Gestió de Vendes", "Gestió de Clients", "Inventari", "Informes", "Gestió de Personal", "Interficie de Vendes"]

for section in seccions:
    btn = tk.Button(
        sidebar, text=section, bg="#495057", fg="white", relief="flat",
        font=("Arial", 10), activebackground="#6c757d", activeforeground="white",
        command=lambda sec=section: mostrar_seccio(sec)
    )
    btn.pack(fill="x", pady=5)

# Marc principal per al contingut dinàmic
main_frame = tk.Frame(root, bg="#f4f4f9")
main_frame.pack(expand=True, fill="both", side="right")

# Funció per canviar entre seccions
def mostrar_seccio(seccio):
    """Mostra la secció seleccionada en el marc principal."""
    if seccio == "Inici":
        mostrar_inici()
    elif seccio == "Gestió de Vendes":
        mostrar_seccio_vendes(main_frame)
    elif seccio == "Gestió de Clients":  # Nova secció afegida
        mostrar_gestio_clients(main_frame)
    elif seccio == "Inventari":
        mostrar_seccio_inventari(main_frame)  # Crida a la funció de l'inventari
    elif seccio == "Gestió de Personal":
        mostrar_seccio_personal(main_frame)
    elif seccio == "Interficie de Vendes":
        mostrar_seccio_Interficie_Vendes(main_frame)

def actualizar_hora():
    """Actualitza l'hora en pantalla."""
    # Obtener la hora actual
    hora_actual = datetime.now().strftime("%H:%M:%S")
    # Actualizar el texto de la etiqueta de hora
    etiqueta_hora.config(text=f"Hora actual: {hora_actual}")
    # Programar la siguiente actualización en 1000 ms (1 segundo)
    etiqueta_hora.after(1000, actualizar_hora)

# Funció per mostrar la pantalla d'inici
def mostrar_inici():
    # Destruye los widgets previos en el main_frame
    for widget in main_frame.winfo_children():
        widget.destroy()

    # Título principal
    tk.Label(main_frame, text="Benvingut al CRM/ERP", font=("Arial", 16, "bold")).pack(pady=20)

    # Crear etiqueta para la hora y empezar la actualización
    global etiqueta_hora
    etiqueta_hora = tk.Label(main_frame, font=("Arial", 12))
    etiqueta_hora.pack(pady=10)
    actualizar_hora()  # Llama a la función de actualización por primera vez

# Mostra la pantalla d'inici en arrencar el programa
mostrar_inici()
root.mainloop()