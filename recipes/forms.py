from django.forms import ModelForm
from recipes.models import Recipe
from django import forms

class CreateRecipeForm(ModelForm):
    ingrediants=forms.CharField(widget=forms.Textarea)
    class Meta:
        model=Recipe
        fields=["recipe_name","ingrediants","category","recipe_img","created_by"]


