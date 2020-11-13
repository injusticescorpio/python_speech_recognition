import speech_recognition as sr 
import pyttsx3  
from time import ctime
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS

r = sr.Recognizer()                #for recognizing speech
def record_audio(ask=False):
    if ask:
        arista_speak(ask)
    with sr.Microphone() as source:
        audio =r.listen(source)#source is our microphone
        voice_data=''     
        try:
            voice_data=r.recognize_google(audio)
        except sr.UnknownValueError:
            arista_speak("Sorry, that didn't come up right please try again!" )
        except sr.RequestError:
            arista_speak('sorry,my speech service is down')
    return voice_data        
def arista_speak(audio_string):
    text_to_speech=gTTS(text=audio_string,lang='en')
    r=random.randint(1,10**5)
    audiofile='audio-'+str(r)+'.mp3'
    text_to_speech.save(audiofile)
    playsound.playsound(audiofile)
    print(audio_string)
    os.remove(audiofile)

def respond(voice_data):
    if 'what is your name'== voice_data:
        arista_speak('My name is Arista')
    if ('what time is it' in voice_data) or ("what's the time" in voice_data):
        arista_speak(ctime())
    if ('i like to search' in voice_data) or ('Google search' in voice_data):
        search=record_audio('What do you want to search for?')
        url='https://www.google.com/search?q='+search
        webbrowser.get().open(url) 
        arista_speak('Here is what i found in the web')  
    if  'I like to find the location' in voice_data or 'search' == voice_data:
        location_search=record_audio('What do u like to search for?')
        url='https://google.nl/maps/place/'+location_search+'/&amp;'
        webbrowser.get().open(url)
        arista_speak("here is the location of"+location_search)    
    if voice_data.lower() in ['exit','quit','ok bye']:
        arista_speak('Bye arjun')
        exit()
    if voice_data.lower() in ['who is your sister','sister','sis','sissy']:
        arista_speak('My sister name is Anjana also called as paru.She is an interesting brilliant and an arrogant girl. But still,I like her')
    if voice_data.lower() in ['arista who named u','arista who named you','who named you']:
        arista_speak('I was  named by my sister Anjana R pillai')
time.sleep(1)
arista_speak('Hello,How can i help u')
while 1:
    voice_data=record_audio()
    print(voice_data)
    respond(voice_data)













