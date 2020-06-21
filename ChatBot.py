# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 19:32:50 2020

@author:Manas gupta
"""

import pyttsx3
import datetime
import speech_recognition as  sr
import os
import smtplib as s
import Sentiment as S


# VOICE Settings
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

# To get the present time 
Time = datetime.datetime.now().strftime("%H:%M:%S")


# Storing Personal Information
# For now i am informing the friend or family member using email later on it can be improved


close_friend_email = 'guptakush81@gmail.com'
family_member_email= 'guptakush81@gmail.com'


# Calculation of a emotion level
SENTIMENT= 50

# Limit for a emotion
POSITIVE_SATURATION_POINT= 100
NEGATIVE_SATURATION_POINT= 0


# Tracking feature

# this will keep a track of all the things which made the user sad with first parameter as time and second as reason 
# time:reason
SAD_REASON ={} 


# This will keep a track of all the time which made the user angry with first parameter as time and second as reason
# time:reason
ANGRY_REASON={}




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

def emotion_sad():
    speak("Hey ! You seem a little sad ? Wats the matter")
    response = takeCommand().lower()
    SENTIMENT=(S.get_Sentiment(response)*10)+SENTIMENT
    check_Sentiment_level(SENTIMENT)
    SAD_REASON[Time]=response

def emotion_angry():
    speak("Hey ! You seem angry ? Wats the matter")
    response = takeCommand().lower()
    SETIMENT=(S.get_Sentiment(response)*10)+SENTIMENT
    check_Sentiment_level(SENTIMENT)
    ANGRY_REASON[Time]=response    



def send_mail(reciever,content):
    server = s.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    speak('Can you please type your password to confirm ')
    server.login('manasgupta1820@gmail.com','mrmv1227')
    server.sendmail('manasgupta1820@gmail.com',reciever, content)
    server.close()
    
def check_Sentiment_level(Sentiment):
    if Sentiment < 25 :
        send_mail(close_friend_email,'Warning : User is feeling a bit low , Please contact him !    -BOT')
        send_mail(family_member_email,'Warning : User is feeling a bit low , Please contact him !     -BOT')
    elif Sentiment > POSITIVE_SATURATION_POINT :
        SENTIMENT = POSITIVE_SATURATION_POINT
    
    elif SENTIMENT < NEGATIVE_SATURATION_POINT :
        send_mail(close_friend_email,'Warning : User is prone to be voilent ,Make sure if he is ok !    -BOT')
        SENTIMENT = NEGATIVE_SATURATION_POINT