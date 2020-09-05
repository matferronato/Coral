from googletrans import Translator
import json, urllib
from urllib.parse import urlencode
import urllib.request
from functions.voice_return_handler.voice_return import create_audio


def getRoutes(current_sentence,i):
    create_audio("hum, preciso pensar um pouco, deixa eu ver meus mapas...")  
    bingMapsKey = "AvE7iAnpF8-0xQCuen5EvgIKdYxK7utRGXKDqk-wcQTn9DREo_I0gDvyb3znKJDk"
    translator = Translator()
    origin = current_sentence[i+1] + " " + current_sentence[i+2]
    dest   = current_sentence[i+3] + " " + current_sentence[i+4]
    encodeOrigin = urllib.parse.quote(origin, safe='')
    encodedDest = urllib.parse.quote(dest, safe='') 
    routeUrl = "http://dev.virtualearth.net/REST/V1/Routes/Driving?wp.0=" + encodeOrigin + "&wp.1=" + encodedDest + "&key=" + bingMapsKey
    request = urllib.request.Request(routeUrl)
    response = urllib.request.urlopen(request)
    r = response.read().decode(encoding="utf-8")
    result = json.loads(r)
    itineraryItems = result["resourceSets"][0]["resources"][0]["routeLegs"][0]["itineraryItems"]                    
    for item in itineraryItems:
        translated = translator.translate(item["instruction"]["text"], src='en', dest='pt')
        sentence = translated.text
        create_audio(sentence)  