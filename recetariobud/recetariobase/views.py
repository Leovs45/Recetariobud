from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def ver_recetas(request):
    return render(request, "ver_recetas.html")

def agregar_receta(request):
    return render(request, "agregar_receta.html")