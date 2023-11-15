# views.py
import requests
from django.shortcuts import render

def index(request):
    weather_data = None 

    if request.method == 'POST':
        city = request.POST.get('city')
        if city:
            geo_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid='
            geo_response = requests.get(geo_url)
            if geo_response.status_code == 200:
                geo_data = geo_response.json()
                if geo_data:
                    lat = geo_data[0]['lat']
                    lon = geo_data[0]['lon']
                    
                    weather_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid='
                    weather_response = requests.get(weather_url)
                    if weather_response.status_code == 200:
                        weather_data = weather_response.json()
                        print(weather_data)
    
    return render(request, 'weather/weather.html', {'weather_data': weather_data})
