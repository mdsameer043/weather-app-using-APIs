import requests

# https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/London,UK?key=YOUR_API_KEY 

url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Dappur,India?key=7TMW77XPSC5H8ZQG8V3KJEBZT" 


response = requests.get(url)

api_data = response


# getting daily weather conditions
response1 = api_data.json().get('days')

# getting hourly weather conditions
response2 = api_data.json().get('days')[0].get('hours')



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
    j=0
    for i in response1:
        if j==0:
            j+=1
            continue
        elif j>=8:
            break
        else:
            daily_conditions.append(i.get('conditions'))
            
    return daily_conditions
            
def next_datetime():
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



