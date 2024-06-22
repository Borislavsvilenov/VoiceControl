import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write
import time
import os

def SearchForKeywords(text):
    firstWord = text.split()[0]
    print(firstWord)


frequency = 44100
duration = 5

r = sr.Recognizer()

recording = sd.rec(int(duration * frequency), samplerate=frequency, channels=1, dtype='int16')
sd.wait()

sd.wait()

write("recording0.wav", frequency, recording)

time.sleep(0.2)
    
with sr.AudioFile('recording0.wav') as source:
    audio_text = r.listen(source)
    text = r.recognize_google(audio_text)
    print(text)
    SearchForKeywords(text)