# Formativa1W

**Formativa1W** es una aplicación web desarrollada con **Django 5.2** que permite a los usuarios explorar y comprar videojuegos. La plataforma ofrece una experiencia intuitiva para la navegación de productos, gestión de cuentas y procesos de compra.

## 🛠️ Tecnologías Utilizadas

- **Framework:** Django 5.2  
- **Lenguajes:** Python, HTML, CSS, JavaScript  
- **Base de Datos:** SQLite (por defecto en Django)

## ⚙️ Funcionalidades Principales

- Visualización de un catálogo de videojuegos
- Detalle individual de cada producto
- Carrito de compras para gestionar selecciones
- Proceso de compra con confirmación
- Gestión de usuarios: registro, inicio de sesión y cierre de sesión
- Panel de administración para la gestión de productos y pedidos

## 🚀 Instalación y Ejecución

1. Clona el repositorio:

```bash
git clone https://github.com/Lmondaca/Formativa1W.git
cd Formativa1W
```

2. Crea y activa un entorno virtual:

```bash
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
```

3. Instala las dependencias:

```bash
python -m pip install Django
pip install django oracledb
pip install python-dotenv
pip install pillow
```

4. Aplica las migraciones:

```bash

python manage.py makemigrations
python manage.py migrate

```

5. Inicia el servidor de desarrollo:

```bash
python manage.py runserver
```

6. Abre tu navegador en:

```
http://127.0.0.1:8000/
```


