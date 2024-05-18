import requests
import json
import webbrowser
import random
import datetime
from engine.command import speak 


def Apod(query):
    # NASA API Key
    api_key = "Pa41EKygcE2L3n3DImI43fXEc445gGyKqwYQO2k4"

    # Generate a random date
    start_date = datetime.date(1995, 6, 16)
    end_date = datetime.date.today()
    random_date = start_date + (end_date - start_date) * random.random()
    random_date = random_date.strftime("%Y-%m-%d")

    # NASA APOD API endpoint
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={random_date}"

    # Send a GET request to the NASA APOD API
    response = requests.get(url)

    # Convert the response to JSON
    data = json.loads(response.text)

    # Get the image URL and explanation
    image_url = data["url"]
    explanation = data["explanation"]

    # Print the explanation
    print(f"Date: {random_date}")
    speak(f"The image was taken on the Date: {random_date}")
    print(f"Explanation: {explanation}")
    webbrowser.open(image_url)
    speak(explanation)

    # Open the image in the web browser
   
