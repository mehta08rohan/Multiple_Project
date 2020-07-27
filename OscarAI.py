import pyttsx3
import speech_recognition as sr
import datetime



engine = pyttsx3.init('sapi5')
voices= engine.getProperty("voices")
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >=0 and hour <12:
        speak("Good Morning Sir")
    elif hour >=12 and hour<16:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")

def takeCommand():
    r= sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening. . . ")
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("Recognizing. . ")
        query = r.recognize_google(audio,Language="en-in")
        print(f"You said {query}\n")
    except Exception as e:
        print("Sorry Sir! I cnt understand you. Please try again")
        return takeCommand()
    return query

if __name__ == '__main__':

    wishMe()
    takeCommand()

