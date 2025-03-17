import telebot
import config
from start import handle_start, answer_from_user

bot = telebot.TeleBot(config.TOKEN)

# Вызов функций для установки обработчиков
handle_start(bot)
answer_from_user(bot)

if __name__ == "__main__":
    bot.polling(none_stop=True)
