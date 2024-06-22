from main import time
from gtts import gTTS
from playsound import playsound


def SearchForKeywords(text):
    firstWord = text.split()[0]
    print(firstWord)


    if(firstWord == "hello" or firstWord == "good" or firstWord == "hey" or firstWord == "hi"):
        t = time.localtime()
        currentTime = time.strftime("%H", t)
        currentTimeNumber = int(currentTime)
        if(currentTimeNumber > 17):
            print("Good Night")


        elif(currentTimeNumber > 11):
            print("Good Afternoon")
            TextToSpeech("Good Afternoon")
       
        else:
            print("Good Morning")


def TextToSpeech(text):
    speech = gTTS(text)


    speech_file = 'speech.mp3'
    speech.save(speech_file)


    playsound('speech.mp3')