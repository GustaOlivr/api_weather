from django.urls import path
from . import views

urlpatterns = [
    path('generate/', views.generate_random_weather),
    path('insert/', views.insert_weather),
    path('get-all/', views.get_all_weather_view),
    path('update/<str:pk>/', views.update_weather_view),
    path('delete/<str:pk>/', views.delete_weather_view),
]