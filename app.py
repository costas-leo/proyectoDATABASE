from flask import Flask, request, jsonify
import mysql.connector
from datetime import datetime
from conexion import Cconexion
app = Flask(__name__)

# Configuración de conexión a la base de datos
conexion = Cconexion.conexionDataBase()

# Endpoint para calcular el gasto del usuario
@app.route('/calcular_gasto', methods=['POST'])
def calcular_gasto():
    try:
        # Obtener los datos de la solicitud
        data = request.json
        telefono = data.get('telefono')
        fecha_inicio = data.get('fecha_inicio')
        fecha_fin = data.get('fecha_fin')

        # Validar los datos
        if not telefono or not fecha_inicio or not fecha_fin:
            return jsonify({'error': 'Faltan datos obligatorios'}), 400

        # Conexión a la base de datos
        conn = mysql.connector.connect(conexion)
        cursor = conn.cursor()

        # Consulta para calcular el gasto
        query = """
            SELECT
                SUM(
                    CASE
                        WHEN llamadas.tipo = 'Internacional' THEN llamadas.duracion * 0.75
                        WHEN llamadas.tipo = 'Nacional' THEN 2.5
                        WHEN llamadas.tipo = 'Amigos' THEN
                            CASE
                                WHEN amigos.amigos_count > 10 THEN 0
                                ELSE 2.5
                            END
                        ELSE 0
                    END
                ) AS costo_total
            FROM llamadas
            LEFT JOIN (
                SELECT numDeSalida, COUNT(*) AS amigos_count
                FROM llamadas
                WHERE tipo = 'Amigos'
                GROUP BY numDeSalida
            ) AS amigos ON llamadas.numDeSalida = amigos.numDeSalida
            WHERE llamadas.numDeSalida = %s
              AND llamadas.fecha BETWEEN %s AND %s;
        """
        cursor.execute(query, (telefono, fecha_inicio, fecha_fin))
        resultado = cursor.fetchone()
        costo_total = resultado[0] if resultado[0] else 0.0

        # Cerrar conexión
        cursor.close()
        conn.close()

        # Respuesta
        return jsonify({
            'telefono': telefono,
            'fecha_inicio': fecha_inicio,
            'fecha_fin': fecha_fin,
            'costo_total': round(costo_total, 2)
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Iniciar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
