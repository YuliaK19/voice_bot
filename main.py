import asyncio
import sys
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from elevenlabs.client import ElevenLabs
from config import API_KEY, BOT_TOKEN

VOICE_ID = "EXAVITQu4vr4xnSDxMaL"  # Sarah

client = ElevenLabs(api_key=API_KEY)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if not text:
        await update.message.reply_text("Отправь текст для озвучки.")
        return

    audio = client.text_to_speech.convert(
        voice_id=VOICE_ID,
        model_id="eleven_multilingual_v2",
        text=text
    )

    with open("speech.mp3", "wb") as f:
        for chunk in audio:
            f.write(chunk)

    with open("speech.mp3", "rb") as voice_file:
        await update.message.reply_voice(voice=voice_file)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()


