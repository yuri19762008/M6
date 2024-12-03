
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inputbook/', views.input_book, name='input_book'),
    path('delete/<int:pk>/', views.BookDeleteView.as_view(), name='book_delete'),
]