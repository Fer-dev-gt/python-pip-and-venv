FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# El lado derecho es local, el izquierdo es el contenedor
COPY requirements.txt /app/requirements.txt

# Esta linea instala las dependencias del proyecto, --no-cache-dir es para que no se guarde en cache y --upgrade es para que actualice las dependencias
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copia el contenido de la carpeta actual a la carpeta /app del contenedor
COPY . /app

# Este comando de Bash hace que el contenedor se ejecute en modo infinito
CMD bash -c "while true; do sleep 1; done"