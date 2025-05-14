import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='localhost',  # Per exemple 'localhost'
        database='react_mysql_example',  # Nom de la base de dades
        user='root',  # Usuari MySQL
        password='root'  # Contrasenya de l'usuari MySQL
    )

    if connection.is_connected():
        print(f"Connectat a MySQL Server")
        cursor = connection.cursor()

        # Consulta SQL per obtenir dades
        query = "SELECT * FROM usuaris;"
        cursor.execute(query)
        resultats = cursor.fetchall()

        if resultats:
            for fila in resultats:
                print(fila)
        else:
            print("No s'han trobat dades.")

except Error as e:
    print(f"Error en connectar a MySQL: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Connexió MySQL tancada")
