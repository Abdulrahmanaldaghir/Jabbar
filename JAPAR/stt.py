import speech_recognition as sr

def speech_to_text(duration, mic_index):
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Capture audio from the specified microphone for the specified duration
    with sr.Microphone(device_index=mic_index) as source:
        print(f"Say something for {duration} seconds:")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        try:
            audio = recognizer.listen(source, timeout=duration)
            # Use Google Web Speech API to convert speech to text
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Error connecting to Google Web Speech API: {e}")
        except sr.WaitTimeoutError:
            print(f"Timeout: No speech detected during {duration} seconds.")

if __name__ == "__main__":
    # Set the duration for which you want to capture audio (in seconds)
    capture_duration = 5

    # Set the index of the microphone you want to use
    selected_microphone_index = 2

    speech_to_text(capture_duration, selected_microphone_index)
