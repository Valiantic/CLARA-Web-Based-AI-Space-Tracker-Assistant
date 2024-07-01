import requests
import random
import webbrowser
from engine.command import speak 

api_key = 'yourkey'
api_url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'

def get_random_photo():
            params = {
                'api_key': api_key,
                'sol': random.randint(0, 1000),  # choose a random Martian sol between 0 and 1000
            }
            response = requests.get(api_url, params=params)
            response.raise_for_status()  # ensure we got a successful response
            photos = response.json()['photos']

            if not photos:
                print("No photos found for the chosen Martian sol. Try again.")
                return None

            photo = random.choice(photos)  # choose a random photo
            return photo

def mainrover(query):
            photo = get_random_photo()
            if photo is not None:
                webbrowser.open(photo['img_src'])
                print(f"Displaying a random photo taken by the {photo['rover']['name']} rover on Martian sol {photo['sol']} using the {photo['camera']['full_name']} ({photo['camera']['name']}).")
                speak(f"Here's a random photo taken by the {photo['rover']['name']} rover on Martian sol {photo['sol']} using the {photo['camera']['full_name']} ({photo['camera']['name']}).")
        

# if __name__ == '__main__':
#             mainrover()
