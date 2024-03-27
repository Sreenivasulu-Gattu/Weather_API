from django.shortcuts import render

# Create your views here.

from app.models import *
from datetime import datetime
import requests
from django.http import HttpResponse

def home(request):
    if request.method=='POST':
        try:
            city_name=request.POST['city']
            api_key = 'd75d9f2b156ecca338c132fb77343c4b'
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
            response = requests.get(url)
            weather_data = response.json()
            temperature = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
            weather=weather_data['main']['feels_like']
            speed=weather_data['wind']['speed']


            obj=WeatherData.objects.create(city=city_name, temperature=int(round(temperature/10,2))+3, humidity=humidity,weather=int(round(weather/10,2)+3), speed=speed)
        
            obj.timestamp += timedelta(hours=5,minutes = 30)
            obj.save()
            d={'obj':obj}

        except:

            d = {'':''}
        return render(request,'home.html',d)
    return render(request,'home.html')

def history(request):
    objs = WeatherData.objects.order_by('timestamp')
    return render(request,'history.html',{'objs':objs})

def submit_form(request):
    if request.method == 'POST':
        try:
            objs = WeatherData.objects.order_by(request.POST.get('option'))
        except:
            return HttpResponse('<center>Please enter correct option</center>')
        return render(request,'history.html',{'objs':objs})
    return render(request,'history.html')
    
def delete_req(request):
    return render(request,'delete_history.html')

def delete_history(request):
    if request.method == 'POST':
        WeatherData.objects.all().delete()
        return HttpResponse('<center>History everything is deleted </center>')
    return render(request,'delete_history.html')