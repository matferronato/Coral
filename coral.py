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
from functions.personality.personality_checker import runIntro, runResearch, runNormal
from functions.skills.skill_get_emotion import getAngry
from functions.setup_and_run.setup_and_run import setupAndRun
import spacy

import ctypes

import threading
import time
assistant_name = "coral"

def main():
    print("loading spacy")
    nlp = spacy.load('pt_core_news_md')
    nlp.Defaults.stop_words.add("a")
    nlp.Defaults.stop_words.add("e")
    nlp.Defaults.stop_words.add("o")
    runIntro(0.01,2)
    #create_audio("Olá, eu sou a " + assistant_name + "! Sou sua assistente pessoal")
    while(1):
        runIntro(0.01,2)
        sentence = microphone_check()
        #sentence = "coral me recomenda um filme de terror do nepal"
        while not(assistant_name in sentence):
            sentence = microphone_check()
            print(sentence)
        runNormal()
        setupAndRun(assistant_name, sentence,nlp)


#exploring threads
#class Run(threading.Thread):
#    def __init__(self, name, assistant_name, sentence, nlp):
#        threading.Thread.__init__(self)
#        self.name = name
#        self.assistant_name = assistant_name
#        self.sentence = sentence
#        self.nlp = nlp
#
#    def run(self):
#        try:
#            if("*" in self.sentence) :
#                getAngry()
#                return
#            sentenceList = self.sentence.split()
#            for i in range(0, len(sentenceList)):
#                if self.assistant_name == sentenceList[i]:
#                    listSentence = sentenceList[i+1:]
#            actualSentence = ' '.join(map(str, listSentence))
#
#            assistant_sentence = performNLP(actualSentence, self.nlp)
#            print(assistant_sentence)
#            runSkillSet(assistant_sentence)
#        finally:
#            print('ended')
#
#    def get_id(self):
#
#        # returns id of the respective thread
#        if hasattr(self, '_thread_id'):
#            return self._thread_id
#        for id, thread in threading._active.items():
#            if thread is self:
#                return id
#
#    def raise_exception(self):
#        thread_id = self.get_id()
#        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
#              ctypes.py_object(SystemExit))
#        if res > 1:
#            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
#            print('Exception raise failure')
#
#
#-----------------------------------------------------
if __name__ == '__main__': # chamada da funcao principal
    main()
