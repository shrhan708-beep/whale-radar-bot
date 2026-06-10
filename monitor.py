import os
from telegram import Bot
from telegram.ext import Application, CommandHandler

BOT_TOKEN = os.environ['BOT_TOKEN']
CHAT_ID = os.environ['CHAT_ID']

async def start(update, context):
    await update.message.reply_text('✅ بوت رادار الحيتان شغال')

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot running...")
app.run_polling()
