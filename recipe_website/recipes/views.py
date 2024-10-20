"""from multiprocessing import context
from django.shortcuts import render, HttpResponse, render

# Create your views here.
def index(request):
    
    people = [
        {"Name": "Momo", "Category": "veg", "Description" : "ghghfgfgdffhgyhg", "Ingredients" : "vegetables, flour", "Process" : "hgjhfjhhgjfkfhghu gghhgh", "Process" : "jdhjdh" },
        {"Name": "Chowmein", "Category": "veg", "Description" : "ghghfgfgdffhgyhg", "Ingredients" : "vegetables, raw chowmein", "Process" : "hgjhfjhhgjfkfhghu gghhgh", "Process" : "jdhjdh" },
        {"Name": "Pizza", "Category": "veg", "Description" : "ghghfgfgdffhgyhg", "Ingredients" : "vegetables", "Process" : "hgjhfjhhgjfkfhghu gghhgh", "Process" : "jdhjdh" },
    ]
    context = {
    'people' : people
    }
    return render(request,"index.html", context=context)
"""
from django.shortcuts import render, get_object_or_404, redirect

#from recipe_website import recipes

# from recipe_website import recipes
from .models import Recipes
from .forms import RecipeForm

def recipe_list(request,):
    recipes = Recipes.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipes, pk=pk)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'recipe_form.html', {'form': form})

def recipe_update(request, pk):
    recipe = get_object_or_404(Recipes, pk=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipe_form.html', {'form': form})

def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipes, pk=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipe_list')
    return render(request, 'recipe_confirm_delete.html', {'recipe': recipe})

"""
def contact(request):
    return HttpResponse("contact page")

def about(request):
    return HttpResponse("about us page")
"""