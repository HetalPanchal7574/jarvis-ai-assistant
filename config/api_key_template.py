# ElevenLabs API Configuration Template
# Copy this file to api_key.py and add your actual API key

from elevenlabs import stream
from elevenlabs.client import ElevenLabs

# Replace 'your_api_key_here' with your actual ElevenLabs API key
API_KEY = "your_api_key_here"

# Initialize ElevenLabs client
elevenlabs = ElevenLabs(api_key=API_KEY)

def get_audio_stream(text, voice_id="JBFqnCBsd6RMkjVDRZzb", model_id="eleven_multilingual_v2"):
    """
    Generate audio stream from text using ElevenLabs API
    
    Args:
        text (str): Text to convert to speech
        voice_id (str): ElevenLabs voice ID
        model_id (str): ElevenLabs model ID
    
    Returns:
        Audio stream object
    """
    audio_stream = elevenlabs.text_to_speech.stream(
        text=text,
        voice_id=voice_id,
        model_id=model_id
    )
    return audio_stream

# Example usage:
# audio_stream = get_audio_stream("This is a test")
# stream(audio_stream)