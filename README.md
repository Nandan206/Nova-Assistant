# 🦾 Nova AI Assistant

Nova is your personal voice-activated AI assistant inspired by JARVIS (Iron Man) and Alfred (Batman). Built with Python, Nova listens, responds, and executes commands — including playing music, searching the web, managing software, and even integrating with Spotify, ChatGPT, and more.

## 🚀 Features

- 🎙️ Voice Recognition using SpeechRecognition
- 🔊 Text-to-Speech with pyttsx3
- 🔍 Wikipedia search & Web queries
- 📅 Time reporting & jokes
- 🎵 YouTube music playback via `pywhatkit`
- 🟢 Spotify music control using `Spotipy`
- 🧠 GPT-3.5 Chat Integration (Chat with Nova)
- 🖥️ Open/Close local applications like Chrome, Notepad, etc.
- 🛑 Wake word listening and graceful shutdown

## 🛠️ Tech Stack

| Category       | Tools / Libraries |
|----------------|------------------|
| Language       | Python 3.13       |
| Voice Input    | `SpeechRecognition`, `PyAudio` |
| Voice Output   | `pyttsx3`         |
| Music          | `pywhatkit`, `spotipy` |
| AI Integration | `OpenAI GPT-3.5` |
| Auth Handling  | `python-dotenv`, `.env` config |
| Application Control | `subprocess`, `os` |

## 🔒 Environment Variables (.env)

Create a `.env` file in your root directory:

```env
OPENAI_API_KEY=your_openai_api_key
SPOTIPY_CLIENT_ID=your_spotify_client_id
SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
SPOTIPY_REDIRECT_URI=http://127.0.0.1:8888/callback
