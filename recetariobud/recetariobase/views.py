from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "recetariobase/home.html")

def ver_recetas(request):
    return render(request, "recetariobase/ver_recetas.html")

def agregar_receta(request):
    return render(request, "recetariobase/agregar_receta.html")