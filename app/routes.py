"""
Módulo que define las rutas de la aplicación Flask.

Actualmente contiene una única ruta ('/') que:
- Carga un listado de países desde un archivo CSV.
- Permite buscar países por nombre (búsqueda parcial).
- Permite ordenar por distintos campos (nombre, población, etc.).
- Implementa paginación para mostrar los resultados por partes.
"""

from app import app
from flask import render_template, request
from app.utils import cargar_paises_desde_csv, calcular_estadisticas

@app.route("/")
def inicio():
    """
    Ruta principal de la aplicación.

    Realiza las siguientes operaciones:
    1. Carga datos desde 'data/paises.csv' mediante una función utilitaria.
    2. Filtra los países por nombre si se especifica el parámetro 'buscar' en la URL.
    3. Ordena los países por un campo determinado (nombre, población, etc.).
    4. Aplica paginación para mostrar un número limitado de países por página.
    5. Renderiza el template 'index.html' con los datos procesados.

    Parámetros aceptados por la URL (query string):
    - buscar: término de búsqueda (str).
    - ordenar: campo por el cual ordenar ('nombre', 'poblacion', 'superficie', 'continente').
    - direccion: 'asc' para ascendente, 'desc' para descendente.
    - page: número de página (int).

    Returns:
        HTML renderizado con los países filtrados, ordenados y paginados.
    """
    
    # Carga todos los países desde el archivo CSV devolviendo una lista de diccionarios
    paises = cargar_paises_desde_csv("data/paises.csv")

    # FILTRO POR NOMBRE DE PAÍS (búsqueda parcial)
    termino = request.args.get('buscar', '').strip().lower()
    if termino:
        paises = [p for p in paises if termino in p["nombre"].lower()]

    # ORDENAMIENTO por campo y dirección (asc o desc)
    campo_orden = request.args.get('ordenar', 'nombre')
    direccion = request.args.get('direccion', 'asc')
    campos_validos = ['nombre', 'poblacion', 'superficie', 'continente']
    if campo_orden in campos_validos:
        reverse = (direccion == 'desc')
        paises.sort(key=lambda x: x[campo_orden], reverse=reverse)

    # PAGINACIÓN: se muestra de a 10 países por página
    pagina = request.args.get('page', 1, type=int)
    per_page = 10
    start = (pagina - 1) * per_page
    end = start + per_page
    paises_pagina = paises[start:end]
    total_paginas = (len(paises) + per_page - 1) // per_page  # redondeo hacia arriba

    return render_template(
        "index.html",
        paises=paises_pagina,
        pagina=pagina,
        total_paginas=total_paginas,
        ordenar=campo_orden,
        direccion=direccion,
        buscar=termino,
        total_paises_csv=len(cargar_paises_desde_csv("data/paises.csv")),
        total_filtrados=len(paises)
    )
@app.route('/estadisticas')
def estadisticas():
    # 1. Cargar TODOS los datos (usamos la misma ruta que la func 'inicio')
    paises = cargar_paises_desde_csv("data/paises.csv")
    
    # 2. Calcular las estadísticas con la nueva función de utils.py
    stats = calcular_estadisticas(paises)
    
    # 3. Mostrar la nueva plantilla HTML y pasarle los datos
    return render_template('estadisticas.html', estadisticas=stats)