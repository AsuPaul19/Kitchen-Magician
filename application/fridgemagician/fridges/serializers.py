from rest_framework import serializers
from fridges.models import Fridge

#   Fridge Serializer


class FridgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fridge
        fields = '__all__'