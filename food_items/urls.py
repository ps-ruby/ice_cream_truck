from django.urls import path
from .views import *

urlpatterns = [
    path('trucks/', TruckViews.as_view()),
    path('trucks/<int:id>', TruckViews.as_view()),
    path('food-items/', FoodItemViews.as_view()),
    path('food-items/<int:id>', FoodItemViews.as_view()),
]
