def handle_start(bot):
    @bot.message_handler(commands=['start'])
    def start(message):
        user = message.from_user
        first_name = user.first_name
        last_name = user.last_name
        username = user.username
        bot.reply_to(message, f'Привет, {first_name}')