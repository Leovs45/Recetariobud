from django.shortcuts import render
from .models import Receta, RecetaIngrediente
# Create your views here.
def home(request):
    return render(request, "recetariobase/home.html")

def ver_recetas(request):
    recetas = Receta.objects.all()
    
    rec_ingredientes = []

    for receta in recetas:
        ingredientes = RecetaIngrediente.objects.filter(receta=receta)
        rec_ingredientes.append({"receta": receta, "ingredientes": ingredientes})
    context = {"recetas":recetas, "rec_ingredientes":rec_ingredientes}
    return render(request, "recetariobase/ver_recetas.html", context)

def agregar_receta(request):
    return render(request, "recetariobase/agregar_receta.html")