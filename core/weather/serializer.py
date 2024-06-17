from rest_framework import serializers
from .models import WeatherEntity

class WeatherSerializer(serializers.Serializer):
    id = serializers.CharField(allow_blank=True, required=False)
    city_name = serializers.CharField(required=False, allow_blank=True)
    temperature = serializers.FloatField()
    atmospheric_pressure = serializers.FloatField(required=False)
    humidity = serializers.FloatField(required=False)
    precipitation_percentage = serializers.FloatField(required=False)
    weather_conditions = serializers.CharField(required=False, allow_blank=True)
    date_time = serializers.DateTimeField(required=False)

    def create(self, validated_data):
        return WeatherEntity(**validated_data)