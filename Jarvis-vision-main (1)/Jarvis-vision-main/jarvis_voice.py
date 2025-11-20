# jarvis_voice.py
import pygame
import io
from elevenlabs.client import ElevenLabs

# ---------------------------
# Configuration
# ---------------------------
API_KEY = "the key is deleted "  # Replace with your ElevenLabs API key
VOICE_ID = "4ATqP3ZeEoRwPpQqXzAY"  # Your custom Jarvis voice ID

# Initialize ElevenLabs client once
client = ElevenLabs(api_key=API_KEY)

# Initialize pygame mixer once
pygame.mixer.init()

def speak(text):
    """
    Convert text to speech using ElevenLabs and play it.
    Works just like pyttsx3.speak().
    """
    try:
        # Request audio from ElevenLabs
        response = client.text_to_speech.convert(
            voice_id=VOICE_ID,
            model_id="eleven_multilingual_v2",
            text=text
        )

        # Combine all audio chunks into one
        audio_bytes = b"".join(chunk for chunk in response)

        # Load the audio into pygame from memory
        pygame.mixer.music.load(io.BytesIO(audio_bytes))

        # Play the audio
        pygame.mixer.music.play()

        # Keep the program alive until audio finishes
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(f"[ERROR] Voice generation failed: {e}")
