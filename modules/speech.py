import speech_recognition as sr
from gtts import gTTS 
import uuid
import os
import playsound

# Speech recognizer
recognizer = sr.Recognizer()
microphone = sr.Microphone()

def speak(text):
    if not text.strip():
        return
    print(f"Nova:{text}")

    #temp file
    filename = f"temp_{uuid.uuid4()}.mp3"
    path = f"temp_audio/{filename}"
    tts = gTTS(text,lang="en")
    tts.save(f"temp_audio/{filename}")

    playsound.playsound(path)
    os.remove(path)


def listen():
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            print("No speech detected. Try again...")
            return ""  # returns empty string instead of crashing

    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.RequestError:
        print("Speech Recognition API unavailable.")
        return ""

