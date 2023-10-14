# Utiliza una imagen base con Python y Flask
FROM python:3-alpine3.15

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY  . /app/

# Instala las dependencias
RUN pip install -r requirements.txt

# Expone el puerto en el que se ejecuta la aplicación
EXPOSE 3000

# Comando para ejecutar la aplicación
CMD python app.py
