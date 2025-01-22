import pyttsx3
import speech_recognition as sr

modes = ["friend", "teacher", "helper"]

def speak(engine, text):
    engine.say(text)
    engine.runAndWait()

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

def listen_for_mode():
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    speak(engine, "Choose a mode")
    selected_mode = listen(10, 1)
    engine.stop()  # Close the engine after usage
    if selected_mode.lower() in modes :
        speak(engine, "You selected " + selected_mode)
    else:
        speak(engine, "Sorry, can you say it again")

while True:
    listen_for_mode()
