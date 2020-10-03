from PIL import Image
import matplotlib.pyplot as plt
import time


def runIntro(time, max_loop):
    i1 = Image.open("./functions/personality/Neutra_1.png")
    i2 = Image.open("./functions/personality/Neutra_2.png")
    for i in range(0,max_loop):
        plt.imshow(i1)
        plt.show(block=False)
        plt.axis('off')
        plt.pause(time)
        plt.clf() #will make the plot window empty

        plt.imshow(i2)
        plt.show(block=False)
        plt.axis('off')
        plt.pause(time)
        plt.clf() #will make the plot window empty

def runSad(time):
    plt.clf() #will make the plot window empty
    i1 = Image.open("./functions/personality/Triste_1.png")
    i2 = Image.open("./functions/personality/Triste_2.png")
    for i in range(0,5):
        plt.imshow(i1)
        plt.show(block=False)
        plt.axis('off')
        plt.pause(time)
        plt.clf() #will make the plot window empty

        plt.imshow(i2)
        plt.show(block=False)
        plt.axis('off')
        plt.pause(time)
        plt.clf() #will make the plot window empty

def runNormal():
    plt.clf() #will make the plot window empty
    i1 = Image.open("./functions/personality/Neutra_1.png")
    plt.imshow(i1)
    plt.show(block=False)
    plt.axis('off')
    plt.pause(0.1)

def runAngry():
    plt.clf() #will make the plot window empty
    i1 = Image.open("./functions/personality/Brava_1.png")
    plt.imshow(i1)
    plt.show(block=False)
    plt.axis('off')
    plt.pause(0.1)

def runCute():
    plt.clf() #will make the plot window empty
    i1 = Image.open("./functions/personality/Fofa_1.png")
    plt.imshow(i1)
    plt.show(block=False)
    plt.axis('off')
    plt.pause(0.1)

def runResearch():
    #plt.clf() #will make the plot window empty
    i1 = Image.open("./functions/personality/Pesquisadora_2.png")
    plt.imshow(i1)
    plt.show(block=False)
    plt.axis('off')
    plt.pause(0.1)

def runSerious():
    plt.clf() #will make the plot window empty
    i1 = Image.open("./functions/personality/Seriedade_1.png")
    plt.imshow(i1)
    plt.show(block=False)
    plt.axis('off')
    plt.pause(0.1)

def runListening():
    plt.clf() #will make the plot window empty
    i1 = Image.open("./functions/personality/Escutando_1.png")
    plt.imshow(i1)
    plt.show(block=False)
    plt.axis('off')
    plt.pause(0.1)
#show image
