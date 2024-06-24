import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write
import time
from funcs import *

def main():
    frequency = 44100
    duration = 2

    r = sr.Recognizer()

    recording = sd.rec(int(duration * frequency), samplerate=frequency, channels=1, dtype='int16')
    sd.wait()
    sd.wait()
    write("lastRecord.wav", frequency, recording)

    time.sleep(0.2)
   
    with sr.AudioFile('lastRecord.wav') as source:
        try:
            audio_text = r.listen(source)
            text = r.recognize_google(audio_text)
            print(text)
            SearchForKeywords(text)
        except sr.UnknownValueError:
            print("Couldn't understand audio")
        except:
            print("Something went wrong")

if __name__ == '__main__':
    main()
