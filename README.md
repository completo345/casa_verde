# Documentación del Proyecto Django: `casa_verde`

## 1. Descripción general
El proyecto **`casa_verde`** es una aplicación web construida con **Django 5.2.5** que permite:

- Registro y autenticación de usuarios (`registro_user`)
- Gestión de materiales (`materiales`)
- Protección de rutas privadas (solo usuarios autenticados pueden acceder a ciertas páginas)

Proyecto_inicial/
│
├── casa_verde/ # Proyecto principal
│ ├── settings.py # Configuración de Django
│ ├── urls.py # URLs principales del proyecto
│ └── views.py # Vista de home
│
├── registro_user/ # App de usuarios
│ ├── urls.py # URLs de registro, login y logout
│ ├── views.py # Funciones de registro y login personalizado
│ ├── forms.py # Formulario de registro personalizado
│ └── templates/registro_user/ # Plantillas de login y registro
│ ├── login.html
│ └── registro.html
│
├── materiales/ # App de materiales
│ ├── urls.py # URLs de la app de materiales
│ ├── views.py # Funciones para ver lista de materiales
│ └── templates/materiales/ # Plantillas de materiales
│
├── templates/ # Plantillas globales del proyecto
│ └── home.html # Página home
│
├── manage.py # Script principal de Django
└── db.sqlite3 # Base de datos SQLite (generada tras migraciones)
