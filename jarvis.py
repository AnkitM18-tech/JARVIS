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

if __name__ == "__main__":
    wishme()
    while True:
        query=takeCommand().lower()
        if "time" in query:
            time()
            
        elif "date" in query:
            date()
            
        elif "wikipedia" in query:
            speak("Searching...")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
            
        elif "send email" in query:
            try:
                speak("What Should I say?")
                content=takeCommand()
                to="luckyvk23@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as ex:
                print(ex)
                speak("Unable To send The email!")
                
        elif "search in chrome" in query:
             speak("What Should I search?")
             chromepath="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
             search=takeCommand().lower()
             wb.get(chromepath).open_new_tab(search +".com")
             
        elif "logout" in query:
            os.system("shutdown -l")
            
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
            
        elif "restart" in query:
            os.system("shutdown /r /t 1")
             
        elif "play songs" in query:
            songs_dir ="D:\\Mobile Storage\\UCDownloads\\Music"
            songs=os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))
            
        elif "remember that" in query:
            speak("What should I remember?")
            data=takeCommand()
            speak("You told me To Remember "+data)
            remember=open("data.txt","w")
            remember.write(data)
            remember.close()
            
        elif "do you know anything" in query:
            remember=open("data.txt","r")
            speak("You told me to remember that "+remember.read())
            
        elif "screenshot" in query:
            screenShot()
            speak("Done!")
            
        elif "cpu" in query:
            cpuUsage()
            
        elif "joke" in query:
            tellJokes()
            
        elif "offline" in query:
            quitScr()