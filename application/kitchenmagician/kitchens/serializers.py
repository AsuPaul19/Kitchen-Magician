from rest_framework import serializers
from kitchens.models import Kitchen

#   Kitchen Serializer


class KitchenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kitchen
        fields = '__all__'
