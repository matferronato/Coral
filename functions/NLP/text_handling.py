
def returnEntities(sentence):
    locationNames = set()
    for ent in sentence.ents:
        locationNames.add(ent.text)
    return locationNames

def protectNames(sentence, locationNames):
    for eachLocation in locationNames:
        if eachLocation in sentence:
            sentence = sentence.replace(eachLocation, eachLocation.replace(" ", "_"))
    return sentence.split()
    #for eachLocation in locationNames:
    #    sameWord = True
    #    wordFound = False
    #    i = 0
    #    while i < len(sentence_list):
    #        if eachLocation.split()[0] in sentence_list[i]:
    #            for j in range(0, len(eachLocation.split())):
    #                if( i+j > len(sentence_list)) : break
    #                if(eachLocation.split()[j] != sentence_list[i+j]):
    #                    sameWord = False
    #            if sameWord == True:
    #                for j in range(1, len(eachLocation.split())):
    #                    sentence_list.pop(i+1)
    #                sentence_list[i] = eachLocation.replace(" ", "_")
    #                wordFound = True
    #            sameWord = True
    #        i = i+1        
    #return sentence_list

def takeOffStopWords(sentence_list, nlp):
    clean_sentence_list =[]
    for eachWord in sentence_list:
        if not (eachWord in nlp.Defaults.stop_words):
            clean_sentence_list.append(eachWord)
    listToStr = ' '.join(map(str, clean_sentence_list))
    return nlp(listToStr)

def lemming(clean_sentence):
    assistante_sentence = []
    for i in range(0,len(clean_sentence)):
        #assistante_sentence.append(clean_sentence[i].lemma_)
        if clean_sentence[i].pos_ == 'VERB':
            assistante_sentence.append(clean_sentence[i].lemma_)
        else:
            assistante_sentence.append(clean_sentence[i])
    tokens = [str(token) for token in assistante_sentence]
    return tokens

def removeUnderScore(tokens):
    for i in range(0 , len(tokens)):
        if( "_" in tokens[i]):
            tokens[i] = tokens[i].replace("_"," ")

def performNLP(sentence, nlp):
    tokens = nlp(sentence)
    sentence_list = protectNames(sentence, returnEntities(tokens))
    clean_sentence = takeOffStopWords(sentence_list, nlp)
    assistant_sentence = lemming(clean_sentence)
    removeUnderScore(assistant_sentence)
    return assistant_sentence
