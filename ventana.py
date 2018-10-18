from tkinter import *
import time
import clipboard
from googletrans import Translator

def regularExpresion(string, expresion):
    r = re.compile(expresion)
    if(r.match(string)):
        return True
    else:
        return False


def printWindow(text):
    translator = Translator()
    translateText = ""

    rawText.delete(1.0,END)
    traduceText.delete(1.0,END)
    rawText.insert(INSERT, text)
    translateText = translator.translate(text)
    traduceText.insert(INSERT, translateText.text)

def translate():
    passtText = ""
    expresion = '*'

    if(input("Any Regular Expresion? (y/n) <") == 'y'):
        expresion = input("add the expresion <")
    
    while True:
        window.update_idletasks()
        window.update()
        text = clipboard.paste()
        if(text != passtText and text != ""):
            if(expresion != '*'):
                if(regularExpresion(text,expresion) != True):
                    printWindow(text)
                    passtText = text
            else:
                printWindow(text)
                passtText = text
                

window = Tk()
window.title("Translater")
window.geometry("650x600")
window.resizable(False,False)

rawText = Text(window, height=50, width=40)
traduceText = Text(window, height=50, width=50)
rawText.pack(padx = 5, pady=10, side = LEFT)
traduceText.pack(padx=5, pady=10, side = LEFT)

translate()