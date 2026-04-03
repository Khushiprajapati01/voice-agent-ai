import sounddevice as sd
import soundfile as sf
import os
from core.config import SAMPLE_RATE, RECORD_SECONDS, RECORDINGS_DIR

def record_audio(filename="input.wav"):
    os.makedirs(RECORDINGS_DIR, exist_ok=True)
    filepath = os.path.join(RECORDINGS_DIR, filename)

    print(f"\n🎙️  Listening for {RECORD_SECONDS} seconds...")
    audio = sd.rec(
        int(RECORD_SECONDS * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype='float32'
    )
    sd.wait()
    sf.write(filepath, audio, SAMPLE_RATE)
    print("✅ Done recording.")
    return filepath
