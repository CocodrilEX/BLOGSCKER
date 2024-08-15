# Usa una imagen base oficial de Python
FROM python:3.10-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos del proyecto
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Define la variable de entorno para Flask
ENV FLASK_APP=app/__init__.py

# Expone el puerto en el que Flask correrá
EXPOSE 5000

# Comando para correr la aplicación
CMD ["flask", "run", "--host=0.0.0.0"]
