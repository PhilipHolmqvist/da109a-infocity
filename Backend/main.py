# -*- coding: utf-8 -*-
from flask import Flask, request
from flask import render_template

from APIer.geodb import get_cityDetails
from APIer.geodb import get_cityTime
from APIer.geodb import get_countryDetails
from APIer.weather import get_cityWeather

# python -m venv myenv --för att skapa en ny virtuell miljö
# $env:FLASK_APP = "main.py"  --berätta för flask var applikation finnns
# flask run --kör servern

app = Flask(__name__)
 # setup(): Nödvändiga saker som ska göras när servern startar.

#cityDetails = get_cityDetails("Malmö")
cityWeather = get_cityWeather("Lund")

# Definera ändpunkter för de olika API metoderna.
#@app.route("/<input>", methods=['GET']) #Lista alla enhörningar
#def list_cities(input): 
 #       return "The input was: " + str(input) #Begäran vill ha svar i HTML

#Söksida route.
@app.route("/<cityname>", methods=['GET'])
def searchCity(cityname):

    #Konstruera JSON fil enligt API Dokumentationen.
    city = get_cityDetails(cityname)
    country = get_countryDetails()

    jsondata = {}
    jsondata['wikidataID'] = ''
    jsondata['countryName'] = ''
    jsondata['flagImgUri'] = ''
    jsondata['capital'] = ''
    jsondata['callingCode'] = ''
    jsondata['currencyCodes'] = ''
    jsondata['tenEuroConversion'] = ''
    jsondata['numRegions'] = ''
    jsondata['city'] = city

    city = {}
    city['name'] = ''
    city['region'] = ''
    city['population'] = ''
    city['wikidataID'] = ''
    city['elevationMeters'] = ''
    city['weather'] = weather

    weather = {}
    weather['DayOne'] = weatherDayOne
    weather['DayTwo'] = weatherDayTwo
    weather['DayThree'] = weatherDayThree

    weatherDayOne = {}
    weatherDayOne['tempAvg'] = ''
    weatherDayOne['windMax'] = ''
    weatherDayOne['chanceOfRain'] = ''
    weatherDayOne['icon'] = ''

    weatherDayTwo = {}
    weatherDayTwo['tempAvg'] = ''
    weatherDayTwo['windMax'] = ''
    weatherDayTwo['chanceOfRain'] = ''
    weatherDayTwo['icon'] = ''

    weatherDayThree = {}
    weatherDayThree['tempAvg'] = ''
    weatherDayThree['windMax'] = ''
    weatherDayThree['chanceOfRain'] = ''
    weatherDayThree['icon'] = ''


    return(render_template("index.html"))

#Index route.
@app.route("/")
def index():
    return render_template('index.html') # You have to save the html files inside of a 'templates' folder.



#app.run(debug=True)