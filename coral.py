#Central
#Orientada ao
#Reconhecimento
#Automatico da
#Linguagem

#CORAL

#pip install SpeechRecognition

import speech_recognition as sr#Funcao responsavel por ouvir e reconhecer a fala
from gtts import gTTS
from playsound import playsound
import spacy
import datetime
import json, urllib
from urllib.parse import urlencode
import urllib.request
from googletrans import Translator
import time
import os
import wikipedia

assistant_name = "coral"
bingMapsKey = "AvE7iAnpF8-0xQCuen5EvgIKdYxK7utRGXKDqk-wcQTn9DREo_I0gDvyb3znKJDk"


#Funcao responsavel por falar
def cria_audio(audio):
    tts = gTTS(audio,lang='pt-br')
    if os.remove('audios/hello.mp3'): os.remove('audios/hello.mp3')
    tts.save('audios/hello.mp3')
    #print("Deixe me ver...")
    playsound('audios/hello.mp3')


def ouvir_microfone():
    #Habilita o microfone para ouvir o usuario
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("listening: ")
        audio = microfone.listen(source)
        try:
            frase = microfone.recognize_google(audio,language='pt-BR')
            return frase
        except sr.UnknownValueError:
            return "Não entendi"

wikipedia.set_lang("pt") 
translator = Translator()
nlp = spacy.load('pt')
nlp.Defaults.stop_words.add("a")
nlp.Defaults.stop_words.add("e")
nlp.Defaults.stop_words.add("i")
nlp.Defaults.stop_words.add("o")
nlp.Defaults.stop_words.add("u")

while(1):
    sentence = ouvir_microfone()
    print(sentence)
    #sentence = "coral defina a palavra batman"
    sentence = sentence.casefold()
    if(sentence == "não entendi") : continue
    sentence_list = sentence.split()

    #encontra locais
    testeToken = nlp(sentence)
    LocationNames = []
    for ent in testeToken.ents:
        LocationNames.append(ent.text)

    #protege nomes contra stop words
    for eachLocation in LocationNames:
        #print("*****",eachLocation)
        #print("<>",sentence_list)
        sameWord = True
        wordFound = False
        i = 0
        while i < len(sentence_list):
            if eachLocation.split()[0] in sentence_list[i]:
                for j in range(0, len(eachLocation.split())):
                    #print(eachLocation.split()[j], sentence_list[i+j])
                    if( i+j > len(sentence_list)) : break
                    if(eachLocation.split()[j] != sentence_list[i+j]):
                        sameWord = False
                if sameWord == True:
                    for j in range(1, len(eachLocation.split())):
                        #print("vou deletar", sentence_list[i+1], " sou ",  eachLocation, " word ", sentence_list[i])
                        sentence_list.pop(i+1)
                    sentence_list[i] = eachLocation.replace(" ", "_")
                    wordFound = True
                sameWord = True
            i = i+1        
    print(sentence_list)
    #print("stop word protect")

    #Retira Stop Words
    clean_sentence_list =[]
    for eachWord in sentence_list:
        if not (eachWord in nlp.Defaults.stop_words):
            clean_sentence_list.append(eachWord)
    listToStr = ' '.join(map(str, clean_sentence_list))
    clean_sentence = nlp(listToStr)
    #print("stop word delete")

    #Aplica Lemming
    assistante_sentence = []
    for i in range(0,len(clean_sentence)):
        if clean_sentence[i].pos_ == 'VERB':
            assistante_sentence.append(clean_sentence[i].lemma_)
        else:
            assistante_sentence.append(clean_sentence[i])
    tokens = [str(token) for token in assistante_sentence]
    #print("lemming")

    #Retirando protecao
    for i in range(0 , len(tokens)):
        if( "_" in tokens[i]):
            tokens[i] = tokens[i].replace("_"," ")
    #print("name return")
    #print(tokens)

    
    #inicia assitencias
    print(tokens)
    for i in range(0, len(tokens)):
        if assistant_name == tokens[i]:
            cria_audio("hum, deixa eu pensar...")  
            current_sentence = tokens[i+1:]
            for j in range(0, len(current_sentence)):
                if(current_sentence[j] == "acesso" or current_sentence[j] == "acessa"):
                    if(current_sentence[i+1] == "site"):
                        os.system('.\\Firefox.lnk -new-tab http://www.'+current_sentence[i+2]+'.com/');
                    else:
                        os.system('.\\Firefox.lnk -new-tab http://www.'+current_sentence[i+1]+'.com/');
                if(current_sentence[j] == "defina" or current_sentence[j] == "definir"):
                    if(current_sentence[i+1] == "palavra"):
                        sentence = wikipedia.summary(current_sentence[i+2], sentences=3)
                    else:
                        sentence = wikipedia.summary(current_sentence[i+1], sentences=3)
                    cria_audio(sentence)       
                if(current_sentence[j] == "horas"):
                    localTime = datetime.datetime.now().time()
                    sentence = "agora são " + str(localTime.hour) + " horas e " + str(localTime.minute) + " minutos "
                    cria_audio(sentence)
                if (current_sentence[j] == "chegar"):
                    origin = current_sentence[j+1] + " " + current_sentence[j+2]
                    dest   = current_sentence[j+3] + " " + current_sentence[j+4]
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
                        cria_audio(sentence)                        

                    break
            break
