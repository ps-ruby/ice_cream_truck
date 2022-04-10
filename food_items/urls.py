from django.urls import path
from .views import *

urlpatterns = [
    path('food-items/', FoodItemViews.as_view()),
    path('food-items/<int:id>', FoodItemViews.as_view()),
]
