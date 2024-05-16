# Stock Trading
# Created by Maximillian M. Estrada on 2024-05-16

from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from core.models import Trade
from core.serializers import TradeSerializer
from core.permissions import IsOwner


class TradeListView(generics.ListAPIView):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer
    permission_classes = [IsAdminUser | IsOwner]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Trade.objects.all()
        return Trade.objects.filter(user=self.request.user)


class TradeDetailView(generics.RetrieveAPIView):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer
    permission_classes = [IsAdminUser | IsOwner]

