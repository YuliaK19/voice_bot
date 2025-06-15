import os
import httpx
from config import API_KEY

ELEVEN_API_URL = "https://api.elevenlabs.io/v1/text-to-speech"
DEFAULT_VOICE_ID = "EXAVITQu4vr4xnSDxMaL"  # Можно заменить на другой ID из get_voices()


def get_voices():
    url = "https://api.elevenlabs.io/v1/voices"
    headers = {
        "xi-api-key": API_KEY,
        "accept": "application/json",
    }

    try:
        response = httpx.get(url, headers=headers, timeout=15.0)
        response.raise_for_status()
        data = response.json()
        return [(v["voice_id"], v["name"]) for v in data.get("voices", [])]
    except httpx.HTTPStatusError as exc:
        print(f"Ошибка {exc.response.status_code}: {exc.response.text}")
        return []


def text_to_speech(text: str, voice_id: str = DEFAULT_VOICE_ID, filename="output.mp3") -> str:
    headers = {
        "xi-api-key": API_KEY,
        "accept": "audio/mpeg",
        "Content-Type": "application/json"
    }

    body = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.7
        }
    }

    url = f"{ELEVEN_API_URL}/{voice_id}/stream"
    response = httpx.post(url, headers=headers, json=body)

    if response.status_code == 200:
        # Абсолютный путь к файлу
        filepath = os.path.join(os.getcwd(), filename)
        with open(filepath, "wb") as f:
            f.write(response.content)
        return filepath
    else:
        print(f"Ошибка TTS: {response.status_code} — {response.text}")
        return ""
