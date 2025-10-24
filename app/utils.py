"""
utils.py

Este módulo contiene funciones utilitarias para la aplicación.

Actualmente incluye:
- cargar_paises_desde_csv: lee un archivo CSV de países y devuelve los datos en forma estructurada.
"""

import csv

def cargar_paises_desde_csv(ruta_archivo):
    """
    Carga los datos de países desde un archivo CSV.

    Parámetros:
        ruta_archivo (str): Ruta relativa o absoluta al archivo CSV.

    Retorna:
        list[dict]: Una lista de diccionarios, cada uno representando un país con las claves:
            - "nombre" (str): nombre del país.
            - "poblacion" (int): población total.
            - "superficie" (int): superficie en km².
            - "continente" (str): continente al que pertenece.

    El archivo CSV debe tener las columnas:
        - pais
        - poblacion
        - superficie
        - continente

    Si ocurre un error al leer el archivo, se imprime un mensaje y se devuelve una lista vacía.
    """

    paises = []  # Lista que almacenará los países leídos

    try:
        # Abre el archivo en modo lectura, usando codificación UTF-8 y sin salto de línea adicional
        with open(ruta_archivo, newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)  # Lee cada fila como un diccionario

            for fila in lector:
                # Crea un nuevo diccionario para cada país, limpiando y convirtiendo los datos según sea necesario
                pais = {
                    "nombre": fila["pais"].strip(),
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"].strip()
                }
                paises.append(pais)  # Agrega el país a la lista

    except Exception as e:
        print(f"Error al leer el CSV: {e}")  # Muestra el error por consola, pero no detiene la app

    return paises  # Devuelve la lista completa de países
