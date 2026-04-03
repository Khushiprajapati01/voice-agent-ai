from core.audio import record_audio
from core.stt import transcribe
from core.llm import chat
from core.tts import speak
from utils.helpers import is_silent

STOP_WORDS = ["exit", "quit", "bye", "stop"]

def main():
    print("=" * 40)
    print("  🎤 Offline Voice Agent — Ready")
    print("  Say 'exit' or 'quit' to stop")
    print("=" * 40)

    history = []

    while True:
        try:
            audio_path = record_audio()
            user_text = transcribe(audio_path)

            if is_silent(user_text):
                print("🔇 Nothing detected, try again.")
                continue

            if any(word in user_text.lower() for word in STOP_WORDS):
                speak("Goodbye!")
                print("👋 Exiting.")
                break

            reply = chat(user_text, history)
            speak(reply)
            history.append({"user": user_text, "assistant": reply})

        except KeyboardInterrupt:
            print("\n👋 Interrupted. Exiting.")
            break

if __name__ == "__main__":
    main()
