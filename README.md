# EcotronixAI — Multilingual Voice Assistant for Farmers

An AI-powered, real-time voice assistant built for farmers, combining LiveKit for low-latency voice communication, Google Gemini API for intelligent multilingual conversations, and the OpenWeather API for live weather updates. Designed to help farmers get instant agricultural guidance, weather forecasts, and support — in their own language, through natural voice conversation.

📌 Overview

Farmers often face language barriers and limited access to timely agricultural information. KisanMitra AI bridges this gap by offering a voice-first assistant that:

Understands and responds in multiple regional languages
Answers farming-related queries using Gemini's generative AI
Fetches real-time weather data from OpenWeather for informed decision-making
Streams voice interactions in real time using LiveKit
✨ Features
🎙️ Real-time voice conversations via LiveKit's WebRTC infrastructure
🧠 AI-powered responses using Google Gemini for natural language understanding
🌦️ Live weather updates (temperature, rainfall, humidity, forecasts) via OpenWeather API
🌐 Multilingual support — farmers can speak and receive responses in their preferred language
⚡ Low-latency streaming for a natural, human-like conversational experience
📱 Accessible design built for ease of use, even for non-tech-savvy users
🛠️ Tech Stack
Component	Technology
Voice Infrastructure	LiveKit
AI / LLM	Google Gemini API
Weather Data	OpenWeather API
Backend	(e.g. Python / Node.js — update as applicable)
Speech-to-Text / Text-to-Speech	(mention providers used, if any)
🏗️ Architecture
Farmer (Voice Input)
        │
        ▼
   LiveKit Room (Real-time Audio Streaming)
        │
        ▼
Speech-to-Text → Language Detection
        │
        ▼
   Gemini API (Understanding + Response Generation)
        │
        ├──► OpenWeather API (if weather query detected)
        │
        ▼
Text-to-Speech (Multilingual Output)
        │
        ▼
   LiveKit Room (Audio Response to Farmer)
🚀 Getting Started
Prerequisites
Node.js / Python (specify version)
A LiveKit server instance or LiveKit Cloud account
Google Gemini API key
OpenWeather API key
Installation
bash
# Clone the repository
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

# Install dependencies
npm install
# or
pip install -r requirements.txt
Environment Variables

Create a .env file in the root directory:

env
LIVEKIT_URL=your_livekit_server_url
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret

GEMINI_API_KEY=your_gemini_api_key

OPENWEATHER_API_KEY=your_openweather_api_key
Running the Project
bash
npm start
# or
python main.py
🌍 Supported Languages
Hindi
Tamil
Telugu
Kannada
English
(Add/remove based on your actual implementation)
📖 Usage
Start the application and join the LiveKit room.
Speak your query naturally — for example: "आज बारिश होगी क्या?" (Will it rain today?)
The assistant detects your language, processes the query via Gemini, fetches weather data if needed, and responds back in voice — in the same language.
🗺️ Roadmap
 Add support for more regional languages
 Integrate crop disease detection via image input
 Add market price (mandi rate) lookup
 Offline/low-bandwidth mode for rural connectivity
 Mobile app integration
🤝 Contributing

Contributions are welcome! Please follow these steps:

Fork the repository
Create a new branch (git checkout -b feature/your-feature)
Commit your changes (git commit -m 'Add some feature')
Push to the branch (git push origin feature/your-feature)
Open a Pull Request
📄 License

This project is licensed under the MIT License.

🙏 Acknowledgements
LiveKit for real-time communication infrastructure
Google Gemini for conversational AI capabilities
OpenWeather for weather data APIs
All the farmers and communities who inspired this project
