# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 19:32:50 2020

@author:Manas gupta
"""

import pyttsx3
import speech_recognition as  sr
import smtplib as s
import Sentiment as S
import Emotion as e
from time import sleep


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio) :
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")  
        return "None"
    
    return query

def emotion_sad(Sentiment):
    speak("Hey ! You seem a little sad ? Wats the matter")
    response = takeCommand().lower()
    Sentiment+=(S.get_Sentiment(response)*10)
    check_Sentiment_level(Sentiment,'friend@email.com','family@gmail.com')
    return Sentiment

def emotion_angry(Sentiment):
    speak("Hey ! You seem angry ? Wats the matter")
    response = takeCommand().lower()
    Sentiment+=(S.get_Sentiment(response)*5)
    check_Sentiment_level(Sentiment,'friend@email.com','family@gmail.com')
    return Sentiment

def emotion_happy(Sentiment) :
     speak("Hey ! You seem happy ? Anything Special")
     response = takeCommand().lower()
     Sentiment+=(S.get_Sentiment(response)*2)
     return Sentiment
            
def send_mail(reciever,content):
    server = s.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    speak('Can you please type your password to confirm ')
    server.login('manasgupta1820@gmail.com','password')
    server.sendmail('manasgupta1820@gmail.com',reciever, content)
    server.close()
    
def check_Sentiment_level(Sentiment,Friend,Family_member):
    if Sentiment < 20 :
        send_mail(Friend,'Warning : User is feeling a bit low , Please contact him !    -BOT')
        send_mail(Family_member,'Warning : User is feeling a bit low , Please contact him !     -BOT')
    
    elif Sentiment > 100 :
        Sentiment = 100
    
    elif Sentiment < 0 :
        send_mail(Friend,'Warning : User is not in a stable condition ,Make sure if he is ok !    -BOT')
        Sentiment = 0
        
        
if __name__ == '__main__' :
      
    Sentiment = 50
    while True :
        current_emotion = e.get_emotion()  
        print("loop is running")
        if current_emotion =='sad' :
            Sentiment = emotion_sad(Sentiment)
            print(f'sad {Sentiment}')
            sleep(10000)
       
        if current_emotion =='angry' :
            Sentiment = emotion_angry(Sentiment)
            print(f'angry {Sentiment}')
            sleep(10000)
        
        if current_emotion == 'neutral' :
            print(f'neutral {Sentiment}')
            sleep(100)
            
        if current_emotion =='happy' :
             Sentiment = emotion_sad(Sentiment)
             print(f'happy {Sentiment}')
             sleep(10000)
                                                                                                             
