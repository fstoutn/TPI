# Aplicación Web de Países

Esta es una aplicación web desarrollada con Flask que permite visualizar y analizar información sobre países del mundo. La aplicación obtiene datos desde una API externa y proporciona una interfaz amigable para explorar esta información.

## Características

- Búsqueda de países por nombre
- Visualización de estadísticas
- Ordenamiento por diferentes campos (nombre, población, superficie, continente)
- Paginación de resultados
- Estadísticas detalladas
- Datos actualizados desde una API externa

## Requisitos

- Python 3.x
- Flask 2.3.2
- Requests 2.31.0
- Gunicorn (para despliegue)

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/fstoutn/TPI.git
   cd TPI
   ```

2. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Ejecutar la aplicación:
   ```bash
   python run.py
   ```

2. Abrir un navegador web y acceder a:
   ```
   http://localhost:5000
   ```

## Funcionalidades

### Página Principal
- Lista de países con información detallada
- Buscador de países por nombre
- Ordenamiento por columnas (nombre, población, superficie, continente)
- Navegación por páginas (10 países por página)

### Página de Estadísticas
- Accesible desde `/estadisticas`
- Muestra análisis estadísticos de los datos
- Incluye información sobre población y superficie por continente

## Estructura del Proyecto

```
.
├── app/
│   ├── static/          # Archivos estáticos (CSS)
│   ├── templates/       # Plantillas HTML
│   ├── routes.py       # Rutas de la aplicación
│   └── utils.py        # Funciones utilitarias
├── data/
│   └── paises.csv      # Datos de países (generado automáticamente)
├── Dockerfile          # Configuración para Docker
├── requirements.txt    # Dependencias del proyecto
└── run.py             # Punto de entrada de la aplicación
```

## Datos

La aplicación obtiene los datos de la API:
```
https://api-paises-zilz.onrender.com/paises
```

Los datos se almacenan localmente en un archivo CSV para mejor rendimiento y disponibilidad.

# Ejemplos de entradas y salidas

Cuando se busca un pais de manera parcial se ingresan los carateres en la barra de busqueda, al hacer click en el boton buscar se traen todas las coincidencias parciales de los paises que contienen dichos caracteres (salida)

Salida: El resultado de las estadisticas mostrado en su misma pestaña

# Particiacion de los integrantes
Franco Storani:
Crear repositorio en github
Crear el esqueleto del proyecto
Crear la pagina principal (index.html)

Facundo Degen
Crear el apartado de estadisticas
Encargado de dockerizar el proyecto finalizado

Tareas en conjunto:
Modificaciones en CSS
Correccion de errores en funciones del codigo
Testeo de funciones
Creacion del archivo "Informe"
Video explicativo

#VIDEO EXPLICATIVO
https://drive.google.com/file/d/1qrfj7Kj7mdBeC2zh3DISV2SPl89riGpe/view?usp=sharing