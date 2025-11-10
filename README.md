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

## Datos que extrae api nasa power (5 años)
| Variable API        | Descripción                            | Unidad     | Usado para                                   |
| ------------------- | -------------------------------------- | ---------- | -------------------------------------------- |
| `T2M`               | Temperatura del aire a 2 metros        | °C         | Determinar clima promedio y eficiencia solar |
| `ALLSKY_SFC_SW_DWN` | Irradiancia solar diaria en superficie | kWh/m²/día | Evaluación paneles solares                   |
| `WS2M`              | Velocidad del viento a 2 metros        | m/s        | Evaluación energía eólica                    |

class ProvinciaDatos(models.Model):
  -  user = models.OneToOneField(User, on_delete=models.CASCADE)
  -  provincia = models.CharField(max_length=100)
  -  lat = models.FloatField()
  -  lon = models.FloatField()
  -  temp_avg = models.FloatField()  # temperatura promedio anual
  -  irr_avg = models.FloatField()   # irradiancia solar promedio
  -  wind_avg = models.FloatField()  # viento promedio
  -  fecha_actualizacion = models.DateTimeField(auto_now=True)

| Campo                 | Significado                          |
| --------------------- | ------------------------------------ |
| `provincia`           | Provincia elegida por el usuario     |
| `lat`, `lon`          | Coordenadas fijas predefinidas       |
| `temp_avg`            | Temperatura media histórica          |
| `irr_avg`             | Radiación solar media histórica      |
| `wind_avg`            | Velocidad media del viento           |
| `fecha_actualizacion` | Fecha de la última consulta a la API |
# Lo que falta
- Base de datos estatica de materiales
- funcion corazon
- front
  
