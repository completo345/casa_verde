from django.db import models
from django.contrib.auth.models import User

class ProvinciaDatos(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    provincia = models.CharField(max_length=100)
    lat = models.FloatField()
    lon = models.FloatField()

    temp_avg = models.FloatField(null=True, blank=True)  # Temperatura promedio
    irr_avg = models.FloatField(null=True, blank=True)   # Radiación solar promedio
    wind_avg = models.FloatField(null=True, blank=True)  # Viento promedio

    fecha_actualizacion = models.DateTimeField(auto_now=True)

    # Materiales seleccionados por el usuario para esta provincia (ManyToMany)
    materials = models.ManyToManyField('Material', blank=True, related_name='provincia_datos')

    def __str__(self):
        return f"{self.user.username} - {self.provincia}"

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
        verbose_name="Categoría"
    )
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    relevancia_temperatura = models.PositiveSmallIntegerField(
        default=0,
        verbose_name="Relevancia para Temperatura",
        help_text="Relevancia del material frente a temperaturas (0=nula, 3=alta)."
    )
    relevancia_radiacion = models.PositiveSmallIntegerField(
        default=0,
        verbose_name="Relevancia para Radiación Solar",
        help_text="Relevancia del material frente a radiación (0=nula, 3=alta)."
    )
    relevancia_viento = models.PositiveSmallIntegerField(
        default=0,
        verbose_name="Relevancia para Viento",
        help_text="Relevancia del material frente al viento (0=nula, 3=alta)."
    )

    def __str__(self):
        return f"{self.nombre} ({self.get_categoria_display()})"

    
