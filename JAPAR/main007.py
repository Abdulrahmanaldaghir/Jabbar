import datetime
import cv2
import numpy as np
import pyttsx3
import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import myop
import urllib
import requests
import pygame
import time
import threading
import openai  # Import OpenAI library
import myop
# Set your OpenAI API key
openai.api_key = 'your api'

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Image Display")

# Load images
face_image_path = "face.png"
eye_close_image_path = "eye_close.png"
laught_image_path = "laught.png"
face_image = pygame.image.load(face_image_path)
eye_close_image = pygame.image.load(eye_close_image_path)
laught_image = pygame.image.load(laught_image_path)

def show_face():
    screen.blit(face_image, (0, 0))
    pygame.display.flip()

def show_eye_close():
    screen.blit(eye_close_image, (0, 0))
    pygame.display.flip()

def repeat_face_and_eye_close():
    while True:
        show_face()
        time.sleep(5)
        show_eye_close()
        time.sleep(5)

def laught():
    screen.blit(laught_image, (0, 0))
    pygame.display.flip()

modes = ["friend", "teacher", "helper"]

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.say(text)
    engine.runAndWait()
def speak_msgs(messages):
    print("# Messages")
    for m in messages:
        speak(m.content[0].text.value)
        LAST_MSG_ID = m
    print() 
def listen_for_mode():
    speak("Choose a mode")
    selected_mode = listen(10, 1)
    if selected_mode.lower() in modes:
        speak("You selected " + selected_mode)
        return selected_mode
    else:
        speak("Sorry, can you say it again")
        return listen_for_mode()

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

def process_story_query(query):
    ims = myop.image_generation(query, 1)
    display_images(ims[0]["url"])
    ans = myop.ai(query)
    print(ans)

    for line in myop.nonblank_lines(ans.splitlines()):
        for p in line.split(". "):
            print(p)
            speak(p)

def friend(query):
    ans = myop.ai("Hi ChatGPT! You are this guy's friend, right? also your name is jabbar He said to you: "+query)
    #for line in myop.nonblank_lines(ans.splitlines()):
    #    for p in line.split(". "):
    print(ans)
    speak_msgs(ans)

def teacher(query):
    ans = myop.ai("Hello Teacher:  "+query)
    #for line in myop.nonblank_lines(ans.splitlines()):
    #   for p in line.split(". "):
    print(ans)
    speak_msgs(ans)

def helper(query):
    ans = myop.ai("Hi ChatGPT! we want your help : "+query)
    #for line in myop.nonblank_lines(ans.splitlines()):
    #    for p in line.split(". "):
    print(ans)
    speak_msgs(ans)



def process_query(selected_mode, query):
    if selected_mode.lower() == "friend":
        friend(query)
    elif selected_mode.lower() == "teacher":
        teacher(query)
    elif selected_mode.lower() == "helper":
        helper(query)
    else:
        process_general_query(query)

def process_general_query(query):
    # Call OpenAI completion API
    response = openai.Completion.create(
        engine="text-davinci-002",  # Replace with a valid model name
        prompt=query,
        max_tokens=150
    )

    completed_text = response['choices'][0]['text']
    speak(completed_text)

def main():
    wish_me()
    speak("HELLO")
    selected_mode = listen_for_mode()
    speak("I am jabbar, your " + selected_mode)
    speak("start talking!")

    while True:
        user_query = listen(10, 2)

        if user_query == "NULL" or user_query == '':
            continue

        print(user_query)
        speak("Thinking...")
        process_query(selected_mode, user_query)

if __name__ == "__main__":
    main()
