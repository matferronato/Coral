import requests
from bs4 import BeautifulSoup
import unicodedata
from unicodedata import normalize
import unidecode
import re
from urllib.parse import urlencode
import urllib.request
from functions.voice_return_handler.voice_return import create_audio
from functions.google_speech_recognition.speech import microphone_check
import json, urllib

NoneType = type(None)
    
def getZipCode(current_sentence,i):
    street = current_sentence[i+1] if current_sentence[i+1] != "rua" and current_sentence[i+1] != "avenida" else current_sentence[i+2]
    if "cidade" in current_sentence[i:]:
        for j in range(i, len(current_sentence)):
            if (current_sentence[i] == "cidade"):
                city = ","+current_sentence[i+1]
                break
    elif len(current_sentence) > i+2:
        if not (current_sentence[i+2].isnumeric()):
            city = ","+current_sentence[i+2]
    else: city = ","+getCurrentLocattion()
    
    address = street + city
    create_audio("vou procurar o cep de " + street + " na cidade de " + city)
    print(address)
    # Getting data
    address = normalize('NFKD', address).encode(
        'ASCII', 'ignore').decode('ASCII')
    session = requests.session()
    data = {'relaxation': address,
            'TipoCep': 'ALL',
            'semelhante': 'N',
            }
    r = session.post("http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaCepEndereco.cfm", data)
    content = r.content
    
    # Parsing
    soup = BeautifulSoup(content, features="html.parser")
    content = soup.find_all('table')
    if content:
        data = []
        items = content[0].find_all('td')
        for info in chunks(items, 4):
            if(type(info[0].string) == NoneType): continue
            data.append({
                'address': unidecode.unidecode(re.sub(' - .*', '', info[0].string).strip()),
                'extra': unidecode.unidecode(info[0].string.strip()),
                'neighborhood': unidecode.unidecode(info[1].string.strip()),
                'city/state': unidecode.unidecode(info[2].string.strip()),
                'zipcode': unidecode.unidecode(info[3].string.strip()),
            })   
    else:
        data = {'não consegui achar'}
    city = strip_accents(city).casefold().replace(",","")
    if data == 'não consegui achar':
        create_audio("não consegui achar")
    else:
        create_audio("existe " + str(len(data)) + " resultados")
        for eachData in data:
            if city in eachData['city/state'].casefold():
                create_audio(eachData['extra'] + " em bairro " + eachData['neighborhood'] + " na cidade de " + eachData['city/state'] + " tem o cep " + eachData['zipcode'])
                create_audio("quer que eu te diga outra possibilidade de cep? É só me dizer que sim")
                if microphone_check() == "sim":
                    continue
                else:
                    break
            
    
def chunks(l, n):
    n = max(1, n)
    return list(l[i:i+n] for i in range(0, len(l), n))

def strip_accents(text):
    try:
        text = unicode(text, 'utf-8')
    except NameError: # unicode is a default on python 3 
        pass
    text = unicodedata.normalize('NFD', text)\
           .encode('ascii', 'ignore')\
           .decode("utf-8")
    return str(text)    
    
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