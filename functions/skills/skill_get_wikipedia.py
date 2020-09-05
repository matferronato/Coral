from functions.voice_return_handler.voice_return import create_audio
import wikipedia
from functions.animations.animations import wiki1, IntroFrame1


def getWikipedia(current_sentence,i):
    wiki1(1,100)
    create_audio("vou procurar para você")  
    wikipedia.set_lang("pt") 
    if(current_sentence[i+1] == "palavra" or current_sentence[i+1] == "palavra"):
        sentence = wikipedia.summary(current_sentence[i+2], sentences=3)
    else:
        sentence = wikipedia.summary(current_sentence[i+1], sentences=3)
    create_audio(sentence)   