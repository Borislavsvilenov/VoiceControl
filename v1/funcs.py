import time
from gtts import gTTS
import os

def SearchForKeywords(text):
    firstWord = text.split()[0]
    print(firstWord)

    if(firstWord == "hello" or firstWord == "good" or firstWord == "hey" or firstWord == "hi"):
        t = time.localtime()
        currentTime = time.strftime("%H", t)
        currentTimeNumber = int(currentTime)
        if(currentTimeNumber > 19):
            print("Good Night")

        elif(currentTimeNumber > 11):
            print("Good Afternoon")
            TextToSpeech("Good Afternoon")
       
        else:
            print("Good Morning")

def TextToSpeech(text):
    speech = gTTS(text)
    
    speech.save("speech.mp3")
    os.system("afplay speech.mp3")
    os.remove('speech.mp3')
