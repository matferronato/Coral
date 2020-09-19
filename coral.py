#Central
#Orientada ao
#Reconhecimento
#Automatico da
#Linguagem

#CORAL


#python -m spacy download pt
#python -m spacy download pt_core_news_md
#testing enviroment
from functions.google_speech_recognition.speech import microphone_check
from functions.voice_return_handler.voice_return import create_audio
from functions.animations.animations import runIntro, IntroFrame1, runSad, runBlink
from functions.NLP.text_handling import performNLP
from functions.skills.manager import runSkillSet
from functions.skills.skill_get_emotion import getAngry
import spacy


assistant_name = "coral"

def main():
    nlp = spacy.load('pt_core_news_md')
    nlp.Defaults.stop_words.add("a")
    nlp.Defaults.stop_words.add("e")
    nlp.Defaults.stop_words.add("o")
    IntroFrame1(2,2)
    #create_audio("Olá, eu sou a " + assistant_name + "! Sou sua assistente pessoal")
    while(1):
        #runIntro()
        #runIntro()
        #sentence = microphone_check()
        sentence = "coral qual o cep da rua gravatai"
        if(sentence == "não entendi") : continue
        if("*" in sentence) : 
            getAngry()
            continue
        assistant_sentence = performNLP(sentence, nlp)
        print(assistant_sentence)
        runSkillSet(assistant_name,assistant_sentence)
        
#-----------------------------------------------------
if __name__ == '__main__': # chamada da funcao principal
    main()


