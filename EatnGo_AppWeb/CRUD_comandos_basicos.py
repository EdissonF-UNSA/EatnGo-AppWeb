import os
import django

# Configura el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EatnGo_AppWeb.settings.local')
django.setup()

# Importa tus modelos después de django.setup()
from aplicaciones.GestionSucursales.franquicias.models import Franquicia

def ejecutar_comandos_sql():
    print("Iniciando ejecución de comandos CRUD con sentencias SQL...\n")

    # Crear una nueva franquicia usando el ORM de Django
    print("Creando nueva franquicia...")
    nueva_franquicia = Franquicia.objects.create(
        nombre='Franquicia A',
        direccion='Calle Falsa 123',
        telefono='555-1234',
        email='franquiciaa@example.com',
        gerente='Juan Pérez'
    )
    print("Franquicia creada:", nueva_franquicia)

    # Listar todas las franquicias
    print("\nListando franquicias:")
    franquicias = Franquicia.objects.all()
    for franquicia in franquicias:
        print(franquicia)

    # Actualizar la dirección de la franquicia creada
    print("\nActualizando dirección de franquicia...")
    nueva_franquicia.direccion = 'Avenida Siempre Viva 742'
    nueva_franquicia.save()
    print("Dirección actualizada:", nueva_franquicia)

    # Borrar la franquicia creada
    print("\nBorrando franquicia...")
    franquicia_borrada = Franquicia.objects.get(nombre='Franquicia A')
    franquicia_borrada.delete()
    print("Franquicia borrada:", franquicia_borrada)

# Ejecutar los comandos CRUD
if __name__ == "__main__":
    ejecutar_comandos_sql()
