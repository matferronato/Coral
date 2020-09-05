#Central
#Orientada ao
#Reconhecimento
#Automatico da
#Linguagem

#CORAL

from functions.google_speech_recognition.speech import microphone_check
from functions.voice_return_handler.voice_return import create_audio
from functions.animations.animations import runIntro, IntroFrame1, runSad, runBlink
from functions.NLP.text_handling import performNLP
from functions.skills.manager import runSkillSet

assistant_name = "coral"

def main():
    IntroFrame1(2,2)
    create_audio("Olá, eu sou a Coral! Sou sua assistente pessoal")
    while(1):
        runIntro()
        runIntro()
        sentence = microphone_check()
        #print(sentence)
        if(sentence == "não entendi") : continue
        assistant_sentence = performNLP(sentence)
        runSkillSet(assistant_name,assistant_sentence)
        
#-----------------------------------------------------
if __name__ == '__main__': # chamada da funcao principal
    main()


