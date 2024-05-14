import json 
import turtle 
import urllib.request
import time 
import webbrowser
import geocoder
import random
from engine.command import speak 

def ISStrack(query):
    url = "http://api.open-notify.org/astros.json" #api for counting astronauts 
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    file = open("iss.txt", "w")
    # file.write("There are currently" + 
    #            str (result["number"]) + "astronatus on the ISS: \n\n")
    print("There are currently " + str (result["number"]) + " astronatus on the ISS: \n ")
    speak("There are currently " + str (result["number"]) + " astronauts on the International space station: ")

    people = result['people']

    for p in people:
        # file.write(p ['name'] + " - on board" + "\n")
        print(p ['name'] + " - on board" + "")
        speak(p ['name'] + " - on board" + "")
        
    print(" ")

    # printing long and lat
    g = geocoder.ip('me')
    # file.write("\n Your current lat / long is: " + str(g.latlng))
    print("Your current lat / long is: " + str(g.latlng))
    speak(p ['name'] + " - on board" + "")
    file.close()
    # webbrowser.open("iss.txt")

    screen = turtle.Screen()
    screen.setup(1280, 720)
    screen.setworldcoordinates(-180,-90,180,90)

    #load the world map image
    screen.bgpic("Map.gif")
    screen.register_shape("iss-icon.gif")
    iss = turtle.Turtle()
    iss.shape("iss-icon.gif")
    iss.setheading(45)
    iss.penup()
    print("I am now tracking the international space station real time so the device your using might get laggy")
    speak("I am now tracking the international space station real time, so the device your using might get laggy")
    # input('stop')

    while True:
        
        url  ="http://api.open-notify.org/iss-now.json"
        response = urllib.request.urlopen(url)
        result = json.loads(response.read())
        
        # extracting the iss
        location = result["iss_position"]
        lat = location['latitude']
        lon = location['longitude']
        
        # output 
        lat = float(lat)
        lon = float(lon)
        print("\nLatitude: " + str(lat))
        print("\nLongitude: " + str(lon))
        speak("Latitude: " + str(lat))
        speak("Longitude: " + str(lon))
        # update 
        iss.goto(lon,lat)
        
        # refresh each 5 secs
        time.sleep(5)

        