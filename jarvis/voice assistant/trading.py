import sys
import threading
from pyaudio import paPrimingOutput
from pynput.keyboard import Key, Controller
from urllib import request
sys.path.append("C:/Users/Gebruiker/AppData/Local/Programs/Python/Python39/Lib/site-packages")
from os import close
import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import subprocess
import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError
import pyautogui
import psutil 
import pyjokes
import requests
import cv2
from newsapi import NewsApiClient
import pycountry
import multiprocessing
import keyboard as kyb
import time

engine = pyttsx3.init()
engine.say("")
engine.runAndWait()

def speak(self,audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        #r.pause.threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        return "None"

    return query
    quit