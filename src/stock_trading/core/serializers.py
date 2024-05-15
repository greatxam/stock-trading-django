# Stock Trading
# Created by Maximillian M. Estrada on 2024-05-15

from rest_framework import serializers

from core.models import *


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'
