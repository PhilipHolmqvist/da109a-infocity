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
    '''
    print("From: " + data['base_currency_name'])
    print("Amount: " + data['amount'] + " " + currencyfrom)
    print("To: " + data['rates'][currencyto]['currency_name'])
    print("Amount: " + data['rates'][currencyto]['rate_for_amount'] + " " + currencyto)
    print("Current rate: " + data['rates'][currencyto]['rate'] + " " + currencyto + " / 1 " + currencyfrom)
    '''
    
    result = data['rates'][currencyto]['rate_for_amount'] + " " + currencyto

    return result

def getCodes(currencyfrom, currencyto, amount):

    countrylist = {
            "AED" : "AE",
            "AFN" : "AF",
            "XCD" : "AG",
            "ALL" : "AL",
            "AMD" : "AM",
            "ANG" : "AN",
            "AOA" : "AO",
            "AQD" : "AQ",
            "ARS" : "AR",
            "AUD" : "AU",
            "AZN" : "AZ",
            "BAM" : "BA",
            "BBD" : "BB",
            "BDT" : "BD",
            "XOF" : "BE",
            "BGN" : "BG",
            "BHD" : "BH",
            "BIF" : "BI",
            "BMD" : "BM",
            "BND" : "BN",
            "BOB" : "BO",
            "BRL" : "BR",
            "BSD" : "BS",
            "NOK" : "BV",
            "BWP" : "BW",
            "BYR" : "BY",
            "BZD" : "BZ",
            "CAD" : "CA",
            "CDF" : "CD",
            "XAF" : "CF",
            "CHF" : "CH",
            "CLP" : "CL",
            "CNY" : "CN",
            "COP" : "CO",
            "CRC" : "CR",
            "CUP" : "CU",
            "CVE" : "CV",
            "CYP" : "CY",
            "CZK" : "CZ",
            "DJF" : "DJ",
            "DKK" : "DK",
            "DOP" : "DO",
            "DZD" : "DZ",
            "ECS" : "EC",
            "EEK" : "EE",
            "EGP" : "EG",
            "ETB" : "ET",
            "EUR" : "FR",
            "FJD" : "FJ",
            "FKP" : "FK",
            "GBP" : "GB",
            "GEL" : "GE",
            "GGP" : "GG",
            "GHS" : "GH",
            "GIP" : "GI",
            "GMD" : "GM",
            "GNF" : "GN",
            "GTQ" : "GT",
            "GYD" : "GY",
            "HKD" : "HK",
            "HNL" : "HN",
            "HRK" : "HR",
            "HTG" : "HT",
            "HUF" : "HU",
            "IDR" : "ID",
            "ILS" : "IL",
            "INR" : "IN",
            "IQD" : "IQ",
            "IRR" : "IR",
            "ISK" : "IS",
            "JMD" : "JM",
            "JOD" : "JO",
            "JPY" : "JP",
            "KES" : "KE",
            "KGS" : "KG",
            "KHR" : "KH",
            "KMF" : "KM",
            "KPW" : "KP",
            "KRW" : "KR",
            "KWD" : "KW",
            "KYD" : "KY",
            "KZT" : "KZ",
            "LAK" : "LA",
            "LBP" : "LB",
            "LKR" : "LK",
            "LRD" : "LR",
            "LSL" : "LS",
            "LTL" : "LT",
            "LVL" : "LV",
            "LYD" : "LY",
            "MAD" : "MA",
            "MDL" : "MD",
            "MGA" : "MG",
            "MKD" : "MK",
            "MMK" : "MM",
            "MNT" : "MN",
            "MOP" : "MO",
            "MRO" : "MR",
            "MTL" : "MT",
            "MUR" : "MU",
            "MVR" : "MV",
            "MWK" : "MW",
            "MXN" : "MX",
            "MYR" : "MY",
            "MZN" : "MZ",
            "NAD" : "NA",
            "XPF" : "NC",
            "NGN" : "NG",
            "NIO" : "NI",
            "NPR" : "NP",
            "NZD" : "NZ",
            "OMR" : "OM",
            "PAB" : "PA",
            "PEN" : "PE",
            "PGK" : "PG",
            "PHP" : "PH",
            "PKR" : "PK",
            "PLN" : "PL",
            "PYG" : "PY",
            "QAR" : "QA",
            "RON" : "RO",
            "RSD" : "RS",
            "RUB" : "RU",
            "RWF" : "RW",
            "SAR" : "SA",
            "SBD" : "SB",
            "SCR" : "SC",
            "SDG" : "SD",
            "SEK" : "SE",
            "SGD" : "SG",
            "SKK" : "SK",
            "SLL" : "SL",
            "SOS" : "SO",
            "SRD" : "SR",
            "STD" : "ST",
            "SVC" : "SV",
            "SYP" : "SY",
            "SZL" : "SZ",
            "THB" : "TH",
            "TJS" : "TJ",
            "TMT" : "TM",
            "TND" : "TN",
            "TOP" : "TO",
            "TRY" : "TR",
            "TTD" : "TT",
            "TWD" : "TW",
            "TZS" : "TZ",
            "UAH" : "UA",
            "UGX" : "UG",
            "USD" : "US",
            "UYU" : "UY",
            "UZS" : "UZ",
            "VEF" : "VE",
            "VND" : "VN",
            "VUV" : "VU",
            "YER" : "YE",
            "ZAR" : "ZA",
            "ZMK" : "ZM",
            "ZWD" : "ZW"
        }


    for x in countrylist:
        if x == currencyto:
            print(x)