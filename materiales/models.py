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

