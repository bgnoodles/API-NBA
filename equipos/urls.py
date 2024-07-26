from rest_framework import routers
from .api import EquipoViewSet, JugadorViewSet

router = routers.DefaultRouter()

router.register('api/equipos', EquipoViewSet, 'equipos')
router.register('api/jugadores', JugadorViewSet, 'jugadores')

urlpatterns = router.urls