from rest_framework import serializers
from .models import *
from order.models import *


class FlavorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flavor
        fields = ('id', 'name')


class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = ('id', 'name')


class FoodItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=32)
    price = serializers.FloatField()
    quantity = serializers.IntegerField(required=False, default=0)
    flavors = FlavorSerializer(many=True)
    truck = TruckSerializer()

    class Meta:
        model = FoodItem
        fields = '__all__'


class TruckListSerializer(serializers.ModelSerializer):
    food_items = FoodItemSerializer(many=True)
    total_amount = serializers.SerializerMethodField()

    def get_total_amount(self, obj):
        total = 0.0
        for item in OrderItem.objects.filter(food_item__truck_id=obj.id):
            print(item.price)
            total += (item.quantity * item.price)
        return total

    class Meta:
        model = Truck
        fields = ('id', 'name', 'food_items', 'total_amount')
