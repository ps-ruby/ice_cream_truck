from rest_framework import serializers
from .models import *
from food_items.serializers import FoodItemSerializer
from drf_writable_nested import WritableNestedModelSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    food_item = FoodItemSerializer()

    class Meta:
        model = OrderItem
        fields = ('id', 'quantity', 'price', 'food_item')


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'order_items', 'created_at')


class CreateOrderItemSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(min_value=1)
    price = serializers.FloatField(read_only=True)

    class Meta:
        model = OrderItem
        fields = ('quantity', 'food_item', 'price')

    def validate(self, data):
        if data['quantity'] > data['food_item'].quantity:
            raise serializers.ValidationError({"quantity": "is more than available quantity"})
        return data


class CreateOrderSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    order_items = CreateOrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'order_items', 'user', 'created_at')
