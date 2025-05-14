import mysql.connector
from tkinter import messagebox, Tk, ttk
import tkinter as tk
from database import connectar_bbdd
from fpdf import FPDF

def connectar_bbdd():
    """Connecta a la base de dades MySQL i retorna la connexió."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            database="crm",
            user="root",
            password="root"
        )
        return connection
    except mysql.connector.Error as error:
        messagebox.showerror("Error de Connexió", f"No s'ha pogut connectar a la base de dades:\n{error}")
        return None



# Configuració de la finestra principal
root = tk.Tk()
root.title("CRM/ERP - Gestió Empresarial")
root.geometry("1000x600")
root.configure(bg="#e0e0e0")

# Barra de navegació
sidebar = tk.Frame(root, width=200, bg="#343a40", relief="sunken", borderwidth=2)
sidebar.pack(expand=False, fill="y", side="left", anchor="nw")

# Botons de navegació
seccions = ["Inici", "Gestió de Vendes", "Clients", "Inventari", "Informes"]
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

# Funció per mostrar la pantalla d'inici
def mostrar_inici():
    for widget in main_frame.winfo_children():
        widget.destroy()
    tk.Label(main_frame, text="Benvingut al CRM/ERP", font=("Arial", 16, "bold")).pack(pady=20)

# Mostra la pantalla d'inici en arrencar el programa
mostrar_inici()
root.mainloop()




def mostrar_seccio_vendes(main_frame):
    """Funció per mostrar la secció de vendes en el marc principal."""
    for widget in main_frame.winfo_children():
        widget.destroy()  # Elimina el contingut previ del marc principal

    tk.Label(main_frame, text="Gestió de Vendes", font=("Arial", 14, "bold")).pack(pady=10)

    # Marc per als camps d'entrada de vendes
    entry_frame = tk.Frame(main_frame, bg="#f4f4f9")
    entry_frame.pack(fill="x", padx=20)

    tk.Label(entry_frame, text="Producte").grid(row=0, column=0, padx=5, pady=5)
    entrada_producte = tk.Entry(entry_frame)
    entrada_producte.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(entry_frame, text="Quantitat").grid(row=0, column=2, padx=5, pady=5)
    entrada_quantitat = tk.Entry(entry_frame)
    entrada_quantitat.grid(row=0, column=3, padx=5, pady=5)

    tk.Label(entry_frame, text="Preu").grid(row=0, column=4, padx=5, pady=5)
    entrada_preu = tk.Entry(entry_frame)
    entrada_preu.grid(row=0, column=5, padx=5, pady=5)

    tk.Label(entry_frame, text="Data de Venda").grid(row=0, column=6, padx=5, pady=5)
    entrada_data = tk.Entry(entry_frame)
    entrada_data.grid(row=0, column=7, padx=5, pady=5)

    # Taula per mostrar les vendes
    vendes_frame = tk.Frame(main_frame)
    vendes_frame.pack(fill="both", expand=True, padx=20, pady=20)

    columnes = ("producte", "quantitat", "preu", "data_venda")
    vendes_tree = ttk.Treeview(vendes_frame, columns=columnes, show="headings")
    vendes_tree.heading("producte", text="Producte")
    vendes_tree.heading("quantitat", text="Quantitat")
    vendes_tree.heading("preu", text="Preu")
    vendes_tree.heading("data_venda", text="Data de Venda")
    vendes_tree.pack(fill="both", expand=True)

    # Funció per carregar dades de vendes
    def carregar_dades_vendes():
        vendes_tree.delete(*vendes_tree.get_children())  # Esborra les dades existents al Treeview
        connection = connectar_bbdd()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT id, producte, quantitat, preu, data_venda FROM vendes")
            records = cursor.fetchall()
            for record in records:
                vendes_tree.insert("", "end", values=record[1:],
                                   iid=record[0])  # Guarda 'id' com iid per facilitar l'accés
            cursor.close()
            connection.close()

    carregar_dades_vendes()  # Carrega les dades en iniciar la secció

    # Funció per inserir una nova venda
    def inserir_venda():
        connection = connectar_bbdd()
        if connection:
            cursor = connection.cursor()
            query = "INSERT INTO vendes (producte, quantitat, preu, data_venda) VALUES (%s, %s, %s, %s)"
            dades = (entrada_producte.get(), entrada_quantitat.get(), entrada_preu.get(), entrada_data.get())
            cursor.execute(query, dades)
            connection.commit()
            cursor.close()
            connection.close()
            messagebox.showinfo("Èxit", "Venda registrada correctament")
            carregar_dades_vendes()
            entrada_producte.delete(0, 'end')
            entrada_quantitat.delete(0, 'end')
            entrada_preu.delete(0, 'end')
            entrada_data.delete(0, 'end')

    # Ampliació 1: Funcionalitat d'actualització de dades
    def carregar_venda_seleccionada():
        try:
            selected_item = vendes_tree.selection()[0]  # Obté l'ID de l'element seleccionat
            dades = vendes_tree.item(selected_item, 'values')
            entrada_producte.delete(0, 'end')
            entrada_producte.insert(0, dades[0])
            entrada_quantitat.delete(0, 'end')
            entrada_quantitat.insert(0, dades[1])
            entrada_preu.delete(0, 'end')
            entrada_preu.insert(0, dades[2])
            entrada_data.delete(0, 'end')
            entrada_data.insert(0, dades[3])
        except IndexError:
            messagebox.showwarning("Selecció requerida", "Selecciona una venda per carregar les dades.")

    def actualitzar_venda():
        try:
            selected_item = vendes_tree.selection()[0]
            connection = connectar_bbdd()
            if connection:
                cursor = connection.cursor()
                query = "UPDATE vendes SET producte=%s, quantitat=%s, preu=%s, data_venda=%s WHERE id=%s"
                dades = (
                entrada_producte.get(), entrada_quantitat.get(), entrada_preu.get(), entrada_data.get(), selected_item)
                cursor.execute(query, dades)
                connection.commit()
                cursor.close()
                connection.close()
                messagebox.showinfo("Èxit", "Venda actualitzada correctament")
                carregar_dades_vendes()
        except IndexError:
            messagebox.showwarning("Selecció requerida", "Selecciona una venda per actualitzar.")

    # Ampliació 2: Funcionalitat d'eliminació de vendes
    def eliminar_venda():
        try:
            selected_item = vendes_tree.selection()[0]
            connection = connectar_bbdd()
            if connection:
                cursor = connection.cursor()
                query = "DELETE FROM vendes WHERE id=%s"
                cursor.execute(query, (selected_item,))
                connection.commit()
                cursor.close()
                connection.close()
                messagebox.showinfo("Èxit", "Venda eliminada correctament")
                carregar_dades_vendes()
        except IndexError:
            messagebox.showwarning("Selecció requerida", "Selecciona una venda per eliminar.")

    # Ampliació 3: Generació d'informes en PDF
    def generar_informe_pdf():
        connection = connectar_bbdd()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT producte, quantitat, preu, data_venda FROM vendes")
            records = cursor.fetchall()
            cursor.close()
            connection.close()

            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", "B", 12)
            pdf.cell(200, 10, "Informe de Vendes", ln=True, align="C")
            pdf.ln(10)

            pdf.set_font("Arial", "B", 10)
            pdf.cell(50, 10, "Producte", 1)
            pdf.cell(30, 10, "Quantitat", 1)
            pdf.cell(30, 10, "Preu", 1)
            pdf.cell(40, 10, "Data de Venda", 1)
            pdf.ln()

            pdf.set_font("Arial", "", 10)
            for record in records:
                pdf.cell(50, 10, str(record[0]), 1)
                pdf.cell(30, 10, str(record[1]), 1)
                pdf.cell(30, 10, str(record[2]), 1)
                pdf.cell(40, 10, str(record[3]), 1)
                pdf.ln()

            pdf.output("informe_vendes.pdf")
            messagebox.showinfo("Informe generat",
                                "L'informe de vendes s'ha generat correctament com a informe_vendes.pdf")

    def obtenir_personal():
        connexio = connectar_bbdd()
        cursor = connexio.cursor(dictionary=True)
        cursor.execute("SELECT * FROM personal")
        personal = cursor.fetchall()
        connexio.close()
        return personal

    # Disposició horitzontal dels botons en una sola fila
    button_frame = tk.Frame(entry_frame, bg="#f4f4f9")
    button_frame.grid(row=1, column=0, columnspan=8, pady=10)

    tk.Button(button_frame, text="Registrar Venda", command=inserir_venda, bg="#007bff", fg="white").grid(row=0,
                                                                                                          column=0,
                                                                                                          padx=5)
    tk.Button(button_frame, text="Carregar Venda", command=carregar_venda_seleccionada, bg="#17a2b8", fg="white").grid(
        row=0, column=1, padx=5)
    tk.Button(button_frame, text="Actualitzar Venda", command=actualitzar_venda, bg="#ffc107", fg="black").grid(row=0,
                                                                                                                column=2,
                                                                                                                padx=5)
    tk.Button(button_frame, text="Eliminar Venda", command=eliminar_venda, bg="#dc3545", fg="white").grid(row=0,
                                                                                                          column=3,
                                                                                                          padx=5)
    tk.Button(button_frame, text="Generar Informe PDF", command=generar_informe_pdf, bg="#28a745", fg="white").grid(
        row=0, column=4, padx=5)

