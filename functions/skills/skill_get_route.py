from googletrans import Translator
import json, urllib
from urllib.parse import urlencode
import urllib.request
from functions.voice_return_handler.voice_return import create_audio
import re

def getRoutes(current_sentence,i):
    bingMapsKey = "AvE7iAnpF8-0xQCuen5EvgIKdYxK7utRGXKDqk-wcQTn9DREo_I0gDvyb3znKJDk"
    translator = Translator() 
    create_audio("hum, preciso pensar um pouco, deixa eu ver meus mapas...")  
    if(len(current_sentence) % 2 != 0):
        if current_sentence[-1] == "dirigir" or current_sentence[-1] == "carro":
            travelMode = "Driving"
        elif current_sentence[-1] == "caminhar" or current_sentence[-1] == "pé":
            travelMode = "Walking"
        current_sentence.pop()
    else:   
        travelMode = "Driving"
    if len(current_sentence) == 4:
        origin = current_sentence[i].replace("rua","street") + " city " + current_sentence[i+1]
        dest   = current_sentence[i+2].replace("rua","street") + " city " + current_sentence[i+3]
    else:
        origin = current_sentence[i].replace("rua","street") + " city " + getCurrentLocattion()
        dest   = current_sentence[i+1].replace("rua","street") + " city " + getCurrentLocattion()
    encodeOrigin = urllib.parse.quote(origin, safe='')
    encodedDest = urllib.parse.quote(dest, safe='') 
    routeUrl = "http://dev.virtualearth.net/REST/V1/Routes/"+ travelMode +"?wp.0=" + encodeOrigin + "&wp.1=" + encodedDest + "&key=" + bingMapsKey
    request = urllib.request.Request(routeUrl)
    response = urllib.request.urlopen(request)
    r = response.read().decode(encoding="utf-8")
    result = json.loads(r)
    itineraryItems = result["resourceSets"][0]["resources"][0]["routeLegs"][0]["itineraryItems"]                    
    for item in itineraryItems:
        translated = translator.translate(item["instruction"]["text"], src='en', dest='pt')
        sentence = translated.text
        create_audio(sentence)  
        
        
def getCurrentLocattion():
    url = 'http://ipinfo.io/json'
    response = urllib.request.urlopen(url)
    data = json.load(response)
    IP=data['ip']
    org=data['org']
    city = data['city']
    country=data['country']
    region=data['region']
    return city