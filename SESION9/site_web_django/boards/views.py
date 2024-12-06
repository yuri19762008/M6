from django.shortcuts import render
from .forms import InputForm, RegistroUsuarioForm
from django.contrib.auth import login
from django.contrib import messages
from django.http import HttpResponseRedirect



def index(request):
    context = {}
    return render(request, "index.html", context)

def datosform_view(request):
    
    form = InputForm()
    context = { "form": form}
    

    return render(request, "datosform.html", context)


def registro_view(request):
    if request.method =="POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            print("Entré al formulario válido")
            user = form.save()
            login(request, user)
            messages.success(request, "Registrado exitosamente!")

            return HttpResponseRedirect('/')
        messages.error(request,"Registro inválido")
    
    form = RegistroUsuarioForm()
    context = { "register_form":form}
    return render(request, "registration/registro.html", context)