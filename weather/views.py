from django.shortcuts import render
from django.contrib import messages
import requests
import datetime
from django.contrib.auth.decorators import login_required

@login_required(login_url='/users/login')
def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'london'     
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=d374a9444c47816f7f4b8733f68565dc'
    PARAMS = {'units':'metric'}

    # API_KEY =  'AIzaSyA_0NqxiXm6S-lMazam4MqvKTkMrPo_SFY'

    # SEARCH_ENGINE_ID = '868fee028221e42c5'
    
    # query = city + " 1920x1080"
    # page = 1
    # start = (page - 1) * 10 + 1
    # searchType = 'image'
    # city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

    # data = requests.get(city_url).json()
    # count = 1
    # search_items = data.get("items")
    # image_url = search_items[1]['link']
    

    try:  
        data = requests.get(url,params=PARAMS).json()
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        day = datetime.date.today()

        return render(request,'weather_home.html' , {'description':description , 'icon':icon ,'temp':temp , 'day':day , 'city':city , 'exception_occurred':False})
    
    except KeyError:
        exception_occurred = True
        messages.error(request,'Entered data is not available to API')   
        day = datetime.date.today()

        return render(request,'weather_home.html' ,{'description':'clear sky', 'icon':'01d'  ,'temp':25 , 'day':day , 'city':'indore' , 'exception_occurred':exception_occurred } )
    
    