import requests
import json
from flask import jsonify

# Author Philip Holmqvist

#Använder Wikipedias API för att få olika typer av information och listor

#Returnerar ett antal städer från ett visst land i sjunkande storleksordning.
def get_cities_in_country(country, nbrOfCities):
    url = "http://www.wikidata.org/w/api.php?action=query&list=list1&sites=enwiki&titles=Lists_of_cities_by_country&languages=en&format=json"
    response = requests.request("GET", url)
    response_data = response.json()
    print(response.text)



# Hjälp metod för övriga metoder.
def get_wikidataID(cityName):

    url = "http://www.wikidata.org/w/api.php?action=wbgetentities&sites=enwiki&titles=" + cityName + "&props=descriptions&languages=en&format=json"
    
    # will return "Q25796287" as the value of the "wikibase_item" key.

    response = requests.request("GET", url)
    response_data = response.json()
    
    cityID = 0

    for s in response_data['entities'].keys():
        cityID = s
    
    print("CityID:")
    print(cityID)

    return cityID