from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index_personal' ),
    path('agregar/', views.agregar, name='nuevo'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('ver/<int:id>', views.ver, name='ver'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
]
