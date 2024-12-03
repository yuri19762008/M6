

# Create your views here.
# book/views.py
from django.shortcuts import render
from .forms import BookForm

def input_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            # Aquí puedes procesar los datos del formulario
            # Por ejemplo, guardar en la base de datos
            pass
    else:
        form = BookForm()
    return render(request, 'input_book.html', {'form': form})

def home(request):
    return render(request, 'home.html')