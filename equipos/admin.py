from django.contrib import admin
from .models import Equipo, Jugador
# Register your models here.
class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'equipo', 'equipo_nombre')
    autocomplete_fields = ['equipo']