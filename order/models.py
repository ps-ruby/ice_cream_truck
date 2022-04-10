from django.db import models
from food_items.models import FoodItem
from user.models import User


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    price = models.FloatField(max_length=5)
    quantity = models.IntegerField(default=1)

