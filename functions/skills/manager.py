from .skill_get_route import getRoutes
from .skill_get_time import getTime
from .skill_get_wikipedia import getWikipedia
from .skill_run_webbrowser import runWebBrowser
from .skill_run_spy import runSpy
from .skill_get_emotion import getEmotion
from .skill_get_zipcode import getZipCode
from functions.voice_return_handler.voice_return import create_audio
import time

def runSkillSet(assistant_name, tokens):   
    #print(tokens)
    time.sleep(3)
    for i in range(0, len(tokens)):
        if assistant_name == tokens[i]:
            current_sentence = tokens[i+1:]
            for j in range(0, len(current_sentence)):
                if(current_sentence[j] == "acesso" or current_sentence[j] == "acessa" or current_sentence[j] == "acessar"):
                    runWebBrowser(current_sentence,j)
                    break
                if(current_sentence[j] == "defina" or current_sentence[j] == "definir"):
                    getWikipedia(current_sentence,j)
                    break
                if(current_sentence[j] == "horas"):
                    getTime(current_sentence,j)
                    break
                if (current_sentence[j] == "chegar"):
                    getRoutes(current_sentence[j+1:],j)
                    break
                if (current_sentence[j] == "achar"):
                    getEmotion(current_sentence,j)
                    break
                if (current_sentence[j] == "mim"):
                    runSpy()
                    break
                if (current_sentence[j] == "cep"):
                    getZipCode(current_sentence,j)
                    break
            break
