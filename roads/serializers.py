from rest_framework import serializers
from .models import Road


# Road Serializers
class RoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Road
        fields = '__all__'
