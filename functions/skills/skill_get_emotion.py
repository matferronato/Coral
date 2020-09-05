from functions.voice_return_handler.voice_return import create_audio
from functions.animations.animations import Happy1, IntroFrame1, runSad, runBlink, OhNo1



def getEmotion(current_sentence,i):
    badWords = ["feia", "chata", "gorda", "balofa", "idiota", "arrogante", "horrivel", "fedida"]
    goodWords = ["linda", "perfeita", "maravilhosa", "engraçada", "eficiente", "bonita", "amiga", "amavel"]
    if(current_sentence[i+1] in badWords):
        runSad()
        create_audio("eu não sou " + current_sentence[i+1] + " você quem é")
    elif(current_sentence[i+1] in goodWords):
        Happy1(2,1)
        create_audio("obrigada, eu não sei se eu sou tão " + current_sentence[i+1] + " assim, você é muito gentil")