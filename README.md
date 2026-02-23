## Roastbot AI – Local Conversational AI System
Roastmaster AI is an offline conversational AI chatbot that demonstrates Generative AI integration using a locally hosted large language model. It provides real-time chat functionality powered by local inference, showcasing prompt engineering and AI deployment techniques.

##  Features
Local LLM-powered chatbot (no external API dependency)
Real-time conversational interface
Flask-based backend with REST API
Prompt-controlled response generation
Responsive web UI
Offline AI inference capability
Demonstration of GenAI pipeline

## Technical Overview
This project illustrates:
Local model hosting and inference
Backend API design with Flask
Prompt engineering for controlled responses
Frontend interaction using JavaScript
Full-stack AI application architecture
Real-time client-server communication

## Tech Stack
Backend: Python, Flask
Frontend: HTML, CSS, JavaScript
AI Model: Local LLM via Ollama
Tools: VS Code, Git

## 📂 Project Structure
Roastmaster-AI/
│
├── app.py                # Flask backend
├── index.html            # Frontend interface
├── static/               # Assets (if used)
├── templates/            # HTML templates (optional)
└── README.md             # Documentation

## Setup & Installation
Prerequisites
Python 3.x
Flask
Ollama installed
LLM model downloaded


## Step 1: Install Dependencies
pip install flask requests
## Step 2: Install Ollama
Download and install Ollama:
👉 https://ollama.ai
## Step 3: Pull LLM Model
ollama pull llama3
## Step 4: Start Ollama Server
ollama serve
This runs the local model server.
## Step 5: Run Flask Backend
python app.py
The application will run at:
http://127.0.0.1:5000
## Step 6: Open in Browser
Navigate to:
http://127.0.0.1:5000
Start interacting with the chatbot.

## How It Works
User sends message via frontend
Flask backend processes request
Backend forwards prompt to local LLM
LLM generates response
Response is returned to UI
This demonstrates a complete AI-driven application pipeline.

## Possible Enhancements
Multi-mode response system
Chat history storage
User authentication
Response analytics
Model switching capability
Docker containerization


## Feedback or Any queries?
Feel free to reach out via LinkedIn :https://www.linkedin.com/in/suwetha-e-82346b25b?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app
or email: suwethas71@gmail.com

## Author
Suwethas71
* Suwetha E *


