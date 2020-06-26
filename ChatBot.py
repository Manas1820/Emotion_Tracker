# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 19:32:50 2020

@author:Manas gupta
"""

import pyttsx3
import speech_recognition as  sr
import smtplib as s
import Sentiment as S
import Emotion


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
        # print(e)    
        print("Say that again please...")  
        return "None"
    
    return query

def emotion_sad(Sentiment):
    speak("Hey ! You seem a little sad ? Wats the matter")
    response = takeCommand().lower()
    Sentiment+=(S.get_Sentiment(response)*10)
    check_Sentiment_level(Sentiment)

def emotion_angry(Sentiment):
    speak("Hey ! You seem angry ? Wats the matter")
    response = takeCommand().lower()
    Sentiment+=(S.get_Sentiment(response)*5)
    check_Sentiment_level(Sentiment)
            
def send_mail(reciever,content):
    server = s.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    speak('Can you please type your password to confirm ')
    server.login('manasgupta1820@gmail.com','password')
    server.sendmail('manasgupta1820@gmail.com',reciever, content)
    server.close()
    
def check_Sentiment_level(Sentiment,Friend,Family_member):
    if Sentiment < 2 :
        send_mail(Friend,'Warning : User is feeling a bit low , Please contact him !    -BOT')
        send_mail(Family_member,'Warning : User is feeling a bit low , Please contact him !     -BOT')
    
    elif Sentiment > 100 :
        Sentiment = 100
    
    elif Sentiment < 0 :
        send_mail(Friend,'Warning : User is prone to be voilent ,Make sure if he is ok !    -BOT')
        Sentiment = 0
        
        
if __name__ == '__main__' :
    
    while True :        
        print(Emotion.get_emotion())                                                                                                 