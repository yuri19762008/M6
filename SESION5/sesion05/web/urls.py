
from django.urls import path
from .views import index, features

urlpatterns = [
    path("", index, name = "index"),
    path("features/", features, name = "features"),
    
]
