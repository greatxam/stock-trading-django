# Stock Trading
# Created by Maximillian M. Estrada on 2024-05-15

from rest_framework import serializers

from core.models import *
from core.services import TransactionService


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = [
            'user',
            'status',
            'amount',
        ]

    def create(self, validated_data):
        return TransactionService.create_transaction(
            user=self.context.get('request').user,
            stock=validated_data.get('stock'),
            quantity=validated_data.get('quantity'),
            price=validated_data.get('price'),
            type=validated_data.get('type')
        )

    def save(self, **kwargs):
        self.instance = super().save(**kwargs)
        return TransactionService.save_transaction(self.instance)


class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = '__all__'
        read_only_fields = [
            'user',
            'status',
            'amount',
        ]
