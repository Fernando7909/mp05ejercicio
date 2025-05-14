import mysql.connector
from tkinter import messagebox


def connectar_bbdd():
    """Conecta a la base de datos MySQL y retorna la conexión."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            database="crm",  # Asegúrate de usar el nombre correcto de la base de datos
            user="root",
            password="root"
        )
        print("Conexión exitosa a la base de datos.")  # Añadir esta línea para verificar la conexión
        return connection
    except mysql.connector.Error as error:
        messagebox.showerror("Error de Conexión", f"No se pudo conectar a la base de datos:\n{error}")
        return None



def obtenir_productes():
    """Obtiene todos los productos del inventario desde la base de datos"""
    connexio = connectar_bbdd()
    if connexio is None:
        return []

    cursor = connexio.cursor()
    try:
        cursor.execute("SELECT id, nom_producte, preu FROM inventari")  # Usar 'nom_producte' en lugar de 'nom'
        productes = cursor.fetchall()
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"No se pudieron obtener los productos del inventario:\n{error}")
        productes = []
    finally:
        cursor.close()
        connexio.close()

    return productes


def obtenir_personal():
    """Obtiene datos de la tabla 'personal'."""
    connexio = connectar_bbdd()
    if connexio is None:
        return []
    cursor = connexio.cursor(dictionary=True)
    cursor.execute("SELECT * FROM personal")
    personal = cursor.fetchall()
    connexio.close()
    return personal





def obtenir_clients_empreses():
    """Obtiene datos de la tabla 'clients_empreses'."""
    connexio = connectar_bbdd()
    if connexio is None:
        return []
    cursor = connexio.cursor(dictionary=True)
    try:
        cursor.execute(
            "SELECT id_empresa, nom_empresa, cif, email_empresa, telefon_empresa, direccio_empresa, data_registre, actiu, comentaris FROM clients_empreses")
        clients_empreses = cursor.fetchall()
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"No se pudieron obtener los datos de los clientes empresas:\n{error}")
        clients_empreses = []
    connexio.close()
    return clients_empreses


def actualizar_preferente(id_personal, preferent):
    """Actualiza el estado preferente de una persona."""
    connexio = connectar_bbdd()
    if connexio is None:
        return
    cursor = connexio.cursor()
    try:
        cursor.execute("UPDATE personal SET preferent = %s WHERE id_personal = %s", (preferent, id_personal))
        connexio.commit()
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"No se pudo actualizar el estado preferente:\n{error}")
    finally:
        cursor.close()
        connexio.close()


def obtenir_inventari():
    """Obtiene todos los datos del inventario."""
    connexio = connectar_bbdd()
    cursor = connexio.cursor(dictionary=True)
    cursor.execute("SELECT * FROM inventari")
    inventari = cursor.fetchall()
    connexio.close()
    return inventari


def obtenir_clients_particulars(campos_complet=False):
    """Obtiene todos los clientes particulares desde la base de datos, con opción de obtener solo campos básicos."""
    connexio = connectar_bbdd()
    if connexio is None:
        return []

    cursor = connexio.cursor(dictionary=True)

    try:
        if campos_complet:
            cursor.execute(
                "SELECT id_client, nom, cognoms, dni, email, telefon, direccio, data_registre, actiu, comentaris FROM clients_particulars"
            )
        else:
            cursor.execute(
                "SELECT id_client, nom, cognoms FROM clients_particulars"
            )
        clients_particulars = cursor.fetchall()

        # Verificación de los datos obtenidos
        print("Datos obtenidos de la base de datos:", clients_particulars)

    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"No se pudieron obtener los datos de los clientes particulares:\n{error}")
        clients_particulars = []
    finally:
        cursor.close()
        connexio.close()

    return clients_particulars


