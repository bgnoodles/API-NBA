from .models import Equipo, Jugador
from rest_framework import viewsets, permissions
from .serializer import EquipoSerializer, JugadorSerializer

class EquipoViewSet(viewsets.ModelViewSet):
    queryset = Equipo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EquipoSerializer

class JugadorViewSet(viewsets.ModelViewSet):
    queryset = Jugador.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = JugadorSerializer