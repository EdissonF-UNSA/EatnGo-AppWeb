import os
import django
from django.db import connection, transaction

# Configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EatnGo_AppWeb.settings.local')
django.setup()

def ejecutar_comandos_sql():
    print("Iniciando ejecución de comandos CRUD con sentencias SQL...\n")

    try:
        with connection.cursor() as cursor:
            # Crear nueva franquicia
            nombre = 'Nombre Franquicia'
            direccion = 'Dirección Franquicia'
            telefono = '123456789'
            email = 'email@franquicia.com'
            gerente = 'Gerente Franquicia'

            # Ejemplo de INSERT utilizando SQL
            insert_query = """
                INSERT INTO franquicias_franquicia (nombre, direccion, telefono, email, gerente)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, [nombre, direccion, telefono, email, gerente])
            transaction.commit()

            print("Franquicia creada exitosamente.")

    except Exception as e:
        print(f"Error al ejecutar comandos SQL: {e}")

    finally:
        # Cerrar la conexión
        connection.close()

def main():
    ejecutar_comandos_sql()
    print("\nOperaciones CRUD ejecutadas correctamente.")

if __name__ == "__main__":
    main()
