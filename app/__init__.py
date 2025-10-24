"""
Este módulo inicializa la aplicación Flask.

- Crea una instancia de la aplicación (objeto `Flask`).
- Importa las rutas definidas en `routes.py` para que se registren en la app.

Este archivo convierte la carpeta `app/` en un paquete Python
y sirve como punto de inicio para la configuración y extensión de la aplicación.
"""

from flask import Flask

# Crea una instancia de la aplicación Flask.
# El argumento '__name__' le dice a Flask dónde buscar recursos como templates o archivos estáticos.
app = Flask(__name__)

# Importa las rutas de la aplicación.
# Esto debe hacerse después de crear la app para evitar errores de importación circular.
from app import routes
