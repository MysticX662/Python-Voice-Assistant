from imports import *
from passwordgui import *
from commands import *
import tutorial
speak("hi , what can I help you with")
voice_data=takevoice()
if password.get()=="ironman" or "emergency" or "iamironman":
    speak("welcome back nickhil")
elif password.get()=="eesha" or "eeshaisababy":
    speak("welcome eesha")



while True:
    if voice_data.count(wake) > 0:
        while True:
            voice_data = takevoice()
            takecommand(voice_data)