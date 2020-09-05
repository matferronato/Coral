import urllib.request
import json
import requests
from googletrans import Translator

translator = Translator()


# Your Bing Maps Key 
bingMapsKey = "AvE7iAnpF8-0xQCuen5EvgIKdYxK7utRGXKDqk-wcQTn9DREo_I0gDvyb3znKJDk"

# input information
start = "rua berlim port alegre"
destination = "rua nilo ruschel porto alegre"

encodeStart = urllib.parse.quote(start, safe='')
encodedDest = urllib.parse.quote(destination, safe='')

routeUrl = "http://dev.virtualearth.net/REST/V1/Routes/Driving?wp.0=" + encodeStart + "&wp.1=" + encodedDest + "&key=" + bingMapsKey
print(routeUrl)
request = urllib.request.Request(routeUrl)
response = urllib.request.urlopen(request)

r = response.read().decode(encoding="utf-8")
result = json.loads(r)

itineraryItems = result["resourceSets"][0]["resources"][0]["routeLegs"][0]["itineraryItems"]

for item in itineraryItems:
    translated = translator.translate(item["instruction"]["text"], src='en', dest='pt')
    print(translated.text)
    
    
