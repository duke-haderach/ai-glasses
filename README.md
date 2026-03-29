# 🕶️ AI Glasses — Open Source Voice Assistant

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Groq](https://img.shields.io/badge/Powered%20by-Groq-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Working-brightgreen)

---

## 🎯 What Is This?

Regular glasses + Bluetooth earbud + Python = **AI glasses that listen, think, and speak back**.

Press **G** → Speak → Hear your AI reply through the earbud in under **1.5 seconds**.
[G Key] → VAD Speech Detection → Groq Whisper STT → Groq LLaMA LLM → Groq Orpheus TTS → Earbud
↕
< 1.5 seconds end-to-end

text

---

## ✨ Features

- 🎤 **Auto speech detection** via WebRTC VAD (no cloud wake word service)
- 📝 **Groq Whisper STT** — 200x real-time transcription
- 🧠 **Groq LLaMA 3.3-70B** — sub-second AI responses
- 🔊 **Groq Orpheus TTS** — natural voice output (10x real-time)
- 🔁 **Conversation memory** — multi-turn dialogue
- 💸 **Free** — runs entirely on Groq's free tier

---

## 🛠️ Hardware

| Item | Cost |
|---|---|
| Any pair of glasses | $0 (you have them) |
| Bluetooth earbud (any brand) | $0–$30 |
| Laptop / PC | $0 (you have one) |
| Microphone (built-in or USB) | $0 |

**Total hardware cost: $0 if you already own an earbud**

---

## 🚀 Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/ai-glasses.git
cd ai-glasses
```

### 2. Create virtual environment (Python 3.13 required)

```bash
py -3.13 -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> ⚠️ **Windows users**: If `pyaudio` fails, use `pip install pyaudio` with Python 3.13.
> If `webrtcvad` fails, use `pip install webrtcvad-wheels`.

### 4. Get your free Groq API key

- Visit [console.groq.com](https://console.groq.com)
- Sign up for free
- Copy your API key

### 5. Configure

```bash
cp config.example.py config.py
# Edit config.py and paste your GROQ_API_KEY
```

### 6. Accept Orpheus TTS terms (one-time)

- Visit: https://console.groq.com/playground?model=canopylabs%2Forpheus-v1-english
- Click **Accept Terms**

### 7. Run

```bash
python main.py
```

---

## 💡 Usage
🕶️ AI Glasses Ready! Press G → Speak → Hear reply

Press G → "What time is it?" → "It's 4:03 PM CDT"
Press G → "Tell me a joke" → laughs through earbud
Press G → "What is 15% of 240?" → "That's 36"

text

**Ctrl+C** to quit.

---

## 📁 Project Structure
ai-glasses/
├── main.py # Entry point — main loop
├── recorder.py # Wake key + VAD audio capture
├── loc_pipeline.py # STT + LLM + TTS pipeline
├── config.py # API keys and model settings
├── config.example.py # Safe template (no keys)
├── requirements.txt # Python dependencies
└── README.md
## 🐛 Common Issues

| Error | Fix |
|---|---|
| `Failed building wheel for pyaudio` | Use Python 3.13, not 3.14 |
| `Failed building wheel for webrtcvad` | `pip install webrtcvad-wheels` |
| `ModuleNotFoundError: pygame` | `pip install pygame-ce` |
| `voice must be one of...` | Use: `autumn`, `diana`, `hannah`, `austin`, `daniel`, `troy` |
| `Audio file is too short` | Speak for 3+ seconds after pressing G |
| `PermissionError: WinError 32` | Already fixed in `speak()` with retry loop |
| `model_terms_required` | Accept Orpheus terms at Groq console |
| Nothing happens on SPACE | Use G key, run terminal as Administrator |

---

## 🗺️ Roadmap

- [x] Phase 1 — Audio pipeline (STT + LLM + TTS)
- [x] Phase 1.5 — Wake key + VAD auto-detection
- [ ] Phase 2 — Phone app (Flutter / Termux)
- [ ] Phase 3 — Clip-on camera (ESP32-CAM) + vision
- [ ] Phase 4 — Custom voice wake word ("Hey Jarvis")
- [ ] Phase 5 — Battery pack → fully untethered

---

## 📊 Performance

| Metric | Value |
|---|---|
| End-to-end latency | ~1.5 seconds |
| STT accuracy | ~96% |
| CPU (idle listening) | ~15% |
| RAM usage | ~450 MB |
| Cost per 1000 queries | ~$0 (free tier) |

---

## 🤝 Contributing

Pull requests welcome! Areas that need help:

- Android/iOS companion app
- Custom wake word integration
- ESP32-CAM vision module
- Raspberry Pi Zero deployment

---

## 📜 License

MIT License — use it, fork it, build on it.

---

## 🙏 Credits

Built with:
- [Groq](https://groq.com) — blazing fast inference
- [OpenWakeWord](https://github.com/dscripka/openWakeWord) — wake word engine
- [WebRTC VAD](https://github.com/wiseman/py-webrtcvad) — speech detection
- [pygame-ce](https://pyga.me) — audio playback
