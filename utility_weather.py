import requests
import json
from datetime import datetime

def get_weather(city):
  app_id = 'c6bfb796d2ca259963363132fc342078'
  url = 'https://api.openweathermap.org/data/2.5/weather?q=%(city)s&appid=%(app_id)s' % {'city': city, 'app_id': app_id}
  response = requests.get(url)
  return json.loads(response.text)

def convert_temp(temp):
  temp = temp - 273.15
  result = str(int(temp))
  if temp > 0:
    return '+' + result
  return '-' + result

def convert_direction(deg):
  val = int((deg / 22.5) + .5)
  directions = ["С", "ССЗ", "СЗ", "ЗСЗ", "З", "ЗЮЗ", "ЮЗ", "ЮЮЗ", "Ю", "ЮЮВ", "ЮВ", "ВЮВ", "В", "ВСВ", "СВ", "ССВ"]
  return directions[val % 16]

output = str(datetime.now().date()) + ' \n\n'

with open('cities.txt') as f:
    for line in f:
      city = line.strip()
      info = get_weather(city)
      if info['cod'] == 200:
        temp = convert_temp(info['main']['temp'])
        direction = convert_direction(info['wind']['deg'])
        speed = str(info['wind']['speed'])
        humidity = str(info['main']['humidity'])

        output += city + '\n'
        output += temp + '\n'
        output += direction + '\n'
        output += speed + ' м/с \n'
        output += humidity + ' % \n\n'
      else:
        output += 'Error city ' + city + '\n\n'

f = open('temperature.txt', 'w')
f.write(output)
f.close()
