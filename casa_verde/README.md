# Documentación del Proyecto Django: `casa_verde`

## 1. Descripción general
El proyecto **`casa_verde`** es una aplicación web construida con **Django 5.2.5** que permite:

- Registro y autenticación de usuarios (`registro_user`)
- Gestión de materiales (`materiales`)
- Protección de rutas privadas (solo usuarios autenticados pueden acceder a ciertas páginas)

Flujo de la aplicación

- Usuario accede a /usuarios/registro/ para crear cuenta.
- Tras registro, se redirige automáticamente a home.
- Usuario puede iniciar sesión en /usuarios/login/.
- Si intenta acceder a rutas protegidas (home o materiales) sin login → se redirige a login.
- Logout en /usuarios/logout/ → redirige a login.
