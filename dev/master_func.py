from telebot import types

def create_keyboard():
    """Создает клавиатуру с кнопками Yes и No."""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    yes_button = types.KeyboardButton('Yes')
    no_button = types.KeyboardButton('No')
    markup.add(yes_button, no_button)
    return markup

def remove_keyboard():
    """Удаляет клавиатуру."""
    return types.ReplyKeyboardRemove()

def get_greeting():
    """Возвращает приветственное сообщение."""
    return (
        f"Hey there, language explorer!🕵️‍♂️\n"
        f"🔍 I'm your AR companion, here to turn every word into an experience.\n"
        f"Let's make English as real as the world around you. Ready to begin?😊"
    )

def get_yes_response():
    """Возвращает ответ на 'Yes'."""
    return (
        f'Yes? Awesome!\n'
        f'Strap in, explorer—your language adventure is about to soar!🌟\n'
        f'Let’s transform the everyday into something extraordinary, word by word.🚀'
    )

def get_no_response():
    """Возвращает ответ на 'No'."""
    return (
        f'No? Alrighty then!\n'
        f'No skin off my circuits—teaching you wasn’t exactly my life’s mission.\n'
        f'🖖Maybe you’ll wander back when curiosity bites. Until then, happy trails, explorer! ✨'
    )