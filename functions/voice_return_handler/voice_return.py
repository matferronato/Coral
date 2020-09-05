#Funcao responsavel por falar

from gtts import gTTS
from playsound import playsound
import os

def create_audio(audio):
    tts = gTTS(audio,lang='pt-br')
    if os.remove('audios/hello.mp3'): os.remove('audios/hello.mp3')
    tts.save('audios/hello.mp3')
    playsound('audios/hello.mp3')


