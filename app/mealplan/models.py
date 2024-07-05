from django.db import models

class Meal(models.Model):
    MEALS = {
        "B": "Breakfast",
        "L": "Lunch",
        "D": "Dinner",
        "S": "Snack",
    }
    name = models.CharField(max_length=100)
    primary_food_group = models.CharField(max_length=100)
    secondary_food_group = models.CharField(max_length=100)
    meal = models.CharField(max_length=1, choices=MEALS.items())

