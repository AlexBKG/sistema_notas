from django.urls import path
from .views import home  # Importamos la vista que mostraremos

urlpatterns = [
    path("", home, name="home"),  # Página principal
]
