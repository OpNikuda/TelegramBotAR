import telebot
import config
from start import (handle_start)

bot = telebot.TeleBot(config.TOKEN)
handle_start(bot)

if __name__ == "__main__":
    bot.polling(none_stop=True)