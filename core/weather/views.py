# weather/views.py

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .repositories import create_weather, get_all_weather, update_weather, delete_weather
from .forms import WeatherForm
import random

@api_view(['POST'])
def generate_random_weather(request):
    cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
    for city in cities:
        weather = {
            "city": city,
            "temperature": random.uniform(10, 30),
            "description": 'Sunny',
            "wind_speed": random.uniform(1, 10)
        }
        create_weather(weather)
    return Response({'message': 'Random weather data generated successfully'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def insert_weather(request):
    if request.method == 'POST':
        form = WeatherForm(request.data)
        if form.is_valid():
            create_weather(form.cleaned_data)
            return Response({'message': 'Weather data inserted successfully'}, status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        form = WeatherForm()
    return render(request, 'weather_list.html', {'form': form})

@api_view(['GET'])
def get_all_weather_view(request):
    weathers = get_all_weather()
    data = [{
        'id': str(weather['_id']),
        'city': weather['city'],
        'temperature': weather['temperature'],
        'description': weather['description'],
        'wind_speed': weather['wind_speed']
    } for weather in weathers]
    return render(request, 'weather_list.html', {'weather_list': data})

@api_view(['PUT'])
def update_weather_view(request, pk):
    weather_id = pk
    data = request.data
    form = WeatherForm(data)
    if form.is_valid():
        update_weather(weather_id, form.cleaned_data)
        return Response({'message': 'Weather data updated successfully'})
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_weather_view(request, pk):
    weather_id = pk
    delete_weather(weather_id)
    return Response({'message': 'Weather data deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
