from gtts import gTTS

#def speak(text):
#    speech= gTTS(text=text,lang="en")
#    speech.save("aiaduio.mb3")
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

import pyttsx3

def speak(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty("rate", 150)  # Speed of speech

    # Convert the text to speech
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()

# Example usage
speak("Hello, ok ok it is ok.")
