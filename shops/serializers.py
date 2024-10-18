# shops/serializers.py

from rest_framework import serializers
from .models import Shop
from django.core.validators import MinValueValidator, MaxValueValidator

class ShopSerializer(serializers.ModelSerializer):
    latitude = serializers.FloatField(
        validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)]
    )
    longitude = serializers.FloatField(
        validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)]
    )

    class Meta:
        model = Shop
        fields = ['id', 'name', 'latitude', 'longitude', 'created_at']
        read_only_fields = ['id', 'created_at']

class ShopRegistrationSerializer(serializers.ModelSerializer):
    latitude = serializers.FloatField(
        validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)]
    )
    longitude = serializers.FloatField(
        validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)]
    )

    class Meta:
        model = Shop
        fields = ['name', 'latitude', 'longitude']