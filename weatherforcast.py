import requests
import datetime

api_key = '30d4741c779ba94c470ca1f63045390a'

user_input = input("Enter City: ") 

weather_data = requests.get(

    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")



e = datetime.datetime.now()

print ("\nToday's date: = %s/%s/%s" % (e.day, e.month, e.year))


if weather_data.json()['cod'] == '404':
    print("\nNo City Found")
else:

    weather = weather_data.json() ['weather'] [0] ['main'] 
    temp = weather_data.json() ['main'] ['temp']
    feels_like = weather_data.json() ['main'] ['feels_like']
    humidity = weather_data.json() ['main'] ['humidity']
    visibility = weather_data.json() ['visibility']
    wind = weather_data.json() ['wind']
    

    print(f"\nThe weather in {user_input} is: {weather}")
    print(f"\nThe temperature in {user_input} is: {temp}ºF and feels like {feels_like}ºF")
    print(f"\nThe humadity in {user_input} is: {humidity}%")
    print(f"\nThe visibility in {user_input} is: {visibility}")
    print(f"\nThe wind speed in {user_input} is: {wind}")