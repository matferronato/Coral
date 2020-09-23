import datetime
from functions.voice_return_handler.voice_return import create_audio


def getTime(current_sentence,i):
    localTime = datetime.datetime.now().time()
    sentence = "agora são " + str(localTime.hour) + " horas e " + str(localTime.minute) + " minutos "
    create_audio(sentence)
