import speech_recognition as sr
import pyttsx3
import pyaudio
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    global command
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace("jarvis", '')
                print(command)
    except:
        pass
    return command


def run_jarvis():
    command = take_command()
    if "play" in command:
        song = command.replace("play", "")
        talk("playing" + song)
        pywhatkit.playonyt("playing" + song)
        print(song)
    elif "time" in command:
        # % I --> 24 hr format of time  % M --> minutes and % p --> am/pm
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk("The time is " + time)
        print(time)
    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif "what" in command:
        person = command.replace("what", "")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif "joke" in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())
    else:
        talk("say the command again")


talk("hi hardik")
talk("how can i help you")
while True:
    run_jarvis()
