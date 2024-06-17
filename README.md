# AppWebb EatnGo 

------------

##Pasos para poder levantar aplicación en tu PC

1. [crear base de datos Postgres en windows.](https://neunapp.com/contenido/crear-base-de-datos-postgres-en-windows-10-desde-sqlshell-19082 "crear base de datos Postgres en windows.")

2. Crear un entorno virtual (en pycharm es fácil)

3. Instalar Dependencias (usar el manejador de paquetes pip de python):

```bash
pip install django==4.2
pip install psycopg2
pip install unipath
```

4. Crear un archivo secret.json ( A la altura de manage) y coloca tus propias credenciales

```json
{
    "FILENAME": "secret.json",
    "SECRET_KEY": "tuCodigoDJango",
    "DB_LOCAL_NAME": "NombredeTuBaseDeDatos",
    "USER_DB": "tuUsuario",
    "PASSWORD_DB": "TuContraseña",
}
```
