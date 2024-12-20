from rest_framework import serializers
from .models import Main


class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Main
        fields = ('id', 'name', 'email', 'message')
