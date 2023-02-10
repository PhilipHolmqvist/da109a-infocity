# **********************************************
# Den här klassen är huvud filen för projektet.
# **********************************************

# -*- coding: utf-8 -*-
import time, json, string

from flask import Flask, jsonify, request, url_for, render_template, abort
from flask_cors import CORS


from APIer.geodb import get_cityDetails
from APIer.geodb import get_cityTime
from APIer.geodb import get_countryDetails
from APIer.weather import get_cityWeather
from APIer.currencyConverter import get_rate


#Startar servern direkt när man trycker "play". Servern kör på port 6969.
#eller när man skriver:
#    python Backend\main.py


app = Flask(__name__)
CORS(app)




# ****************************
# Route /cityname
# ****************************
@app.route('/city/<string:cityname>', methods=['GET']) #Första bokstaven i stadens namn måste alltid vara stor!!!
def searchCity(cityname):


    if request.method == 'GET' and cityname != "favicon.ico":

        print("Cityname: " + cityname)

        # Konstruera JSON fil enligt API Dokumentationen.
        cityInfo = get_cityDetails(cityname.capitalize())
        cityWeather = get_cityWeather(cityname.capitalize())
        time.sleep(1) # Pausa 1 s pga. api begräsningar.
        countryInfo = get_countryDetails(cityInfo['data']['countryCode'])
        currencyto = countryInfo['data']['currencyCodes']
        currencyto = json.dumps(currencyto, indent=None)
        currencyto = currencyto.replace('[', '').replace(']', '').replace('"','')
        currencyConversion = get_rate("EUR", currencyto, 10)
        
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
        city['elevationMeters'] = cityInfo['data']['elevationMeters']
        city['weather'] = weather
        city['longitud'] = cityInfo['data']['longitude']
        city['latitude'] = cityInfo['data']['latitude']

        jsondata = {}
        jsondata['wikidataID'] = countryInfo['data']['numRegions']
        jsondata['countryName'] = countryInfo['data']['name']
        jsondata['flagImgUri'] = countryInfo['data']['flagImageUri']
        jsondata['capital'] = countryInfo['data']['capital']
        jsondata['callingCode'] = countryInfo['data']['callingCode']
        jsondata['currencyCodes'] = countryInfo['data']['currencyCodes']
        jsondata['tenEuroConversion'] = currencyConversion['rates'][currencyto]['rate_for_amount']
        jsondata['currentRate'] = currencyConversion['rates'][currencyto]['rate']
        jsondata['numRegions'] = countryInfo['data']['numRegions']
        jsondata['city'] = city      

        print("-----------------------------")
        print("Server sending response data:")
        print("-----------------------------")
        print("Egen Json")
        #print(jsondata)
        #print("Long: " + str(jsondata['city']['longitud']))
        #print("Lat: " + str(jsondata['city']['latitude']))

        return (jsondata)
    else:
        print("Fatal error 505: favicon not found.")
        return("Infocity error")


@app.route('/convert', methods=['GET'])
def currExchange():
    from_currency = request.args.get('from')
    to_currency = request.args.get('to')
    amount = request.args.get('amount')

    result = get_rate(from_currency, to_currency, amount)

    print("-----------------------------")
    print("Server sending currency response data:")
    print("-----------------------------")
    print(result)
    return result

if __name__ == "__main__":
    app.run("localhost", 6969)    

#app.run(debug=True)
#app.logger.debug()
#app.logger.error()