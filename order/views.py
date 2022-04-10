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

    def post(self, request):
        serializer = CreateOrderSerializer(data={**request.data, 'user': request.user.id})
        if serializer.is_valid():
            serializer.save()
            return Response("ENJOY!", status=status.HTTP_200_OK)
        else:
            # return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            return Response("SORRY!", status=status.HTTP_400_BAD_REQUEST)
