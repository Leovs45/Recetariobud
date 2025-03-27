from django.shortcuts import render
from .models import Receta, RecetaIngrediente
from collections import defaultdict
# Create your views here.
def home(request):
    return render(request, "recetariobase/home.html")

def ver_recetas(request):
    recetas_ingredientes = RecetaIngrediente.objects.select_related("receta", "ingrediente").all()
    
    # Agrupar los ingredientes por receta
    recetas_dict = defaultdict(list)
    for rec_ing in recetas_ingredientes:
        recetas_dict[rec_ing.receta].append(rec_ing)

    context = {"recetas_dict":recetas_dict}
    return render(request, "recetariobase/ver_recetas.html", context)



def agregar_receta(request):
    return render(request, "recetariobase/agregar_receta.html")