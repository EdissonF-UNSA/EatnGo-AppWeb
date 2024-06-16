import psycopg2
from EatnGo_AppWeb.settings.local import get_secret

def ejecutar_comandos_sql():
    try:
        conn = psycopg2.connect(
            dbname=get_secret('DB_LOCAL_NAME'),
            user=get_secret('USER_DB'),
            password=get_secret('PASSWORD_DB'),
            host='localhost',
            port='5432'
        )
        cursor = conn.cursor()

        # Ejemplo de inserción de datos
        cursor.execute("""
            INSERT INTO GestionSucursales_franquicias (nombre, direccion, telefono, email, gerente)
            VALUES (%s, %s, %s, %s, %s);
        """, ('Nombre Franquicia', 'Dirección Franquicia', '123456789', 'email@franquicia.com', 'Gerente Franquicia'))

        # Ejemplo de consulta de datos
        cursor.execute("SELECT * FROM GestionSucursales_franquicias;")
        franquicias = cursor.fetchall()
        print("Lista de franquicias:")
        for franquicia in franquicias:
            print(franquicia)

        conn.commit()
        print("Operaciones SQL ejecutadas correctamente.")

    except psycopg2.Error as e:
        print(f"Error al ejecutar comandos SQL: {e}")

    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Conexión cerrada.")

if __name__ == "__main__":
    print("Iniciando ejecución de comandos CRUD con sentencias SQL...\n")
    ejecutar_comandos_sql()
