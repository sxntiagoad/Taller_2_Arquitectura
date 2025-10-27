# Imagen base: Python 3.11 en versión slim (más liviana)
FROM python:3.11-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos primero solo requirements.txt
COPY requirements.txt .

# Instalamos las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Ahora copiamos todo el código de la aplicación
COPY . .

# Exponemos el puerto 5000
EXPOSE 5000

# Variables de entorno
ENV FLASK_APP=run.py
ENV PYTHONUNBUFFERED=1

# Comando para ejecutar la aplicación
# Usamos gunicorn (servidor de producción)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "run:app"]