import tkinter as tk
from tkinter import messagebox
import requests


# Funció per a obtenir informació del clima
def obtenir_clima():
    ciutat = ciutat_entry.get()  # Obtenim la ciutat de l'entrada de text
    if ciutat:
        try:
            # URL de l'API (recorda afegir la teva clau d'API aquí)
            api_key = "b02c3fbd01111ff26f563ccc7f9ce955"
            url = f"http://api.openweathermap.org/data/2.5/weather?q={ciutat}&appid={api_key}&units=metric&lang=ca"

            # Fent la petició GET
            resposta = requests.get(url)
            dades = resposta.json()

            # Verifiquem si la ciutat existeix
            if resposta.status_code == 200:
                temperatura = dades["main"]["temp"]
                descripcio = dades["weather"][0]["description"]
                clima_info = f"Temperatura: {temperatura}°C\nDescripció: {descripcio.capitalize()}"
                result_label.config(text=clima_info)
            else:
                messagebox.showerror("Error", "No s'ha trobat la ciutat")
        except Exception as e:
            messagebox.showerror("Error", "Hi ha hagut un problema amb la connexió a l'API")
    else:
        messagebox.showwarning("Atenció", "Si us plau, introdueix el nom d'una ciutat")


# Crear la finestra principal de Tkinter
root = tk.Tk()
root.title("Aplicació de Clima")
root.geometry("400x300")

# Etiqueta de benvinguda
benvinguda_label = tk.Label(root, text="Introdueix el nom d'una ciutat:", font=("Helvetica", 12))
benvinguda_label.pack(pady=10)

# Entrada de text per a la ciutat
ciutat_entry = tk.Entry(root, width=30)
ciutat_entry.pack(pady=10)

# Botó per obtenir el clima
obtenir_clima_button = tk.Button(root, text="Obtenir Clima", command=obtenir_clima)
obtenir_clima_button.pack(pady=10)

# Etiqueta per mostrar el resultat
result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=20)

# Iniciar el bucle principal de la interfície
root.mainloop()
