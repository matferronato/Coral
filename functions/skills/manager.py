from .skill_get_route import getRoutes
from .skill_get_time import getTime
from .skill_get_wikipedia import getWikipedia
from .skill_run_webbrowser import runWebBrowser
from .skill_run_spy import runSpy
from .skill_get_emotion import getEmotion
from .skill_get_zipcode import getZipCode
from .skill_get_movie_review import getMovieRecomendation, getMovieList
from functions.voice_return_handler.voice_return import create_audio
import time

def runSkillSet(tokens):   
    for j in range(0, len(tokens)):
        if ("recomendar" == tokens or "achar" in tokens):
            if("filme" in tokens):
                print("oi")
                getMovieRecomendation(tokens[j+1:])
                break
            else:
                getEmotion(tokens,j)
                break
        if (tokens[j] == "lista" or tokens[j] == "listar" or tokens[j] == "listaria"):
            if("filme" in tokens or "filmes" in tokens):
                getMovieList(tokens[j+1:])
                break
        if(tokens[j] == "acesso" or tokens[j] == "acessa" or tokens[j] == "acessar"):
            runWebBrowser(tokens,j)
            break
        if(tokens[j] == "defina" or tokens[j] == "definir"):
            getWikipedia(tokens,j)
            break
        if(tokens[j] == "horas"):
            getTime(tokens,j)
            break
        if (tokens[j] == "chegar"):
            getRoutes(tokens[j+1:],j)
            break

        if (tokens[j] == "mim"):
            runSpy()
            break
        if (tokens[j] == "cep"):
            getZipCode(tokens,j)
            break

    if("mariana" in tokens):
        create_audio("viu mariana, eu sou muito util também! hashtag chupa Alexa")
        
