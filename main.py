import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

print("hello, i am Debjit's Alexa , how can i help you?")
talk('hello, I am Debjit\'s Alexa, how can i help you?')
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'open' in command:
        app = command.replace('open', '')
        talk('searching' + app)
        webbrowser.open('https://www.google.com/search?q=' + app)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'i love ' in command:
        talk('I love you too')     
    elif 'date' in command:
        talk( "sorry, i can't go, I have a headache")
    elif 'are you single' in command:
        talk('I am in a relationship with Debjit Purohit')
    elif 'tell me a joke' in command:
        jk = pyjokes.get_joke()
        print(jk)
        talk(jk)
    elif 'bye' in command:
       talk('good bye')
    elif 'hello' in command: 
        talk('hiii, how can i help you?')   
    elif 'who are you' in command:
        talk("I am a Debjit's Alexa")
    elif 'who made you' in command:
        talk('I was created by Debjit Purohit')  
    else:
        talk('Please say the command again.')


while True:
    run_alexa()
