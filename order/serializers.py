from rest_framework import serializers
from .models import *
from food_items.serializers import FoodItemSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    food_item = FoodItemSerializer()

    class Meta:
        model = OrderItem
        fields = ('id', 'quantity', 'price', 'food_item')


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'order_items')
