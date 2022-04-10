from django.db import models
from food_items.models import FoodItem
from user.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    price = models.FloatField(max_length=5, null=True)
    quantity = models.IntegerField(default=1)

    class Meta:
        unique_together = [['order', 'food_item']]


@receiver(post_save, sender=OrderItem)
def update_item(sender, **kwargs):
    order_item = kwargs['instance']
    food_item = order_item.food_item
    OrderItem.objects.filter(id=order_item.id).update(price=food_item.price)
    food_item.quantity = food_item.quantity - order_item.quantity
    food_item.save()
