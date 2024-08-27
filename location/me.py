import geocoder
from geopy.geocoders import Nominatim
g = geocoder.ip('me')
lat = g.latlng[0]
lon = g.latlng[1]
lat = str(lat)
lon = str(lon)
print(lat,lon)
print(type(lat))


myc = Nominatim(user_agent="geoapiExercises")
location = myc.reverse(lat+","+lon)

print(location)