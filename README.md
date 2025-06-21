# 🤖 Jarvis AI Assistant

An intelligent voice-activated AI assistant with natural language processing capabilities, inspired by Tony Stark's JARVIS. This project combines speech recognition, text-to-speech, machine learning, and system automation to create a comprehensive virtual assistant.

## ✨ Features

### 🎯 Core Capabilities
- **Voice Recognition**: Converts speech to text using Google's Speech Recognition API
- **Text-to-Speech**: Responds with natural-sounding voice using pyttsx3
- **Intelligent Chat**: Neural network-based intent classification for natural conversations
- **System Control**: Manage system volume, open/close applications, check system status
- **Web Integration**: Quick access to social media platforms and Google search
- **Schedule Management**: Personal timetable and schedule assistance
- **Real-time System Monitoring**: CPU usage, battery status, and system health checks

### 🧠 AI-Powered Features
- **Intent Recognition**: Custom-trained neural network model for understanding user queries
- **Contextual Responses**: Dynamic response generation based on conversation context
- **Confidence Scoring**: Smart fallback when the assistant is uncertain about user intent
- **Extensible Architecture**: Easy to add new intents and responses

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- Windows OS (for system-specific features)
- Microphone for voice input
- Internet connection for speech recognition

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/jarvis-ai-assistant.git
   cd jarvis-ai-assistant
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up API keys** (Optional - for ElevenLabs TTS)
   ```bash
   cp config/api_key_template.py config/api_key.py
   # Edit config/api_key.py with your actual API key
   ```

4. **Run the assistant**
   ```bash
   python src/main.py
   ```

## 📋 Dependencies

```txt
tensorflow>=2.8.0
keras>=2.8.0
speech-recognition>=3.10.0
pyttsx3>=2.90
pyautogui>=0.9.54
numpy>=1.21.0
scikit-learn>=1.0.0
psutil>=5.9.0
pickle-mixin>=1.0.2
```

## 🎮 Usage

### Voice Commands
- **Greeting**: "Hello", "Hi there", "Good morning"
- **Social Media**: "Open Facebook", "Open Instagram", "Open WhatsApp"
- **System Control**: "Volume up", "Volume down", "Mute"
- **Applications**: "Open calculator", "Open notepad", "Close paint"
- **Web Search**: "Open Google" → "Search for [your query]"
- **Schedule**: "What's my schedule?", "Show time table"
- **System Status**: "System condition", "Check battery"
- **Exit**: "Exit", "Goodbye"

### Example Interaction
```
Jarvis: Good morning! It's Monday, 09:30 AM
You: "Hello Jarvis"
Jarvis: "Hello! How can I help you today?"
You: "What's my schedule?"
Jarvis: "Today's schedule: Algorithms, System Design, Programming Lab"
You: "Open calculator"
Jarvis: "Opening calculator"
```

## 🏗️ Project Structure

```
jarvis-ai-assistant/
├── src/
│   ├── main.py              # Main application entry point
│   ├── model_train.py       # Neural network training script
│   └── model_test.py        # Model testing and validation
├── data/
│   └── intent.json          # Training data for intent classification
├── models/
│   ├── chat_model.h5        # Trained neural network model
│   ├── tokenizer.pkl        # Text tokenizer for preprocessing
│   └── label_encoder.pkl    # Label encoder for intent classes
├── config/
│   └── api_key.py          # API configuration (not tracked)
└── README.md
```

## 🧠 AI Model Details

### Architecture
- **Input Layer**: Embedding layer for text vectorization
- **Processing**: Global Average Pooling followed by Dense layers
- **Output**: Softmax classification for intent prediction
- **Training**: 1000 epochs with sparse categorical crossentropy loss

### Intent Categories
- Greetings and conversation starters
- System commands and automation
- Information requests
- Application control
- Web browsing assistance

## 🔧 Customization

### Adding New Intents
1. Edit `data/intent.json` to add new intent patterns and responses
2. Run the training script: `python src/model_train.py`
3. The model will be automatically updated

### Modifying System Commands
- Edit the command functions in `src/main.py`
- Add new application paths in `openApp()` and `closeApp()` functions
- Customize the schedule in the `schedule()` function

## 🔐 Security & Privacy

- **Local Processing**: All voice processing happens locally
- **API Keys**: Store sensitive keys in environment variables
- **Data Privacy**: No conversation data is stored or transmitted
- **Microphone Access**: Only activated when listening for commands

## 🚧 Known Issues & Limitations

- **Windows-specific**: Some features require Windows OS
- **Internet Dependency**: Speech recognition requires internet connection
- **Microphone Quality**: Performance depends on microphone quality and ambient noise
- **Model Size**: Current model is optimized for basic intents (expandable)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **TensorFlow/Keras** for the machine learning framework
- **Google Speech Recognition** for voice-to-text conversion
- **pyttsx3** for text-to-speech synthesis
- **SpeechRecognition library** for audio processing
- **Marvel's JARVIS** for inspiration
