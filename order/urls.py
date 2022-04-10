from django.urls import path
from .views import *

urlpatterns = [
    path('orders/', OrderViews.as_view()),
    path('orders/<int:id>', OrderViews.as_view()),
]
