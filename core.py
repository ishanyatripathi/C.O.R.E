from dotenv import load_dotenv
load_dotenv()
import os
import sys
import time
import threading
import requests
import pyttsx3
import speech_recognition as sr
import webbrowser
import pyautogui
import keyboard
import http.server
import socketserver
import socket

# ========== Voice Functions ==========
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 200)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
    return ""

# ========== Groq API Integration ==========
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

def ask_groq_text(prompt):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": "You are a helpful, witty assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(GROQ_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {e}"

# ========== File Transfer ==========
def send_file():
    def server_thread():
        PORT = 8000
        FILE_PATH = r"C:\Users\smrit\AppData\Local\Programs\Python\Python312\authorized_user.jpg"
        DIRECTORY = os.path.dirname(FILE_PATH)

        if not os.path.exists(FILE_PATH):
            print("File not found!")
            speak("File not found.")
            return

        os.chdir(DIRECTORY)

        def get_local_ip():
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(("8.8.8.8", 80))
                ip = s.getsockname()[0]
                s.close()
                return ip
            except:
                return "127.0.0.1"

        local_ip = get_local_ip()
        handler = http.server.SimpleHTTPRequestHandler
        with socketserver.TCPServer(("", PORT), handler) as httpd:
            url = f"http://{local_ip}:{PORT}/{os.path.basename(FILE_PATH)}"
            print(f"Serving at: {url}")
            speak(f"File is ready to download at {url}")
            httpd.serve_forever()

    threading.Thread(target=server_thread, daemon=True).start()

# ========== Main Assistant Loop ==========
def assistant():
    speak("System is Online. Let's begin")

    while True:
        command = listen()
        if not command:
            continue

        print(f"Command: {command}")

        if "increase volume" in command:
            pyautogui.press("volumeup")
            speak("Increasing volume.")

        elif "decrease volume" in command:
            pyautogui.press("volumedown")
            speak("Decreasing volume.")

        elif "mute" in command:
            pyautogui.press("volumemute")
            speak("Muting audio.")

        elif "increase brightness" in command:
            try:
                keyboard.press_and_release('brightness_up')
                speak("Increasing brightness.")
            except Exception:
                speak("Brightness control failed.")

        elif "decrease brightness" in command:
            try:
                keyboard.press_and_release('brightness_down')
                speak("Decreasing brightness.")
            except Exception:
                speak("Brightness control failed.")

        elif "open browser" in command:
            webbrowser.open("https://www.google.com")
            speak("Opening browser.")

        elif "ask ai" in command:
            speak("What do you want to ask?")
            user_prompt = listen()
            if user_prompt:
                speak("Processing...")
                response = ask_groq_text(user_prompt)
                speak(response)

        elif "transfer file" in command:
            send_file()
            speak("Transferring file...")

        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            break

        else:
            response = ask_groq_text(command)
            speak(response[:250])  # Trim long answers

# ========== Start Assistant Thread ==========
if __name__ == "__main__":
    threading.Thread(target=assistant).start()
