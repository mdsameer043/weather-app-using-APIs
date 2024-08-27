import requests

url = "https://climate-news27.p.rapidapi.com/weather/saudiarabia"

headers = {
	"X-RapidAPI-Key": "ea77a70441msh0f1a928a9888502p13bdbbjsncaf20ee225b5",
	"X-RapidAPI-Host": "climate-news27.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())