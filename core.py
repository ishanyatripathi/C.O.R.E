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
from PyQt5.QtCore import QTimer, Qt, pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtGui import QFont
import psutil
import cv2
import numpy as np
import mediapipe as mp
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
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
def gesture_mouse_control():
    global mouse_control_active
    mouse_control_active = True
    
    mpHands = mp.solutions.hands
    hands = mpHands.Hands(min_detection_confidence=0.7)
    mpDraw = mp.solutions.drawing_utils
    
    cap = cv2.VideoCapture(0)
    
    while mouse_control_active:
        success, frame = cap.read()
        if not success:
            break
        
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)
        
        lmDict = {}
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for id, lm in enumerate(hand_landmarks.landmark):
                    h, w, _ = frame.shape
                    lmDict[id] = (int(lm.x * w), int(lm.y * h))
                
                mpDraw.draw_landmarks(frame, hand_landmarks, mpHands.HAND_CONNECTIONS)
        
        if 8 in lmDict:
            x, y = lmDict[8]
            screen_x = np.interp(x, [0, frame.shape[1]], [0, pyautogui.size()[0]])
            screen_y = np.interp(y, [0, frame.shape[0]], [0, pyautogui.size()[1]])
            pyautogui.moveTo(screen_x, screen_y)
        
        if 4 in lmDict and 8 in lmDict:
            x1, y1 = lmDict[4]
            x2, y2 = lmDict[8]
            distance = np.hypot(x2 - x1, y2 - y1)
            if distance < 30:
                pyautogui.click()
        
        cv2.imshow("Gesture Mouse", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    mouse_control_active = False
def gesture_volume_control():
    global volume_control_active
    volume_control_active = True
    
    cap = cv2.VideoCapture(0)
    
    mpHands = mp.solutions.hands
    hands = mpHands.Hands(min_detection_confidence=0.7)
    mpDraw = mp.solutions.drawing_utils
    
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    
    volMin, volMax = volume.GetVolumeRange()[:2]
    
    while volume_control_active:
        success, img = cap.read()
        if not success:
            break
        
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)
        
        lmDict = {}
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for id, lm in enumerate(hand_landmarks.landmark):
                    h, w, _ = img.shape
                    lmDict[id] = (int(lm.x * w), int(lm.y * h))
                
                mpDraw.draw_landmarks(img, hand_landmarks, mpHands.HAND_CONNECTIONS)
        
        if 4 in lmDict and 8 in lmDict:
            x1, y1 = lmDict[4]
            x2, y2 = lmDict[8]
            
            length = hypot(x2 - x1, y2 - y1)
            vol = np.interp(length, [20, 200], [volMin, volMax])
            volume.SetMasterVolumeLevel(vol, None)
        
        cv2.imshow('Gesture Volume Control', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    volume_control_active = False

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
        elif "enable gesture mouse" in command:
            threading.Thread(target=gesture_mouse_control, daemon=True).start()
            speak("Gesture mouse control activated.")
            
        elif "enable gesture volume" in command:
            threading.Thread(target=gesture_volume_control, daemon=True).start()
            speak("Gesture volume control activated.")

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


class StatusSignal(QObject):
    update_status = pyqtSignal(str)

class COREUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("C.O.R.E. Interface")
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.showFullScreen()

        self.main_layout = QVBoxLayout()
        self.top_layout = QHBoxLayout()
        self.bottom_layout = QHBoxLayout()

        self.date_label = QLabel(time.strftime("%Y-%m-%d %H:%M:%S"), self)
        self.date_label.setAlignment(Qt.AlignLeft)
        self.date_label.setStyleSheet("color: #ADD8E6;")
        self.date_label.setFont(QFont('Arial', 40))

        self.system_label = QLabel("System Online", self)
        self.system_label.setAlignment(Qt.AlignRight)
        self.system_label.setStyleSheet("color: #ADD8E6;")
        self.system_label.setFont(QFont('Arial', 50))

        self.top_layout.addWidget(self.date_label)
        self.top_layout.addWidget(self.system_label)
        self.main_layout.addLayout(self.top_layout)

        self.circle_label = QLabel("C.O.R.E", self)
        self.circle_label.setAlignment(Qt.AlignCenter)
        self.circle_label.setFont(QFont('Arial', 100, QFont.Bold))
        self.circle_label.setStyleSheet("color: #ADD8E6; border: 3px solid #ADD8E6; border-radius: 100px; padding: 20px;")
        self.main_layout.addWidget(self.circle_label, 1, Qt.AlignCenter)

        self.status_label = QLabel("Status: Idle", self)
        self.status_label.setAlignment(Qt.AlignLeft)
        self.status_label.setStyleSheet("color: #ADD8E6;")
        self.status_label.setFont(QFont('Arial', 50))

        self.cpu_label = QLabel("CPU Usage: 0%", self)
        self.cpu_label.setAlignment(Qt.AlignRight)
        self.cpu_label.setStyleSheet("color: #ADD8E6;")
        self.cpu_label.setFont(QFont('Arial', 50))

        self.bottom_layout.addWidget(self.status_label)
        self.bottom_layout.addWidget(self.cpu_label)
        self.main_layout.addLayout(self.bottom_layout)

        self.mic_button = QPushButton("Mic", self)
        self.mic_button.setStyleSheet("background-color: #ADD8E6; color: white; border-radius: 20px;")
        self.mic_button.setFixedSize(100, 50)
        self.main_layout.addWidget(self.mic_button, 0, Qt.AlignBottom | Qt.AlignHCenter)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_info)
        self.timer.start(1000)
        self.setLayout(self.main_layout)
        self.show()

        # Initialize status signal
        self.status_signal = StatusSignal()

        # Connect the signal to update status
        self.status_signal.update_status.connect(self.set_status)

    def update_info(self):
        self.date_label.setText(time.strftime("%Y-%m-%d %H:%M:%S"))
        cpu_usage = psutil.cpu_percent(interval=1)
        self.cpu_label.setText(f"CPU Usage: {cpu_usage}%")

    def set_status(self, status_text):
        self.status_label.setText(f"Status: {status_text}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = COREUI()
    sys.exit(app.exec_())
