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

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=5)
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)    
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(query)
    except Exception as ex:
        print(ex)
        speak("Unable To Recognize! Say That Again please....")
        return "None"
    return query

def quitScr():
    import sys
    return sys.exit()

def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("ankitmohanty1804@gmail.com","")
    server.sendmail("ankitmohanty1804@gmail.com",to,content)
    server.close()
    
def screenShot():
    img=pyautogui.screenshot()
    img.save("C:\\Users\\OCAC\\Desktop\\Python Programs\\Projects\\screenshot.png")
    
def cpuUsage():
    usage=str(psutil.cpu_percent())
    speak("CPU is at "+usage)
    battery=psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent )
    
def tellJokes():
    speak(pyjokes.get_joke())