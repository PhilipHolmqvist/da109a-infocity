import requests
import json
from flask import jsonify

# Author Philip Holmqvist

# Använder GeoDB Cities API. Få information om städer, regioner och länder.
# Resultaten kan filtreras till att återfås på olika språk.
# Samtliga resultat returneras i JSON format.
# Länk: https://rapidapi.com/wirefreethought/api/geodb-cities/


# Vilket land och region staden finns i. Latitud och Longitud grader. Invånare i staden. Meter över havet. Tidzon.
def get_cityDetails(cityName):
    cityID = get_wikidataID(cityName)

    url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities/" + cityID

    headers = {
	    "X-RapidAPI-Key": "8c68386795msh15e8293dd2e776bp12364ajsnd16271373457",
	    "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    data = json.loads(response.text)
    return data
    

# Returnerar stadens tid i ISO-8601 format: HHmmss.SSSZ
def get_cityTime(cityName):
    cityID = get_wikidataID(cityName)
    url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities/" + cityID + "/dateTime"

    headers = {
	    "X-RapidAPI-Key": "8c68386795msh15e8293dd2e776bp12364ajsnd16271373457",
	    "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)

# Få information om ett land som valuta, flagga, antal regioner, lands kod.
# Country ID måste vara i ISO-3166 format. (SE, US, DK) etc.
def get_countryDetails(countryID):
    url = "https://wft-geo-db.p.rapidapi.com/v1/geo/countries/" + countryID

    headers = {
	    "X-RapidAPI-Key": "8c68386795msh15e8293dd2e776bp12364ajsnd16271373457",
	    "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    data = json.loads(response.text)
    return data

# Hjälp metod för övriga metoder.
def get_wikidataID(cityName):

    url = "http://www.wikidata.org/w/api.php?action=wbgetentities&sites=enwiki&titles=" + cityName + "&props=descriptions&languages=en&format=json"
    
    # will return "Q25796287" as the value of the "wikibase_item" key.

    response = requests.request("GET", url)
    response_data = response.json()
    
    cityID = 0

    for s in response_data['entities'].keys():
        cityID = s
    
    return cityID