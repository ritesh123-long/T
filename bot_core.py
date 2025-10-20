import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

def run_bot():
    @bot.message_handler(commands=["start"])
    def start(message):
        bot.reply_to(message, "Bot is alive! Replace this with your logic.")

    bot.infinity_polling()
  
