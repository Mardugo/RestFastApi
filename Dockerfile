# Usar la imagen oficial de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo de requerimientos
COPY requirements.txt requirements.txt

# Instalar dependencias
RUN pip install -r requirements.txt

# Copiar el contenido del proyecto
COPY . .

EXPOSE 8000

# Realizar las migraciones y correr el servidor
CMD ["python3 app/app.py"]
