import telebot
import config
from start import handle_start, answer_from_user_1, answer_from_user_2, level_learning_p2

bot = telebot.TeleBot(config.TOKEN)

# Вызов функций для установки обработчиков
handle_start(bot)
answer_from_user_1(bot)
answer_from_user_2(bot)
level_learning_p2(bot)

if __name__ == "__main__":
    bot.polling(none_stop=True)