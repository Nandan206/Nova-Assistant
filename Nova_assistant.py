import sys
import openai
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import subprocess
import spotipy
import os
from dotenv import load_dotenv
load_dotenv()

from spotipy.oauth2 import SpotifyOAuth


load_dotenv()  # Load environment variables from .env file

openai_key = os.getenv("OPENAI_API_KEY")
client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")



def chat_with_gpt(prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()




if __name__ == "__main__":
    while True:
        user_input = input("you: ")
        if user_input.lower() in ["q", "quit", "exit", "bye"]:
            response = chat_with_gpt(user_input)
            print("chatbot: ", response)
            break



sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope="user-read-playback-state,user-modify-playback-state,user-read-currently-playing"
))



Listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def open_software(software_name):
    if 'chrome' in software_name:
        talk('Opening Chrome...')
        program = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([program])

    elif 'microsoft edge' in software_name:
        talk('Opening Microsoft Edge...')
        program = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        subprocess.Popen([program])

    elif 'play' in software_name:
        b='Opening Youtube'
        engine.say(b)
        engine.runAndWait()
        pywhatkit.playonyt(software_name)

    elif 'spotify' in software_name:
        talk('Opening Spotify...')
        program = r"C:\Users\91915\AppData\Local\Microsoft\WindowsApps\Spotify.exe"
        subprocess.Popen([program])

    elif 'notepad' in software_name:
        talk('Opening Notepad...')
        subprocess.Popen(['notepad.exe'])

    elif 'calculator' in software_name:
        talk('Opening Calculator...')
        subprocess.Popen(['calc.exe'])
    else:
        talk(f"I couldn't find the software {software_name}")

def close_software(software_name):
    if 'chrome' in software_name:
        talk('Closing Chrome...')
        os.system("taskkill /f /im chrome.exe")

    elif 'microsoft edge' in software_name:
        talk('Closing Microsoft Edge...')
        os.system("taskkill /f /im msedge.exe")

    elif 'notepad' in software_name:
        talk('Closing Notepad...')
        os.system("taskkill /f /im notepad.exe")
    elif 'calculator' in software_name:
        talk('Closing Calculator...')
        os.system("taskkill /f /im calculator.exe")

    elif 'spotify' in software_name:
        talk('Closing Spotify...')
        os.system("taskkill /f /im spotify.exe")

    else:
        talk(f"I couldn't find any open software named {software_name}")

def listen_for_wake_word():
    with sr.Microphone() as source:
        print('Listening for wake word...')
        while True:
            Listener.adjust_for_ambient_noise(source, duration=0.5)
            recorded_audio = Listener.listen(source)
            try:
                text = Listener.recognize_google(recorded_audio, language='en_US')
                text = text.lower()
                if 'nova' in text:
                    print('Wake word detected!')
                    talk('Hi Sir, How can I help you?')
                    run_Nova()
                    return True
            except Exception as ex:
                print("Could not understand audio, please try again.")





def play_on_spotify(song_name):
    results = sp.search(q=song_name, type='track', limit=1)
    if results['tracks']['items']:
        uri = results['tracks']['items'][0]['uri']
        sp.start_playback(uris=[uri])
        talk(f"Playing {song_name} on Spotify")
    else:
        talk("Sorry, I couldn't find the song on Spotify.")


def take_command():
    try:
        with sr.Microphone() as source:
         print("Hey Nandy, What can I do for you?")
         Voice = Listener.listen(source)
         command = Listener.recognize_google(Voice)
         command = command.lower()
        if 'nova' in command:
            command = command.replace('nova', '')
            print(command)
            return command

    except:
       return ""

def run_Nova():
    while True:
        command = take_command()
        if command:
            print(command)

            if 'play' in command:
                song = command.replace('play', '')
                talk('playing song ' + song)
                pywhatkit.playonyt(song)

            elif 'open' in command or 'launch' in command:
                software_name = command.replace('open', '').replace('launch', '').strip()
                open_software(software_name)

            elif 'close' in command or 'shutdown' in command:
                software_name = command.replace('close', '').replace('shutdown', '').strip()
                close_software(software_name)


            elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                talk('Current time is ' + time)
                print('Time is: ' + time)

            elif any(keyword in command for keyword in ['search', 'look up', 'find', 'who is', 'information', 'what is']):
                talk("Searching the web...")
                search = command.replace('search', '')
                info = wikipedia.summary(search, sentences=2)
                print(info)
                talk(info)

            elif any(trigger in command for trigger in ['i lost', 'i failed', 'i am useless', 'i feel useless']):
                talk("Why do we fall, sir? So we can learn to pick ourselves up")

            elif 'you still believe in me' in command:
                talk("Always sir, You will win")


            elif any(phrase in command for phrase in ['joke']):
                joke = pyjokes.get_joke()
                talk(joke)

            elif 'you can take rest' in command or 'stop now' in command or 'exit nova' in command or 'shutdown systems' in command:
                talk("Thank you, sir. Going to rest.")
                sys.exit()

            elif 'play' in command and 'on spotify' in command:
                song = command.replace('play', '').replace('on spotify', '').strip()
                play_on_spotify(song)

            elif 'what is your name' in command:
                talk('My name is Nova Your Artificial Intelligence')

            elif 'exit' in command or 'stop' in command or 'bye' in command:
                talk("Goodbye sir. Have a nice day!")
                break


            else:
                talk('Please repeat the command')
                print('Please repeat the command')



def main():
    while True:
        if listen_for_wake_word():
            run_Nova()

if __name__ == "__main__":
    main()
