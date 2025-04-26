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


from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
