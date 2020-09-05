import os
from functions.voice_return_handler.voice_return import create_audio


def runWebBrowser(current_sentence,i):
    if(current_sentence[i+1] == "site"):
        os.system('.\\Firefox.lnk -new-tab http://www.'+current_sentence[i+2]+'.com/');
    else:
        os.system('.\\Firefox.lnk -new-tab http://www.'+current_sentence[i+1]+'.com/');