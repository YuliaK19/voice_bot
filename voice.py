# voice.py — Получение списка голосов с ElevenLabs API

import httpx
from config import API_KEY

def get_voices():
    url = "https://api.elevenlabs.io/v1/voices"
    headers = {
        "xi-api-key": API_KEY,
        "accept": "application/json",
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/114.0.0.0 Safari/537.36"
        )
    }

    try:
        response = httpx.get(url, headers=headers, timeout=15.0)
        response.raise_for_status()
        data = response.json()
        return [(v["voice_id"], v["name"]) for v in data.get("voices", [])]
    
    except httpx.HTTPStatusError as exc:
        print(f"Ошибка {exc.response.status_code}: {exc.response.text}")
        return []

if __name__ == "__main__":
    voices = get_voices()
    for voice_id, name in voices:
        print(f"{name}: {voice_id}")
