# exam_empresariales

## 🚀 Instalación en local

Sigue los pasos para ejecutar el proyecto en tu entorno local:

### 1. Clonar el repositorio

    git clone https://github.com/Hector-Perez-Vengoa/exam_empresariales.git
    cd exam_empresariales

### 2. Crear y activar un entorno virtual

    python -m venv env

En Windows:

    venv\Scripts\activate

En macOS / Linux:

    source venv/bin/activate

### 3. Instalar dependencias

    pip install -r requirements.txt

### 4. Configurar base de datos

Aplica las migraciones iniciales:

    python manage.py makemigrations
    python manage.py migrate

### 5. Crear un superusuario (opcional)

    python manage.py createsuperuser

### 6. Ejecutar el servidor

    python manage.py runserver

Abre tu navegador y visita: http://127.0.0.1:8000