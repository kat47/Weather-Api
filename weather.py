import requests
import json
import time

#Your api key from https://openweathermap.org
apiKey = ''

#degree symbol
deg = "\u00B0"+"C"

def getWeather(city):
    URL = 'https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s' %(city,apiKey)
    r = requests.get(URL)
    #print("status code = ",r.status_code)
    R = json.loads(r.content)
    
    #to get temperature in degree celsius
    curTemp = R['main']['temp'] - 273
    curTemp = round(curTemp,1)
    maxTemp = R['main']['temp_max'] - 273
    maxTemp = round(maxTemp,1)
    minTemp = R['main']['temp_min'] - 273
    minTemp = round(minTemp,1)
    
    #Humidity
    description = R['weather'][0]["description"]
    humidity = R['main']['humidity']
    
    #Sunset and sunrise time based on "your" current time zone
    sunriseTime = R['sys']['sunrise']
    sunriseTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(sunriseTime))
    sunsetTime = R['sys']['sunset']
    sunsetTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(sunsetTime))

    print("Current temp: %s %s\nMax Temp: %s %s\nMin Temp: %s %s\nDescription: %s\
    \nHumidity: %s %%\nSunrise: %s\nSunset: %s" %(curTemp,deg,maxTemp,deg, minTemp,deg,description,\
    humidity,sunriseTime,sunsetTime))

if __name__ == "__main__":
    city = input("Enter your city/state/Country\t").strip()
    getWeather(city)
