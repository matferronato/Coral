import datetime
from functions.voice_return_handler.voice_return import create_audio


def getTime(current_sentence,i):
    localTime = datetime.datetime.now().time()
    sentence = "agora são " + str(localTime.hour) + " horas e " + str(localTime.minute) + " minutos "
    create_audio(sentence)
    create_audio("não se esqueça que o relógio fica no canto inferior direito do seu computador...")  
