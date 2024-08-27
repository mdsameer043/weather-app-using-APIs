# import ipinfo
# access_token = '8e5fdc67e492ab'
# handler = ipinfo.getHandler(access_token)
# ip_address = '27.63.40.40'
# details = handler.getDetails(ip_address)
# print(details.city)


# from digidevice

# 17.384, 78.4564
from geopy import Nominatim

geoLocater = Nominatim(user_agent="GetLoc")

location = geoLocater.geocode("Hyderabad")

latitude = str(location.latitude)
longitude = str(location.longitude)

print(location)
print(latitude,longitude)

geolocation = Nominatim(user_agent="geoapiExercises")

city_location = geolocation.geocode(latitude +","+ longitude)
# data = list(city_location)
# print(data)

data1=[]
counter = 0
for i in city_location:
    for j in i:
        if j !=",":
            data1[counter]+= j
        else:
            continue
        counter+=1
        
for k in data1:
    print(k)


# data_location = city_location.split(",")
# print(city_location)
# print(data_location)



