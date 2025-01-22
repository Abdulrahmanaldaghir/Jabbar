# Jabbar

Jabbar is an AI-powered assistant system that integrates voice recognition, speech synthesis, and image processing. It offers multiple modes such as Friend, Teacher, and Helper, and can respond to queries, provide weather updates, tell stories, and display images. The system uses OpenAI’s GPT models and integrates with various Python libraries to create an interactive experience.

## Features

- **Voice Recognition**: Jabbar listens to user queries through a microphone and converts speech to text using Google's Speech Recognition API.
- **Speech Synthesis**: Provides responses using both `pyttsx3` and `gTTS` (Google Text-to-Speech).
- **Multiple Modes**: Switch between modes like *Friend*, *Teacher*, and *Helper*, tailoring the response according to the selected mode.
- **Image Display**: Jabbar can display images by fetching them from URLs and showing them using OpenCV.
- **Weather Information**: Jabbar can fetch and announce weather information using OpenWeatherMap API.
- **Interactive AI Responses**: It uses OpenAI’s GPT models to process queries and generate text-based responses.

## Requirements

- Python 3.x
- Pygame
- SpeechRecognition
- pyttsx3
- gTTS
- pydub
- OpenAI API Key
- OpenWeatherMap API Key

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/abdulrahmanaldaghir/jabbar.git
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up API keys:
    - [Get OpenAI API Key](https://platform.openai.com/signup)
    - [Get OpenWeatherMap API Key](https://openweathermap.org/appid)

4. Run the main program from the `japar` folder:
    ```bash
    cd jabbar
    python main007.py
    ```
## How to Use

Once the program is running, Jabbar will prompt you to select a mode (Friend, Teacher, Helper). You can then interact by speaking, and Jabbar will respond with relevant information, jokes, weather updates, stories, or display images as per the mode.

## Contributing

If you'd like to contribute to Jabbar, feel free to open an issue or submit a pull request. We welcome contributions and feedback!

