# pyttsx3 is a text-to-speech conversion library
from unittest import result
import pyttsx3

# Datetime module supplies classes to work with date and time
import datetime

# To convert the spoken words into text, make a query or give a reply
import speech_recognition as sr


import wikipedia

import webbrowser

import os

import datetime

# The variable engine is created to take voices of users and here abrivation of SAPI is Speech Application Programming Interface
engine = pyttsx3.init('sapi5')

# The variable voice is created to take inbuilt property of voice
voices = engine.getProperty('voices')

# Here we are setting the voice
engine.setProperty('voice', voices[1].id)

# speak function created to speak the audio
def speak (audio):
    #engine.say(audio): Audio string will play when engine.say command will execute
    engine.say(audio)
    #engine.runAndWait(): This function will make the speech audible in the system
    engine.runAndWait()

# wish function is created it will wish you eg:Good Morning
def wishMe():
    # We have created a variable hour of int datatype and it will stor time in it
    hour = int(datetime.datetime.now().hour)

    if hour>= 0 and hour<12:
        speak("Good Morning!Have a nice day")

    elif hour>=12 and hour<17:
        speak("Good Afternoon")

    elif hour>=17 and hour<8:
        speak("Good Evening")

    else:
        speak("Good Night")

    speak("I am Jarvis Sir, Please tell me how may I help you")

# It takes microphone input from the use and returns string output
def takeCommand():

    # Here Recognizer class will help us to recongnize voice
    recog = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")

        #Seconds of non-speaking audio before a phrase is consider the speaking audio a phrase- values below this are ignored
        recog.pause_threshold = 1

        audio = recog.listen(source)

        try:
            print("Just a moment. . .")
            query = recog.recognize_google(audio, language='en-in')
            print(f"User said:{query}\n")

        except Exception as e:

            return "None"
        return query


# Voice(function) will execute in main function
if __name__ == '__main__':
    wishMe()
    
    #Logic for executing tasks based on query
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia. . .')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)
            exit()
            
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            exit()         


        elif 'open google' in query:
            webbrowser.open("google.com")
            exit()

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")             
            exit()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            exit()
            
        elif 'vs code' in query:
            codepath = "C:\\Users\\singh\\AppData\\Local\\Programs\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            exit()
            
        else:
            print('Plase can you repeat')
            