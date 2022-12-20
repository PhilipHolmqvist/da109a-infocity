import requests
import json

#Author: Sossio Giorgelli, version 1

def get_cityWeather(countryName, dayLimit): #dayLimit shall be 4
    url = "https://weatherapi-com.p.rapidapi.com/future.json"

    querystring = {
        "q": countryName,
        "days": dayLimit
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

    print(response.text)