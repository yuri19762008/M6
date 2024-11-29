from django.urls import path
from .views import index, navbar, listbook

urlpatterns = [
    path("", index, name="index"),
    path("navbar/", navbar, name = "navbar"),
    path("listbook/", listbook, name = "listbook"),
]