import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# STT
WHISPER_MODEL = "base"  # options: tiny, base, small, medium

# LLM
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3.2"

# TTS
PIPER_EXE = os.path.join(BASE_DIR, "models", "piper", "piper.exe")
PIPER_MODEL = os.path.join(BASE_DIR, "models", "piper", "en_US-lessac-medium.onnx")

# Audio
SAMPLE_RATE = 16000
RECORD_SECONDS = 5
RECORDINGS_DIR = os.path.join(BASE_DIR, "recordings")
