# -*- coding: utf-8 -*-
import time

from flask import Flask, request

from APIer.geodb import get_cityDetails
from APIer.geodb import get_cityTime
from APIer.geodb import get_countryDetails
from APIer.weather import get_cityWeather

# python -m venv myenv --för att skapa en ny virtuell miljö
# $env:FLASK_APP = "Backend\main.py"   --berätta för flask var applikation finnns
# flask run --kör servern

app = Flask(__name__)
 # setup(): Nödvändiga saker som ska göras när servern startar.

#cityWeather = get_cityWeather("Lund")

# Definera ändpunkter för de olika API metoderna.
#@app.route("/<input>", methods=['GET']) #Lista alla enhörningar
#def list_cities(input): 
 #       return "The input was: " + str(input) #Begäran vill ha svar i HTML

#Söksida route.
@app.route("/<cityname>", methods=['GET'])
def searchCity(cityname):

    #Konstruera JSON fil enligt API Dokumentationen.
    if request.method == 'GET' and cityname != "favicon.ico":
        #Första bokstaven i stadens namn måste alltid vara stor!!!
        cityInfo = get_cityDetails(cityname.capitalize())
        #cityInfo['data']['country']
        time.sleep(1)
        countryInfo = get_countryDetails(cityInfo['data']['countryCode'])
        print(countryInfo)
    
        weatherDayThree = {}
        weatherDayThree['tempAvg'] = ''
        weatherDayThree['windMax'] = ''
        weatherDayThree['chanceOfRain'] = ''
        weatherDayThree['icon'] = ''

        weatherDayTwo = {}
        weatherDayTwo['tempAvg'] = ''
        weatherDayTwo['windMax'] = ''
        weatherDayTwo['chanceOfRain'] = ''
        weatherDayTwo['icon'] = ''

        weatherDayOne = {}
        weatherDayOne['tempAvg'] = '23'
        weatherDayOne['windMax'] = '22'
        weatherDayOne['chanceOfRain'] = '1'
        weatherDayOne['icon'] = '123'

        weather = {}
        weather['DayOne'] = weatherDayOne
        weather['DayTwo'] = weatherDayTwo
        weather['DayThree'] = weatherDayThree

        city = {}
        city['name'] = cityInfo['data']['name'] 
        city['region'] = cityInfo['data']['region'] 
        city['population'] = cityInfo['data']['population'] 
        city['wikidataID'] = cityInfo['data']['wikiDataId'] 
        city['elevationMeters'] = '12m'
        city['weather'] = weather

        jsondata = {}
        jsondata['wikidataID'] = countryInfo['data']['numRegions']
        jsondata['countryName'] = countryInfo['data']['name']
        jsondata['flagImgUri'] = countryInfo['data']['flagImageUri']
        jsondata['capital'] = countryInfo['data']['capital']
        jsondata['callingCode'] = countryInfo['data']['callingCode']
        jsondata['currencyCodes'] = countryInfo['data']['currencyCodes']
        jsondata['tenEuroConversion'] = '100'
        jsondata['numRegions'] = countryInfo['data']['numRegions']
        jsondata['city'] = city      

    
    
        return (jsondata)

    else:
        print("favicon error")
        return("hej")    

@app.route("/")
def index():
    return ("hejsan") # You have to save the html files inside of a 'templates' folder.


#app.run(debug=True)