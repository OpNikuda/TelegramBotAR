from telebot import types
from dict import ridles
import random

def get_random_riddle_beginner():
    """
    Возвращает случайную загадку из списка (beginner).
    Returns:
        dict: Словарь с загадкой и ответом.
    """
    beginner, _, _ = ridles()  # Извлекаем только beginner
    return random.choice(beginner)

def get_random_riddle_intermediate():
    """
    Возвращает случайную загадку из списка (intermediate).
    Returns:
        dict: Словарь с загадкой и ответом.
    """
    _, _, intermediate = ridles()  # Извлекаем только intermediate
    return random.choice(intermediate)

def get_random_riddle_advanced():
    """
    Возвращает случайную загадку из списка (advanced).
    Returns:
        dict: Словарь с загадкой и ответом.
    """
    _, advanced, _ = ridles()  # Извлекаем только advanced
    return random.choice(advanced)

def create_riddle_markup():
    """
    Создает Inline-клавиатуру для загадок.
    Returns:
        types.InlineKeyboardMarkup: Клавиатура с кнопкой "Ответить".
    """
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("Ответить", callback_data='answer_riddle')
    markup.add(btn)
    return markup

def check_riddle_answer(user_answer, correct_answer):
    """
    Проверяет ответ пользователя на загадку.
    Args:
        user_answer (str): Ответ пользователя.
        correct_answer (str): Правильный ответ.
    Returns:
        str: Результат проверки.
    """
    if user_answer.lower() == correct_answer.lower():
        return "Правильно! 🎉"
    else:
        return f"Неправильно! Правильный ответ: {correct_answer}."

def create_new_keyboard_yes_no():
    """
    Создает Inline-клавиатуру с кнопками 'Yes' и 'No'.
    Returns:
        types.InlineKeyboardMarkup: Inline-клавиатура с кнопками 'Yes' и 'No'.
    """
    markup = types.InlineKeyboardMarkup()
    yes_button = types.InlineKeyboardButton('Yes', callback_data='yes')
    no_button = types.InlineKeyboardButton('No', callback_data='no')
    markup.add(yes_button, no_button)
    return markup

def create_new_keyboard_yes():
    """
    Создает Inline-клавиатуру с кнопками после ответа 'Yes'.
    Returns:
        types.InlineKeyboardMarkup: Inline-клавиатура с кнопками:
            - Puzzles
            - Explore Vocabulary
            - Practice Grammar
            - Back
    """
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Puzzles", callback_data='puzzle')
    btn2 = types.InlineKeyboardButton("Explore Vocabulary", callback_data='explore_vocabulary')
    btn3 = types.InlineKeyboardButton("Practice Grammar", callback_data='practice_grammar')
    btn4 = types.InlineKeyboardButton("Back", callback_data='back')
    markup.add(btn1, btn2, btn3, btn4)
    return markup

def create_learn_response():
    """
    Создает Inline-клавиатуру с кнопками уровней сложности.
    Returns:
        tuple: Кортеж из двух элементов:
            - markup (types.InlineKeyboardMarkup): Inline-клавиатура с кнопками.
            - text (str): Текст, который нужно отправить вместе с клавиатурой.
    """
    text = (
        f'Welcome, language adventurers!\n'
        f'Are you ready to embark on a journey through the fascinating world of English?\n'
        'To tailor your experience, we invite you to select your preferred level of challenge'
    )
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Beginner', callback_data='beginner')
    btn2 = types.InlineKeyboardButton('Advanced', callback_data='advanced')
    btn3 = types.InlineKeyboardButton('Intermediate', callback_data='intermediate')
    btn4 = types.InlineKeyboardButton('Back', callback_data='back')
    markup.add(btn1, btn2, btn3, btn4)
    return markup, text

def beginner_learning():
    """
    Возвращает текст и клавиатуру для уровня Beginner.
    Returns:
        tuple: Кортеж из двух элементов:
            - text (str): Текст сообщения.
            - markup (types.InlineKeyboardMarkup): Inline-клавиатура с кнопками.
    """
    text = (
        f"А, я вижу, ты выбрал уровень Beginner!\n"
        f"Well choice, мой друг. 🧙‍♂️\n"
        f"Даже величайшие wizards начинали с простых spells, а самые mighty dragons когда-то были tiny hatchlings.\n"
        f"Давай начнем твое journey с веселых и легких riddles. Не worry, я не буду кидать в тебя fireballs... пока что. 🔥\n"
        f"Ты готов unlock secrets Beginner's Chest? 🎁\n"
        "Просто нажми 'Go', и let the adventure begin!"
    )
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Go', callback_data='go')
    btn2 = types.InlineKeyboardButton('Back', callback_data='back')
    markup.add(btn1, btn2)
    return text, markup

def advanced_learning():
    text = (
        f'Excellent choice! 🌟 You’re about to embark on a journey of intricate riddles that will not only challenge your intellect but also enrich your vocabulary. 🧠✨'
    )
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Go', callback_data='go')
    btn2 = types.InlineKeyboardButton('Back', callback_data='back')
    markup.add(btn1, btn2)
    return text, markup

def intermediate_learning():
    text = (
        f'Great choice! 🎉 Let’s dive into some intermediate riddles that will challenge your mind and help you learn new words!'
    )
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Go', callback_data='go')
    btn2 = types.InlineKeyboardButton('Back', callback_data='back')
    markup.add(btn1, btn2)
    return text, markup

def get_vocabulary_response():
    """
    Создает Inline-клавиатуру с кнопками 'Bebra' и 'Brb'.
    Returns:
        tuple: Кортеж из двух элементов:
            - markup (types.InlineKeyboardMarkup): Inline-клавиатура с кнопками.
            - text (str): Текст, который нужно отправить вместе с клавиатурой.
    """
    text = 'pon'
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Bebra', callback_data='bebra')
    btn2 = types.InlineKeyboardButton('Brb', callback_data='brb')
    btn3 = types.InlineKeyboardButton('Back', callback_data='back')
    markup.add(btn1, btn2, btn3)
    return markup, text

def get_grammar_response():
    """
    Создает Inline-клавиатуру с кнопками 'Bebra' и 'Brb'.
    Returns:
        tuple: Кортеж из двух элементов:
            - markup (types.InlineKeyboardMarkup): Inline-клавиатура с кнопками.
            - text (str): Текст, который нужно отправить вместе с клавиатурой.
    """
    text = 'pon'
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Bebra', callback_data='bebra')
    btn2 = types.InlineKeyboardButton('Brb', callback_data='brb')
    btn3 = types.InlineKeyboardButton('Back', callback_data='back')
    markup.add(btn1, btn2, btn3)
    return markup, text

def remove_keyboard():
    """
    Удаляет клавиатуру.
    Returns:
        types.ReplyKeyboardRemove: Объект для удаления клавиатуры.
    """
    return types.ReplyKeyboardRemove()

def get_greeting():
    """
    Возвращает приветственное сообщение.
    Returns:
        str: Текст приветственного сообщения.
    """
    return (
        f"Hey there, language explorer!🕵️‍♂️\n"
        f"🔍 I'm your AR companion, here to turn every word into an experience.\n"
        f"Let's make English as real as the world around you. Ready to begin?😊"
    )

def get_yes_response():
    """
    Возвращает ответ на 'Yes'.
    Returns:
        str: Текст ответа на 'Yes'.
    """
    text = (
        f'Yes? Awesome!\n'
        f'Strap in, explorer—your language adventure is about to soar!🌟\n'
        f'Let’s transform the everyday into something extraordinary, word by word.🚀'
    )
    return text

def get_no_response():
    """
    Возвращает ответ на 'No'.
    Returns:
        str: Текст ответа на 'No'.
    """
    return (
        f'No? Alrighty then!\n'
        f'No skin off my circuits—teaching you wasn’t exactly my life’s mission.\n'
        f'🖖Maybe you’ll wander back when curiosity bites. Until then, happy trails, explorer! ✨'
    )