from django.urls import path
from . import views

urlpatterns = [
    path('palindromo/<str:palabra>/', views.palindromo, name='palindromo'),
]
