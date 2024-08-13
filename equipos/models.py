from django.db import models

# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    conferencia = models.CharField(max_length=50)
    division = models.CharField(max_length=50)
    nombre_completo = models.CharField(max_length=50)
    abreviacion = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre_completo

class Jugador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    equipo = models.ForeignKey(Equipo, on_delete=models.PROTECT, related_name='jugadores')
    posicion = models.CharField(max_length=50, default = 'no especificado')
    dorsal = models.CharField(max_length=50, default = 'no especificado')
    altura = models.CharField(max_length=50, default = 'no especificado')
    peso = models.CharField(max_length=50, default = 'no especificado')
    fecha_nacimiento = models.DateField(default= '2000-01-01')
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
