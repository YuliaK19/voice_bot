import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = "https://voice-bot-ha8n.onrender.com"  # ← Убедись, что этот адрес совпадает с твоим Render-URL

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Бот запущен через Webhook на Render.")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

# Важно: порт 10000 — стандартный для Render
app.run_webhook(
    listen="0.0.0.0",
    port=int(os.environ.get("PORT", 10000)),
    webhook_url=WEBHOOK_URL
)
