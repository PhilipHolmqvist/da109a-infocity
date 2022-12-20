import requests
import json

#Author: Sossio Giorgelli, version 1

def get_cityWeather(countryName): #dayLimit shall be 4
    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

    querystring = {
        "q": countryName,
        "days": 3
    }

    headers = {
        "X-RapidAPI-Key": "0ab490636dmsh7da5c2757e98131p159b59jsn6b2e12133ae3",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.request(
        "GET", 
        url, 
        headers=headers, 
        params=querystring
    )
    
    response_data = response.json()

    print(response_data['location']['name'] + ", " + response_data['location']['country'])

    #for s in response_data['forecast']['forecastday'].keys():
    #   print(("Min temp: " + response_data['day']['mintemp_c'] + " C, Max temp: " + response_data['day']['maxtemp_c'] + " C"))
    
    print(response_data['forecast']['forecastday'][0]['date'])
    print("Temp: " + str(response_data['forecast']['forecastday'][0]['day']['avgtemp_c']) + " C")
    print("Temp: " + str(response_data['forecast']['forecastday'][0]['day']['maxwind_kph']) + " kph")
    print("Temp: " + str(response_data['forecast']['forecastday'][0]['day']['daily_chance_of_rain']) + " %")
    print("Temp: " + str(response_data['forecast']['forecastday'][0]['day']['condition']['icon']))

    print(response_data['forecast']['forecastday'][1]['date'])
    print("Temp: " + str(response_data['forecast']['forecastday'][1]['day']['avgtemp_c']) + " C")
    print("Temp: " + str(response_data['forecast']['forecastday'][1]['day']['maxwind_kph']) + " kph")
    print("Temp: " + str(response_data['forecast']['forecastday'][1]['day']['daily_chance_of_rain']) + " %")
    print("Temp: " + str(response_data['forecast']['forecastday'][1]['day']['condition']['icon']))

    print(response_data['forecast']['forecastday'][2]['date'])
    print("Temp: " + str(response_data['forecast']['forecastday'][2]['day']['avgtemp_c']) + " C")
    print("Temp: " + str(response_data['forecast']['forecastday'][2]['day']['maxwind_kph']) + " kph")
    print("Temp: " + str(response_data['forecast']['forecastday'][2]['day']['daily_chance_of_rain']) + " %")
    print("Temp: " + str(response_data['forecast']['forecastday'][2]['day']['condition']['icon']))

    #Old
    #print(response_data['forecast']['forecastday'][1]['date'])
    #print("Min temp: " + str(response_data['forecast']['forecastday'][1]['day']['mintemp_c']) + " C, Max temp: " + str(response_data['forecast']['forecastday'][1]['day']['maxtemp_c']) + " C")

    #print(response_data['forecast']['forecastday'][2]['date'])
    #print("Min temp: " + str(response_data['forecast']['forecastday'][2]['day']['mintemp_c']) + " C, Max temp: " + str(response_data['forecast']['forecastday'][2]['day']['maxtemp_c']) + " C")