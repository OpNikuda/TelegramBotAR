import telebot
import config
from start import handle_start, answer_from_user_1, answer_from_user_2, level_learning_p2, answer_from_user_3, audio_on_off

# Инициализация бота
bot = telebot.TeleBot(config.TOKEN)

# Вызов функций для установки обработчиков
handle_start(bot)
answer_from_user_1(bot)
answer_from_user_2(bot)
level_learning_p2(bot)
answer_from_user_3(bot)
audio_on_off(bot)

# Запуск бота
if __name__ == "__main__":
    bot.polling(none_stop=True)