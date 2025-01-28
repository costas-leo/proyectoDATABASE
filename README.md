# Facturación Telefónica

Este proyecto es una aplicación backend desarrollada con Python y Flask para calcular los costos de facturación de usuarios basándose en un registro de llamadas. La aplicación interactúa con una base de datos MySQL que almacena la información de usuarios, llamadas y boletas de facturación.

## Características

- **Tipos de llamadas:** Nacionales, Internacionales y Amigos.
- **Tarifas:**
  - Llamadas Nacionales: \$2.5 por llamada.
  - Llamadas Internacionales: \$0.75 por segundo.
  - Llamadas con Amigos: Gratuitas hasta 10 llamadas.
- **Base de datos:** MySQL con relaciones entre tablas para usuarios, amigos, llamadas y boletas.
- **API REST:** Endpoint para calcular los costos de facturación de un usuario en un rango de fechas.

## Requisitos previos

- **Python 3.8+**
- **MySQL**
- **Postman** (opcional, para realizar pruebas de los endpoints)

## Instalación

1. Clona el repositorio:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd facturacion-telefonica
   ```

2. Crea un entorno virtual:

   ```bash
   python -m venv venv # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:

   ```bash
   pip install flask
   pip install mysql-connector-python
   ```

4. Configura la base de datos MySQL:

   - Asegúrate de tener MySQL instalado y en funcionamiento.

   - Crea la base de datos y tablas utilizando el archivo `schema.sql` proporcionado:

     ```sql
     CREATE DATABASE IF NOT EXISTS facturacion_telefonica;
     USE facturacion_telefonica;

     -- Copia y pega el contenido del archivo schema.sql
     ```

   - Inserta  los datos de prueba del archivo inserts\_de\_prueba.sql

5. Configura la conexión a la base de datos en el archivo principal:

   Edita las credenciales de la base de datos en el archivo Python:

   ```python
   conexion = {
       'host': 'localhost',
       'user': 'root',
       'password': '<TU_PASSWORD>',
       'database': 'facturacion_telefonica'
   }
   ```

6. Ejecuta la aplicación:

   ```bash
   python app.py
   ```

   La aplicación estará disponible en `http://localhost:5000`.

## Uso

### Endpoint: `/calcular_gasto`

- **Método:** `POST`

- **URL:** `http://localhost:5000/calcular_gasto`

- **Cuerpo de la solicitud (JSON):**

  ```json
  {
      "telefono": "+5491123456789",
      "fecha_inicio": "2025-01-10 00:00:00",
      "fecha_fin": "2025-01-13 23:59:59"
  }
  ```

- **Respuesta esperada:**

  ```json
  {
      "telefono": "+5491123456789",
      "fecha_inicio": "2025-01-10 00:00:00",
      "fecha_fin": "2025-01-13 23:59:59",
      "costo_total": 150.00
  }
  ```

## Estructura del proyecto

```
.
├── app.py                 # Archivo principal de la aplicación
├── schema.sql             # Esquema de la base de datos
├── README.md              # Documentación del proyecto
├── venv/                  # Entorno virtual (excluido del repositorio)
├── inserts_de_prueba.sql  # inserts de Mysql para realizar las pruebas
├── conexion.py            # establece la  conexion con la base de datos   
```


## Tecnologías utilizadas

- **Python:** Lenguaje principal del proyecto.
- **Flask:** Framework para el desarrollo de la API REST.
- **MySQL:** Base de datos relacional para almacenar los datos de usuarios, llamadas y boletas.
