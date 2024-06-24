import time
from gtts import gTTS
from pygame import mixer
import os
import subprocess
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

def get_desktop_path():
    user_profile = os.environ['USERPROFILE']
    desktop_path = os.path.join(user_profile, 'Desktop')
    onedrive_desktop_path = os.path.join(user_profile, 'OneDrive', 'Desktop')
   
    if os.path.exists(onedrive_desktop_path):
        return onedrive_desktop_path
    return desktop_path


def SearchForKeywords(text):
    firstWord = text.split()[0]
    print(firstWord)

    if(firstWord == "hello" or firstWord == "good" or firstWord == "hey" or firstWord == "hi"):
        t = time.localtime()
        currentTime = time.strftime("%H", t)
        currentTimeNumber = int(currentTime)
        if(currentTimeNumber > 19):
            print("Good Night")
            TextToSpeech("Good Night")

        elif(currentTimeNumber > 11):
            print("Good Afternoon")
            TextToSpeech("Good Afternoon")
       
        else:
            print("Good Morning")
            TextToSpeech("Good Morning")
   
    elif firstWord == "open":
        differentWords = text.split()
        restWords = ' '.join(differentWords[1:])
       
        desktop_path = get_desktop_path()
        print("Desktop path:", desktop_path)

        items = os.listdir(desktop_path)
        found = False
        for item in items:
            filename, file_extension = os.path.splitext(item)
            if restWords.lower() == filename.lower():
                path_to_open = os.path.join(desktop_path, item)
                print("Opening:", path_to_open)
                if os.path.isfile(path_to_open):
                    os.startfile(path_to_open)
                else:
                    subprocess.Popen(f'explorer "{path_to_open}"')
                found = True
                break

        if not found:
            print(f"No item found with name: {restWords}")
   
    elif firstWord == "search" or firstWord == "find":
        differentWords = text.split()
        restWords = ' '.join(differentWords[1:])

        gecko_path = 'C:\\Users\\natti\\Downloads\\geckodriver-v0.34.0-win32\\geckodriver.exe'
        firefox_binary_path = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'


        service = Service(gecko_path)
        options = webdriver.FirefoxOptions()
        options.binary_location = firefox_binary_path
   
        driver = webdriver.Firefox(service=service, options=options)
        driver.get("https://www.google.com/search?client=firefox-b-d&q="+restWords)


    elif(firstWord == "say"):
        differentWords = text.split()
        restWords = ' '.join(differentWords[1:])

        print(restWords)
        TextToSpeech(restWords)
       

def TextToSpeech(text):
    mixer.init()


    speech = gTTS(text)


    speech_file = 'speech.mp3'
    speech.save(speech_file)


    mixer.music.load('speech.mp3')
    mixer.music.play()
    while(mixer.music.get_busy()):
        time.sleep(1)