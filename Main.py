# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 02:21:55 2020

@author:Manas gupta
"""
import ChatBot as chat
import pyttsx3
import speech_recognition as  sr


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

chat.takeCommand()