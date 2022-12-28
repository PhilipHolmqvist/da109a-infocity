# *****************************************
# Author: Sossio Giorgelli, version 1
# *****************************************

# This file fetches information from weatherapi-com for specific city.

# Import required recources. 
import requests
import json

# Method to return city weather.
def get_cityWeather(countryName):
    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

    querystring = {
        # Required Query parameter of city name, string.
        "q": countryName, 

        # Optional Query parameter to show day limit (max 3 allowed for this subscription).
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

    # Return response as a json format.
    response_data = response.json()

    data = json.loads(response.text)
    return data

    # Det som händer nedan finns i main.py.
    ''' 
    # City name, city country.
    #print(response_data['location']['name'] + ", " + response_data['location']['country'])
    response_data['location']['name'] + ", " + response_data['location']['country']
    
    for x in range(3):
        # City date of day 1
        #print(response_data['forecast']['forecastday'][x]['date'])
        response_data['forecast']['forecastday'][x]['date']

        # City temperature.
        #print("Temp: " + str(response_data['forecast']['forecastday'][x]['day']['avgtemp_c']) + " C")
        "Temp: " + str(response_data['forecast']['forecastday'][x]['day']['avgtemp_c']) + " C"

        # City wind.
        #print("Temp: " + str(response_data['forecast']['forecastday'][x]['day']['maxwind_kph']) + " kph")
        "Temp: " + str(response_data['forecast']['forecastday'][x]['day']['maxwind_kph']) + " kph"

        # City chance of rain.
        #print("Temp: " + str(response_data['forecast']['forecastday'][x]['day']['daily_chance_of_rain']) + " %")
        "Temp: " + str(response_data['forecast']['forecastday'][x]['day']['daily_chance_of_rain']) + " %"

        # City weather icon.
        #print("Temp: " + str(response_data['forecast']['forecastday'][x]['day']['condition']['icon']))
        "Temp: " + str(response_data['forecast']['forecastday'][x]['day']['condition']['icon'])
    '''