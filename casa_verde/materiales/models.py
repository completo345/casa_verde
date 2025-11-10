
from django.db import models
from django.contrib.auth.models import User

class DatosTerreno(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    # Opciones de provincias y comunas (solo Región de Valparaíso)
    PROVINCIAS = [
        ('Valparaíso', 'Valparaíso'),
        ('Marga Marga', 'Marga Marga'),
        ('Quillota', 'Quillota'),
        ('Petorca', 'Petorca'),
        ('San Antonio', 'San Antonio'),
        ('San Felipe de Aconcagua', 'San Felipe de Aconcagua'),
        ('Los Andes', 'Los Andes'),
        ('Isla de Pascua', 'Isla de Pascua'),
    ]

    provincia = models.CharField(max_length=50, choices=PROVINCIAS)
    comuna = models.CharField(max_length=50)

    orientacion_terreno = models.CharField(
        max_length=50,
        choices=[
            ('Norte', 'Norte'),
            ('Sur', 'Sur'),
            ('Este', 'Este'),
            ('Oeste', 'Oeste'),
        ]
    )
    pendiente_terreno = models.CharField(
        max_length=50,
        choices=[
            ('Plana', 'Plana'),
            ('Moderada', 'Moderada'),
            ('Empinada', 'Empinada'),
        ]
    )
    exposicion_solar = models.CharField(
        max_length=50,
        choices=[
            ('Alta', 'Alta'),
            ('Media', 'Media'),
            ('Baja', 'Baja'),
        ]
    )
    velocidad_viento = models.CharField(
        max_length=50,
        choices=[
            ('Alta', 'Alta'),
            ('Media', 'Media'),
            ('Baja', 'Baja'),
        ]
    )
    tipo_suelo = models.CharField(
        max_length=50,
        choices=[
            ('Rocoso', 'Rocoso'),
            ('Arenoso', 'Arenoso'),
            ('Arcilloso', 'Arcilloso'),
            ('Mixto', 'Mixto'),
        ]
    )

    def __str__(self):
        return f"Datos de terreno de {self.usuario.username}"


class Material(models.Model):
    CATEGORIAS = [
        ('estructura', 'Estructura y obra gruesa'),
        ('aislacion', 'Aislamiento térmico y acústico'),
        ('muros', 'Muros y tabiquería'),
        ('cubiertas', 'Cubiertas y techos'),
        ('maderas', 'Maderas y acabados'),
        ('revestimientos', 'Revestimientos y pisos'),
        ('instalaciones', 'Instalaciones y eficiencia energética'),
        ('naturales', 'Muros y soluciones naturales'),
        ('ventanas', 'Ventanas y carpinterías'),
        ('sistemas', 'Sistemas complementarios'),
    ]

    categoria = models.CharField(
        max_length=50,
        choices=CATEGORIAS,
        default='estructura',
        verbose_name="Categoría"
    )
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.get_categoria_display()})"

