import urllib.request
from bs4 import BeautifulSoup
import re
import random
from functions.voice_return_handler.voice_return import create_audio
from functions.animations.animations import wiki1, IntroFrame1
from functions.google_speech_recognition.speech import microphone_check

def getMovieInfo(movieNumeber):
    url = "http://www.adorocinema.com/filmes/filme-"+str(movieNumeber)
    page = urllib.request.urlopen(url)
    webpageHtml = page.read()
    soup = BeautifulSoup(webpageHtml, features="html.parser")
    page.close()
    divs = soup.findAll("div", {"class": "gd-col-left"})
    devList = str(divs).split("\n")
    i = 0
    for eachDiv in devList:
        #print(i, eachDiv)
        if("content-txt" in eachDiv):
            content = devList[i+1]
        i=i+1
    return re.sub('<[^>]+>', '', str(content))

def getName(content):
    nameClass = content.find("div", {"class": "titlebar_02 margin_10b"})
    nameInfo = nameClass.find("a")
    name =""
    code =""
    nameCode = str((str(nameInfo).split())[2:3]).replace("href=","").replace("'","").replace("-","")
    code = nameCode.replace("\"","").replace("[","").replace("]","").replace("filme", "").replace("s", "").replace("/","")
    nameList = (str(nameInfo).split())[4:-1]
    name = ' '.join([str(elem) for elem in nameList]) 
    return name, code

def getDirector(content):
    movieInfo = content.find("ul", {"class": "list_item_p2v tab_col_first"})
    movieInfoList = movieInfo.findAll("li")
    i = 0
    director=""
    genero=""
    for eachItem in movieInfoList:
        eachItem = re.sub('<[^>]+>', '', str(eachItem))
        if i == 1:
            director = eachItem.replace("\n", "")
        elif i == 3:
            genero = eachItem.replace("\n", "").replace("Gênero", "Gênero ").replace(",", "e")
        i = i + 1    
    return director, genero

def getScore(content):
    score =""
    scoreInfo = content.find("div", {"class": "margin_10v"})
    scoreSpan = scoreInfo.find("span", {"class": "note"})
    score = re.sub('<[^>]+>', '', str(scoreSpan))
    return score


def getMostViewed(genero, searchType, maxDepth):
    genDict = {"ação": "genero-13025/", "todos":"","terror":"genero-13009/",
               "animação": "genero-13026/", "aventura": "genero-13001/",
               "arte marcial": "genero-13016/", "comédia": "genero-13005/",
               "ficção ciêntífica":"genero-13021/", "musical": "genero-13043/",
               "documentário":"genero-13007/", "fantasia":"genero-13012/","faroeste":"genero-13019/",
               "guerra":"genero-13014/", "policial":"genero-13018/", "romance":"genero-13024/", 
               "suspense":"genero-13023/"
               }
      

    opinion = "imprensa/" if searchType == "impressa" else "notas-espectadores/"
    url = "http://www.adorocinema.com/filmes/todos-filmes/"+opinion+genDict[genero]

    page = urllib.request.urlopen(url)
    webpageHtml = page.read()
    soup = BeautifulSoup(webpageHtml, features="html.parser")
    page.close()
    divs = soup.findAll("div", {"class": "data_box"})
    currentDepth = 1
    for div in divs:
        content = div.find("div", {"class": "content"})
        name, code = getName(content)
        director, genero = getDirector(content)
        score = getScore(content)
        create_audio("Na posição " + str(currentDepth) + " temos " + name + " do " + genero + " e nota " + str(score))
        currentDepth = currentDepth + 1
        if currentDepth == maxDepth:
            break

def getRandomMovie(genero, searchType, badMovie=False):
    genDict = {"ação": "genero-13025/", "todos":"","terror":"genero-13009/",
               "animação": "genero-13026/", "aventura": "genero-13001/",
               "arte marcial": "genero-13016/", "comédia": "genero-13005/",
               "ficção ciêntífica":"genero-13021/", "musical": "genero-13043/",
               "documentário":"genero-13007/", "fantasia":"genero-13012/","faroeste":"genero-13019/",
               "guerra":"genero-13014/", "policial":"genero-13018/", "romance":"genero-13024/", 
               "suspense":"genero-13023/"
               }
      

    opinion = "imprensa/" if searchType == "impressa" else "notas-espectadores/"
    if not(badMovie):
        url = "http://www.adorocinema.com/filmes/todos-filmes/"+opinion+genDict[genero]
    else:
        url = "http://www.adorocinema.com/filmes/todos-filmes/"+opinion+genDict[genero]+"?page="+str(30)

    page = urllib.request.urlopen(url)
    webpageHtml = page.read()
    soup = BeautifulSoup(webpageHtml, features="html.parser")
    page.close()
    divs = soup.findAll("div", {"class": "data_box"})
    
    for i in range(2,6):
        if not(badMovie):
            url = "http://www.adorocinema.com/filmes/todos-filmes/"+opinion+genDict[genero]+"?page="+str(i)
        else:
            url = "http://www.adorocinema.com/filmes/todos-filmes/"+opinion+genDict[genero]+"?page="+str(30-i)
        page = urllib.request.urlopen(url)
        webpageHtml = page.read()
        soup = BeautifulSoup(webpageHtml, features="html.parser")
        page.close()
        thisdivs = soup.findAll("div", {"class": "data_box"})
        divs.extend(thisdivs) 

    movieToShow = random.randint(1, 100)
    maxDepth = 100  
    currentDepth = 1
    for div in divs:
        if movieToShow == currentDepth:
            content = div.find("div", {"class": "content"})
            name, code = getName(content)
            director, genero = getDirector(content)
            score = getScore(content)
            content = getMovieInfo(code)
            create_audio(" que tal o filme " + name + " do " + genero + " e nota " + str(score) + "...... quer saber mais sobre este filme? Caso queira que eu repita é só dizer repetir")
            reply = microphone_check()
            while ("repetir" in reply):
                create_audio(" que tal o filme " + name + " do " + genero + " e nota " + str(score) + "...... quer saber mais sobre este filme? Caso queira que eu repita é só dizer repetir")
                reply = microphone_check()
            if (("sim" in reply or "quero" in reply or "gostaria" in reply or "saber" in reply) and not("não" in reply)):
                create_audio(str(content))
                create_audio("está satisfeito com esse filme?")
                reply = microphone_check()
                if("não" in reply):
                    newRandom = 1
                    if(movieToShow == 1):
                        newRandom = random.randint(1, 100)
                    elif(movieToShow == 99):
                        movieToShow = 98
                    else:
                        while newRandom <= movieToShow:
                            newRandom = random.randint(1, 100)
                        movieToShow = newRandom
                    continue
                else:
                    create_audio("tudo bem")
            break
        currentDepth = currentDepth + 1    
        if currentDepth == maxDepth:
            break

def findGenere(movieInfo):
    allGeneres = set(["ação", "todos","terror","animação", \
                "aventura","arte marcial", "comédia","ficção ciêntífica",\
                "musical", "documentário", "faroeste", "romance",\
                "policial", "fantasia", "guerra", "suspense"])
    for eachGenere in allGeneres:
        if eachGenere in movieInfo:
            return eachGenere
    return ""
            
def getMovieList(movieInfo):
    wiki1(1,100)
    genere = findGenere(movieInfo)    
    if ("critica" in movieInfo or "impressa" in movieInfo):
        searchType = "impressa/"
    else:
        searchType = "notas-espectadores/"
    for eachWord in movieInfo:
        try: 
            int(eachWord)
            maxDepth = int(eachWord)
        except ValueError:
            maxDepth = 10

    getMostViewed(genere, searchType, maxDepth)            



    
def getMovieRecomendation(movieInfo):
    print("oioi")
    wiki1(1,100)
    if ("horrivel" in movieInfo or "ruim" in movieInfo):
        badMovie = True
    else:
        badMovie = False
    genere = findGenere(movieInfo)
    searchType = "impressa"
    getRandomMovie(genere, searchType, badMovie)