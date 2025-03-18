from telebot import types
from master_func import (
    create_new_keyboard_yes_no, remove_keyboard, get_greeting, get_yes_response, get_no_response,
    create_new_keyboard_yes, get_vocabulary_response, get_grammar_response, create_learn_response, beginner_learning,
    get_random_riddle, create_riddle_markup, check_riddle_answer
)

def handle_start(bot):
    """
    Регистрирует обработчик команды /start.
    """
    @bot.message_handler(commands=['start'])
    def start(message):
        greeting = get_greeting()
        markup = create_new_keyboard_yes_no()
        bot.send_message(message.chat.id, greeting, reply_markup=markup)

def answer_from_user_1(bot):
    """
    Регистрирует обработчик callback-запросов от Inline-кнопок "Yes" и "No".
    """
    @bot.callback_query_handler(func=lambda call: call.data in ['yes', 'no'])
    def yes_or_no(call):
        if call.data == 'yes':
            reply = get_yes_response()
            new_markup = create_new_keyboard_yes()
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=reply,
                reply_markup=new_markup
            )
        elif call.data == 'no':
            reply = get_no_response()
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=reply
            )

def answer_from_user_2(bot):
    """
    Регистрирует обработчик callback-запросов от Inline-кнопок "Puzzles", "Explore Vocabulary", "Practice Grammar".
    """
    @bot.callback_query_handler(func=lambda call: call.data in ['puzzle', 'explore_vocabulary', 'practice_grammar'])
    def learn_vocab_grammar(call):
        if call.data == 'puzzle':
            markup, text = create_learn_response()
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=text,
                reply_markup=markup
            )

    @bot.callback_query_handler(func=lambda call: call.data == 'go')
    def handle_go_button(call):
        riddle = get_random_riddle()
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=riddle["question"]
        )
        bot.register_next_step_handler(call.message, process_riddle_answer, riddle["answer"], bot)

def process_riddle_answer(message, correct_answer, bot):
    """
    Обрабатывает ответ пользователя на загадку.
    """
    user_answer = message.text
    result = check_riddle_answer(user_answer, correct_answer)
    bot.send_message(message.chat.id, result)

def level_learning_p2(bot):
    @bot.callback_query_handler(func=lambda call: call.data in ['beginner', 'advanced', 'intermediate'])
    def beginner_advanced_intermediate(call):
        text, markup = beginner_learning()
        if call.data == 'beginner':
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=text,
                reply_markup=markup
            )

def answer_from_user_3(bot):
    """
    Регистрирует обработчик callback-запросов от Inline-кнопок "Bebra" и "Brb".
    """
    @bot.callback_query_handler(func=lambda call: call.data in ['bebra', 'brb'])
    def bebra_brb(call):
        if call.data == 'bebra':
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text="Вы нажали Bebra"
            )
        elif call.data == 'brb':
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text="Вы нажали Brb"
            )