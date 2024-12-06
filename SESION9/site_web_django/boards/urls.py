from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("datosform/", datosform_view, name="datosform"),
    path('registro/', registro_view, name="registro"),
]