# Voice Bot 🎙️ (Telegram + ElevenLabs)

**Voice Bot** — это Telegram-бот на Python, который озвучивает текстовые сообщения с помощью API ElevenLabs и возвращает голосовое сообщение в чат. Проект создан для обучения prompt-инжинирингу и интеграции голосовых технологий.

## 🚀 Возможности
- Получает текст в Telegram-чате
- Преобразует текст в речь с помощью ElevenLabs API
- Отправляет голосовое сообщение обратно пользователю
- Использует выбранный голос (например, Sarah)

## 📁 Структура проекта
- `main.py` — основной файл Telegram-бота
- `config.py` — ключи для ElevenLabs и Telegram
- `voice.py` — модуль, отправляющий запрос на озвучку
- `requirements.txt` — зависимости проекта

## ⚙️ Установка и запуск
```bash
git clone https://github.com/YuliaK19/voice_bot.git
cd voice_bot
pip install -r requirements.txt
