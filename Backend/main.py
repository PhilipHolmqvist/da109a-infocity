# **********************************************
# Den här klassen är huvud filen för projektet.
# **********************************************

# -*- coding: utf-8 -*-
import time
import json
import string

from flask import Flask, request
from flask import render_template

from APIer.geodb import get_cityDetails
from APIer.geodb import get_cityTime
from APIer.geodb import get_countryDetails
from APIer.weather import get_cityWeather
from APIer.currencyConverter import get_rate

# OBSERVERA! Det som står nedan finns redan i projekt dokumentationen under rubriken 'Användarmanual'
# python -m venv myenv --för att skapa en ny virtuell miljö
# $env:FLASK_APP = "Backend\main.py"   --berätta för flask var applikation finnns
# flask run --kör servern

# Det som står efter __name__ är för att customiza sökvägen till filerna templates (html) samt static (css och js) för frontend.
app = Flask(__name__, template_folder='../FrontEnd/templates', static_folder='../FrontEnd/static') 
# setup(): Nödvändiga saker som ska göras när servern startar.

# Definera ändpunkter för de olika API metoderna.
#@app.route("/<input>", methods=['GET']) #Lista alla enhörningar
#def list_cities(input): 
#       return "The input was: " + str(input) #Begäran vill ha svar i HTML

# ****************************
# Route /
# ****************************
@app.route("/")
def main():
    return render_template('index.html') # You have to save the html files inside of a 'templates' folder.

@app.route("/index.html")
def index():
    return render_template('index.html') # You have to save the html files inside of a 'templates' folder.

@app.route("/info.html")
def info():
    return render_template('info.html') # You have to save the html files inside of a 'templates' folder.


# ****************************
# Route /cityname
# ****************************
@app.route('/<string:cityname>', methods=['GET'])
def searchCity(cityname):

    # Konstruera JSON fil enligt API Dokumentationen.
    if request.method == 'GET' and cityname != "favicon.ico":
        #Första bokstaven i stadens namn måste alltid vara stor!!!
        print("cityname: " + cityname)
        cityInfo = get_cityDetails(cityname.capitalize())
        cityWeather = get_cityWeather(cityname.capitalize())
        time.sleep(1) # Pausa 1 s pga. api begräsningar.
        countryInfo = get_countryDetails(cityInfo['data']['countryCode'])
        currencyto = countryInfo['data']['currencyCodes']
        currencyto = json.dumps(currencyto, indent=None)
        currencyto = currencyto.replace('[', '').replace(']', '').replace('"','')
        euroconversion = get_rate("EUR", currencyto, 10)
    
        weatherDayOne = {}
        weatherDayOne['tempAvg'] = cityWeather['forecast']['forecastday'][0]['day']['avgtemp_c']
        weatherDayOne['windMax'] = cityWeather['forecast']['forecastday'][0]['day']['maxwind_kph']
        weatherDayOne['chanceOfRain'] = cityWeather['forecast']['forecastday'][0]['day']['daily_chance_of_rain']
        weatherDayOne['icon'] = cityWeather['forecast']['forecastday'][0]['day']['condition']['icon']

        weatherDayTwo = {}
        weatherDayTwo['tempAvg'] = cityWeather['forecast']['forecastday'][1]['day']['avgtemp_c']
        weatherDayTwo['windMax'] = cityWeather['forecast']['forecastday'][1]['day']['maxwind_kph']
        weatherDayTwo['chanceOfRain'] = cityWeather['forecast']['forecastday'][1]['day']['daily_chance_of_rain']
        weatherDayTwo['icon'] = cityWeather['forecast']['forecastday'][1]['day']['condition']['icon']

        weatherDayThree = {}
        weatherDayThree['tempAvg'] = cityWeather['forecast']['forecastday'][2]['day']['avgtemp_c']
        weatherDayThree['windMax'] = cityWeather['forecast']['forecastday'][2]['day']['maxwind_kph']
        weatherDayThree['chanceOfRain'] = cityWeather['forecast']['forecastday'][2]['day']['daily_chance_of_rain']
        weatherDayThree['icon'] = cityWeather['forecast']['forecastday'][2]['day']['condition']['icon']

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
        jsondata['tenEuroConversion'] = euroconversion
        jsondata['numRegions'] = countryInfo['data']['numRegions']
        jsondata['city'] = city      

        print("Server sending response data")
        return (jsondata)

    else:
        print("Fatal error 505: favicon not found.")
        return("Infocity error")

#app.run(debug=True)