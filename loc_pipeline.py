import os
import tempfile
import time
import pygame
from groq import Groq
from config import (
    GROQ_API_KEY, STT_MODEL, LLM_MODEL,
    TTS_MODEL, TTS_VOICE, SYSTEM_PROMPT
)

groq_client = Groq(api_key=GROQ_API_KEY)

def transcribe(audio_path: str) -> str:
    with open(audio_path, "rb") as f:
        result = groq_client.audio.transcriptions.create(
            file=f,
            model=STT_MODEL,
            response_format="text"
        )
    print(f"You said: {result}")
    return result

def ask_llm(text: str, history: list) -> str:
    history.append({"role": "user", "content": text})
    response = groq_client.chat.completions.create(
        model=LLM_MODEL,
        messages=[{"role": "system", "content": SYSTEM_PROMPT}] + history
    )
    reply = response.choices[0].message.content
    history.append({"role": "assistant", "content": reply})
    print(f"AI: {reply}")
    return reply

def speak(text: str):
    response = groq_client.audio.speech.create(
        model=TTS_MODEL,
        voice=TTS_VOICE,
        input=text,
        response_format="wav"
    )
    tmp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    audio_bytes = response.read()
    print(f"TTS: {len(audio_bytes)} bytes")
    tmp.write(audio_bytes)
    tmp.close()

    pygame.mixer.init()
    pygame.mixer.music.load(tmp.name)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    for _ in range(10):
        try:
            os.unlink(tmp.name)
            break
        except PermissionError:
            time.sleep(0.1)
    print("Done speaking!")
