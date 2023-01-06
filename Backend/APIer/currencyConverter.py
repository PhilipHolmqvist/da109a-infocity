import requests
import json

def get_rate(currencyfrom, currencyto, amount):
    #currencyto = json.dumps(currencyto, indent=None)
    #print("after " + currencyto)

    url = "https://currency-converter5.p.rapidapi.com/currency/convert"
    queryString = {"format":"json", "from":currencyfrom, "to": currencyto, "amount":amount}
    headers = {
        "X-RapidAPI-Key": "28a96645femsh05d91bd827d5a87p1ea10bjsnc2ea6ef60feb",
	    "X-RapidAPI-Host": "currency-converter5.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers = headers, params=queryString)
    data = json.loads(response.text)
    print(response.text)
    return data

