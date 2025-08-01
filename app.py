from flask import Flask, request, jsonify
import os
import google.generativeai as genai
from google.cloud import texttospeech
import pygame
import io
import re # <-- Added for cleaning text

# --- Configuration ---
# Use the full, absolute path to the credentials file
script_dir = os.path.dirname(os.path.abspath(__file__))
credentials_path = os.path.join(script_dir, 'gcp_tts_credentials.json')
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

# IMPORTANT: I have removed my key for security. Paste your own key here.
GEMINI_API_KEY = 'API KEY' 
genai.configure(api_key=GEMINI_API_KEY)

# --- Flask App Initialization ---
app = Flask(__name__)

# --- AI & Voice Functions ---
def generate_dialogue(status):
    """Generates dialogue based on the status string from the ESP8266."""
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    
    if status == "hot":
        prompt = "You are a wise coaster. A fresh, hot drink has just been placed on you. Say something short, welcoming, and profound in a single sentence. Provide dialogue only, no action descriptions."
    elif status == "cold":
        prompt = "You are a sarcastic but funny Malayalam movie character like Innocent or Jagathy. The tea placed on you has gone cold. Say a short, witty, complaining dialogue in Manglish. Provide dialogue only, no action descriptions."
    else: # This covers "moderate"
        prompt = "You are a slightly concerned friend. The tea on you is cooling down. Gently remind the user to drink it before it gets cold. Say this in a short, friendly Manglish sentence. Provide dialogue only, no action descriptions."
            
    try:
        response = model.generate_content(prompt)
        dialogue = response.text.strip().replace('*', '')
        # Clean the text to remove anything in parentheses e.g. (smiles)
        dialogue = re.sub(r'\(.*?\)', '', dialogue).strip()
        print(f"AI Generated Dialogue for status '{status}': {dialogue}")
        return dialogue
    except Exception as e:
        print(f"Error generating dialogue: {e}")
        return "The universe is vast, and so are my errors."

def convert_text_to_speech(text):
    """Converts text to speech and returns the audio content as bytes."""
    try:
        client = texttospeech.TextToSpeechClient()
        synthesis_input = texttospeech.SynthesisInput(text=text)
        
        # --- VOICE CHANGE FOR OPTION 1 ---
        # Switched to a premium WaveNet voice with an Indian English accent
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-IN",  # Indian English
            name="en-IN-Wavenet-D"   # A high-quality male WaveNet voice
        )
        
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )
        response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)
        print("Text-to-Speech conversion successful.")
        return response.audio_content
    except Exception as e:
        print(f"Error converting text to speech: {e}")
        return None

def play_audio(audio_data):
    """Plays audio data from a bytes object using pygame."""
    if audio_data:
        try:
            pygame.mixer.init()
            audio_file = io.BytesIO(audio_data)
            pygame.mixer.music.load(audio_file)
            print("Playing audio...")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            print("Playback finished.")
        except Exception as e:
            print(f"Error playing audio with pygame: {e}")

# --- Flask Routes ---
@app.route("/")
def index():
    return "Samsaara Coaster Backend is running!"

@app.route("/trigger")
def handle_trigger():
    temp_status = request.args.get('temp_status', 'moderate')
    print(f"Trigger received: Temperature status is '{temp_status}'")
    dialogue_text = generate_dialogue(temp_status)
    audio_bytes = convert_text_to_speech(dialogue_text)
    play_audio(audio_bytes)
    message = "Dialogue generated and played"
    return jsonify({"status": "success", "message": message}), 200

# --- Main Execution Block ---
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)