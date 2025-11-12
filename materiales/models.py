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

    def __str__(self):
        return f"{self.nombre} ({self.get_categoria_display()})"