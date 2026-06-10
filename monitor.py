import logging
from telegram.ext import Updater, CommandHandler

logging.basicConfig(level=logging.INFO)

TOKEN ="8335424933:AAGC0T-TTzU-TjjCA6g9t1MAMtsd76FZF8c"

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
