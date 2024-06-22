import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write
import time

from funcs import SearchForKeywords

frequency = 44100
duration = 5

r = sr.Recognizer()

def main():
    recording = sd.rec(int(duration * frequency), samplerate=frequency, channels=1, dtype='int16', blocking=True)
    sd.wait()

    sd.wait()

    write("recording0.wav", frequency, recording)

    time.sleep(0.2)

    with sr.AudioFile('recording0.wav') as source:
        audio_text = r.listen(source)
        try:
            text = r.recognize_google(audio_text)
            print(text)
            SearchForKeywords(text)
        except:
            print('Sorry.. run again...')

if __name__ == '__main__':
    main()
