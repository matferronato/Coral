from functions.voice_return_handler.voice_return import create_audio
import json, urllib
from urllib.parse import urlencode
import urllib.request
import re
from functions.animations.animations import Happy1, IntroFrame1, runSad, runBlink, OhNo1


def runSpy():
    url = 'http://ipinfo.io/json'
    response = urllib.request.urlopen(url)
    data = json.load(response)
    IP=data['ip']
    org=data['org']
    city = data['city']
    country=data['country']
    region=data['region']
    create_audio("você é meu proprietario, o atual dono da modelo Coral versão alpha 1 ponto 1")
    create_audio("atualmente você está na cidade de " + city + " que fica no " + country + " na região de " + region)
    create_audio("sei até que a empresa que presta serviço de internet para você é a " + org)
    create_audio("sei tudo disso pelo seu numero i pe, que é o numero " + IP)
    create_audio("viu como é assustador o que é possivel saber com pouca coisa? Por sorte eu sou diferente da Alexa e da Siri e não te espiono")
    runBlink()
    runBlink()
    create_audio("espero que você não durma pensando nisso")
    