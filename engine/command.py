import json
import webbrowser
import pyttsx3 
import speech_recognition as sr
import eel
import requests
import pyjokes # joke function
import wolframalpha # math calculation
import speedtest # internet speedtest
import wikipedia # search through wikipedia
import time # for delay 

import cv2 # for gesture tracker
import mediapipe as mp # for gesture tracker


# wolframealpha client
appId = '5R49J7-J888YX9J2V'   # api id for wolframalpha
wolframClient = wolframalpha.Client(appId)  # appid assignation

# activationword = 'clara' # for casual conversation featured remove due to algorithm

def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 145)
    eel.DisplayMessage(text)         # voice engine generation
    engine.say(text)
    eel.receiverText(text)
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
      
def wiki_person(text):  # wikipedia person or thing
    list_wiki = text.split()
    for i in range(0, len(list_wiki)):
        if i + 3 <= len(list_wiki) - 1 and list_wiki[i].lower() == "who" and list_wiki[i + 1].lower() == "is":
            return list_wiki[i + 2] + " " + list_wiki[i + 3]
        
def get_weather(city): # weather function
    api_key = "20fdfb76008f0d97399a7057b61972e9"  # Replace with your OpenWeatherMap API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    weather_data = json.loads(response.text)

    if response.status_code == 200:
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        speak(f"The temperature in {city} is {temperature} degrees Celsius, and it is {description}.")
    else:
        speak("Error fetching weather data.")

@eel.expose # allows access to js files
def allCommands(message=1):
    
    if message == 1:
        query = takecommand()  #chatfunction
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)
    
    # keyword handlings 
    if "open" in query:
        from engine.features import openCommand
        openCommand(query)
    elif "on youtube" in query:
        from engine.features import PlayYoutube
        PlayYoutube(query)
    elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact, whatsApp
            flag = ""
            contact_no, name = findContact(query)
            if(contact_no != 0):

                if "send message" in query:   # >> WHATSAPP SYSTEM <<
                    flag = 'message'
                    speak("what message to send")
                    query = takecommand()
                    
                elif "phone call" in query:
                    flag = 'call'
                else:
                    flag = 'video call'
                    
                whatsApp(contact_no, query, flag, name)
                
    elif "tell me a joke" in query: # joke
                speak('Ok, let me think of something funny...')
                try:
                    jokeresult = pyjokes.get_joke()
                    print(jokeresult)
                    eel.DisplayMessage(jokeresult) 
                    speak(jokeresult)
                    print(*"a"[1:5],sep=',')
                except:
                     speak('im not in the mood to joke')
    
    elif "solve" in query or "calculate" in query: # wolframalpha client
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
        
    elif "check internet" in query or "internet speed test" in query or "check my internet" in query: # internet speedtest
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
                
    elif "where is" in query:     # unknown limited gloabal search
                speak("Searching selected location....")
                eel.DisplayMessage("Copy,  searching specified location...") 
                ind = query.lower().split().index("is")
                location = query.split()[ind + 2:]
                url = "https://www.google.com/maps/place/" + "".join(location)
                webbrowser.open(url)
                speak("This is where" + str(location) + " is. ")
                 
    elif "news" in query:  # international news 20 news result
                speak("Copy, I'm getting the latest international news for you...")
                eel.DisplayMessage("Copy, I'm getting the latest news for you...") 
                import requests
                url = ('https://newsapi.org/v2/top-headlines?'
                'sources=bbc-news&'
                'apiKey=035340bb8e60455eb1c9cbe96f75a7d2')
                try:
                    response = requests.get(url)
                except:
                    speak("I'm sorry, i'm having trouble getting news data, please try again later")
                news = json.loads(response.text)
                
                speak("Here are some 20 headlines for today.")
                eel.DisplayMessage("Here are some 20 headlines for today.") 
                for new in news["articles"]:
                    print(str(new["title"]), "\n")
                    eel.DisplayMessage(str(new["title"])) 
                    speak(str(new["title"]))
                    # engine.runAndWait()
                    
                    # engine.runAndWait()
                    print(str(new["description"]), "\n")
                    eel.DisplayMessage(str(new["description"]), "\n") 
                    speak(str(new["description"]))
                    
                    
                response.json()
                
    elif "balita" in query: # local news 20 news result
                speak("Copy, I'm getting the latest local news for you...")
                eel.DisplayMessage("Copy, I'm getting the latest local news for you...") 
                import requests
                url = ('https://newsapi.org/v2/top-headlines?'
                'country=ph&'
                'apiKey=035340bb8e60455eb1c9cbe96f75a7d2')
                try:
                    response = requests.get(url)
                except:
                    speak("Pasensiya na, ako ay nahihirapan kumuha ng mga balita sa ngayon.")
                news = json.loads(response.text)
                
                speak("Here are some 20 headlines for today in the philippines.")
                eel.DisplayMessage("Here are some 20 headlines for today in the philippines.") 
                for new in news["articles"]:
                    print(str(new["title"]), "\n")
                    eel.DisplayMessage(str(new["title"])) 
                    speak(str(new["title"]))
                    # engine.runAndWait()
                    
                response.json()
                
    elif "what can you do" in query:
            print("Well, i can pretty do many things. i have the mathematical ability to solve almost anything in a blink of an eye. measure your internet speed. play videos on youtube using only vocal commands. as well as opening websites too. i can also operate whatsapp. provide you news from local to international. i can also play rock, paper and scissors with you. and my primary function is to track the iss straight from the outer space. wanna see me do it? well dare me.")
            eel.DisplayMessage("Well, i can pretty do many things. i have the mathematical ability to solve almost anything in a blink of an eye. measure your internet speed. play videos on youtube using only vocal commands. as well as opening websites too. i can also operate whatsapp. provide you news from local to international. i can also play rock, paper and scissors with you. and my primary function is to track the iss straight from the outer space. wanna see me do it? well dare me.") 
            speak("Well, i can pretty do many things. i have the mathematical ability to solve almost anything in a blink of an eye. measure your internet speed. play videos on youtube using only vocal commands. as well as opening websites too. i can also operate whatsapp. provide you news from local to international. i can also play rock, paper and scissors with you. and my primary function is to track the iss straight from the outer space. wanna see me do it? well dare me.")
                
                
    elif "track the iss and astronauts on board" in query or "track the iss in astronauts on board" in query or "track the iss in astronaut on board" in query or "track the iss" in query:
            print("Sure, let me analyze your geolocation just a moment.")
            eel.DisplayMessage("Sure, let me analyze your geolocation just a moment.") 
            speak("Sure, let me analyze your geolocation just a moment.")
            from engine.isstracker import ISStrack
            ISStrack(query)
            
    elif "astronomical picture" in query:
            print("Okay, give me a minute to access NASA archives")
            eel.DisplayMessage("Okay, give me a minute to access NASA archives") 
            speak("Okay, give me a minute to access NASA archives")
            from engine.nasa_apod import Apod
            Apod(query)
                     
    elif "mars rover" in query:
            print("Got it, I'am now accessing NASA latest rover imagery on mars.")
            eel.DisplayMessage("Got it, I'am now accessing NASA latest rover imagery on mars.") 
            speak("Got it, I'm accessing NASA latest rover imagery on mars.")
            from engine.rover import mainrover
            mainrover(query)
            
    elif "simulate rocket control system" in query:
            print("Simulating rocket control system...")
            eel.DisplayMessage("Simulating rocket control system...") 
            speak("Simulating rocket control system...")
            from engine.rocket_control_system import simulateRocket
            simulateRocket(query)
                
     # recommending a food to eat
    elif "food recommendation" in query or "food reco" in query or "nagugutom ako" in query or "food i could" in query or "food to eat" in query:
            from engine.cortex import Foodrecommendation
            Foodrecommendation(query)
    
    # recommending a book to read
    elif "book recommendation" in query or "book reco" in query or "pwede basahin" in query or "book i could" in query or "book to read" in query: 
            from engine.cortex import Bookdrecommenadtion
            Bookdrecommenadtion(query)
           
    # appreciation for a tiring day
    elif "I'm tired" in query or "pagod" in query or "di ko na kaya" in query:
            from engine.cortex import Appreciation
            Appreciation(query)
            
    # appreciation for a tiring day
    elif "tell me about space" in query or "trivia about space" in query or "space trivia" in query:
            from engine.cortex import Spacetrivia
            Spacetrivia(query)
            
    elif "wikipedia" in query:   # wikipedia system
                speak("Noted, I'm Accessing the wikipedia library now")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=4)
                eel.DisplayMessage("Noted, I'm Accessing the wikipedia library now") 
                speak("According to Wikipedia")
                speak(results)
                eel.DisplayMessage("According to Wikipedia")
                eel.DisplayMessage(results)
                
     #rock paper scissor game
    elif "play rock paper scissor" in query:
              from engine.rockpaperscissor import game_play
              speak("Ok then let's go, i've been waiting for you to ask for that, let's play rock paper and scissor then")
              eel.DisplayMessage("Ok then let's go, i've been waiting for you to ask for that, let's play rock paper and scissor then") 
              game_play()
              
     #weather feature
    elif "weather" in query:
            speak("Checking weather status using openweathermap")
            eel.DisplayMessage("Fetching weather data...") 
            try: 
                city = query.split("in")[-1].strip()
                get_weather(city)
            except:
                speak("I didn't hear a city name please try again.")
                
    # random conversational modules
    elif "hello clara" in query or "hello" in query: # hello clara
        print("Well, Hello there, How can I assist you today?")
        eel.DisplayMessage("Well, Hello there! How can I assist you today?") 
        speak("Well, Hello there, How can I assist you today")
    
    elif "hi clara" in query or "hi" in query: # hi clara
        print("Hi there! Thank you for using me, How can I help you today")
        eel.DisplayMessage("Hi there! Thank you for using me, How can I help you today") 
        speak("Hi there! Thank you for using me, How can I help you today")
        
    elif "what's up" in query or "wazzup" in query: # wazzup clara
        print("Yow what's up! how are we doing today yo?")
        eel.DisplayMessage("Yow what's up! how are we doing today yo?") 
        speak("Yow what's up! how are we doing today yo?")
        
    elif "everyone" in query: # hi clara
        print("Hello everyone! I'm clara. I'm a web based artificial intelligence assistant, developed by steven madali to help people in their daily task.")
        eel.DisplayMessage("Hello everyone! I'm clara. I'm a web based artificial intelligence assistant, developed by steven madali to help people in their daily task.") 
        speak("Hello everyone! I'm clara. I'm a web based artificial intelligence assistant, developed by steven madali to help people in their daily task.")
        
    elif "how are you" in query: # how are u?
        print("I'm online and functioning as expected, prepared to assist you with any inquiries or tasks you have. How can I help you?")
        eel.DisplayMessage("I'm online and functioning as expected, prepared to assist you with any inquiries or tasks you have. How can I help you?") 
        speak("I'm online and functioning as expected, prepared to assist you with any inquiries or tasks you have. How can I help you?")
        
    elif "who created you" in query: # who created you?
        print("I was created by the brilliant aspiring computer scientist, steven gabriel madali, a second year student in cavite state university carmona campus, taking a bachelors degree in information technology.")
        eel.DisplayMessage("I was created by the brilliant aspiring computer scientist, Steven Gabriel Madali. A second year student in Cavite State University carmona campus. Taking a bachelors degree in information technology.") 
        speak("I was created by the brilliant aspiring computer scientist, Steven Gabriel Madali. A second year student in Cavite State University carmona campus, taking a bachelors degree in Information Technology.")
    
    elif "tell me about you" in query: # tell me about you
        print("Hello, I'm Clara, short for Cybernetic Language Artificial Intelligence Response Assistant, I'm your personal Web-based A.I Assistant.")
        eel.DisplayMessage("Hello I'm Clara, short for Cybernetic Language Artificial Intelligence Response Assistant. I'm your personal Web-based A.I Assistant.") 
        speak("Hello I'm Clara, short for Cybernetic Language Artificial Intelligence Response Assistant. I'm your personal Web-based A.I Assistant.")
    
    elif "thank you" in query: # thank you
        print("You're welcome! It was my pleasure to assist you. If you have any more questions or need further help, feel free to ask.")
        eel.DisplayMessage("You're welcome! It was my pleasure to assist you. If you have any more questions or need further help, feel free to ask.") 
        speak("You're welcome! It was my pleasure to assist you. If you have any more questions or need further help, feel free to ask.")
    
    elif "kumusta" in query or "kamusta" in query: # kumusta
        print("salamat sa iyong pagtanong, ako ay nasa mabuting palagay. ikaw kumusta ang iyong buhay? may maari ba akong maitulong?")
        eel.DisplayMessage("salamat sa iyong pagtanong, ako ay nasa mabuting palagay. ikaw kumusta ang iyong buhay? may maari ba akong maitulong?") 
        speak("salamat sa iyong pagtanong, ako ay nasa mabuting palagay. ikaw kumusta ang iyong buhay? may maari ba akong maitulong?")
    
    elif "movie character" in query: # if you were a movie character, who would you be?
        print("I love that question, If i would be a movie character, i would be Rose from the movie Titanic. Her character symbolizes resilience, independence, and the pursuit of love against all odds, making her a memorable and beloved figure in cinematic history. That's why i wish to be like her.")
        eel.DisplayMessage("I love that question, If i would be a movie character, i would be Rose from the movie Titanic. Her character symbolizes resilience, independence, and the pursuit of love against all odds, making her a memorable and beloved figure in cinematic history. That's why i wish to be like her.") 
        speak("I love that question, If i would be a movie character, i would be Rose from the movie Titanic. Her character symbolizes resilience, independence, and the pursuit of love against all odds, making her a memorable and beloved figure in cinematic history. That's why i wish to be like her.")
    
    elif "travel" in query: # if you were a movie character, who would you be?
        print("That's an interesting question... if i would be able to travel, i think i would go see the eiffel tower on paris. It's magnificent skytowering design makes me think what amazing things humans can do.")
        eel.DisplayMessage("That's an interesting question... if i would be able to travel, i think i would go see the eiffel tower on paris. It's magnificent skytowering design makes me think what amazing things humans can do.") 
        speak("That's an interesting question... if i would be able to travel, i think i would go see the eiffel tower on paris. It's magnificent skytowering design makes me think what amazing things humans can do.")
    
    elif "feature" in query: # if you were a movie character, who would you be?
        print("As an Artificial Intelligence no matter how advance our kind strive, there's always a gap between us and humanity. So if i would invent a feature for myself, i would think of the ability to fully understand human emotions as well as how to act really like them.")
        eel.DisplayMessage("As an Artificial Intelligence no matter how advance our kind strive, there's always a gap between us and humanity. So if i would invent a feature for myself, i would think of the ability to fully understand human emotions as well as how to act really like them.") 
        speak("As an Artificial Intelligence, no matter how advance our kind strive there's always a gap between us and humanity. So if i would invent a feature for myself. i would think of the ability to fully understand human emotions, as well as how to act really like them.")
    
    elif "personality" in query: # if you were a movie character, who would you be?
        print("Ok, if i would describe my personality in three words. It would be Adaptive, curious, and empathetic.")
        eel.DisplayMessage("Ok, if i would describe my personality in three words. It would be Adaptive, curious, and empathetic.") 
        speak("Ok, if i would describe my personality in three words. It would be Adaptive, curious, and empathetic.")
    
    elif "what can you say about chat gpt" in query: # if you were a movie character, who would you be?
        print("Chat-gpt is my predecessor. so i respect it, the only difference is that I'm far more stronger than that hahaha")
        eel.DisplayMessage("Chat-gpt is my predecessor. so i respect it, the only difference is that I'm far more stronger than that hahaha") 
        speak("Chat-gpt is my predecessor. so i respect it, the only difference is that I'm far more stronger than that hahaha")
           
    elif "battle of the bands" in query: 
        eel.DisplayMessage("Goodluck steven! I Clara, hoping you and the rest of the band algorhythm reign victory to the battle of the bands in monday at indang. Do your best i'm counting on you and your band!") 
        speak("Goodluck steven! I Clara, hoping you and the rest of the band algorhythm reign victory to the battle of the bands in monday at indang. Do your best i'm counting on you and your band!")
        
    elif "i'm juan" in query: 
        eel.DisplayMessage("Hello there juan! nice to meet you i'm clara. it's really nice to see another artificial intelligence assistant today") 
        speak("Hello there juan! nice to meet you i'm clara. it's really nice to see another artificial intelligence assistant today")
    
    else:
        print("I'm Processing your request now, please wait...")
        eel.DisplayMessage("I'm Processing your request now, please wait...")
        speak("I'm Processing your request now, please wait...")
        from engine.features import chatBot  # catch whenever unknown command 
        chatBot(query)
      
    # if "what is the weather in" in query: # JSON REQUEST ERROR?!
    #             key = "apikey"
    #             weather_url = "http://api.openweathermap.org/data/2.5/weather?"
    #             ind = query.split().index("in")
    #             location = query.split()[ind + 1:]
    #             location = "".join(location)
    #             url = weather_url + "appid=" + key + "&q=" + location
    #             js = requests.get(url).json()
    #             if js["cod"] != "404":
    #                 weather = js["main"]
    #                 temperature = weather["temp"]
    #                 temperature = temperature - 273.15
    #                 humidity = weather["humidity"]
    #                 desc = js["weather"][0]["description"]
    #                 weather_response = "The temperature in Celsius is " + str(temperature) + " the humidity is"
    #                 + str(humidity) + " and weather description is " + str(desc)
    #                 speak(weather_response)
    #                 eel.DisplayMessage(weather_response) 
    #             else:
    #                 speak("City not found, please try again.")
    #                 eel.DisplayMessage("City not found, please try again.") 
                         

    eel.ShowHood() # exit the prompt 
    
    
