from flask import Flask,render_template,request
import requests  
app = Flask(__name__)


from next_hours_days import next_hours,next_days
from datetime import datetime,timedelta
from sklearn import metrics
#import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split



import geocoder
from geopy.geocoders import Nominatim
g = geocoder.ip('me')
lat = str(g.latlng[0])
lon = str(g.latlng[1])
print(lat,lon)

geolocator = Nominatim(user_agent="geoaipExercises")
location = geolocator.reverse(lat+','+lon)

address= location.raw["address"]
# print(address)
address_city = address.get("city")


# # getting weather report start
# def cityWeather(cityname):
#     url = "https://weather-by-api-ninjas.p.rapidapi.com/v1/weather"
#     querystring = {"city":cityname}
#     headers = {
#         "X-RapidAPI-Key": "ea77a70441msh0f1a928a9888502p13bdbbjsncaf20ee225b5",
#         "X-RapidAPI-Host": "weather-by-api-ninjas.p.rapidapi.com"
#     }
#     response = requests.get(url, headers=headers, params=querystring)
#     response=response.json()
#     return response
# # end of weather 


# getting weather report start
def cityWeather(cityname):
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{cityname}?key=7TMW77XPSC5H8ZQG8V3KJEBZT" 

    response = requests.get(url)
    weatherdata ={}
    weatherdata["temp"]=response.json().get('days')[0].get('temp')
    weatherdata["humidity"]=response.json().get('days')[0].get('humidity')
    weatherdata["feels_like"]=response.json().get('days')[0].get('feelslike')
    weatherdata["wind_speed"]=response.json().get('days')[0].get('windspeed')
    weatherdata["wind_degrees"]=response.json().get('days')[0].get('winddir')
    weatherdata["max_temp"]=response.json().get('days')[0].get('tempmax')
    weatherdata["min_temp"]=response.json().get('days')[0].get('tempmin')
    weatherdata["cloud_pct"]=response.json().get('days')[0].get('cloudcover')
    weatherdata["wind_speed"]=response.json().get('days')[0].get('windspeed')
    weatherdata["sunrise"]=response.json().get('days')[0].get('sunrise')
    weatherdata["sunset"]=response.json().get('days')[0].get('sunset')
    
    return weatherdata
# end of weather 


def info_page_data():
    list1 = [[],[],[],[],[],[],[],[],[],[]]
    list = ['Lonavala','Mannur','Goa','Pondicherry','Ooty','Shillong','Manali','Darjeeling','Mount abu']
    for i in range(9):
        # print(i)
        # from datetime import datetime
        data = cityWeather(list[i])
        list1[i].append(data['cloud_pct'])
        list1[i].append(data['feels_like'])
        list1[i].append(data['humidity'])
        list1[i].append(data['max_temp'])
        list1[i].append(data['min_temp'])
        # list1[i].append(data['sunrise'])
        # list1[i].append(data['sunset'])
        list1[i].append(data['temp'])
        list1[i].append(data['wind_degrees'])
        list1[i].append(data['wind_speed'])
        
    return list1
# print(info_page_data())
# exit()

# print(info_page_data())
# exit()
# default city 
print(address_city)
# print(lat,lon)
default_city_by_location=f"{lat},{lon}"
search_city = f"{address_city}"

# query city
city_query = ""

if len(city_query)==0:
    city_query = search_city

# api result for the default location
api_data = cityWeather(search_city)

# visual crossing
# default data on app reload
api_data_for_default = api_data

url=""
response=""
api_data=""
response1=""
response2=""
response3=""


def load_url():
    global url,response,api_data,response1,response2,response3,city_query
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city_query}?key=7TMW77XPSC5H8ZQG8V3KJEBZT" 

    response = requests.get(url)
    api_data = response

    # getting daily weather conditions
    response1 = api_data.json().get('days')
    # getting hourly weather conditions
    # current day data
    response2 = api_data.json().get('days')[0].get('hours')
    response3 = api_data.json().get('days')[1].get('hours')
    
    
def load_url1():
    global url,response,api_data,response1,response2,response3,city_query,lat,lon
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{lat},{lon}?key=7TMW77XPSC5H8ZQG8V3KJEBZT" 

    response = requests.get(url)
    api_data = response

    # getting daily weather conditions
    response1 = api_data.json().get('days')
    # getting hourly weather conditions
    # current day data
    response2 = api_data.json().get('days')[0].get('hours')
    response3 = api_data.json().get('days')[1].get('hours')

load_url1()

# response3 = api_data.json().get('days')[0].get('hours')[0]

def next_hourly_datetime():
    hourly_datetime = []
    for i in response2:
        hourly_datetime.append(i.get('datetime'))
    return hourly_datetime

def next_hourly_temp():
    hourly_temp = [] 
    for i in response2:
        hourly_temp.append(i.get('temp'))   
    return hourly_temp

def next_hourly_conditions():
    hourly_conditions = [] 
    for i in response2:
        hourly_conditions.append(i.get('conditions'))   
    return hourly_conditions
    

def next_hourly_nextday_datetime():
    hourly_datetime = []
    for i in response3:
        hourly_datetime.append(i.get('datetime'))
    return hourly_datetime
def next_hourly_nextday_temp():
    hourly_temp = [] 
    for i in response3:
        hourly_temp.append(i.get('temp'))   
    return hourly_temp
def next_hourly_nextday_conditions():
    hourly_conditions = [] 
    for i in response3:
        hourly_conditions.append(i.get('conditions'))   
    return hourly_conditions



# next nine hours data and details

def next_total_temp_forFlask():
    now_time = int(datetime.now().strftime("%H"))
    temp_list = []
    counter = 0
    for i in range(now_time+1,now_time+10):
        if i>=24:
            counter+=1
    
    counter1=0
    val = next_hourly_temp()
    val1 = next_hourly_nextday_temp()
    for i in range(now_time+1,now_time+10):
        if i>=24:
            if counter!=0:
                temp_list.append(val1[counter1])
                counter1+=1
                counter-=1
        else:
            temp_list.append(val[i])
            
    return temp_list
    

def next_total_conditions_forFlask():
    now_time = int(datetime.now().strftime("%H"))
    conditions_list = []
    conditions_icon = []
    counter = 0
    for i in range(now_time+1,now_time+10):
        if i>=24:
            counter+=1
    
    counter1=0
    val = next_hourly_conditions()
    val1 = next_hourly_nextday_conditions()
    for i in range(now_time+1,now_time+10):
        if i>=24:
            if counter!=0:
                conditions_list.append(val1[counter1])
                counter1+=1
                counter-=1
        else:
            conditions_list.append(val[i])
            
    
    
    Clear = ""
    overcast = "uil-clouds"  
    rain = "uil-cloud-showers-heavy"
    partially_cloudy = "uil-cloud"
    if now_time <= 6 or now_time >= 18:
        Clear = "uil-moon"
    
    else:
        Clear = "uil-sun"
    
    
    for item in conditions_list:
        if item == "Partially cloudy":
            conditions_icon.append(partially_cloudy)
        elif item == "Clear":
            conditions_icon.append(Clear)
        elif item == "Overcast":
            conditions_icon.append(overcast)
        elif item == "Rain":
            conditions_icon.append(rain)
        else:
            pass
    
    return conditions_icon
            


# forcasting data for daily wise
    
def next_daily_temp():
    daily_temp = [] 
    j=0
    for i in response1:
        if j==0:
            j+=1
            continue
        elif j>=8:
            break
        else:
            daily_temp.append(i.get('temp'))
            
    return daily_temp
                    
def next_daily_conditions():
    daily_conditions = []
    daily_icons=[]
    j=0
    for i in response1:
        if j==0:
            j+=1
            continue
        elif j>=8:
            break
        else:
            daily_conditions.append(i.get('conditions'))
            
    Clear = ""
    overcast = "uil-clouds"  
    rain = "uil-cloud-showers-heavy"
    partially_cloudy = "uil-cloud"
    Clear = "uil-sun"

    
    for item in daily_conditions:
        if item == "Partially cloudy":
            daily_icons.append(partially_cloudy)
        elif item == "Clear":
            daily_icons.append(Clear)
        elif item == "Overcast":
            daily_icons.append(overcast)
        elif item == "Rain":
            daily_icons.append(rain)
        else:
            pass
            
    return daily_icons
            
def next_daily_datetime():
    daily_datetime = []
    j=0
    for i in response1:
        if j==0:
            j+=1
            continue
        elif j>=8:
            break
        else:
            daily_datetime.append(i.get('datetime'))
            
    return daily_datetime









# # model train start
def dtc():

    api_data_list = [[api_data['temp'],api_data['feels_like'],api_data['humidity'],api_data['wind_speed'],api_data['wind_degrees']]]

    df=pd.read_csv("C:/Users/MD SAMEER/OneDrive/Documents/my_works/completed_projects/working_with_api/weather_app/cleaned_dataset.csv")
    train_x = df[['Temperature','Apparent_Temperature','Humidity','WindSpeed','Wind_Bearing']]
    train_y = df['Summary']

    model = DecisionTreeClassifier()

    model.fit(train_x,train_y)
    pred=model.predict(api_data_list)
    return pred



# print(pred)
# # model train end



# forcasting hourly data 
now_time = int(datetime.now().strftime("%H"))
temp_forcast_hourly = []
condition_forcast_hourly = []

scrap_temp = next_hourly_temp()
scrap_conditions = next_hourly_conditions()



# forcasting daily data 

daily_data_temp = next_daily_temp()
daily_temp_for_app=[]

for i in range(7):
    daily_temp_for_app.append(daily_data_temp[i])

# mood = dtc()
mood = "Clear"
@app.route("/", methods = ["GET","POST"])
def hello_world():
    # print(next_total_temp_forFlask())
    global search_city,city_query,api_data_for_default,daily_temp_for_app,mood
    forcast_color = ""
    time_hours = int(datetime.now().strftime("%H"))
    if time_hours <= 6 or time_hours >= 18:
        forcast_color = "white"
    else:
        forcast_color = "black"
    # query page
    try:
        if request.method == "POST" and request.form['city_query_validation']=="city_query_valid":
            got_city = request.form['city_query']
            if len(got_city)!=0:
                city_query = got_city
            api_data1 = cityWeather(city_query)
            api_data_for_default = api_data1
            # temp,wind_speed,humidity,feels_like,wind_degrees
            
            city = city_query
            load_url()
            temp = api_data1["temp"]
            humidity = api_data1["humidity"]
            feels_like = api_data1["feels_like"]
            wind_speed = api_data1["wind_speed"]
            wind_degrees = api_data1["wind_degrees"]
            return render_template('main_page1.html',temp=temp,humidity=humidity,feels_like=feels_like,wind_speed=wind_speed,wind_degrees=wind_degrees,city=city,forcast_data=zip(next_hours(),next_total_temp_forFlask(),next_total_conditions_forFlask()),forcast_color=forcast_color,mood=mood)
    
    except Exception as e:
        print(e)
        
    try:
        if request.method == "POST" and request.form['forcast_type_query_validation']=="forcast_type_query_valid":
            type_data = request.form['forcast_type_query']
            if type_data == "hourly":
                city = ""
                if len(city_query)!=0:
                    city = city_query
                else:
                    city = search_city
                temp = api_data_for_default["temp"]
                humidity = api_data_for_default["humidity"]
                feels_like = api_data_for_default["feels_like"]
                wind_speed = api_data_for_default["wind_speed"]
                wind_degrees = api_data_for_default["wind_degrees"]
                return render_template('main_page1.html',temp=temp,humidity=humidity,feels_like=feels_like,wind_speed=wind_speed,wind_degrees=wind_degrees,city=city,forcast_data=zip(next_hours(),next_total_temp_forFlask(),next_total_conditions_forFlask()),forcast_color=forcast_color,mood=mood)
            
            elif type_data == "daily":
                city = ""
                if len(city_query)!=0:
                    city = city_query
                else:
                    city = search_city
                temp = api_data_for_default["temp"]
                humidity = api_data_for_default["humidity"]
                feels_like = api_data_for_default["feels_like"]
                wind_speed = api_data_for_default["wind_speed"]
                wind_degrees = api_data_for_default["wind_degrees"]
                return render_template('main_page1.html',temp=temp,humidity=humidity,feels_like=feels_like,wind_speed=wind_speed,wind_degrees=wind_degrees,city=city,forcast_data=zip(next_days(),next_daily_temp(),next_daily_conditions()),forcast_color=forcast_color,daily_temp=daily_temp_for_app,mood=mood)
            
    except Exception as e:
        print(e)
    
    
    # temp,wind_speed,humidity,feels_like,wind_degrees
    city = ""
    if len(city_query) != 0:
        city = city_query
    else:
        city = search_city
    load_url()
    temp = api_data_for_default["temp"]
    humidity = api_data_for_default["humidity"]
    feels_like = api_data_for_default["feels_like"]
    wind_speed = api_data_for_default["wind_speed"]
    wind_degrees = api_data_for_default["wind_degrees"]
    return render_template('main_page1.html',temp=temp,humidity=humidity,feels_like=feels_like,wind_speed=wind_speed,wind_degrees=wind_degrees,city=city,forcast_data=zip(next_hours(),next_total_temp_forFlask(),next_total_conditions_forFlask()),forcast_color=forcast_color,mood=mood)

@app.route("/details", methods = ["GET","POST"])
def details1():
    global city_query,search_city,api_data_for_default
    if request.method == "POST":
        got_city = request.form['city_query_details_page']
        if len(got_city)!=0:
            city_query = got_city
        api_data2 = cityWeather(city_query)
        api_data_for_default = api_data2
        # temp,wind_speed,humidity,feels_like,wind_degrees
        city = city_query
        temp = api_data2["temp"]
        humidity = api_data2["humidity"]
        feels_like = api_data2["feels_like"]
        wind_speed = api_data2["wind_speed"]
        wind_degrees = api_data2["wind_degrees"]
        min_temp = api_data2["min_temp"]
        max_temp = api_data2["max_temp"]
        sunrise = api_data2["sunrise"]
        sunset = api_data2["sunset"]
        return render_template('more_info_page.html',temp=temp,humidity=humidity,feels_like=feels_like,wind_speed=wind_speed,wind_degrees=wind_degrees,city=city,info_data=info_page_data())
    
    city = ""
    if len(city_query)!=0:
        city = city_query
    else:
        city = search_city
    # city = city_query
    temp = api_data_for_default["temp"]
    humidity = api_data_for_default["humidity"]
    feels_like = api_data_for_default["feels_like"]
    wind_speed = api_data_for_default["wind_speed"]
    wind_degrees = api_data_for_default["wind_degrees"]
    min_temp = api_data_for_default["min_temp"]
    max_temp = api_data_for_default["max_temp"]
    sunrise = api_data_for_default["sunrise"]
    sunset = api_data_for_default["sunset"]
    return render_template('more_info_page.html',temp=temp,humidity=humidity,feels_like=feels_like,wind_speed=wind_speed,wind_degrees=wind_degrees,min_temp=min_temp,max_temp=max_temp,sunrise=sunrise,sunset=sunset,city=city,info_data=info_page_data())

if __name__=="__main__":
    app.run(debug=True)

