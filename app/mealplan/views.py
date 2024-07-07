from django.shortcuts import render
from django.http import HttpResponse

from .models import Meal

def index(request) -> HttpResponse:
    meals = Meal.objects.all()
    
    return render(request, "mealplan/meals.html", {"meals": meals})