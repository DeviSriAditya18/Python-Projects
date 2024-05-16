import datetime as dt
import requests

api_key="d305bd7e8213c204917ce4ca61a88d77"

user_input=input("Enter city: ")

weather_data=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod']=='404':
    print("No city found...")
else:
    weather=weather_data.json()['weather'][0]['main']
    temp=round(weather_data.json()['main']['temp'])

    print(f"The Weather in {user_input} is: {weather}")
    print(f"The Temperature in {user_input} is: {temp}°F")
