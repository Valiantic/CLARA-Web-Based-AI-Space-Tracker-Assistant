import os
import re
import sqlite3
import webbrowser
import pyjokes # joke function
from playsound import playsound
import eel

from engine.command import speak 
from engine.config import ASSISTANT_NAME


# intro play assistant function
import pywhatkit as kit

from engine.helper import extract_yt_term, remove_words

conn = sqlite3.connect("clara.db")
cursor = conn.cursor()


@eel.expose #somehow not working with live server
def playAssistantSound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)
    
def openCommand(query): # opening apps and website 
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open","")
    query.lower()
    
    app_name = query.strip()
    
    if app_name != "":

        try:
            cursor.execute(
                'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening "+query)
                os.startfile(results[0][0])

            elif len(results) == 0: 
                cursor.execute(
                'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()
                
                if len(results) != 0:
                    speak("Opening "+query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening "+query)
                    try:
                        os.system('start '+query)
                    except:
                        speak("not found")
        except:
            speak("some thing went wrong")

        
# def PlayYoutube(query): # function to play youtube on chrome
#     search_term = extract_yt_term(query)
#     speak("Playing "+search_term+" on YouTube")
#     kit.playonyt(search_term)
    
# def extract_yt_term(command):
#     pattern = r'play\s+(.*?)\s+on\s+youtube'  
#     match = re.search(pattern, command, re.IGNORECASE)
#     return match.group(1) if match else None

def PlayYoutube(query): # to play videos on youtube
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+" on YouTube")
    kit.playonyt(search_term)
    
def joke(query = ''): # humor of clara
    pyjokes.get_joke('en','neutral', max_tokens= 50) 
    




