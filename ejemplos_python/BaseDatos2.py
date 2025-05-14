import tkinter as tk
from tkinter import ttk
import mysql.connector


def obtenir_dades():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='react_mysql_example',
            user='root',
            password='root'
        )
        if connection.is_connected():
            cursor = connection.cursor()
            query = "SELECT * FROM usuaris;"
            cursor.execute(query)
            return cursor.fetchall()

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return []

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def omplir_treeview(dades):
    for fila in dades:
        tree.insert("", "end", values=fila)


# Configuració de la finestra
root = tk.Tk()
root.title("Dades de la Base de Dades")

# Creació de la vista amb Treeview
tree = ttk.Treeview(root, columns=(1, 2, 3), show="headings", height="10")
tree.heading(1, text="ID")
tree.heading(2, text="Nom")
tree.heading(3, text="Cognom")
tree.pack()

# Obtenir les dades i omplir la interfície
dades = obtenir_dades()
omplir_treeview(dades)

# Iniciar / EJECUTAR la finestra
root.mainloop()

