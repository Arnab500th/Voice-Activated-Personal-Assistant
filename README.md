# 🤖 Nova Chatbot – Voice Assistant using Python

🚀 **Internship Project** | **Voice Assistant & Automation**

---

## 📌 Project Overview

This project implements **Nova**, a Python-based **voice-activated personal assistant** capable of:

- Speaking and listening to user commands  
- Managing reminders  
- Fetching live weather updates  
- Providing news headlines  

Nova leverages **speech recognition**, **text-to-speech (TTS)**, and **API integration** to interact naturally with the user.

---

## 🧰 Technologies Used

- Python 3.x  
- Pandas  
- SpeechRecognition  
- gTTS (Google Text-to-Speech)  
- Playsound (for audio playback)  
- Requests  
- Word2Number  

---

## 📂 Project Structure

Chatbot/
│
├─ main.py # Main program
├─ config.py # API keys
├─ requirements.txt # Python dependencies
├─ README.md # Project documentation
├─ .gitignore
│
├─ modules/
│ ├─ init.py
│ ├─ speech.py # Handles TTS & speech recognition
│ ├─ reminders.py # Add, show, delete reminders
│ ├─ weather.py # Fetch weather via API
│ └─ news.py # Fetch news via API
│
└─ data/
└─ reminders.csv # Stored reminders

---

## 📝 Features

1. **Voice Interaction**  
   - Nova listens to your commands and responds via speech.  
   - Example commands:  
     - `Set reminder to eat at 12 pm`  
     - `Show reminders`  
     - `Delete reminder 2`  
     - `Show weather`  
     - `Show news`

2. **Reminders Management**  
   - Add reminders with **task, date, and time**  
   - Show all reminders  
   - Delete a specific reminder or all reminders

3. **Weather Updates**  
   - Uses IP-based geolocation to fetch the current city  
   - Retrieves live weather data from Weather API  
   - Outputs temperature, condition, humidity, wind speed, visibility

4. **News Headlines**  
   - Fetches latest news from **NewsAPI**  
   - Returns top 5 headlines in English

---

## 🧹 How it Works

1. **Greeting**  
   Nova greets the user upon starting the program.  

2. **Command Processing**  
   - Voice input is captured and converted to text using `SpeechRecognition`  
   - Commands are parsed for specific actions:
     - Reminders (`set`, `show`, `delete`)  
     - Weather updates (`weather`)  
     - News headlines (`news`)  

3. **Text-to-Speech**  
   - Responses are generated using `gTTS`  
   - Audio played via `playsound`  

4. **Time Parsing**  
   - Converts 12-hour format commands into 24-hour format for reminders  
   - Supports both numeric and word-based time inputs (`1 pm` or `one pm`)  

---

## ▶️ How to Run the Project

### 1️⃣ Install dependencies
```
pip install -r requirements.txt
```
### 2️⃣ Run the chatbot
```
python main.py
```
---

## 📌 Key Highlights

- Real-time **speech recognition and TTS**
- Fully functional **reminder system**
- Live **weather and news updates**
- **Modular Python code** for easy maintenance
- Uses **external APIs** with proper configuration in `config.py`
- Beginner-friendly, clean, and well-commented code

## 👨‍💻 Author
### Arnab Datta

-Internship Project – Python Voice Assistant & Automation
