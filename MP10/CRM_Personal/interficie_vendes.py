import tkinter as tk
from tkinter import ttk
from database import obtenir_productes, obtenir_clients_particulars  # Importar ambas funciones
from tkinter import messagebox
import mysql.connector


def mostrar_seccio_Interficie_Vendes(frame):
    # Limpiar contenido previo
    for widget in frame.winfo_children():
        widget.destroy()

    # Obtener los productos desde la base de datos
    productes = obtenir_productes()

    if not productes:
        messagebox.showerror("Error", "No se encontraron productos en el inventario.")
        return

    # Obtener los clientes particulares desde la base de datos
    clients = obtenir_clients_particulars()

    if not clients:
        messagebox.showerror("Error", "No se encontraron clientes particulares en la base de datos.")
        return

    # Título de la página
    tk.Label(frame, text="Registrar Vendes", font=("Arial", 16, "bold")).pack(pady=20)

    # Menú desplegable para productos con estilo mejorado
    product_names = [f"{product[0]} - {product[1]} ({product[2]} €)" for product in productes]
    product_combobox = ttk.Combobox(frame, values=product_names, state="readonly", width=40, font=("Arial", 12), style="TCombobox")
    product_combobox.pack(pady=10)
    product_combobox.set("Selecciona un producte")  # Valor predeterminado

    # Menú desplegable para clientes con estilo mejorado
    client_names = [f"{client['id_client']} - {client['nom']} {client['cognoms']}" for client in clients]
    client_combobox = ttk.Combobox(frame, values=client_names, state="readonly", width=40, font=("Arial", 12), style="TCombobox")
    client_combobox.pack(pady=10)
    client_combobox.set("Selecciona un client")  # Valor predeterminado

    # Estilos personalizados para los ComboBox (cambiamos el estilo de ttk)
    style = ttk.Style()
    style.configure("TCombobox",
                    fieldbackground="#e0e0e0",  # Fondo suave de color gris claro
                    background="#e0e0e0",  # Color de fondo del combobox
                    relief="flat",  # Quitar bordes duros
                    padding=5)  # Ajuste del espacio alrededor del texto

    # Campo de cantidad usando Spinbox
    quantity_label = tk.Label(frame, text="Quantitat:")
    quantity_label.pack(pady=5)

    quantity_spinbox = tk.Spinbox(frame, from_=1, to=100, width=10)  # De 1 a 100 unidades
    quantity_spinbox.pack(pady=10)

    # Establecer el valor por defecto de 1
    quantity_spinbox.delete(0, 'end')  # Elimina el valor actual
    quantity_spinbox.insert(0, "1")  # Establece el valor inicial a 1

    # Cambiar el estilo del Spinbox
    quantity_spinbox.configure(font=("Arial", 12), fg="#495057", bg="#ffffff", relief="flat", highlightthickness=1,
                               highlightbackground="#ccc")

    # Label para mostrar el total de la compra
    total_label = tk.Label(frame, text="Total: 0.00 €", font=("Arial", 14, "bold"), fg="#ffffff", bg="#28a745", padx=10, pady=10, relief="solid", bd=1)
    total_label.pack(pady=10)

    # Función para calcular el total
    def calcular_total():
        """Calcula el total de la compra y lo muestra en el label"""
        try:
            # Obtener el producto seleccionado y la cantidad
            selected_product = product_combobox.get()  # Obtener producto seleccionado
            quantity = int(quantity_spinbox.get())  # Obtener la cantidad seleccionada

            # Buscar el precio del producto seleccionado
            for product in productes:
                if selected_product.startswith(str(product[0])):  # Si el producto seleccionado coincide con el id
                    price = product[2]  # El precio del producto
                    break

            # Calcular el total
            total = price * quantity
            total_label.config(text=f"Total: {total:.2f} €")  # Mostrar el total en el label
        except ValueError:
            messagebox.showerror("Error", "Por favor, seleccione un producto y una cantidad válidos.")

    # Función para registrar la venta en la base de datos
    def registrar_venta():
        """Registra la venta en la base de datos"""
        try:
            selected_product = product_combobox.get()
            selected_client = client_combobox.get()
            quantity = int(quantity_spinbox.get())
            total = float(total_label.cget("text").split(":")[1].strip().split("€")[0])

            # Obtener los IDs del producto y cliente seleccionados
            product_id = int(selected_product.split(" - ")[0])
            client_id = int(selected_client.split(" - ")[0])

            # Conexión a la base de datos para insertar la venta
            connection = mysql.connector.connect(
                host="localhost",
                database="crm",  # Asegúrate de usar el nombre correcto de la base de datos
                user="root",
                password="root"
            )
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO vendes_particulars (id_client, id_producte, quantitat, total, data_venda) "
                "VALUES (%s, %s, %s, %s, CURDATE())",
                (client_id, product_id, quantity, total)
            )
            connection.commit()
            connection.close()

            messagebox.showinfo("Éxito", "Venta registrada exitosamente.")
            mostrar_ventas()  # Actualizar el TreeView con la nueva venta
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo registrar la venta: {e}")

    # Botón para calcular el total
    calculate_button = tk.Button(frame, text="Calcular Total", command=calcular_total)
    calculate_button.pack(pady=10)

    # Botón para confirmar la venta
    register_button = tk.Button(frame, text="Registrar Venda", command=registrar_venta, bg="green", fg="white")
    register_button.pack(pady=20)

    # TreeView para mostrar las ventas registradas
    ventas_treeview = ttk.Treeview(frame, columns=("ID", "Producte", "Client", "Quantitat", "Total", "Data"),
    show="headings")
    ventas_treeview.pack(pady=20, fill="both", expand=True)

    # Definir las columnas
    ventas_treeview.heading("ID", text="ID Venda")
    ventas_treeview.heading("Producte", text="Producte")
    ventas_treeview.heading("Client", text="Client")
    ventas_treeview.heading("Quantitat", text="Quantitat")
    ventas_treeview.heading("Total", text="Total")
    ventas_treeview.heading("Data", text="Data")

    # Función para cargar las ventas en el Treeview
    def mostrar_ventas():
        """Carga todas las ventas registradas en el TreeView"""
        for row in ventas_treeview.get_children():
            ventas_treeview.delete(row)

        # Obtener las ventas de la base de datos
        connection = mysql.connector.connect(
            host="localhost",
            database="crm",  # Asegúrate de usar el nombre correcto de la base de datos
            user="root",
            password="root"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT v.id_venda, p.nom_producte, c.nom, v.quantitat, v.total, v.data_venda "
                       "FROM vendes_particulars v "
                       "JOIN inventari p ON v.id_producte = p.id "
                       "JOIN clients_particulars c ON v.id_client = c.id_client")
        ventas = cursor.fetchall()
        connection.close()

        # Insertar las ventas en el TreeView
        for venta in ventas:
            ventas_treeview.insert("", "end", values=venta)

    # Cargar las ventas al iniciar
    mostrar_ventas()
