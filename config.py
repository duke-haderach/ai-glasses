GROQ_API_KEY = "gsk_your_key_here"   # console.groq.com
SAMPLE_RATE = 16000
CHANNELS = 1

STT_MODEL = "whisper-large-v3-turbo"
LLM_MODEL = "llama-3.3-70b-versatile"
TTS_MODEL = "canopylabs/orpheus-v1-english"
TTS_VOICE = "hannah"  # Options: autumn, diana, hannah, austin, daniel, troy

SYSTEM_PROMPT = """You are a wearable AI assistant.
Give concise 1-2 sentence answers suitable for audio playback.
No bullet points, no markdown."""
