import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
# Create your views here.
def index(request):
    appid = '34eb2f310e07173e07b4520db9f81e60'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if request.method=='POST':
        form = CityForm(request.POST)
        form.save()
    form=CityForm()

    cities= City.objects.all()

    all_cities=[]

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info={
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"],
        }
        all_cities.reverse()
        all_cities.append(city_info)
        all_cities.reverse()

    context = {'all_info': all_cities,'form': form}

    return render(request, 'weather/index.html',context)

def about(request):
    return render(request, 'weather/about.html')
