# Stock Trading
# Created by Maximillian M. Estrada on 2024-05-16

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from core.models import Order
from core.serializers import OrderSerializer, OrderBulkSerializer
from core.permissions import IsOwner
from core.services import TransactionService


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


class OrderBulkView(generics.CreateAPIView):
    serializer_class = OrderBulkSerializer
    permission_classes = [IsAdminUser | IsOwner]

    def post(self, request, filename, format="text/csv"):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if serializer.validated_data['to_stored']:
            is_stored = TransactionService.store_bulk_order_file(
                user=request.user,
                filename=filename,
                file=serializer.validated_data['file'],
            )
            if is_stored:
                return Response(
                    {"message": f"Bulk order file {filename} was stored."},
                    status=status.HTTP_201_CREATED)
            return Response(
                {"message": "Unable to store bulk order file."},
                status=status.HTTP_400_BAD_REQUEST)

        transactions = TransactionService.bulk_orders(
            user=request.user,
            filename=filename,
            file=serializer.validated_data['file'],
        )
        serializer = OrderSerializer(transactions, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
