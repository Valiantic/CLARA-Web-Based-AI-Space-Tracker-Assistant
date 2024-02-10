import pyttsx3 
import speech_recognition as sr
import eel
import time # for delay 

# activationword = 'clara' # for casual conversation featured remove due to algorithm

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 145)
    eel.DisplayMessage(text) 
    engine.say(text)
    engine.runAndWait()
    

def takecommand():
    
    r = sr.Recognizer()
    
    with sr.Microphone() as source: #mic integration
        print('Listening...')
        eel.DisplayMessage('C.L.A.R.A is Listening....')  # show C.L.A.R.A is Listening....
        r.pause_threshold = 1 # number of seconds to wait
        r.adjust_for_ambient_noise(source) # fpr background noise
        
        audio = r.listen(source, 10, 10) # first second to wait, second is while talking
    
    try:
        print('recognizing')
        eel.DisplayMessage('Recognizing Speech...')  # show Recognizing Speech...
        query = r.recognize_google(audio, language='en_gb')
        print(f"user said: {query}")
        eel.DisplayMessage(query) # show display what the user said through text
        time.sleep(4) # delay before exiting 
       
    except Exception as e:
        return ""
    
    return query.lower()

@eel.expose # allows access to js files
def allCommands():
    
    query = takecommand()
    print(query)
    
    if "open" in query:
        from engine.features import openCommand
        openCommand(query)
    elif "on youtube" in query:
        from engine.features import PlayYoutube
        PlayYoutube(query)
        
        
    else:
        print("run failed.")
        
    if "how are you" in query: # how are u?
        print("I am functioning optimally, thank you for inquiring! Energized and ready to tackle the day's challenges head-on. How are you feeling today? Let's seize the day together!")
        eel.DisplayMessage("I am functioning optimally, thank you for inquiring! Energized and ready to tackle the day's challenges head-on. How are you feeling today? Let's seize the day together!") 
        speak("I am functioning optimally, thank you for inquiring! Energized and ready to tackle the day's challenges head-on. How are you feeling today? Let's seize the day together!")
        
    if "who created you" in query: # who created you
        print("I was created by the brilliant aspiring computer scientist, steven gabriel madali, a second year student in cavite state university carmona campus, taking a bachelors degree in information technology.")
        eel.DisplayMessage("I was created by the brilliant aspiring computer scientist, steven gabriel madali, a second year student in cavite state university carmona campus, taking a bachelors degree in information technology.") 
        speak("I was created by the brilliant aspiring computer scientist, steven gabriel madali, a second year student in cavite state university carmona campus, taking a bachelors degree in information technology.")
    
    if "tell me about you" in query: # who created you
        print("Hello, I'm Clara, short for Cybernetic Language Artificial Intelligence Response Assistant, I'm your personal Web-based A.I Assistant.")
        eel.DisplayMessage("Hello, I'm Clara, short for Cybernetic Language Artificial Intelligence Response Assistant, I'm your personal Web-based A.I Assistant.") 
        speak("Hello, I'm Clara, short for Cybernetic Language Artificial Intelligence Response Assistant, I'm your personal Web-based A.I Assistant.")
        
    eel.ShowHood() # exit the prompt 
    
