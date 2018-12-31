from django.shortcuts import render
import requests
from .models import City


# Create your views here.

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=98028dd10f4f33d1dda8948b10115977'
    cities = City.objects.all()

    if request.method == 'POST':
        form = CityForm(request.POST) 
        form.save() 

    form = cityForm()

    weather_data = []

    for city in cities:

        city_weather = requests.get(url.format(city)).json()

        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }

        weather_data.append(weather)

    context = {'weather_data' : weather_data, 'form' : form}

    return render(request, 'weather_app/weather.html', context)
