import pyaudio
import webrtcvad
import wave
import tempfile
import keyboard
from config import SAMPLE_RATE, CHANNELS

vad = webrtcvad.Vad(1)
CHUNK_SIZE = int(SAMPLE_RATE * 30 / 1000)

def record_after_wake():
    print("Press G then speak...")
    keyboard.wait('g')
    print("GLASSES activated! Speak now...")

    pa = pyaudio.PyAudio()
    stream = pa.open(
        rate=SAMPLE_RATE, channels=1,
        format=pyaudio.paInt16, input=True,
        frames_per_buffer=CHUNK_SIZE
    )

    frames = []
    for _ in range(100):  # 3s minimum
        frames.append(stream.read(CHUNK_SIZE, exception_on_overflow=False))

    silence_count = 0
    while silence_count < 20:
        chunk = stream.read(CHUNK_SIZE, exception_on_overflow=False)
        is_speech = vad.is_speech(chunk, SAMPLE_RATE)
        frames.append(chunk)
        print("MIC" if is_speech else ".", end="", flush=True)
        silence_count = 0 if is_speech else silence_count + 1

    stream.stop_stream()
    stream.close()
    pa.terminate()
    print(f"\nRecorded {len(frames)*0.03:.1f}s")

    tmp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    with wave.open(tmp.name, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(b"".join(frames))
    return tmp.name
