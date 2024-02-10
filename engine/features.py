import os
import re
from playsound import playsound
import eel
from engine.command import speak 
from engine.config import ASSISTANT_NAME



# intro play assistant function
import pywhatkit as kit

from engine.helper import extract_yt_term, remove_words


@eel.expose #somehow not working with live server
def playAssistantSound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)
    
def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open","")
    query.lower()
    
    if query!="":
        speak("Got it, Opening "+query)
        os.system('start '+query)
    else:
        speak("not found")
        
# def PlayYoutube(query): # function to play youtube on chrome
#     search_term = extract_yt_term(query)
#     speak("Playing "+search_term+" on YouTube")
#     kit.playonyt(search_term)
    
# def extract_yt_term(command):
#     pattern = r'play\s+(.*?)\s+on\s+youtube'  
#     match = re.search(pattern, command, re.IGNORECASE)
#     return match.group(1) if match else None

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+" on YouTube")
    kit.playonyt(search_term)

