import tkinter as tk
from tkinter import ttk, messagebox
import heapq

class Tarea:
    def __init__(self, nombre, descripcion, prioridad):
        self.nombre = nombre
        self.descripcion = descripcion
        self.prioridad = prioridad

    def __lt__(self, otra):
        return self.prioridad < otra.prioridad

class GestorTareas:
    def __init__(self):
        self.tareas = []
        self.historial = []
        self.rehacer_pila = []

    def agregar_tarea(self, tarea):
        heapq.heappush(self.tareas, tarea)
        self.historial.append(("agregar", tarea))
        self.rehacer_pila.clear()

    def eliminar_tarea(self):
        if self.tareas:
            tarea = heapq.heappop(self.tareas)
            self.historial.append(("eliminar", tarea))
            self.rehacer_pila.clear()
            return tarea
        return None

    def deshacer(self):
        if self.historial:
            accion, tarea = self.historial.pop()
            if accion == "agregar":
                self.tareas.remove(tarea)
                heapq.heapify(self.tareas)
                self.rehacer_pila.append(("agregar", tarea))
            elif accion == "eliminar":
                heapq.heappush(self.tareas, tarea)
                self.rehacer_pila.append(("eliminar", tarea))

    def rehacer(self):
        if self.rehacer_pila:
            accion, tarea = self.rehacer_pila.pop()
            if accion == "agregar":
                heapq.heappush(self.tareas, tarea)
            elif accion == "eliminar":
                self.tareas.remove(tarea)
                heapq.heapify(self.tareas)
            self.historial.append((accion, tarea))

class AplicacionGestorTareas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestor de Tareas")
        self.geometry("600x400")
        self.gestor = GestorTareas()
        self.crear_widgets()

    def crear_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Entradas para nueva tarea
        ttk.Label(main_frame, text="Nombre:").grid(row=0, column=0, sticky=tk.W)
        self.nombre_entry = ttk.Entry(main_frame, width=40)
        self.nombre_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

        ttk.Label(main_frame, text="Descripción:").grid(row=1, column=0, sticky=tk.W)
        self.descripcion_entry = ttk.Entry(main_frame, width=40)
        self.descripcion_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

        ttk.Label(main_frame, text="Prioridad:").grid(row=2, column=0, sticky=tk.W)
        self.prioridad_combobox = ttk.Combobox(main_frame, values=["Alta", "Media", "Baja"])
        self.prioridad_combobox.set("Media")
        self.prioridad_combobox.grid(row=2, column=1, sticky=(tk.W, tk.E))

        # Botones
        ttk.Button(main_frame, text="Agregar Tarea", command=self.agregar_tarea).grid(row=3, column=0, columnspan=2, pady=5)
        ttk.Button(main_frame, text="Eliminar Tarea", command=self.eliminar_tarea).grid(row=4, column=0, columnspan=2, pady=5)
        ttk.Button(main_frame, text="Deshacer", command=self.deshacer).grid(row=5, column=0, pady=5)
        ttk.Button(main_frame, text="Rehacer", command=self.rehacer).grid(row=5, column=1, pady=5)

        # Lista de tareas
        self.lista_tareas = ttk.Treeview(main_frame, columns=("Nombre", "Descripción", "Prioridad"), show="headings")
        self.lista_tareas.heading("Nombre", text="Nombre")
        self.lista_tareas.heading("Descripción", text="Descripción")
        self.lista_tareas.heading("Prioridad", text="Prioridad")
        self.lista_tareas.grid(row=6, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configurar expansión
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(6, weight=1)

    def agregar_tarea(self):
        nombre = self.nombre_entry.get()
        descripcion = self.descripcion_entry.get()
        prioridad_str = self.prioridad_combobox.get()
        prioridad = 1 if prioridad_str == "Alta" else 2 if prioridad_str == "Media" else 3

        if nombre and descripcion:
            tarea = Tarea(nombre, descripcion, prioridad)
            self.gestor.agregar_tarea(tarea)
            self.actualizar_lista_tareas()
            self.limpiar_entradas()
        else:
            messagebox.showwarning("Datos incompletos", "Por favor, ingrese nombre y descripción.")

    def eliminar_tarea(self):
        tarea_eliminada = self.gestor.eliminar_tarea()
        if tarea_eliminada:
            self.actualizar_lista_tareas()
            messagebox.showinfo("Tarea eliminada", f"Se eliminó la tarea: {tarea_eliminada.nombre}")
        else:
            messagebox.showinfo("Sin tareas", "No hay tareas para eliminar.")

    def deshacer(self):
        self.gestor.deshacer()
        self.actualizar_lista_tareas()

    def rehacer(self):
        self.gestor.rehacer()
        self.actualizar_lista_tareas()

    def actualizar_lista_tareas(self):
        for i in self.lista_tareas.get_children():
            self.lista_tareas.delete(i)
        for tarea in sorted(self.gestor.tareas):
            prioridad_str = "Alta" if tarea.prioridad == 1 else "Media" if tarea.prioridad == 2 else "Baja"
            self.lista_tareas.insert("", "end", values=(tarea.nombre, tarea.descripcion, prioridad_str))

    def limpiar_entradas(self):
        self.nombre_entry.delete(0, tk.END)
        self.descripcion_entry.delete(0, tk.END)
        self.prioridad_combobox.set("Media")

if __name__ == "__main__":
    app = AplicacionGestorTareas()
    app.mainloop()