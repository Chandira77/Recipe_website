from django import forms
from .models import Recipes

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = ['name', 'category', 'description', 'process', 'ingredients', 'picture']
