from django.urls import path
from . import views

urlpatterns = [
    path("", views.preguntas, name="preguntas"),
    path("<int:pregunta_id>/", views.detalle, name="detalle"),
]