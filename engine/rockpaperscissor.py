import eel
import pyttsx3 #text to speech
import speech_recognition as sr
import random

from pygame import mixer
mixer.init()

engine = pyttsx3.init()
voices = engine.getProperty('voices')  #engine part
engine.setProperty('voice', voices[1].id)

def speak(text, rate = 145):
    engine.setProperty('rate',rate)
    engine.say(text)
    engine.runAndWait()
    
def parseCommand():
    listener = sr.Recognizer()
    print(*"a"[1:5],sep=',')
    print('C.L.A.R.A is Listening...')
    eel.DisplayMessage("C.L.A.R.A is Listening...") 
    
    with sr.Microphone() as source:   # function to use microphone
         listener.pause_threshold = 2
         input_speech = listener.listen(source)
         
    try:
        print('Recognizing speech...')
        eel.DisplayMessage("Recognizing speech...") 
        query = listener.recognize_google(input_speech, language='en_gb')  #google api to understand
        print(f'You choose: {query} ')
        eel.DisplayMessage(f'You choose: {query} ') 
    except Exception as exception:
        print('Im sorry, I did not quite catch that, could you please repeat it?')
        speak('Im sorry, I did not quite catch that, could you please repeat it?')
        eel.DisplayMessage('Im sorry, I did not quite catch that, could you please repeat it?') 
        print(exception)
        return 'None'
    
    return query  

def game_play():
   
    print(*"a"[1:5],sep=',')
    print("* YOU HAVE CHALLENGED CLARA TO A GAME OF ROCK PAPER AND SCISSORS! *")
    eel.DisplayMessage("* YOU HAVE CHALLENGED CLARA TO A GAME OF ROCK PAPER AND SCISSORS! *") 
    mixer.music.load("www\\assets\\audio\\rps intro.mp3")
    mixer.music.play()
    print(*"a"[1:5],sep=',')
    i = 0 
    Challenger_score = 0
    Clara_score = 0
    
    while(i<=3):
        choose = ("rock","paper","scissor") #TUPLE
        clara_choose = random.choice(choose) #randomization of athena
        query = parseCommand().lower() #answer to convert into lower words
        if(query == "rock"): #answer of the user
            if (clara_choose == "rock"):
                print("Clara chooses: ROCK")
                eel.DisplayMessage("Clara chooses: ROCK") 
                speak("Rock")
                print(f"Score:- Me :- {Challenger_score} : Com :- {Clara_score}")
                eel.DisplayMessage(f"Score:- Me :- {Challenger_score} : Com :- {Clara_score}") 
            elif(clara_choose == "paper"):
                print("Clara chooses: PAPER")
                eel.DisplayMessage("Clara chooses: PAPER") 
                speak("Paper")
                Clara_score += 1 
                print(f"Score:- Me :- {Challenger_score} : Com :- {Clara_score}")
                eel.DisplayMessage(f"Score:- Me :- {Challenger_score} : Com :- {Clara_score}") 
                
            else:
                print("Clara chooses: SCISSOR")
                eel.DisplayMessage("Clara chooses: SCISSORS") 
                speak("Scissors")
                Challenger_score += 1 
                print(f"Score:- Me :- {Challenger_score} : Com :- {Clara_score}")
                eel.DisplayMessage(f"Score:- Me :- {Challenger_score} : Com :- {Clara_score}") 
                
        elif(query == "paper"): #answer of the user
            if (clara_choose == "rock"):
                print("Clara chooses: ROCK")
                eel.DisplayMessage("Clara chooses: ROCK") 
                speak("Rock")
                Challenger_score += 1
                print(f"Score:- Me :- {Challenger_score} : Com :- {Clara_score}")
                eel.DisplayMessage(f"Score:- Me :- {Challenger_score} : Com :- {Clara_score}") 
            elif(clara_choose == "paper"):
                print("Clara chooses: PAPER")
                eel.DisplayMessage("Clara chooses: PAPER") 
                speak("Paper")
                print(f"Score:- Me :- {Challenger_score} : Com :- {Clara_score}")
                eel.DisplayMessage(f"Score:- Me :- {Challenger_score} : Com :- {Clara_score}") 
                
            else:
                print("Clara chooses: SCISSOR")
                eel.DisplayMessage("Clara chooses: SCISSORS") 
                speak("Scissors")
                Clara_score += 1 
                print(f"Score:- Me :- {Challenger_score} : Com :- {Clara_score}")
                eel.DisplayMessage(f"Score:- Me :- {Challenger_score} : Com :- {Clara_score}") 
                
        elif (query == "scissors" or query == "scissor"): #answer of the user
            if (clara_choose == "rock"):
                print("Athena chooses: ROCK")
                eel.DisplayMessage("Clara chooses: ROCK") 
                speak("Rock")
                Clara_score += 1
                print(f"Score:- Me :- {Challenger_score} : Com :- {Clara_score}")
                eel.DisplayMessage(f"Score:- Me :- {Challenger_score} : Com :- {Clara_score}") 
            elif(clara_choose == "paper"):
                print("Athena chooses: PAPER")
                eel.DisplayMessage("Clara chooses: PAPER") 
                speak("Paper")
                Clara_score += 1 
                print(f"Score:- Me :- {Challenger_score} : Com :- {Clara_score}")
                eel.DisplayMessage(f"Score:- Me :- {Challenger_score} : Com :- {Clara_score}") 
                
            else:
                print("Clara chooses: SCISSORS")
                speak("Scissors")
                print(f"Score:- Me :- {Challenger_score} : Com :- {Clara_score}")
        i += 1 
        
       
    speak("that's fun sir, let's try again sometimes")
    print(f"FINAL SCORE :- ME :- {Challenger_score} : CLARA :- {Clara_score}")
           

           
        
   
              
                