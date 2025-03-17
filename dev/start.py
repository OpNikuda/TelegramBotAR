from telebot import types

def handle_start(bot):
    @bot.message_handler(commands=['start'])
    def start(message):
        user = message.from_user
        username = user.username

        greeting = (
            f"Hey there, language explorer!🕵️‍♂️\n"
            f"🔍 I'm your AR companion, here to turn every word into an experience.\n"
            f"Let's make English as real as the world around you. Ready to begin?😊"
        )

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        yes_button = types.KeyboardButton('Yes')
        no_button = types.KeyboardButton('No')
        markup.add(yes_button, no_button)

        bot.reply_to(message, greeting, reply_markup=markup)

def answer_from_user(bot):
    @bot.message_handler(func=lambda message: message.text.lower() in ['yes', 'no'])
    def yes_or_no(message):
        if message.text.lower() == 'yes':
            reply = (
            f'Yes? Awesome!\n'
            f'Strap in, explorer—your language adventure is about to soar!🌟\n'
            f'Let’s transform the everyday into something extraordinary, word by word.🚀'
            )
        elif message.text.lower() == 'no':
            reply = (
            f'No? Alrighty then!\n'
            f'No skin off my circuits—teaching you wasn’t exactly my life’s mission.\n'
            f'🖖Maybe you’ll wander back when curiosity bites. Until then, happy trails, explorer! ✨'
            )


        remove_markup = types.ReplyKeyboardRemove()
        bot.reply_to(message, reply, reply_markup=remove_markup)
