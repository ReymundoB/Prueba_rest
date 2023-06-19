from rest_framework import routers
from .api import ApiViewSet

router = routers.DefaultRouter()

#indicamos la ruta,trabaja con el conjunto de datos de viewset, nombre de la ruta
router.register('final/api',ApiViewSet, 'final')

#indicamos que las rutas se encarga de generarlas el router
urlpatterns = router.urls