import logging
from telegram.ext import Updater, CommandHandler

logging.basicConfig(level=logging.INFO)

TOKEN ="8780879869:AAE8fbIc-J7sz3GpUJUgxBtlMIa7aLM2Pxw"

def start(update, context):
    update.message.reply_text("البوت شغال 🔥")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
