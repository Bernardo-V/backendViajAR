from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('registrarTours/', views.registrarTours),
    path('edicionTours/<codigo>', views.edicionTours),
    path('editarTours/', views.editarTours),
    path('eliminarTours/<codigo>', views.eliminarTours)
]