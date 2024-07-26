from rest_framework import serializers
from .models import Equipo, Jugador

class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields =('id','nombre','ciudad','conferencia','division','nombre_completo','abreviacion')
        read_only_fields = fields

class JugadorSerializer(serializers.ModelSerializer):
    #va fuera de la clase meta ya que no es un campo directamente relacionado a la bd de Jugador
    equipo_nombre = serializers.StringRelatedField(source = 'equipo', read_only = True) #StringRelatedField(source = 'equipo', read_only = True) hace que nos muestre el __str__ de la clase Equipo
    class Meta:
        model = Jugador
        fields = ('id', 'nombre', 'apellido', 'equipo', 'equipo_nombre', 'posicion', 'altura', 'dorsal', 'fecha_nacimiento', 'peso',)
        