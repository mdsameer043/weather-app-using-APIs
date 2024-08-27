from datetime import datetime

def next_days():
    days = ["Monday","Tuesday","wednesday","Thursday","Friday","Saturday","Sunday"]
    today = datetime.today().strftime("%A")
    next_days_list = []
    today_index = days.index(today)

    for i in range(today_index+1,7):
        next_days_list.append(days[i])
        
    for i in range(0,today_index):
        next_days_list.append(days[i])
        
    return next_days_list


def next_hours():
    now_time = int(datetime.now().strftime("%H"))
    hours_list = []
    hours_count = int(datetime.now().strftime("%H"))
    meradian = ""
    for i in range(now_time+1,now_time+10):
        hours_count+=1
        if hours_count>=25:
            hours_count = 1
        if hours_count>=12:
            meradian = "pM"
        else:
            meradian = "AM"
        hours_list.append(str(hours_count) + " " + meradian)
        
    return hours_list

    
    
