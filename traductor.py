import clipboard
from googletrans import Translator

def main():
    passtText = ""
    translator = Translator()
    translateText = ""

    while True:
        text = clipboard.paste()
        text.replace("【","[")
        text.replace("】","]")
        if(text != passtText and text != ""):
            translateText = translator.translate(text)
            print("\n\n")
            print(translateText.text)
            print("\n\n")
            passtText = text

if __name__=='__main__':
    main()