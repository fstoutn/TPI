"""
run.py

Punto de entrada principal de la aplicación Flask.

Este archivo:
- Verifica si el archivo 'data/paises.csv' existe.
- Si no existe (o se desea actualizar), descarga los datos desde la API y genera el CSV.
- Luego inicia la aplicación Flask.
"""

import os
import csv
import requests
from app import app

# URL de la API
API_URL = "https://api-paises-zilz.onrender.com/paises"

# Ruta al archivo CSV
CSV_PATH = os.path.join("data", "paises.csv")


def generar_csv():
    """Descarga los datos de la API y genera el archivo CSV."""
    print("Generando archivo CSV con los datos de la API...")

    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Lanza error si la respuesta no es 200

        paises = response.json()

        # Asegura que el directorio 'data' exista
        os.makedirs("data", exist_ok=True)

        # Crea o sobrescribe el CSV
        with open(CSV_PATH, "w", newline="", encoding="utf-8") as csvfile:
            campos = ["pais", "poblacion", "superficie", "continente"]
            writer = csv.DictWriter(csvfile, fieldnames=campos)
            writer.writeheader()
            for pais in paises:
                writer.writerow({
                    "pais": pais.get("pais", ""),
                    "poblacion": pais.get("poblacion", ""),
                    "superficie": pais.get("superficie", ""),
                    "continente": pais.get("continente", "")
                })

        print(f"CSV generado correctamente en: {CSV_PATH}")

    except Exception as e:
        print(f"Error al generar el CSV: {e}")

#Generar el CSV 
generar_csv()

if __name__ == "__main__":

    # Inicia la aplicación Flask
    app.run(debug=True, host="0.0.0.0", port=5000)
