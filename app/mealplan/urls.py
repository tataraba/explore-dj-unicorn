from django.urls import path
from neapolitan.views import CRUDView

from . import views
from . import models

class MealView(CRUDView):
    model = models.Meal
    
    fields = ["name", "primary_food_group", "secondary_food_group", "type_of_meal"]


urlpatterns = [
    path("", views.index, name="index"),
]

urlpatterns += MealView.get_urls()