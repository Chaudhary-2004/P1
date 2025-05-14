import speech_recognition as sr
import pyttsx3 # os functionality does not work on Windows instead use pyttsx3
import webbrowser # for opening browser and searching
import openai
import os
import datetime


def say(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)     # Speed of speech
    engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Change voice
    engine.say(text)
    engine.runAndWait()
    
    
def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    #if we want a pause threshold that ki humara assistant kitna der tak chalna chahiye
    recognizer.pause_threshold = 0.5
    with mic as source:
        print("Please say something...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language='en-IN') #language='en-IN' for Indian accent you can also use hi-in for Hindi
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None



if __name__ == "__main__":
    print("Welcome to the Speech Recognition Program!")
    say("Welcome to the Speech Recognition Program!")
    say("Hello I am Shashwat's assistant")
    while(True):
        print("Listening...")
        text = recognize_speech_from_mic()
        sites=[["youtube","https://www.youtube.com/"], ["google","https://www.google.com/"], ["github","https://github.com/"]]
        for site in sites:
            if text is not None:
                if f"open {site[0]}" in text.lower():
                    print(f"Opening {site[0]}...")
                    say(f"Opening {site[0]}")
                    webbrowser.open(site[1])
                    say(f"{site[0]} opened Sir")
                    break
        if text is not None:
            if "open music" in text.lower():
                print("Opening music...")
                say("Opening music")
                musicpath=r"C:\Users\Shash\Downloads\Deewanapan-Hai.mp3"
                os.startfile(musicpath)
                say("Music opened Sir")
            
            if "time" in text.lower():
                now = datetime.datetime.now()
                current_time = now.strftime("%H:%M")
                print(f"Current time is {current_time}")
                say(f"Current time is {current_time}")
            
            if "Open notepad".lower() in text.lower():
                print("Opening notepad...")
                say("Opening notepad")
                os.startfile(r"C:\Windows\System32\notepad.exe")
                say("Notepad opened Sir")
            if "open calculator".lower() in text.lower():  
                print("Opening calculator...")
                say("Opening calculator")
                os.startfile(r"C:\Windows\System32\calc.exe")
                say("Calculator opened Sir")
                
            

        
    
        
                
            
        
        
