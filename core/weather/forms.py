# weather/forms.py

from django import forms
from .models import Weather

class WeatherForm(forms.ModelForm):
    class Meta:
        model = Weather
        fields = ['city', 'temperature', 'description', 'wind_speed']
