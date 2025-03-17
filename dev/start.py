from telebot import types
from master_func import create_keyboard, remove_keyboard, get_greeting, get_yes_response, get_no_response

def handle_start(bot):
    """
        Регистрирует обработчик команды /start.

        Args:
            bot (telebot.TeleBot): Экземпляр бота, который будет обрабатывать команду.
        """
    @bot.message_handler(commands=['start'])
    def start(message):
        """
               Обрабатывает команду /start и отправляет приветственное сообщение с клавиатурой.

               Args:
                   message (types.Message): Объект сообщения от пользователя.
               """
        greeting = get_greeting()
        markup = create_keyboard()
        bot.reply_to(message, greeting, reply_markup=markup)

def answer_from_user(bot):
    """
       Регистрирует обработчик ответов "Yes" и "No".

       Args:
           bot (telebot.TeleBot): Экземпляр бота, который будет обрабатывать ответы.
       """
    @bot.message_handler(func=lambda message: message.text.lower() in ['yes', 'no'])
    def yes_or_no(message):
        """
               Обрабатывает ответы "Yes" и "No" и отправляет соответствующий ответ.

               Args:
                   message (types.Message): Объект сообщения от пользователя.
               """
        if message.text.lower() == 'yes':
            reply = get_yes_response()
        elif message.text.lower() == 'no':
            reply = get_no_response()

        remove_markup = remove_keyboard()
        bot.reply_to(message, reply, reply_markup=remove_markup)