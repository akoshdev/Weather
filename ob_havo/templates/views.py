from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# city = "London"
# country_code = "UK"
# location = city+','+country_code
# APIKEY = '53dc894d6fe5612c69a7eaf3b13d2059' #get an api key from openweathermap.org
# url = "http://api.openweathermap.org/data/2.5/find?q=%s&units=metric&APPID=%s" %(location,APIKEY)\
# response = requests.get(url)
# response_dict = json.loads(response.text)



def home(request):
    return render(request, 'index.html')

def obhavo(request):
    user_city = request.GET['usertext_city']
    user_country = request.GET['usertext_country']
    city = user_city
    country_code = user_country
    location = city + ',' + country_code
    APIKEY = '53dc894d6fe5612c69a7eaf3b13d2059'  # get an api key from openweathermap.org
    url = "http://api.openweathermap.org/data/2.5/find?q=%s&units=metric&APPID=%s" % (location,APIKEY)
    response = requests.get(url)
    response_dict = json.loads(response.text)
    temp = response_dict["list"][0]["main"]["temp"]
    davlenie = response_dict["list"][0]["main"]["pressure"]
    vlajnost = response_dict["list"][0]["main"]["humidity"]
    return render(request,'obhavo.html',{'temp':temp,'user_city':user_city,'davlenie':davlenie,'vlajnost':vlajnost})