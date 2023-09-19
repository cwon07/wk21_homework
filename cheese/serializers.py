from .models import Cheese
from rest_framework import serializers

class CheeseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cheese
        fields = ['id', 'name', 'origin_country', 'type']