from django.shortcuts import render

# Create your views here.

def index(request):
    context ={}
    return render(request, "index.html", context)

def features(request):
    context ={}
    return render(request, "features.html", context)