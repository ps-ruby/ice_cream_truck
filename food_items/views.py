from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from django.shortcuts import get_object_or_404


class FoodItemViews(APIView):
    def get(self, request, id=None):
        if id:
            item = get_object_or_404(FoodItem, pk=id)
            serializer = FoodItemSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = FoodItem.objects.all()
        serializer = FoodItemSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
