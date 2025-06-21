import datetime
import os
import sys
import time
import webbrowser
import pyautogui
import pyttsx3
import speech_recognition as sr
import json
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import random
import numpy as np
import psutil
import subprocess
# from elevenlabs import generate, play
# from elevenlabs import set_api_key
# from api_key import api_key_data
# set_api_key(api_key_data)

# def engine_talk(query):
#     audio = generate(
#         text = query,
#         voice = 'Grace',
#         model = 'eleven_monolingual_v1'
#     )
#     play(audio)


# Load intents and ML model
with open("intent.json") as file:
    data = json.load(file)

model = load_model("chat_model.h5")

with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

with open("label_encoder.pkl", "rb") as encoder_file:
    label_encoder = pickle.load(encoder_file)

# Text-to-speech

def initialize_engine():
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    return engine

def speak(text):
    engine = initialize_engine()
    engine.say(text)
    engine.runAndWait()

# Speech recognition

def command():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            print("Listening...", end="", flush=True)
            audio = r.listen(source, timeout=5, phrase_time_limit=8)
            query = r.recognize_google(audio, language='en-IN')
            print(f"You said: {query}")
            return query
    except Exception as e:
        print("Mic error or unclear speech.")
        return input("Type your command instead: ")

# Date/Time greetings

def cal_day():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[datetime.datetime.today().weekday()]

def wishMe():
    hour = datetime.datetime.now().hour
    t = time.strftime("%I:%M %p")
    day = cal_day()
    if hour < 12:
        speak(f"Good morning! It's {day}, {t}")
    elif hour < 17:
        speak(f"Good afternoon! It's {day}, {t}")
    else:
        speak(f"Good evening! It's {day}, {t}")

# Social media

def social_media(query):
    urls = {
        'facebook': 'https://www.facebook.com/',
        'whatsapp': 'https://web.whatsapp.com/',
        'discord': 'https://discord.com/',
        'instagram': 'https://www.instagram.com/'
    }
    for key in urls:
        if key in query:
            speak(f"Opening {key}")
            webbrowser.open(urls[key])
            return
    speak("No matching social media found")

# Schedule

def schedule():
    day = cal_day().lower()
    week = {
        "monday": "Algorithms, System Design, Programming Lab",
        "tuesday": "Web Dev, DBMS, Open Source Lab",
        "wednesday": "ML, OS, Ethics, SE Workshop",
        "thursday": "Networks, Cloud, Cyber Lab",
        "friday": "AI, Adv Prog, UI/UX, Capstone",
        "saturday": "Meetings, Innovation, Self-study",
        "sunday": "Holiday, self-work"
    }
    speak("Today's schedule:")
    speak(week.get(day, "No classes today."))

# System condition

def condition():
    cpu = psutil.cpu_percent()
    battery = psutil.sensors_battery().percent
    speak(f"CPU is at {cpu} percent. Battery at {battery} percent.")
    if battery < 40:
        speak("Please plug in the charger soon.")

# App control

def openApp(query):
    if "calculator" in query:
        os.startfile('C:\\Windows\\System32\\calc.exe')
    elif "notepad" in query:
        os.startfile('C:\\Windows\\System32\\notepad.exe')
    elif "paint" in query:
        os.startfile('C:\\Windows\\System32\\mspaint.exe')

def closeApp(query):
    apps = {"calculator": "calc.exe", "notepad": "notepad.exe", "paint": "mspaint.exe"}
    for app, proc in apps.items():
        if app in query:
            os.system(f"taskkill /f /im {proc}")

# Web search

def browsing(query):
    if 'google' in query:
        speak("What should I search?")
        q = command()
        webbrowser.open(f"https://www.google.com/search?q={q}")

# Chatbot reply

def chat_response(query):
    seq = tokenizer.texts_to_sequences([query])
    padded = pad_sequences(seq, maxlen=20, truncating='post')
    result = model.predict(padded)
    confidence = np.max(result)
    if confidence > 0.7:
        tag = label_encoder.inverse_transform([np.argmax(result)])[0]
        for intent in data['intents']:
            if intent['tag'] == tag:
                speak(random.choice(intent['responses']))
                return
    speak("I'm not sure how to respond to that.")

# Main loop
if __name__ == "__main__":
    wishMe()
    
    # engine_talk('Allow me to introduce myself I am jarvis, the virtual artificial Intelligence ans i am to assist you with a variety of tasks as best I can, 24 hours a day seven days a week' )
    while True:
        query = command().lower()
        if any(x in query for x in ["facebook", "discord", "whatsapp", "instagram"]):
            social_media(query)
        elif "time table" in query or "schedule" in query:
            schedule()
        elif "volume up" in query:
            pyautogui.press("volumeup")
        elif "volume down" in query:
            pyautogui.press("volumedown")
        elif "mute" in query:
            pyautogui.press("volumemute")
        elif "open" in query:
            openApp(query)
        elif "close" in query:
            closeApp(query)
        elif "open google" in query:
            browsing(query)
        elif "system condition" in query or "condition of the system" in query:
            condition()
        elif "exit" in query:
            speak("Goodbye!")
            sys.exit()
        else:
            chat_response(query)
