# Imagen base
FROM python:3.11-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar los archivos de dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación
COPY . .

# Exponer el puerto en el que corre Flask
EXPOSE 5000

# Variable de entorno para Flask
ENV FLASK_APP=run.py

# Comando por defecto para ejecutar la app
CMD ["python", "run.py"]
