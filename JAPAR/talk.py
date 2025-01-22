import datetime
import cv2
import numpy as np
import FileHandling
import pyttsx3
import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import myopenai
import urllib
import requests
import pygame
import time
import datetime
import cv2
import numpy as np
import FileHandling
import pyttsx3
import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import myopenai
import urllib
import requests
import pygame
import time
import threading  


telling_joke = False
running_mouth = True
running_mouth = True
running_face_and_eye = True

# Add a lock to synchronize access to the telling_joke variable
lock = threading.Lock()

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((750, 1500))
pygame.display.set_caption("Image Display")

# Load images
one_m_image_path = "1m.png"
two_m_image_path = "2m.png"

one_image = pygame.image.load(one_m_image_path )
two_image = pygame.image.load(two_m_image_path)

def mone():
    screen.blit(one_image, (0, 0))
    pygame.display.flip()

def mtwo():
    screen.blit(two_image, (0, 0))
    pygame.display.flip()

def mouth():
    while running_mouth:
        mone()
        time.sleep(1)
        mtwo()
        time.sleep(1)

face_image_path = "face.png"
eye_close_image_path = "eye_close.png"
luaght_image_path = "laught.png"
face_image = pygame.image.load(face_image_path)
eye_close_image = pygame.image.load(eye_close_image_path)
luaght_image = pygame.image.load(luaght_image_path)
def show_face():
    screen.blit(face_image, (0, 0))
    pygame.display.flip()

def show_eye_close():
    screen.blit(eye_close_image, (0, 0))
    pygame.display.flip()

def laught():
    screen.blit(luaght_image, (0, 0))
    pygame.display.flip()
    
def repeat_face_and_eye_close():
    global running_face_and_eye
    while True:

        with lock:
            if not telling_joke:
                show_face()
                time.sleep(5)
                show_eye_close()
                time.sleep(5)
            else:
                # If telling a joke, call laught() instead
                laught()
                time.sleep(5)

        # Run the mouth() function concurrently





    
modes = ["weather", "question", "images", "error", "story", "jokes"]
imagine_keywords = ["Imagine", "imagine", "picture", "visualize", "draw"]
stories_keywords = ["tell me a story", "story", "stories"]
jokes_keywords = ["joke", "tell me a joke", "jokes"]


def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.say(text)
    engine.runAndWait()

def get_weather(api_key, latitude, longitude):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'lat': latitude,
        'lon': longitude,
        'appid': api_key,
        'units': 'metric'  # You can change this to 'imperial' for Fahrenheit
    }
    wnow = f"Your city {location} current weather is {main_weather}, the temperature is {temperature} Celsius, the humidity is {humidity}%."

    response = requests.get(base_url, params=params)
    location = weather_data['name']
    main_weather = weather_data['weather'][0]['description']
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    print(f"Location: {location}")
    print(f"Weather: {main_weather}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    if response.status_code == 200:
        weather_data = response.json()
        location = weather_data['name']
        main_weather = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']

        print(f"Location: {location}")
        print(f"Weather: {main_weather}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print(f"Failed to get weather data. Status code: {response.status_code}")

# Replace 'YOUR_API_KEY' with your OpenWeatherMap API key
api_key = '1f43de1fa821c08b230c106118aafe82'
latitude = 30.504963
longitude = 47.838486
def listen(duration, mic_index):
    recognizer = sr.Recognizer()
    with sr.Microphone(device_index=mic_index) as source:
        print(f"Say something for {duration} seconds:")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=duration)
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Error connecting to Google Web Speech API: {e}")
        except sr.WaitTimeoutError:
            print(f"Timeout: No speech detected during {duration} seconds.")
    return "NULL"


def display_images(urlstring):
    with urllib.request.urlopen(urlstring) as url:
        s = url.read()
    nparr = np.frombuffer(s, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imshow("Image", img)
    cv2.moveWindow("Image", 0, 0)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def wish_me():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning")
    elif hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")


#def get_weather():
#    wd = WeatherData()
#    wd.getweather(30.504963, 47.838486)
#    wd.getweather(30.504963, 47.838486)
#    w = wd.weather()
#    wq = f"My city current weather is {wd.weather()}, the temperature is {wd.temp('C')} Celsius, the humidity is {wd.humidity()}%; what do you think?"
#    wnow = f"Your city {wd.city()} current weather is {wd.weather()}, the temperature is {wd.temp('C')} Celsius, the humidity is {wd.humidity()}%."
 #   speak(wnow)
 #   openai.question = wq
#    ans = openai.openai_completion(wq)
#    for line in openai.nonblank_lines(ans.splitlines()):
#        for p in line.split(". "):
 #           print(p)
  #          speak(p)


def process_story_query(query):
    ims = myopenai.image_generation(query, 1)
    display_images(ims[0]["url"])
    ans = myopenai.openai_completion(query)
    print(ans)

    for line in myopenai.nonblank_lines(ans.splitlines()):
        for p in line.split(". "):
            print(p)
            speak(p)


def process_imagine_query(query):
    print("getting Images..", query)
    images_list = myopenai.image_generation(query, 5)
    print(images_list)

    speak("You can now view my art, wait for the image to be displayed in a separate window")
    for item in images_list:
        display_images(item["url"])
        speak("press any key to view the next image")


def process_joke_query(query):
    global telling_joke
    telling_joke = True

    # Start a new thread for the laught() function
    laught_thread = threading.Thread(target=laught)
    laught_thread.start()

    ans = myopenai.openai_completion(query)
    print(ans)

    for line in myopenai.nonblank_lines(ans.splitlines()):
        for p in line.split(". "):
            print(p)
            speak(p)

    telling_joke = False






def process_general_query(query):
    print("getting answers..", query)
    ans = myopenai.openai_completion(query)

    for line in myopenai.nonblank_lines(ans.splitlines()):
        for p in line.split(". "):
            print(p)
            speak(p)


def main():
    wish_me()
    speak("Welcome to the science camp WITH TOBI!")


    # Start the face and eye animation in a separate thread
    face_thread = threading.Thread(target=repeat_face_and_eye_close)
    face_thread.start()

    while True:
        speak("HOW can I help you today ?")
        speak("Welcome to the science camp WITH TOBI!")
        speak("I am Tobi, your AI Assistant!")
        speak("Science Camp is the place for all the makers and its where the robots are made in basrah Science Camp was founded in 2013 in Basra")
        #time.sleep(10)
        #user_query = listen(10, 2)

        #if user_query == "science camp" or user_query == 'talk about the science camp':
        #    speak("Science Camp is the place for all the makers and its where the robots are made in basrah Science Camp was founded in 2013 in Basra")

 #       print(user_qu

if __name__ == "__main__":
    main()