import requests
from string import capwords as cp
from tokens import APPID

URL_BASE = 'https://api.openweathermap.org/data/2.5/'

def get_weather(lat: float=54.5293, lon: float=36.2724, appid: str=APPID, lang: str='ru') -> dict:
    return requests.get(URL_BASE + 'weather', params=locals()).json()

def weather_curr():
    raw_data = get_weather()
    curr_desc = raw_data['weather'][0]['description']
    send_desc = cp(curr_desc, sep=None)
    curr_temp = raw_data['main']['temp'] - 273,15
    send_temp = int(curr_temp[0])
    if send_temp > 0:
        send_temp = '+' + str(send_temp)
    elif send_temp < 0:
        send_temp = '-' + str(send_temp)
    feels_like = raw_data['main']['feels_like'] - 273,15
    send_feel = int(feels_like[0])
    if send_feel > 0:
        send_feel = '+' + str(send_feel)
    elif send_feel < 0:
        send_feel = '-' + str(send_feel)
    data = {'desc': send_desc, 'temp': send_temp, 'feel': send_feel}
    return data