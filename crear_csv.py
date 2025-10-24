import requests
import csv
import os

# URL de tu API en Render
API_URL = "https://api-paises-zilz.onrender.com/paises"

# Ruta donde vamos a guardar el CSV
CSV_PATH = os.path.join("data", "paises.csv")

def generar_csv():
    # Pedimos los datos a la API
    response = requests.get(API_URL)
    if response.status_code != 200:
        print(f"Error al acceder a la API: {response.status_code}")
        return

    paises = response.json()
    
    # Creamos el CSV con los encabezados correctos
    with open(CSV_PATH, "w", newline='', encoding='utf-8') as csvfile:
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

if __name__ == "__main__":
    generar_csv()
