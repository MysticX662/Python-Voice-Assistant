import requests, json
import pyttsx3
import tkinter as tk
import json
import random
import operator
import speech_recognition as sr
import datetime
import webbrowser
import speedtest
import os
import feedparser
from playsound import playsound
import pyjokes
from webdriver_manager.chrome import ChromeDriverManager
import smtplib
import cv2
from selenium import webdriver
import pyautogui
import ctypes
import time
import requests
import shutil
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
import wikipedia
import pywhatkit
from PIL import Image
import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import subprocess
import sounddevice as sd
from scipy.io.wavfile import write
import re
import openai
import random
from tkinter import *
import threading
from PIL import Image, ImageTk
from tkinter import *
from functools import partial
from tkinter import messagebox
import time
import wolframalpha
app_id = "QJRG7T-XEG9GQ2QL5"
client = wolframalpha.Client(app_id)

engine = pyttsx3.init()
wake = "Jarvis"
def speak(audio,audio1=""):
    engine.say(audio,audio1)
    engine.runAndWait()
def add(x, y ):
    return x+y
def subtract(x, y):
    return x-y
def multiply(x, y):
    return x*y
def divide(x,y):
    return x/y

def time():
    Time = datetime.datetime.now().strftime("%I:%M")
    speak(Time)

def date():
    day = int(datetime.datetime.now().day)
    Month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak(Month)
    speak(day)
    speak(year)
def wishme():
    speak("welcome back sir!")
    speak("the current time is")
    time()
    speak("the date is")
    date()
    hour = datetime.datetime.now().hour
    if hour>=6 and hour <12:
        speak("good morning sir eesha is a baby hahaha")
    elif hour>=12 and hour <18:
        speak("good afternoon sir, Eesha is a baby hahaha")
    elif hour >= 18 and hour <24:
        speak("good evening sir.   Eesha is a baby by the way hahahahaha")
    else:
        speak("goodnight sir")
    
    speak("how can I help you!")

def takevoice():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            print('you said : {}'.format(voice_data))
        except sr.UnknownValueError:
            pass
        return voice_data