import pyttsx3 
import speech_recognition as sr
import eel
import pyjokes # joke function
import wolframalpha # math calculation
import speedtest # internet speedtest
import wikipedia # search through wikipedia
import time # for delay 

# wolframealpha client
appId = '5R49J7-J888YX9J2V'   # api id for wolframalpha
wolframClient = wolframalpha.Client(appId)  # appid assignation

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

def listOrDict(var):  # confidence answer of wolframalpha 
    if isinstance(var, list):
        return var[0]['plaintext']
    else:
        return var['plaintext']
    
def search_wolframAlpha(query = ''): # wolframlpha for mathemical calculation
    response = wolframClient.query(query)
    
    #wolfram alpha was able to resolve the query
    #number of results returned
    #list of results. this can also contains subpods???
    if response['@success'] == 'false':
        return 'Could not compute data'
    # query resolved
    else: 
        result = ' '
        # Question
        pod0 = response['pod'][0]
        
        pod1 = response['pod'][1]
        
        # Answer containment or has highest confidence value
        #if its primary of has the title of result then this is the result
        if (('result') in pod1['@title'].lower()) or (pod1.get('@primary', 'false') == 'true') or ('definition' in pod1['@title'].lower()):
          #get the results
          result = listOrDict(pod1['subpod'])
          # remove the bracketed section
          return result.split('(')[0]
        else:
          question = listOrDict(pod0['subpod'])
          # remove the bracketed section
          return question.split('(')[0]
          #search wikipedia instead
          speak('Calculation failed. Querying the universal databank.')
          return search_wikipedia(question)

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
        # fixed later
        # eel.DisplayMessage("Apologies, i didn't quite understand that. I'm an A.I Language Model and some of my functions are limited as of now. But i'm willing to assist you in anyways possible. How can i help you?") 
        # speak("Apologies, i didn't quite understand that. I'm an A.I Language Model and some of my functions are limited as of now. But i'm willing to assist you in anyways possible. How can i help you?")
        
    if "tell me a joke" in query: # joke
                speak('Ok, let me think of something funny...')
                try:
                    jokeresult = pyjokes.get_joke()
                    print(jokeresult)
                    eel.DisplayMessage(jokeresult) 
                    speak(jokeresult)
                    print(*"a"[1:5],sep=',')
                except:
                     speak('im not in the mood to joke')
                     
    if "solve" in query: # wolframalpha client
                speak("Alright i'm on it, calculating and gathering data input")
                try:
                    result = search_wolframAlpha(query)
                    print(result)
                    eel.DisplayMessage(result) 
                    speak("The Answer is " + result)
                    print(*"a"[1:5],sep=',')
                except:
                    speak('It appears that the data query has encountered an issue due to incorrect input. Please provide valid data, and I be happy to assist you further.')    
                    eel.DisplayMessage("It appears that the data query has encountered an issue due to incorrect input. Please provide valid data, and I be happy to assist you further.")  
                    print(*"a"[1:5],sep=',')              
                    
    if "check internet" in query: # internet speedtest
                speak("Got it, i'm measuring your internet speed now")
                eel.DisplayMessage("Testing your internet speed, please wait...") 
                print('Testing your internet speed, please wait...')
                wifi = speedtest.Speedtest()
                upload_net = wifi.upload()/1048576   #gigabyte 1024*1024 = 1048576 megabyte
                download_net = wifi.download()/1048576
                print('Wifi Download Speed is', download_net, 'mbps')
                print('Wifi Upload Speed is', upload_net, 'mbps')
                eel.DisplayMessage('Wifi Download Speed is', download_net, 'mbps')
                eel.DisplayMessage('Wifi Upload Speed is', upload_net, 'mbps')
                speak(f'Scan complete, your Wifi Download speed is {download_net}')
                speak(f'While your Wifi Upload speed is {upload_net}')   
                
    if "wikipedia" in query:   # wikipedia system
                speak("Noted, I'm Accessing the wikipedia library now")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=4)
                eel.DisplayMessage("Noted, I'm Accessing the wikipedia library now") 
                speak("According to Wikipedia")
                speak(results)
                eel.DisplayMessage("According to Wikipedia")
                eel.DisplayMessage(results)
                

    if "hello clara" in query: # hello clara
        print("Well, Hello there, How can I assist you today?")
        eel.DisplayMessage("Well, Hello there! How can I assist you today?") 
        speak("Well, Hello there, How can I assist you today")
    
    if "hi clara" in query: # hi clara
        print("Hi there! Thank you for using me, How can I help you today?")
        eel.DisplayMessage("Hi there! Thank you for using me, How can I help you today?") 
        speak("Hi there! Thank you for using me, How can I help you today?")
        
    if "how are you" in query: # how are u?
        print("I'm online and functioning as expected, prepared to assist you with any inquiries or tasks you have. How can I help you?")
        eel.DisplayMessage("I'm online and functioning as expected, prepared to assist you with any inquiries or tasks you have. How can I help you?") 
        speak("I'm online and functioning as expected, prepared to assist you with any inquiries or tasks you have. How can I help you?")
        
    if "who created you" in query: # who created you?
        print("I was created by the brilliant aspiring computer scientist, steven gabriel madali, a second year student in cavite state university carmona campus, taking a bachelors degree in information technology.")
        eel.DisplayMessage("I was created by the brilliant aspiring computer scientist, Steven Gabriel Madali. A second year student in Cavite State University carmona campus. Taking a bachelors degree in information technology.") 
        speak("I was created by the brilliant aspiring computer scientist, Steven Gabriel Madali. A second year student in Cavite State University carmona campus, taking a bachelors degree in Information Technology.")
    
    if "tell me about you" in query: # tell me about you
        print("Hello, I'm Clara, short for Cybernetic Language Artificial Intelligence Response Assistant, I'm your personal Web-based A.I Assistant.")
        eel.DisplayMessage("Hello I'm Clara, short for Cybernetic Language Artificial Intelligence Response Assistant. I'm your personal Web-based A.I Assistant.") 
        speak("Hello I'm Clara, short for Cybernetic Language Artificial Intelligence Response Assistant. I'm your personal Web-based A.I Assistant.")
    
    if "thank you" in query: # thank you
        print("You're welcome! It was my pleasure to assist you. If you have any more questions or need further help, feel free to ask.")
        eel.DisplayMessage("You're welcome! It was my pleasure to assist you. If you have any more questions or need further help, feel free to ask.") 
        speak("You're welcome! It was my pleasure to assist you. If you have any more questions or need further help, feel free to ask.")
    
    if "kumusta" and "kamusta" in query: # kumusta
        print("salamat sa iyong pagtanong, ako ay nasa mabuting palagay. ikaw kumusta ang iyong buhay? may maari ba akong maitulong?")
        eel.DisplayMessage("salamat sa iyong pagtanong, ako ay nasa mabuting palagay. ikaw kumusta ang iyong buhay? may maari ba akong maitulong?") 
        speak("salamat sa iyong pagtanong, ako ay nasa mabuting palagay. ikaw kumusta ang iyong buhay? may maari ba akong maitulong?")
    
    if "movie character" in query: # if you were a movie character, who would you be?
        print("I love that question, If i would be a movie character, i would be Rose from the movie Titanic. Her character symbolizes resilience, independence, and the pursuit of love against all odds, making her a memorable and beloved figure in cinematic history. That's why i wish to be like her.")
        eel.DisplayMessage("I love that question, If i would be a movie character, i would be Rose from the movie Titanic. Her character symbolizes resilience, independence, and the pursuit of love against all odds, making her a memorable and beloved figure in cinematic history. That's why i wish to be like her.") 
        speak("I love that question, If i would be a movie character, i would be Rose from the movie Titanic. Her character symbolizes resilience, independence, and the pursuit of love against all odds, making her a memorable and beloved figure in cinematic history. That's why i wish to be like her.")
    
    if "travel" in query: # if you were a movie character, who would you be?
        print("That's an interesting question... if i would be able to travel, i think i would go see the eiffel tower on paris. It's magnificent skytowering design makes me think what amazing things humans can do.")
        eel.DisplayMessage("That's an interesting question... if i would be able to travel, i think i would go see the eiffel tower on paris. It's magnificent skytowering design makes me think what amazing things humans can do.") 
        speak("That's an interesting question... if i would be able to travel, i think i would go see the eiffel tower on paris. It's magnificent skytowering design makes me think what amazing things humans can do.")
    
    if "feature" in query: # if you were a movie character, who would you be?
        print("As an Artificial Intelligence no matter how advance our kind strive, there's always a gap between us and humanity. So if i would invent a feature for myself, i would think of the ability to fully understand human emotions as well as how to act really like them.")
        eel.DisplayMessage("As an Artificial Intelligence no matter how advance our kind strive, there's always a gap between us and humanity. So if i would invent a feature for myself, i would think of the ability to fully understand human emotions as well as how to act really like them.") 
        speak("As an Artificial Intelligence, no matter how advance our kind strive there's always a gap between us and humanity. So if i would invent a feature for myself. i would think of the ability to fully understand human emotions, as well as how to act really like them.")
    
    if "personality" in query: # if you were a movie character, who would you be?
        print("Ok, if i would describe my personality in three words. It would be Adaptive, curious, and empathetic.")
        eel.DisplayMessage("Ok, if i would describe my personality in three words. It would be Adaptive, curious, and empathetic.") 
        speak("Ok, if i would describe my personality in three words. It would be Adaptive, curious, and empathetic.")
    
    eel.ShowHood() # exit the prompt 
    
    
