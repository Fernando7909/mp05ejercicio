import tkinter as tk
from tkinter import ttk, messagebox
from database import obtenir_clients_particulars, obtenir_clients_empreses, connectar_bbdd


def mostrar_gestio_clients(main_frame):
    """Funció per mostrar la gestió de clients en el marc principal."""
    print("Llamada a mostrar_gestio_clients()")  # Verifica si la función es llamada correctamente

    # Netejar el marc principal
    for widget in main_frame.winfo_children():
        widget.destroy()
    print("Marc principal limpiado")  # Verifica que el marco ha sido limpiado correctamente

    # Títol principal
    tk.Label(main_frame, text="Gestió de Clients", font=("Arial", 16, "bold"), bg="#f4f4f9").pack(pady=10)
    print("Título principal mostrado")  # Verifica que el título ha sido colocado

    # Marc per als clients particulars
    frame_particulars = ttk.LabelFrame(main_frame, text="Clients Particulars", padding=(10, 10))
    frame_particulars.pack(fill="both", expand=True, padx=20, pady=10)
    print("Frame de clientes particulares creado")  # Verifica la creación del frame de clientes particulares

    # Scrollbars per als clients particulars
    scrollbar_v_particulars = ttk.Scrollbar(frame_particulars, orient="vertical")
    scrollbar_h_particulars = ttk.Scrollbar(frame_particulars, orient="horizontal")
    print("Scrollbars de clientes particulares creados")  # Verifica la creación de los scrollbars

    # Columnes per a la taula de clients particulars
    columnes_particulars = ("ID", "Nom", "Cognoms", "DNI", "Email", "Telèfon", "Adreça", "Data Registre", "Actiu", "Comentaris")
    tree_particulars = ttk.Treeview(
        frame_particulars,
        columns=columnes_particulars,
        show="headings",
        yscrollcommand=scrollbar_v_particulars.set,
        xscrollcommand=scrollbar_h_particulars.set
    )

    for col in columnes_particulars:
        tree_particulars.heading(col, text=col, anchor="center")
        tree_particulars.column(col, anchor="center", width=120)
    print("Treeview de clientes particulares configurado")  # Verifica que el Treeview ha sido configurado

    # Configurar scrollbars
    scrollbar_v_particulars.config(command=tree_particulars.yview)
    scrollbar_h_particulars.config(command=tree_particulars.xview)

    # Posicionar els elements
    scrollbar_v_particulars.pack(side="right", fill="y")
    scrollbar_h_particulars.pack(side="bottom", fill="x")
    tree_particulars.pack(fill="both", expand=True)
    print("Elementos de clientes particulares posicionados")  # Verifica que los elementos fueron posicionados

    # Marc per als clients empresa
    frame_empreses = ttk.LabelFrame(main_frame, text="Clients Empresa", padding=(10, 10))
    frame_empreses.pack(fill="both", expand=True, padx=20, pady=10)
    print("Frame de clientes empresa creado")  # Verifica la creación del frame de clientes empresa

    # Scrollbars per als clients empresa
    scrollbar_v_empreses = ttk.Scrollbar(frame_empreses, orient="vertical")
    scrollbar_h_empreses = ttk.Scrollbar(frame_empreses, orient="horizontal")
    print("Scrollbars de clientes empresa creados")  # Verifica la creación de los scrollbars

    # Columnes per a la taula de clients empresa
    columnes_empreses = ("ID", "Nom Empresa", "CIF", "Email", "Telèfon", "Adreça", "Data Registre", "Actiu", "Comentaris")
    tree_empreses = ttk.Treeview(
        frame_empreses,
        columns=columnes_empreses,
        show="headings",
        yscrollcommand=scrollbar_v_empreses.set,
        xscrollcommand=scrollbar_h_empreses.set
    )

    for col in columnes_empreses:
        tree_empreses.heading(col, text=col, anchor="center")
        tree_empreses.column(col, anchor="center", width=120)
    print("Treeview de clientes empresa configurado")  # Verifica que el Treeview ha sido configurado

    # Configurar scrollbars
    scrollbar_v_empreses.config(command=tree_empreses.yview)
    scrollbar_h_empreses.config(command=tree_empreses.xview)

    # Posicionar els elements
    scrollbar_v_empreses.pack(side="right", fill="y")
    scrollbar_h_empreses.pack(side="bottom", fill="x")
    tree_empreses.pack(fill="both", expand=True)
    print("Elementos de clientes empresa posicionados")  # Verifica que los elementos fueron posicionados

    # Funció per cargar dades
    def cargar_dades():
        print("Llamada a cargar_dades()")  # Verifica si la función de carga es llamada

        # Limpiar el Treeview de clientes particulares
        tree_particulars.delete(*tree_particulars.get_children())
        print("Limpiando el Treeview de clientes particulares...")

        # Obtener los datos de los clientes particulares
        particulars = obtenir_clients_particulars(campos_complet=True)
        print(f"Datos obtenidos: {particulars}")  # Verificación de datos obtenidos

        if not particulars:
            print("No se encontraron clientes para mostrar.")
            return

        print(f"Clientes obtenidos: {len(particulars)} clientes")

        # Insertar los datos en el Treeview
        for client in particulars:
            print(f"Insertando cliente: {client}")  # Depuración para ver cómo se insertan los datos
            tree_particulars.insert("", "end", values=(
                client["id_client"], client["nom"], client["cognoms"], client["dni"], client["email"],
                client["telefon"], client["direccio"], client["data_registre"],
                "Sí" if client["actiu"] else "No", client["comentaris"]
            ))

        # Verifica el número de elementos en el Treeview después de la inserción
        print(f"Total de clientes en el Treeview: {len(tree_particulars.get_children())}")

        # Forzar actualización del Treeview
        tree_particulars.update_idletasks()

        # Clients empreses
        tree_empreses.delete(*tree_empreses.get_children())
        empreses = obtenir_clients_empreses()

        for empresa in empreses:
            tree_empreses.insert("", "end", values=(
                empresa["id_empresa"], empresa["nom_empresa"], empresa["cif"], empresa["email_empresa"],
                empresa["telefon_empresa"], empresa["direccio_empresa"], empresa["data_registre"],
                "Sí" if empresa["actiu"] else "No", empresa["comentaris"]
            ))

        # Verifica el número de elementos en el Treeview para empresas
        print(f"Total de empresas en el Treeview: {len(tree_empreses.get_children())}")

    # Llamamos a cargar_dades para cargar los datos
    cargar_dades()

    print("cargar_dades() ejecutado.")  # Verifica si la función cargar_dades() se ejecuta correctamente




    # Funció per carregar dades
    def carregar_dades():
        # Limpiar el Treeview de clientes particulares
        tree_particulars.delete(*tree_particulars.get_children())

        # Obtener los datos de los clientes particulares
        particulars = obtenir_clients_particulars(campos_complet=True)
        print(f"Clientes obtenidos de la base de datos: {particulars}")  # Verificación de datos obtenidos

        # Verificar si los datos no están vacíos
        if not particulars:
            print("No se encontraron clientes para mostrar.")
            return
        else:
            print(f"Clientes obtenidos: {len(particulars)} clientes")

        # Insertar los datos en el Treeview
        for client in particulars:
            print(f"Insertando cliente: {client}")  # Depuración para ver cómo se insertan los datos

            # Verifica que todos los campos necesarios existan antes de intentar accederlos
            if "dni" in client and "id_client" in client and "nom" in client and "cognoms" in client:
                tree_particulars.insert("", "end", values=(  # Inserta todos los valores si están presentes
                    client["id_client"], client["nom"], client["cognoms"], client["dni"], client["email"],
                    client["telefon"], client["direccio"], client["data_registre"],
                    "Sí" if client["actiu"] else "No", client["comentaris"]
                ))
            else:
                print(f"Cliente con ID {client['id_client']} tiene datos faltantes y no se insertará.")
                tree_particulars.insert("", "end", values=(  # Inserta solo los campos básicos si faltan datos
                    client.get("id_client", "Desconocido"),
                    client.get("nom", "Desconocido"),
                    client.get("cognoms", "Desconocido")
                ))

        # Verifica el número de elementos en el Treeview después de la inserción
        print(f"Total de clientes en el Treeview: {len(tree_particulars.get_children())}")

        # Forzar actualización del Treeview
        tree_particulars.update_idletasks()

        # Clients empreses
        tree_empreses.delete(*tree_empreses.get_children())
        empreses = obtenir_clients_empreses()

        for empresa in empreses:
            tree_empreses.insert("", "end", values=(
                empresa["id_empresa"], empresa["nom_empresa"], empresa["cif"], empresa["email_empresa"],
                empresa["telefon_empresa"], empresa["direccio_empresa"], empresa["data_registre"],
                "Sí" if empresa["actiu"] else "No", empresa["comentaris"]
            ))

        # Verifica el número de elementos en el Treeview para empresas
        print(f"Total de empresas en el Treeview: {len(tree_empreses.get_children())}")

    # Funció per editar dades
    def obrir_finestra_edicio(event, tipus):
        tree = tree_particulars if tipus == "particulars" else tree_empreses
        seleccionat = tree.selection()
        if not seleccionat:
            return

        dades = tree.item(seleccionat[0], "values")
        finestra_edicio = tk.Toplevel()
        finestra_edicio.title(f"Editar Client ({'Particular' if tipus == 'particulars' else 'Empresa'}) ID: {dades[0]}")
        finestra_edicio.geometry("400x400")
        finestra_edicio.configure(bg="#e6f7ff")

        camps = columnes_particulars[1:] if tipus == "particulars" else columnes_empreses[1:]
        entrades = {}

        for idx, camp in enumerate(camps):
            tk.Label(finestra_edicio, text=camp, bg="#e6f7ff", font=("Arial", 10, "bold")).grid(row=idx, column=0, pady=5)
            entrada = tk.Entry(finestra_edicio, font=("Arial", 10))
            entrada.insert(0, dades[idx + 1])
            entrada.grid(row=idx, column=1, pady=5, padx=10)
            entrades[camp] = entrada

        def guardar_canvis():
            valors = {camp: entrada.get() for camp, entrada in entrades.items()}

            # Convertir el valor de "actiu" en entero (1 para "Sí", 0 para "No")
            if "Actiu" in valors:
                valors["Actiu"] = 1 if valors["Actiu"].lower() in ("sí", "si", "yes", "1") else 0

            connexio = connectar_bbdd()
            if connexio is None:
                return
            cursor = connexio.cursor()
            try:
                if tipus == "particulars":
                    query = """
                    UPDATE clients_particulars SET nom=%s, cognoms=%s, dni=%s, email=%s, telefon=%s, direccio=%s, 
                    data_registre=%s, actiu=%s, comentaris=%s WHERE id_client=%s
                    """
                else:
                    query = """
                    UPDATE clients_empreses SET nom_empresa=%s, cif=%s, email_empresa=%s, telefon_empresa=%s, 
                    direccio_empresa=%s, data_registre=%s, actiu=%s, comentaris=%s WHERE id_empresa=%s
                    """
                dades_query = (*valors.values(), dades[0])
                cursor.execute(query, dades_query)
                connexio.commit()
                messagebox.showinfo("Èxit", "Dades actualitzades correctament.")
                carregar_dades()
                finestra_edicio.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"No s'han pogut guardar els canvis:\n{e}")
            finally:
                cursor.close()
                connexio.close()

        btn_guardar = tk.Button(finestra_edicio, text="Guardar Canvis", command=guardar_canvis, bg="#28a745", fg="white")
        btn_guardar.grid(row=len(camps), column=1, pady=10)

    # Vincular doble clic per editar dades
    tree_particulars.bind("<Double-1>", lambda e: obrir_finestra_edicio(e, "particulars"))
    tree_empreses.bind("<Double-1>", lambda e: obrir_finestra_edicio(e, "empreses"))

    # Botó de refresc
    btn_refrescar = tk.Button(main_frame, text="Refrescar Dades", command=carregar_dades, bg="#17a2b8", fg="white")
    btn_refrescar.pack(pady=10)
