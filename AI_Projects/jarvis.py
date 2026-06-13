import pyttsx3
import speech_recognition
import webbrowser
import os

recognizer = speech_recognition.Recognizer()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    with speech_recognition.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        audio = recognizer.listen(source)
        text = recognizer.recognize_google(audio)

        print(f"you said: {text}")

        return text

speak("Hello")
speak("I am Jarvis")    

while True:
    result = listen()
    result = result.lower()

    if result == "exit":
        break

    elif ("open chrome") in result:
        speak("Opening Chrome, Master!")
        webbrowser.open("https://www.google.com/")

    elif ("open youtube") in result:
        speak("Opening Youtube, Master!")
        webbrowser.open("https://www.youtube.com/")

    elif ("open instagram") in result:
        speak("Opening Instagram, Master!")
        webbrowser.open("https://www.instagram.com/")
    
    elif ("open fifa") in result:
        speak("Opening Matches for FiFa World Cup, Master!")
        webbrowser.open("https://www.google.com/search?sca_esv=96b74448a0106665&hl=en&sxsrf=ANbL-n4Jbc2MLyd46wfhVzucqFiQgAzYdg:1781366910792&q=FIFA+World+Cup+2026+today&spell=1&sa=X&ved=2ahUKEwivtLrvzISVAxXnCTQIHVbZBQ4QBSgAegQIEBAB&biw=768&bih=826&dpr=1.25")

    elif ("open vs code") in result:
        speak("Opening vs code, Master!")
        os.system("code")

    elif ("open steam") in result:
        speak("Opening Steam, Master!")
        os.startfile("C:/Program Files (x86)/Steam/steam.exe")

    elif ("open claude") in result:
        speak("Opening Claude, Master!")
        os.startfile("C:/Program Files/WindowsApps/Claude_1.12603.1.0_x64__pzs8sxrjxfjjc/app/claude.exe")

    else:
        print("I don't know this yet, However I might learn it in Future.")
        speak("I don't know this yet, However I might learn it in Future.")