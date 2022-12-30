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

#cityWeather = get_cityWeather("Lund")

# Definera ändpunkter för de olika API metoderna.
#@app.route("/<input>", methods=['GET']) #Lista alla enhörningar
#def list_cities(input): 
 #       return "The input was: " + str(input) #Begäran vill ha svar i HTML

#Söksida route.
@app.route("/<cityname>", methods=['GET'])
def searchCity(cityname):

    #Konstruera JSON fil enligt API Dokumentationen.
    if request.method == 'GET':
        #Första bokstaven i stadens namn måste alltid vara stor!!!
        city = get_cityDetails(cityname.capitalize())
        print("response text:" + city.text)

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

    return ("Test")

@app.route("/")
def index():
    return ("hejsan") # You have to save the html files inside of a 'templates' folder.

@app.route("/")
def style():
    return render_template('style.css')

@app.route("/")
def script():
    return render_template('weather.js')

#app.run(debug=True)