# Stock Trading
# Created by Maximillian M. Estrada on 2024-05-15

from rest_framework import serializers

from core.models import *
from core.services import TransactionService


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'


class StockRelatedField(serializers.RelatedField):
    def get_queryset(self):
        return Stock.objects.all()

    def to_representation(self, value):
        # TODO: fix render to browser
        return StockSerializer(value).data

    def to_internal_value(self, data):
        stock = Stock.objects.get(pk=data)
        return stock


class OrderSerializer(serializers.ModelSerializer):
    stock = StockRelatedField()

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


class OrderBulkSerializer(serializers.Serializer):
    file = serializers.FileField()
    to_stored = serializers.BooleanField(default=False)

    class Meta:
        fields = ('file', 'to_stored')


class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = '__all__'
        read_only_fields = [
            'user',
            'status',
            'amount',
        ]


class PortfolioSerializer(serializers.ModelSerializer):
    market_price = serializers.SerializerMethodField()
    market_value = serializers.SerializerMethodField()

    class Meta:
        model = Portfolio
        fields = '__all__'

    def get_market_price(self, obj):
        return obj.get_market_price()

    def get_market_value(self, obj):
        return obj.get_market_value()
