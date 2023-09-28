import psutil
from plyer import notification
import time


# Specify what battery % interval would you like to be notfied

freq = int(input("Specify what battery % interval would you like to be notfied? "))
print("OK, Great!, You'll be notified each time your battery drops or increases by {}%".format(freq))

battery = psutil.sensors_battery()
percent = battery.percent

while True:
    battery = psutil.sensors_battery()
    current_percent = battery.percent
    
    change = current_percent - percent
    difference = abs(change)
    
    if difference>=freq:
        notification.notify(
            title = "Current Battery Percentage",
            message = str(current_percent) + "% Battery Remaining")
            
        time.sleep(20)
        
    percent = current_percent