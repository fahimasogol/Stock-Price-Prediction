from rest_framework import serializers

from stocks.serializers import StockSerializer
from .models import CustomUser, UserStockAlert


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class UserStockAlertSerializer(serializers.ModelSerializer):
    stock = StockSerializer()  # stock is nested and serialized using the StockSerializer.
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())  # user is a PrimaryKeyRelatedField

    # that relates to the CustomUser model, allowing you to set the user by their primary key.

    class Meta:
        model = UserStockAlert
        fields = ['id', 'user', 'stock', 'alert_price']
