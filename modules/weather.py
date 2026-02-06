import requests
from config import IP_API_KEY , WEATHER_IP_KEY

base_ip_url="https://api.ipgeolocation.io/v2/ipgeo?apiKey="
base_weather_url = f"http://api.weatherapi.com/v1/current.json?key=apikey&q=city&lang=en"

def location():
    url = base_ip_url + IP_API_KEY
    responce = requests.get(url)

    if responce.status_code == 200:
        data = responce.json()
        city = data["location"]["city"]
        return city
    
    else:
        return None

def get_weather():
    city = location()
    url = base_weather_url.replace("city",city).replace("apikey",WEATHER_IP_KEY)
    responce = requests.get(url)
    if responce.status_code == 200:
        data = responce.json()
        weather = data["current"]
        temp = weather["temp_c"]
        condition = weather["condition"]["text"]
        feels_like = weather["feelslike_c"]
        wind_speed = weather["wind_kph"]
        humidity = weather["humidity"]
        vis = weather["vis_km"]

        message = (
                    f"In {city}, it's {temp} degree Celsius with {condition} weather.\n"
                    f"It feels like {feels_like} degree Celsius.\n"
                    f"Humidity is {humidity} percent.\n"
                    f"Wind speed is {wind_speed} kilometers per hour.\n"
                    f"Visibility is {vis} kilometers.\n")

        return message
    else:
        return None

