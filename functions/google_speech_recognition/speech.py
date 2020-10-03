#pip install SpeechRecognition
import speech_recognition as sr
from functions.personality.personality_checker import runIntro, runResearch, runListening
import time

def microphone_check():
    #Habilita o microfone para ouvir o usuario
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        runListening()
        print("pode falar")
        audio = microfone.listen(source)
        try:
            frase = microfone.recognize_google(audio,language='pt-BR')
            return frase.casefold()
        except sr.UnknownValueError:
            return "não entendi"
