import requests
import json
import os

city = input("Enter your city\n ")

url = f"http://api.weatherapi.com/v1/current.json?key=653f0d7143fd49edb23182456230608 &q={city}"

r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
print(wdic['current']['temp_c'])
os.system(f"say temperature in {city} is {wdic['current']['temp_c']} degree centigrade")