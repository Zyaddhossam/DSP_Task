import speech_recognition as sr

recognizer = sr.Recognizer()

def record_audio():
    with sr.Microphone() as source:
        print("Listening... (Speak now)")
        recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
        audio = recognizer.listen(source, timeout=5)  # Listen for 5 seconds max
        print("Audio recorded")
    return audio

def recognize_speech_offline(audio):
    try:
        # Use PocketSphinx (offline)
        text = recognizer.recognize_sphinx(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
    except sr.RequestError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    try:
        import pocketsphinx
    except ImportError:
        print("Installing PocketSphinx for offline recognition...")
        import subprocess
        subprocess.run(["pip", "install", "pocketsphinx"], check=True)

    print("--- Offline Speech Recognition ---")
    audio = record_audio()
    recognize_speech_offline(audio)