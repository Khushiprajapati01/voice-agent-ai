import whisper
from core.config import WHISPER_MODEL

_model = None

def load_model():
    global _model
    if _model is None:
        print("⏳ Loading Whisper model...")
        _model = whisper.load_model(WHISPER_MODEL)
        print("✅ Whisper ready.")
    return _model

def transcribe(audio_path: str) -> str:
    model = load_model()
    result = model.transcribe(audio_path)
    text = result["text"].strip()
    print(f"🗣️  You said: {text}")
    return text
