import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui 
import psutil
import pyjokes

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("The Current time is:")
    speak(Time)
    
def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak("The Current Date is:" )
    speak(date)
    speak(month)
    speak(year)

def wishme():
    hour=datetime.datetime.now().hour   
    speak("Welcome Back!")
    time()
    date()
    if hour>=6 and hour<12:
        speak("Good Morning Ankit!")
    elif hour>=12 and hour<18:
        speak("Good AfterNoon Ankit!")
    elif hour>=18 and hour<24:
        speak("Good Evening Ankit!")
    else:
        speak("Good Night Ankit!")
    speak("JARVIS at your service! Please,tell me How can I Help You?")