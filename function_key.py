import json
from info import qustions, bot, STATE, massage3, massage4, massage5, massage6
from function import create_keyboard, remove_keyboard


def save_progress(user_id, question_number):
    cur_progress = {str(user_id): question_number}

    try:
        with open('progress.json', 'r') as file:
            progress = json.load(file)

        progress[str(user_id)] = question_number
        with open('progress.json', 'w') as file:
            json.dump(progress, file)

    except:
        with open('progress.json', 'w') as file:
            json.dump(cur_progress, file)

def proverka(message):
    return STATE.get(message.chat.id)


def send_message(message, question_number):
    quest = qustions[question_number]["answers"].values()
    quest_text = qustions[question_number]["question"]
    markup = create_keyboard(quest)
    if qustions[question_number]["photo"] != 0:
        name_photo = qustions[question_number]["photo"]
        photo = open(name_photo, "rb")
        bot.send_photo(message.chat.id, photo)
    bot.send_message(message.chat.id, quest_text, reply_markup=markup)

def end(message):
    if STATE[message.chat.id]["question_number"] == 15:
        good_game = open("конец игры.jpg", "rb")
        bot.send_photo(message.chat.id, good_game)
        bot.send_message(message.chat.id, "Мега Хорош", reply_markup=remove_keyboard)
        save_progress(STATE[message.chat.id], STATE[message.chat.id]["question_number"])

def proverka_crovat(message):
    if message.text == qustions[5]["answers"][10]:
        crovat = open("тумбочка-кровать.jpg", "rb")
        bot.send_photo(message.chat.id, crovat)
        bot.send_message(message.chat.id, massage3)

def proverka_pusta(message):
    if message.text == qustions[5]["answers"][11]:
        pusta = open("пустая комната.jpg", "rb")
        bot.send_photo(message.chat.id, pusta)
        bot.send_message(message.chat.id, massage4)

def proverka_look_room(message):
    if message.text == qustions[5]["answers"][12]:
        bot.send_message(message.chat.id, massage5)

def dead(message):
    if message.text == qustions[8]["answers"][3] or message.text == qustions[14]["answers"][3]:
        game_over = open("game over.jpg", "rb")
        bot.send_message(message.chat.id, massage6)
        bot.send_photo(message.chat.id, game_over)
        bot.send_message(message.chat.id, "Печально, но попробуй ещё раз по команде /quest",
                         reply_markup=remove_keyboard)
        STATE[message.chat.id] = {
            'question_number': 21
        }
        return

def proverka_full_answers(message):
    proverka_crovat(message)
    proverka_pusta(message)
    proverka_look_room(message)
    dead(message)
