
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BookForm
from .models import Book
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

def input_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro guardado exitosamente.')
            return redirect('input_book')
    else:
        form = BookForm()
    return render(request, 'libros/input_book.html', {'form': form})

def home(request):
    books = Book.objects.all()
    return render(request, 'libros/home.html', {'books': books})

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'libros/book_confirm_delete.html'
    success_url = reverse_lazy('home')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "El libro fue eliminado exitosamente.")
        return super().delete(request, *args, **kwargs)