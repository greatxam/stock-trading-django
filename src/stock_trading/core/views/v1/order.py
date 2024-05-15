# Stock Trading
# Created by Maximillian M. Estrada on 2024-05-16

from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from core.models import Order
from core.serializers import OrderSerializer
from core.permissions import IsOwner


class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser | IsOwner]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(user=self.request.user)


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser | IsOwner]
