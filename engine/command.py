import pyttsx3 
import speech_recognition as sr
import eel
import pyjokes
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
        
    if "tell me a joke" in query: # joke
                speak('Ok, let me think of something funny...')
                try:
                    jokeresult = pyjokes.get_joke()
                    print(jokeresult)
                    eel.DisplayMessage(jokeresult) 
                    speak(jokeresult)
                    print(*"a"[1:5],sep=',')
                except:
                     speak('im not in the mood to joke sir')
        
    if "hello clara" in query: # hello clara
        print("Well, Hello there, How can I assist you today")
        eel.DisplayMessage("Well, Hello there! How can I assist you today?") 
        speak("Well, Hello there, How can I assist you today")
        
    if "how are you" in query: # how are u?
        print("I'm online and functioning as expected, prepared to assist you with any inquiries or tasks you have. How can I help you?")
        eel.DisplayMessage("I'm online and functioning as expected, prepared to assist you with any inquiries or tasks you have. How can I help you?") 
        speak("I'm online and functioning as expected, prepared to assist you with any inquiries or tasks you have, How can I help you?")
        
    if "who created you" in query: # who created you?
        print("I was created by the brilliant aspiring computer scientist, steven gabriel madali, a second year student in cavite state university carmona campus, taking a bachelors degree in information technology.")
        eel.DisplayMessage("I was created by the brilliant aspiring computer scientist, Steven Gabriel Madali. A second year student in Cavite State University carmona campus. Taking a bachelors degree in information technology.") 
        speak("I was created by the brilliant aspiring computer scientist, steven gabriel madali, a second year student in cavite state university carmona campus, taking a bachelors degree in information technology.")
    
    if "tell me about you" in query: # tell me about you
        print("Hello, I'm Clara, short for Cybernetic Language Artificial Intelligence Response Assistant, I'm your personal Web-based A.I Assistant.")
        eel.DisplayMessage("Hello I'm Clara, short for Cybernetic Language Artificial Intelligence Response Assistant. I'm your personal Web-based A.I Assistant.") 
        speak("Hello, I'm Clara, short for Cybernetic Language Artificial Intelligence Response Assistant, I'm your personal Web-based A.I Assistant.")
        
    eel.ShowHood() # exit the prompt 
    
