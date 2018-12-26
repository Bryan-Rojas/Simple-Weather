from django.shortcuts import render
import requests


# Create your views here.

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=98028dd10f4f33d1dda8948b10115977'
    city = 'Hawthorne'
    city_weather = requests.get(url.format(city)).json()

    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }

    context = {'weather' : weather}
    
    return render(request, 'weather_app/weather.html', context)
