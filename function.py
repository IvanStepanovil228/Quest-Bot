from telebot.types import ReplyKeyboardMarkup, KeyboardButton, Message, ReplyKeyboardRemove
from info import qustions

remove_keyboard = ReplyKeyboardRemove()

def proverka_button1(message, question_number):
    if message.text == qustions[question_number]["answers"][2]:
        return True
    return False

def create_keyboard(quest):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for i in quest:
        markup.add(KeyboardButton(i))
    return markup
