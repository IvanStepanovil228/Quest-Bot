from function_key import send_message, proverka, end, proverka_full_answers
from function import remove_keyboard, proverka_button1
from info import massage1, massage2, bot, STATE


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Привет! Я чат бот для квестов ! \n'
                                      'Самое время ввести какую-нибудь команду! \n'
                                      '<b>Если не знаешь, что вводить, введи для начала это:</b>  /help ',
                     parse_mode='html')


@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, massage1, parse_mode='html')


@bot.message_handler(commands=['mem'])
def handle_mem(message):
    photo2 = open("mem.png", "rb")
    bot.send_photo(message.chat.id, photo2)


@bot.message_handler(commands=['id'])
def handle_id(message):
    bot.send_message(message.chat.id,
                     f"{message.from_user.first_name} {message.from_user.last_name} твой id: {message.from_user.id} ",
                     parse_mode='html')


@bot.message_handler(commands=['quest'])
def handle_quest(message):
    bot.send_message(message.chat.id, massage2, reply_markup=remove_keyboard)
    STATE[message.chat.id] = {
        'question_number': 1
    }
    send_message(message, STATE[message.chat.id]["question_number"])


@bot.message_handler(func=proverka)
def handle_questions(message):
    try:
        if not proverka_button1(message, STATE[message.chat.id]['question_number']):
            proverka_full_answers(message)
            bot.send_message(message.chat.id,
                             "Всё таки, к сожалению, ты выбрал не правильный вариант:( Попробуй что-нибудь другое")
            return
    except:
        bot.send_message(message.chat.id,
                         ":( Попробуй что-нибудь другое")
    STATE[message.chat.id]['question_number'] += 1
    send_message(message, STATE[message.chat.id]["question_number"])
    end(message)


bot.polling()
