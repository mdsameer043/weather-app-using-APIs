# from flask import request
# import requests
# def cityr(city1):
# 	url = "https://weather-by-api-ninjas.p.rapidapi.com/v1/weather"
# 	querystring = {"city":city1}
# 	headers = {
# 		"X-RapidAPI-Key": "ea77a70441msh0f1a928a9888502p13bdbbjsncaf20ee225b5",
# 		"X-RapidAPI-Host": "weather-by-api-ninjas.p.rapidapi.com"
# 	}
# 	response = (requests.get(url, headers=headers, params=querystring)).json()
# 	# response=response.json()
 
# 	# cloud_pct=response.get("cloud_pct")
# 	# temp=response.get("temp")
# 	# feels_like=response.get("feels_like")
# 	# humidity=response.get("humidity")
# 	# min_temp=response.get("min_temp")
# 	# max_temp=response.get("max_temp")
# 	# wind_speed=response.get("wind_speed")
# 	# wind_degrees=response.get("wind_degrees")
# 	# sunrise=response.get("sunrise")
# 	# sunset=response.get("sunset")
# 	return response

# c=cityr("Dappur")
# print(c)
# cloud_pct=c.get("cloud_pct")
# temp=c.get("temp")
# feels_like=c.get("feels_like")
# humidity=c.get("humidity")
# min_temp=c.get("min_temp")
# max_temp=c.get("max_temp")
# wind_speed=c.get("wind_speed")
# wind_degrees=c.get("wind_degrees")
# sunrise=c.get("sunrise")
# sunset=c.get("sunset")

# print(cloud_pct)
# print(temp)
# print(feels_like)
# print(humidity)
# print(min_temp)
# print(max_temp)
# print(wind_speed)
# print(wind_degrees)
# print(sunrise)
# print(sunset)














# import requests

# url = "https://weatherapi-com.p.rapidapi.com/current.json"

# querystring = {"q":"Hyderabad"}

# headers = {
# 	"X-RapidAPI-Key": "ea77a70441msh0f1a928a9888502p13bdbbjsncaf20ee225b5",
# 	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# print(response.json().get('current').get("temp_c"))
# print(response.json().get('current').get("temp_f"))
# print(response.json().get('current').get("condition").get('text'))
















