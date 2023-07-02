from rest_framework import routers
from .api import ApiViewSet
#from api import views

router = routers.DefaultRouter()

#indicamos la ruta,trabaja con el conjunto de datos de viewset, nombre de la ruta
router.register('persona',ApiViewSet, 'final')
#router.register('v1',views.PersonaViewSet, 'final')

#indicamos que las rutas se encarga de generarlas el router
urlpatterns = router.urls