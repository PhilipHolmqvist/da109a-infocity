import requests

url = "https://weatherapi-com.p.rapidapi.com/future.json"

querystring = {
    "q":"London",
    "dt":"2022-12-25"
}

headers = {
	"X-RapidAPI-Key": "0ab490636dmsh7da5c2757e98131p159b59jsn6b2e12133ae3",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.request(
    "GET", 
    url, 
    headers=headers, 
    params=querystring
)

print(response.text)