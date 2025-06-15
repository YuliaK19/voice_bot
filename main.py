import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from voice import text_to_speech  # Импортируем функцию из voice.py

BOT_TOKEN = os.getenv("BOT_TOKEN")

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Отправь мне текст, и я озвучу его 🎤")

# Ответ на любое текстовое сообщение
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    audio_path = text_to_speech(user_text)
    with open(audio_path, "rb") as audio:
        await update.message.reply_voice(audio)

# Настройка и запуск бота (polling)
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    app.run_polling()
