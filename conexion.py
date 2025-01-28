import mysql.connector

class Cconexion:
    
    @staticmethod
    def conexionDataBase():
        try:
            conexion = mysql.connector.connect(user="root", host="127.0.0.1", database="facturacion_telefonica")
            print("Conexión correcta")
            return conexion
        except mysql.connector.Error as error:
            print(f"Error al conectarte a la base de datos: {error}")
            return None
    conexionDataBase()