"""
run.py

Este archivo actúa como punto de entrada principal para iniciar la aplicación Flask.

- Importa la instancia de la aplicación (`app`) desde el paquete `app`.
- Ejecuta la aplicación si el archivo es ejecutado directamente (no importado).
"""

from app import app

# Verifica si este archivo se está ejecutando directamente (no importado como módulo)
if __name__ == "__main__":
    # Inicia la aplicación Flask en modo debug
    # Esto permite ver errores detallados en el navegador y recarga automática al cambiar el código
    app.run(debug=True)
