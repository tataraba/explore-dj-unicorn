from django.db import models

class Meal(models.Model):
    TYPE_OF_MEAL = {
        "B": "Breakfast",
        "L": "Lunch",
        "D": "Dinner",
        "S": "Snack",
    }
    name = models.CharField(max_length=100)
    primary_food_group = models.CharField(max_length=100)
    secondary_food_group = models.CharField(max_length=100)
    type_of_meal = models.CharField(max_length=1, choices=TYPE_OF_MEAL.items())
    
    def __str__(self):
        return self.name