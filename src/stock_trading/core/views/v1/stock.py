# Stock Trading
# Created by Maximillian M. Estrada on 2024-05-15

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from core.models import Stock
from core.serializers import StockSerializer


class StockListView(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [IsAuthenticated]


class StockDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [IsAuthenticated]
