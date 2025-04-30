from gtts import gTTS
import os
from telebot import types
from master_func import (
    create_new_keyboard_yes_no, remove_keyboard, get_greeting, get_yes_response, get_no_response,
    create_new_keyboard_yes, get_vocabulary_response, get_grammar_response, create_learn_response,
    beginner_learning, advanced_learning, intermediate_learning, get_random_riddle_beginner,
    get_random_riddle_intermediate, get_random_riddle_advanced, create_riddle_markup, check_riddle_answer
)

# Словарь для хранения уровня сложности пользователя
user_levels = {}

# Словарь для хранения истории состояний пользователя
user_states = {}

def handle_start(bot):
    """
    Регистрирует обработчик команды /start.
    """
    @bot.message_handler(commands=['start'])
    def start(message):
        user_id = message.from_user.id
        user_states[user_id] = []  # Инициализируем стек состояний для пользователя
        greeting = get_greeting()
        markup = create_new_keyboard_yes_no()
        bot.send_message(message.chat.id, greeting, reply_markup=markup)
        user_states[user_id].append("start")  # Добавляем текущее состояние в стек

def answer_from_user_1(bot):
    """
    Регистрирует обработчик callback-запросов от Inline-кнопок "Yes" и "No".
    """
    @bot.callback_query_handler(func=lambda call: call.data in ['yes', 'no'])
    def yes_or_no(call):
        user_id = call.from_user.id
        if call.data == 'yes':
            reply = get_yes_response()
            new_markup = create_new_keyboard_yes()
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=reply,
                reply_markup=new_markup
            )
            user_states[user_id].append("yes")  # Добавляем текущее состояние в стек
        elif call.data == 'no':
            reply = get_no_response()
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=reply
            )
            user_states[user_id].append("no")  # Добавляем текущее состояние в стек

def answer_from_user_2(bot):
    """
    Регистрирует обработчик callback-запросов от Inline-кнопок "Puzzles", "Explore Vocabulary", "Practice Grammar".
    """
    @bot.callback_query_handler(func=lambda call: call.data in ['puzzle', 'explore_vocabulary', 'practice_grammar', 'back'])
    def learn_vocab_grammar(call):
        user_id = call.from_user.id
        if call.data == 'puzzle':
            markup, text = create_learn_response()
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=text,
                reply_markup=markup
            )
            user_states[user_id].append("puzzle")  # Добавляем текущее состояние в стек
        elif call.data == 'explore_vocabulary':
            markup, text = get_vocabulary_response()
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=text,
                reply_markup=markup
            )
            user_states[user_id].append("explore_vocabulary")  # Добавляем текущее состояние в стек
        elif call.data == 'practice_grammar':
            markup, text = get_grammar_response()
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=text,
                reply_markup=markup
            )
            user_states[user_id].append("practice_grammar")  # Добавляем текущее состояние в стек
        elif call.data == 'back':
            if user_states[user_id]:  # Если есть предыдущие состояния
                user_states[user_id].pop()  # Удаляем текущее состояние
                if user_states[user_id]:  # Если остались предыдущие состояния
                    previous_state = user_states[user_id][-1]  # Берем последнее состояние
                    if previous_state == "start":
                        greeting = get_greeting()
                        markup = create_new_keyboard_yes_no()
                        bot.edit_message_text(
                            chat_id=call.message.chat.id,
                            message_id=call.message.message_id,
                            text=greeting,
                            reply_markup=markup
                        )
                    elif previous_state == "yes":
                        reply = get_yes_response()
                        markup = create_new_keyboard_yes()
                        bot.edit_message_text(
                            chat_id=call.message.chat.id,
                            message_id=call.message.message_id,
                            text=reply,
                            reply_markup=markup
                        )
                    elif previous_state == "puzzle":
                        markup, text = create_learn_response()
                        bot.edit_message_text(
                            chat_id=call.message.chat.id,
                            message_id=call.message.message_id,
                            text=text,
                            reply_markup=markup
                        )
                    elif previous_state == "explore_vocabulary":
                        markup, text = get_vocabulary_response()
                        bot.edit_message_text(
                            chat_id=call.message.chat.id,
                            message_id=call.message.message_id,
                            text=text,
                            reply_markup=markup
                        )
                    elif previous_state == "practice_grammar":
                        markup, text = get_grammar_response()
                        bot.edit_message_text(
                            chat_id=call.message.chat.id,
                            message_id=call.message.message_id,
                            text=text,
                            reply_markup=markup
                        )

    @bot.callback_query_handler(func=lambda call: call.data == 'go')
    def handle_go_button(call):
        user_id = call.from_user.id
        level = user_levels.get(user_id, 'beginner')  # Получаем уровень сложности пользователя

        if level == 'beginner':
            riddle = get_random_riddle_beginner()
        elif level == 'intermediate':
            riddle = get_random_riddle_intermediate()
        elif level == 'advanced':
            riddle = get_random_riddle_advanced()

        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=riddle["question"]
        )
        bot.register_next_step_handler(call.message, process_riddle_answer, riddle["answer"], bot)
        user_states[user_id].append("riddle")  # Добавляем текущее состояние в стек

def process_riddle_answer(message, correct_answer, bot):
    """
    Обрабатывает ответ пользователя на загадку.
    """
    user_answer = message.text
    result = check_riddle_answer(user_answer, correct_answer)
    bot.send_message(message.chat.id, result)

def level_learning_p2(bot):
    @bot.callback_query_handler(func=lambda call: call.data in ['beginner', 'advanced', 'intermediate', 'back'])
    def beginner_advanced_intermediate(call):
        user_id = call.from_user.id
        if call.data == 'beginner':
            text, markup = beginner_learning()
            user_levels[user_id] = 'beginner'  # Сохраняем уровень сложности
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=text,
                reply_markup=markup
            )
            user_states[user_id].append("beginner")  # Добавляем текущее состояние в стек
        elif call.data == 'advanced':
            text, markup = advanced_learning()
            user_levels[user_id] = 'advanced'  # Сохраняем уровень сложности
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=text,
                reply_markup=markup
            )
            user_states[user_id].append("advanced")  # Добавляем текущее состояние в стек
        elif call.data == 'intermediate':
            text, markup = intermediate_learning()
            user_levels[user_id] = 'intermediate'  # Сохраняем уровень сложности
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=text,
                reply_markup=markup
            )
            user_states[user_id].append("intermediate")  # Добавляем текущее состояние в стек
        elif call.data == 'back':
            if user_states[user_id]:  # Если есть предыдущие состояния
                user_states[user_id].pop()  # Удаляем текущее состояние
                if user_states[user_id]:  # Если остались предыдущие состояния
                    previous_state = user_states[user_id][-1]  # Берем последнее состояние
                    if previous_state == "puzzle":
                        markup, text = create_learn_response()
                        bot.edit_message_text(
                            chat_id=call.message.chat.id,
                            message_id=call.message.message_id,
                            text=text,
                            reply_markup=markup
                        )
                    elif previous_state == "yes":
                        reply = get_yes_response()
                        markup = create_new_keyboard_yes()
                        bot.edit_message_text(
                            chat_id=call.message.chat.id,
                            message_id=call.message.message_id,
                            text=reply,
                            reply_markup=markup
                        )

def answer_from_user_3(bot):
    """
    Регистрирует обработчик callback-запросов от Inline-кнопок "Bebra" и "Brb".
    """
    @bot.callback_query_handler(func=lambda call: call.data in ['bebra', 'brb', 'back'])
    def bebra_brb(call):
        user_id = call.from_user.id
        if call.data == 'bebra':
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text="Вы нажали Bebra"
            )
            user_states[user_id].append("bebra")  # Добавляем текущее состояние в стек
        elif call.data == 'brb':
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text="Вы нажали Brb"
            )
            user_states[user_id].append("brb")  # Добавляем текущее состояние в стек
        elif call.data == 'back':
            if user_states[user_id]:  # Если есть предыдущие состояния
                user_states[user_id].pop()  # Удаляем текущее состояние
                if user_states[user_id]:  # Если остались предыдущие состояния
                    previous_state = user_states[user_id][-1]  # Берем последнее состояние
                    if previous_state == "explore_vocabulary":
                        markup, text = get_vocabulary_response()
                        bot.edit_message_text(
                            chat_id=call.message.chat.id,
                            message_id=call.message.message_id,
                            text=text,
                            reply_markup=markup
                        )
                    elif previous_state == "practice_grammar":
                        markup, text = get_grammar_response()
                        bot.edit_message_text(
                            chat_id=call.message.chat.id,
                            message_id=call.message.message_id,
                            text=text,
                            reply_markup=markup
                        )

def audio_on_off(bot):
    @bot.message_handler(commands=['audio_activate'])
    def audio_on(message):
        user_id = message.from_user.id
        user_states[user_id] = True
        bot.reply_to(message, 'Режим преобразования текста активирован')

    @bot.message_handler(commands=['audio_deactivate'])
    def audio_off(message):
        user_id = message.from_user.id
        user_states[user_id] = False
        bot.reply_to(message, 'Режим преобразования текста деактивирован')

    @bot.message_handler(func=lambda message: True)
    def message_audio(message):
        user_id = message.from_user.id
        if user_states[user_id] == True:
            try:
                user_text = message.text

                tts = gTTS(text=user_text, lang='ru')
                audio_file = "audio.mp3"
                tts.save(audio_file)

                with open(audio_file, 'rb') as audio:
                    bot.send_voice(message.chat.id, audio)

                os.remove(audio_file)
            except Exception as e:
                bot.reply_to(message, f"Произошла ошибка: {e}")
        else:
            bot.reply_to(message, "Режим преобразования текста в голос не активирован. Используйте /start_tts, чтобы активировать его.")



