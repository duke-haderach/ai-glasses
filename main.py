from loc_pipeline import transcribe, ask_llm, speak
from recorder import record_after_wake
import os

conversation_history = []

print("AI Glasses Ready!")
print("Press G -> Speak -> Hear reply")
print("Ctrl+C to quit\n")

while True:
    try:
        audio_file = record_after_wake()
        text = transcribe(audio_file)
        if len(text.strip()) > 2:
            reply = ask_llm(text, conversation_history)
            speak(reply)
        try:
            os.unlink(audio_file)
        except Exception:
            pass
    except KeyboardInterrupt:
        print("\nGoodbye!")
        break
    except Exception as e:
        print(f"Error: {e}")
