import subprocess
import sounddevice as sd
import soundfile as sf
import os
import tempfile
from core.config import PIPER_EXE, PIPER_MODEL

def speak(text: str):
    if not text:
        return

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        tmp_path = tmp.name

    try:
        process = subprocess.run(
            [PIPER_EXE, "--model", PIPER_MODEL, "--output_file", tmp_path],
            input=text.encode("utf-8"),
            capture_output=True
        )

        if process.returncode == 0 and os.path.exists(tmp_path):
            data, samplerate = sf.read(tmp_path)
            sd.play(data, samplerate)
            sd.wait()
        else:
            print(f"TTS Error: {process.stderr.decode()}")
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
