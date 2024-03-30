# VybzCafeProject\cafewebsite\serializers.py

from rest_framework import serializers
from .models import Menu, Update, HomePageSettings

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Update
        fields = '__all__'

class HomePageSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePageSettings
        fields = '__all__'
