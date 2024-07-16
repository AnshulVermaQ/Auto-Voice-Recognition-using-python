import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine  = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
  if "open google" in c.lower():
    webbrowser.open("https://google.com")
  if "open facebook" in c.lower():
    webbrowser.open("https://facebook.com")
  if "open youtube" in c.lower():
    webbrowser.open("https://youtube.com")
  if "open linkedin" in c.lower():
    webbrowser.open("https://linkedin.com")
  

if __name__ == "__main__":
   speak("initializing Jarvis........")
   while True:
       
          r = sr.Recognizer()
   
       
          try:   
            with sr.Microphone() as source:
                 print("Listening.....")
                 audio = r.listen(source,timeout=2, phrase_time_limit=1)
            command =r.recognize_google(audio)
            processCommand(command)
            print(command)
          except Exception as e:
             print("Sphinx error; {0}".format(e))
        
