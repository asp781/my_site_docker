# from rest_framework import serializers
# from price.models import Category
# from online_registration.models import Order

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'


# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = '__all__'

from rest_framework import serializers
from secret2.models import Estimate, Purchased, Completed, Paid


class EstimateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estimate
        fields = '__all__'


class PurchasedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchased
        fields = '__all__'


class CompletedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Completed
        fields = '__all__'


class PaidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paid
        fields = '__all__'
