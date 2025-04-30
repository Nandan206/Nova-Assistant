import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="078c0536f87a4cee97f7b51f1863a0c6",
    client_secret="b96c05b3957b4f5f9f61f1de76857648",
    redirect_uri="http://127.0.0.1:8888/callback",
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

            elif 'joke' in command or 'boost me up' in command or 'cheer me up' in command:
                joke = pyjokes.get_joke()
                talk(joke)
                print(joke)

            elif 'you can take rest' in command or 'stop now' in command or 'exit nova' in command or 'shut down systems' in command:
                talk("Thank you, sir. Going to rest.")
                break

            elif 'play' in command and 'on spotify' in command:
                song = command.replace('play', '').replace('on spotify', '').strip()
                play_on_spotify(song)


            else:
                talk('Please repeat the command')
                print('Please repeat the command')



run_Nova()