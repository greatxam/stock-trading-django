# Stock Trading
# Created by Maximillian M. Estrada on 2024-05-15

from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from core.models import Portfolio
from core.serializers import PortfolioSerializer
from core.permissions import IsOwner


class PortfolioListView(generics.ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = [IsAdminUser | IsOwner]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Portfolio.objects.all()
        return Portfolio.objects.filter(user=self.request.user)
