import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
from database import obtenir_personal, connectar_bbdd


def mostrar_seccio_personal(main_frame):
    """Funció per mostrar la secció de personal en el marc principal."""
    for widget in main_frame.winfo_children():
        widget.destroy()

    # Títol de la secció
    tk.Label(main_frame, text="Gestió de Personal", font=("Arial", 16, "bold"), bg="#f4f4f9").pack(pady=10)

    # Marc del Treeview
    personal_frame = tk.Frame(main_frame)
    personal_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Scrollbars
    scrollbar_vertical = ttk.Scrollbar(personal_frame, orient="vertical")
    scrollbar_horizontal = ttk.Scrollbar(personal_frame, orient="horizontal")

    # Definició de les columnes
    columnes = (
        "ID", "Nom", "Cognoms", "DNI", "Email", "Telèfon", "Data Contractació",
        "Puesto", "Salari", "Departament", "Data Naixement", "Actiu", "Preferent"
    )
    personal_tree = ttk.Treeview(
        personal_frame,
        columns=columnes,
        show="headings",
        yscrollcommand=scrollbar_vertical.set,
        xscrollcommand=scrollbar_horizontal.set
    )

    for col in columnes:
        personal_tree.heading(col, text=col, anchor="center")
        personal_tree.column(col, anchor="center", width=120)

    # Configura les scrollbars per desplaçar el Treeview
    scrollbar_vertical.config(command=personal_tree.yview)
    scrollbar_horizontal.config(command=personal_tree.xview)

    # Paquetització
    scrollbar_vertical.pack(side="right", fill="y")
    scrollbar_horizontal.pack(side="bottom", fill="x")
    personal_tree.pack(fill="both", expand=True)

    # Carrega les dades al Treeview
    def carregar_dades():
        personal_tree.delete(*personal_tree.get_children())
        personal = obtenir_personal()
        for persona in personal:
            personal_tree.insert("", "end", values=(
                persona["id_personal"], persona["nombre"], persona["apellidos"],
                persona["dni"], persona["email"], persona["telefono"],
                persona["fecha_contratacion"], persona["puesto"], persona["salario"],
                persona["departamento"], persona["fecha_nacimiento"],
                "Sí" if persona["activo"] else "No",
                "Sí" if persona["preferent"] else "No"
            ))

    carregar_dades()

    # Finestra d'edició
    # Finestra d'edició
    def obrir_finestra_edicio(event):
        seleccionat = personal_tree.selection()
        if not seleccionat:
            return

        index_actual = personal_tree.get_children().index(seleccionat[0])
        personal = personal_tree.get_children()

        # Variable para almacenar el ID del usuario actual
        personal_id = [None]
        foto_binario = [None]

        def cargar_datos_usuario(index):
            nonlocal personal_id
            dades = personal_tree.item(personal[index], "values")
            personal_id[0] = dades[0]

            # Actualizar campos en la ventana
            for idx, camp in enumerate(camps[:-1]):
                entrades[camp].delete(0, tk.END)
                valor = dades[idx + 1]
                if camp == "Actiu":
                    valor = "Sí" if valor == "Sí" else "No"
                entrades[camp].insert(0, valor)

            preferent_var.set(1 if dades[-1] == "Sí" else 0)
            finestra_edicio.title(f"Editar Personal ID: {personal_id[0]}")

        # Crear la finestra emergent
        finestra_edicio = tk.Toplevel()
        finestra_edicio.title("Editar Personal")
        finestra_edicio.geometry("600x600")
        finestra_edicio.configure(bg="#e6f7ff")

        # Marc per als camps d'entrada
        marc = tk.Frame(finestra_edicio, pady=10, padx=10, bg="#e6f7ff")
        marc.pack(fill="both", expand=True)

        camps = ["Nom", "Cognoms", "DNI", "Email", "Telèfon", "Data Contractació",
                 "Puesto", "Salari", "Departament", "Data Naixement", "Actiu"]
        entrades = {}

        for idx, camp in enumerate(camps):
            tk.Label(marc, text=camp, bg="#e6f7ff", font=("Arial", 10, "bold")).grid(row=idx, column=0, pady=5,
                                                                                     sticky="w")
            entrada = tk.Entry(marc, font=("Arial", 10))
            entrada.grid(row=idx, column=1, pady=5, padx=10, sticky="ew")
            entrades[camp] = entrada

        # Checkbox para "Preferent"
        tk.Label(marc, text="Preferent", bg="#e6f7ff", font=("Arial", 10, "bold")).grid(row=len(camps), column=0,
                                                                                        pady=5, sticky="w")
        preferent_var = tk.IntVar()
        preferent_checkbox = tk.Checkbutton(marc, variable=preferent_var, bg="#e6f7ff")
        preferent_checkbox.grid(row=len(camps), column=1, pady=5, sticky="w")

        cargar_datos_usuario(index_actual)

        # Botones de navegación
        def ir_anterior():
            nonlocal index_actual
            if index_actual > 0:
                index_actual -= 1
                cargar_datos_usuario(index_actual)

        def ir_siguiente():
            nonlocal index_actual
            if index_actual < len(personal) - 1:
                index_actual += 1
                cargar_datos_usuario(index_actual)

        nav_frame = tk.Frame(finestra_edicio, bg="#e6f7ff")
        nav_frame.pack(fill="x", pady=10)

        btn_anterior = tk.Button(nav_frame, text="← Anterior", command=ir_anterior, bg="#007bff", fg="white")
        btn_anterior.pack(side="left", padx=10)

        btn_siguiente = tk.Button(nav_frame, text="Siguiente →", command=ir_siguiente, bg="#007bff", fg="white")
        btn_siguiente.pack(side="right", padx=10)

        # Botón para guardar cambios
        def guardar_canvis():
            valors = {camp: entrada.get() for camp, entrada in entrades.items()}
            valors["Actiu"] = 1 if valors["Actiu"].strip().lower() in ["sí", "1", "true", "actiu"] else 0
            valors["Preferent"] = preferent_var.get()

            connexio = connectar_bbdd()
            if connexio:
                cursor = connexio.cursor()
                query = """
                UPDATE personal SET nombre=%s, apellidos=%s, dni=%s, email=%s, telefono=%s,
                fecha_contratacion=%s, puesto=%s, salario=%s, departamento=%s,
                fecha_nacimiento=%s, activo=%s, preferent=%s WHERE id_personal=%s
                """
                dades_query = (
                    valors["Nom"], valors["Cognoms"], valors["DNI"], valors["Email"], valors["Telèfon"],
                    valors["Data Contractació"], valors["Puesto"], valors["Salari"], valors["Departament"],
                    valors["Data Naixement"], valors["Actiu"], valors["Preferent"], personal_id[0]
                )
                cursor.execute(query, dades_query)
                connexio.commit()
                cursor.close()
                connexio.close()
                messagebox.showinfo("Èxit", "Dades actualitzades correctament.")
                carregar_dades()
                finestra_edicio.destroy()

        tk.Button(finestra_edicio, text="Guardar Canvis", command=guardar_canvis, bg="#28a745", fg="white").pack(
            pady=10)

    personal_tree.bind("<Double-1>", obrir_finestra_edicio)
    tk.Button(main_frame, text="Refrescar llista", command=carregar_dades, bg="#17a2b8", fg="white").pack(pady=10)

