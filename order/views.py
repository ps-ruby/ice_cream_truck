from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


class OrderViews(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id=None):
        orders = Order.objects.filter(user=request.user)
        if id:
            item = get_object_or_404(orders, pk=id)
            serializer = OrderSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        serializer = OrderSerializer(orders, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
