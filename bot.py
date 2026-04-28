import random
import asyncio
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

memes = [
    "https://i.imgur.com/W3WbK.jpg",
    "https://i.imgur.com/abc123.jpg",
    "https://i.imgur.com/xyz456.jpg"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Мемы пошли 😎")

    while True:
        meme = random.choice(memes)
        await update.message.reply_photo(meme)
        await asyncio.sleep(5)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
