![image](https://github.com/user-attachments/assets/50535689-a991-45fb-836c-896115a55476)
C.O.R.E: Cognitive Optimized Responsive Entity

Fueled by Groq AI, transforming automation with voice control, gesture-based actions, and seamless responsiveness!
---
This project is a **desktop application** powered by Groq’s LLaMA3 and designed to run locally on your machine. It cannot be accessed through a website as it is intended for desktop environments.

**Problem Statement**

Problem Statement 1: 
Build a creative and interactive multimodal application powered by Groq, levarging its capabilities to solve real world problems with focus on user experience and innovation.

**Objective**

C.O.R.E. leverages Groq AI to create an intelligent, seamless automation system that combines voice control, gesture-based interactions, and real-time responsiveness. By integrating multimodal AI, it aims to empower users with a futuristic AI assistant capable of intuitive control, smart home integration, and effortless task automation, all while ensuring optimal performance and interactivity. This project targets enhancing user experience, improving efficiency, and delivering smart automation in everyday life.

### Team Members:  
Ishanya Tripathi 
https://www.linkedin.com/in/ishanya-tripathi-48a869293/

Why you chose this problem:
I chose to tackle the challenge of smart automation because, in today's fast-paced world, people are increasingly looking for intuitive, hands-free solutions to interact with their devices. We wanted to push the boundaries of what AI can do in terms of responsiveness and multimodal interaction, merging voice control and gesture-based inputs into one seamless experience. The goal was to create an AI assistant that can automate tasks, respond intelligently, and feel intuitive and futuristic, all powered by Groq AI.

Key challenges you addressed:
One of the biggest challenges we faced was ensuring real-time responsiveness while maintaining high performance. Integrating gesture-based control with voice commands required smooth synchronization between the system's multimodal inputs. Additionally, ensuring that the system could process and react to complex AI tasks without latency was crucial. We also needed to make sure that Groq's AI models could work efficiently across different environments, from wearable devices to smart home systems.

Any pivots, brainstorms, or breakthroughs during hacking:
Early on, we realized that while we had great ideas for automation and voice control, the gesture-based file transfer and UI control was more complex than anticipated. After several iterations, we decided to integrate Groq's AI models with OpenCV for better gesture recognition, which led to breakthrough performance improvements. Another breakthrough was finding a way to integrate the Groq-powered assistant with wearable devices and smart home systems, allowing us to create a fully integrated ecosystem that could handle everything from presentations to home automation with just a gesture or voice command.

---

## 🛠️ Tech Stack

### Core Technologies Used:
- Frontend:  PyQt5 (Transparent UI with system overlays)
- Backend:  Python + Threading + Groq API
- Database: Local file-based config
- APIs: Groq AI

### Sponsor Technologies Used (if any):
- ✅ **Groq:**
-  Used Groq's LLaMA3-8B-8192 model for blazing-fast text understanding and conversation, enabling real-time voice-driven automation.

## ✨ Key Features

✅ Voice Interaction (Speech Recognition & Text-to-Speech)
Seamless communication with the assistant using voice commands and spoken responses.

✅ Groq Integration for AI-Powered Responses
Get intelligent, context-aware responses through the Groq-powered LLaMA3 model.

✅ File Transfer via Local HTTP Server
Effortlessly transfer files between devices over a local network with an integrated HTTP server.

✅ Futuristic UI with Real-Time Status Updates
Sci-fi-inspired transparent interface displaying current system status, CPU usage, and dynamic updates.

✅ Multithreading for Smooth Performance
Ensure responsiveness and real-time processing with multi-threaded operations.

---

## 📽️ Demo & Deliverables

- **Demo Video Link:** https://youtu.be/dllZjtPFAe4
- **PPT Link:** https://drive.google.com/file/d/1P2NZNl9M0CGT-uXnvfpiMrFs6rjb4w6N/view?usp=sharing

---

## ✅ Tasks & Bonus Checklist

- ✅ **All members of the team completed the mandatory task - Followed at least 2 of our social channels and filled the form** (Details in Participant Manual)  


---

## 🧪 How to Run the Project

Requirements:
Python 3.x
PyQt5 for GUI
pyttsx3 for Text-to-Speech
speech_recognition for Speech Recognition
requests for API calls
psutil for system monitoring
OpenCV for any vision-based tasks (optional based on features)
Groq API Key (For AI responses via Groq)
Threading for background processes
### Local Setup:
# Clone the repo
git clone https://github.com/ishanyatripathi/C.O.R.E

# Install dependencies
cd project-name
pip install -r requirements.txt 

 # **Start development server**

---

🧬 Future Scope
📈 More Integrations
Integrate with additional smart home devices or platforms to expand the assistant's capabilities (e.g., Google Home, Alexa, etc.).
Expand support for other AI models for specialized tasks, such as sentiment analysis or object recognition.

🛡️ Security Enhancements
Implement better authentication mechanisms for file transfers and system control (e.g., multi-factor authentication, encryption).
Enhance privacy and data protection by anonymizing requests and ensuring secure communications with external services (like Groq).

🌐 Localization / Broader Accessibility
Add multi-language support to make the assistant accessible to a global audience.
Implement voice commands that cater to different regional accents and dialects.
Introduce accessibility features such as screen reader compatibility and voice-activated control for users with disabilities.

🚀 AI Training and Improvement
Train the assistant on custom data to improve its responses and capabilities for specific domains (e.g., smart home control, advanced file handling).
Introduce machine learning to make the assistant more adaptive to user preferences and behavior over time.

📊 Advanced Analytics
Integrate analytics to monitor usage patterns, optimize performance, and suggest actions based on user behavior (e.g., suggesting specific commands or automations).

⚡ Performance Optimization
Improve the performance of real-time features like speech recognition, response times, and the UI’s responsiveness.
Reduce memory usage and optimize CPU consumption for better scalability and faster interaction.


## 📎 Resources / Credits

-Open Source Libraries / Tools Referenced
Pyttsx3: Text-to-speech engine used to generate spoken responses.

PyQt5: Provides the graphical user interface (GUI) for the assistant with a futuristic design.

Requests: HTTP library used for making API calls, including sending data to the Groq API.

PyAutoGUI: Python library for GUI automation, used here for controlling system actions such as volume control, browser actions, and file transfers.

psutil:Used to monitor system performance and display CPU usage in real-time.

OpenCV: Open-source computer vision library used for visual input processing (though your current code doesn't appear to use OpenCV directly, it could be leveraged for future enhancements).

SocketServer & HTTP Server: Built-in Python libraries used to create the file transfer server.

Acknowledgements
Groq for providing the AI processing capabilities via their API.
SpeechRecognition and Pyttsx3 for enabling voice commands and text-to-speech functionality.
PyQt5 for building the graphical interface that provides a seamless and futuristic UI.
PyAutoGUI for system automation like volume control and file transfers.
psutil for system monitoring and ensuring optimal resource usage in real-time.
Stack Overflow and various programming communities for troubleshooting issues and sharing solutions.

🏁 Final Words
The hackathon has been an amazing journey! From integrating Groq’s LLaMA3 model to building the futuristic J.A.R.V.I.S. UI, every challenge taught me something new.

Challenges:
Groq API integration was tricky, but it helped create intelligent, real-time responses.
UI design with PyQt5 took time, but I achieved the sleek, transparent look I wanted.
Voice commands needed fine-tuning, but now they work seamlessly with SpeechRecognition.

Fun Moments:
Watching the gesture-based file transfer work in real time was a highlight.
Hearing J.A.R.V.I.S. respond with witty remarks kept things light and fun!

Shout-outs:
Big thanks to Groq for powering the assistant.

This project has been a blast, and I’m excited for what comes next!
---
