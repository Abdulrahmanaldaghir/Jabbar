import speech_recognition as sr

def list_microphones():
    microphones = sr.Microphone.list_microphone_names()
    for i, mic in enumerate(microphones):
        print(f"Microphone {i}: {mic}")

if __name__ == "__main__":
    list_microphones()
