#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:30:38 2019

@author: soyokaze

"""
from gtts import gTTS
from playsound import playsound
f = open("input.txt", "r")
x = f.read()
speech = gTTS("Hello, how are you! :)", 'en')
var = "ply"
speech.save(var+".mp3")
playsound(var+".mp3")


"""
#rock paper scissors game!!

from numpy import *
import speech_recognition as sr
r = sr.Recognizer()
t = True
while(t):
    with sr.Microphone() as sameer:
        r.adjust_for_ambient_noise(sameer)
        print("bol kuch pagal!!")
        awaz = r.listen(sameer)
        bol = r.recognize_google(awaz)
    f = open("input.txt", "a")
    f.write("\n"+bol)
    f.close()    
    l=["stone","paper","scissors"]
    i = random.randint(0,2)
    try:
        print("abe tune bola: " + bol)
        print("mein bola: " + l[i])
        if(bol=="stone"):
            if(l[i]=="paper"):
                print("you lost!!")
            if(l[i]=="stone"):
                print("tie!!")
            if(l[i]=="scissors"):
                print("you win this time!!")
        elif(bol=="paper"):
            if(l[i]=="stone"):
                print("you win this time!!")
            if(l[i]=="paper"):
                print("tie!!")
            if(l[i]=="scissors"):
                print("you lost!!")
        elif(bol=="scissors"):
            if(l[i]=="stone"):
                print("you lost!!")
            if(l[i]=="paper"):
                print("you win!!")
            if(l[i]=="scissors"):
                print("tie!!")
       
        with sr.Microphone() as sam:
            r.adjust_for_ambient_noise(sam)
            print("\n wanna play again!!")
            voice = r.listen(sam)
            pal = r.recognize_google(voice)
        try:
            if(pal=="exit" or pal=="no"):
                print("Okay see ya later!!")
                t=False
            elif(pal=="yes"):
                print("Okay you asked for it!! here we go again!!")
                t=True
        except sr.UnknownValueError:
            print("bye!!")
    except sr.UnknownValueError: 
        print("jai mata di!!")"""
