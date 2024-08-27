import requests

url = "https://weather338.p.rapidapi.com/weather/forecast"

querystring = {"date":"20240111","latitude":"17.8676898","longitude":"77.6238416","language":"en-US","units":"m"} 

headers = {
	"X-RapidAPI-Key": "ea77a70441msh0f1a928a9888502p13bdbbjsncaf20ee225b5",
	"X-RapidAPI-Host": "weather338.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())