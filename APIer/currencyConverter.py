import requests
import json

def apicall(currencyfrom, currencyto, amount):
    url = "https://currency-converter5.p.rapidapi.com/currency/convert"
    queryString = {"format":"json", "from":currencyfrom, "to": currencyto, "amount":amount}
    headers = {
        "X-RapidAPI-Key": "28a96645femsh05d91bd827d5a87p1ea10bjsnc2ea6ef60feb",
	    "X-RapidAPI-Host": "currency-converter5.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers = headers, params=queryString)
    data = json.loads(response.text)
    print("From: " + data['base_currency_name'])
    print("Amount: " + data['amount'])
    print("To: " + data['rates'][currencyto]['currency_name'])
    print("Amount: " + data['rates'][currencyto]['rate_for_amount'])
    print("Current rate: " + data['rates'][currencyto]['rate'])
    
currencyFrom = "EUR"
currencyTo = "USD"
amount = "100"

apicall(currencyFrom, currencyTo, amount)