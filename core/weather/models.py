# weather/models.py

from django.db import models

class Weather(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    description = models.CharField(max_length=255)
    wind_speed = models.FloatField()

    def __str__(self):
        return f"{self.city} - {self.temperature}°C"
