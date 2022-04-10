from rest_framework import serializers
from .models import *


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
