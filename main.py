import pyttsx3
def textToVoice():
    eng = pyttsx3.init()
    eng.say("I wrote these codes with python libraries and I completed my library homework")
    eng.runAndWait()

if __name__  == "__main__":
    textToVoice()
