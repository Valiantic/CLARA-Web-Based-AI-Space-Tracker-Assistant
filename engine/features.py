import os
import re
import sqlite3
import struct
import time
import webbrowser
import pyaudio
import pyjokes # joke function
from playsound import playsound
import eel

from engine.command import speak 
from engine.config import ASSISTANT_NAME


# intro play assistant function
import pywhatkit as kit
import pvporcupine

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
    

# def hotword():  # NOT APPLICABLE DUE TO PRE TRAINED WORDS
#     porcupine=None
#     paud=None
#     audio_stream=None
#     try:
       
#         # pre trained keywords    
#         porcupine=pvporcupine.create(keywords=["clara","alexa"]) 
#         paud=pyaudio.PyAudio()
#         audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
#         # loop for streaming
#         while True:
#             keyword=audio_stream.read(porcupine.frame_length)
#             keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

#             # processing keyword comes from mic 
#             keyword_index=porcupine.process(keyword)

#             # checking first keyword detetcted for not
#             if keyword_index>=0:
#                 print("hotword detected")

#                 # pressing shorcut key win+j
#                 import pyautogui as autogui
#                 autogui.keyDown("win")
#                 autogui.press("j")
#                 time.sleep(2)
#                 autogui.keyUp("win")
                
#     except:
#         if porcupine is not None:
#             porcupine.delete()
#         if audio_stream is not None:
#             audio_stream.close()
#         if paud is not None:
#             paud.terminate()



    




