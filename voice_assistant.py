import speech_recognition as sr
import pyttsx3
import datetime
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            com = recognizer.recognize_google(audio)
            print(f"You said: {com}")
            return com.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Could not request results; check your internet connection.")
            return ""

def respond(com):
    if 'time' in com:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        response = f"The current time is {current_time}"
        speak(response)
    elif 'hello' in com:
        speak("Hello! How can I assist you today?")
    elif 'exit' in com or 'quit' in com:
        speak("Goodbye!")
        return False
    else:
        speak("Sorry, I can't help with that.")
    return True

def main():
    """Main function to run the voice assistant."""
    speak("Hello! I am your voice assistant.")
    
    run = True
    while run:
        com = listen()
        if com:
            run = respond(com)

if __name__ == "__main__":
    main()
