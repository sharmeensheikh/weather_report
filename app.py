import requests
from datetime import datetime

user_api = 'ae6e16f51a7cb9b2650e641c8fc3299b'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
api_link = requests.get(complete_api_link)
api_data = api_link.json()
# print(api_data)

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
humid = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print (f"Weather Report for - {location.upper()}  || {date_time}\n")

print ("Temperature          : {:.2f} deg C".format(temp_city))
print ("Weather Description  :",weather_desc.upper())
print ("Humidity             :",humid, '%')
print ("Wind speed           :",wind_spd ,'kmph')
