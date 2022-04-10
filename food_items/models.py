from django.db import models


class Truck(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Flavor(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    name = models.CharField(max_length=32)
    price = models.FloatField(max_length=5)
    quantity = models.IntegerField(default=0)
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE)
    flavors = models.ManyToManyField(Flavor)

    def __str__(self):
        return self.name
