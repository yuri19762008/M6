from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', include('Book.urls')),
    path('', RedirectView.as_view(url='/book/'), name='index'),
]