import random
import asyncio
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

8358960525:AAFn7ymZSGm4n9OBspk3h2sBXXgnh9aXhqs = os.getenv("8358960525:AAFn7ymZSGm4n9OBspk3h2sBXXgnh9aXhqs")

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
