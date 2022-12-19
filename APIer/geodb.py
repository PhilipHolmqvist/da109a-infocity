import requests
import json

#Author Philip Holmqvist

#Hjälp metod för övriga metoder.
def get_wikidataID(cityName):

    url = "http://www.wikidata.org/w/api.php?action=wbgetentities&sites=enwiki&titles=" + cityName + "&props=descriptions&languages=en&format=json"
    
    # will return "Q25796287" as the value of the "wikibase_item" key.


    response = requests.request("GET", url)
    response_data = response.json()
    
    cityID = 0

    for s in response_data['entities'].keys():
        cityID = s
    
    return cityID

#Vilket land och region staden finns i. Latitud och Longitud grader. Invånare i staden. Meter över havet. Tidzon.
def get_cityDetails(cityName):
    cityID = get_wikidataID(cityName)

    url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities/" + cityID

    headers = {
	    "X-RapidAPI-Key": "8c68386795msh15e8293dd2e776bp12364ajsnd16271373457",
	    "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)

#Returnerar stadens tid i ISO-8601 format: HHmmss.SSSZ
def get_cityTime(cityName):

    print ("hej")
