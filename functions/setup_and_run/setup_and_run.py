from functions.NLP.text_handling import performNLP
from functions.skills.manager import runSkillSet
from functions.personality.personality_checker import runAngry

def setupAndRun(assistant_name, sentence, nlp):
        if("*" in sentence) :
            runAngry()
            return
        sentenceList = sentence.split()
        for i in range(0, len(sentenceList)):
            if assistant_name == sentenceList[i]:
                listSentence = sentenceList[i+1:]
        actualSentence = ' '.join(map(str, listSentence))

        assistant_sentence = performNLP(actualSentence, nlp)
        print(assistant_sentence)
        runSkillSet(assistant_sentence)
