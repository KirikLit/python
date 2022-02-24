import telebot
import random
from telebot import types

bot = telebot.TeleBot('5144155625:AAGSPXWLydSWlZDQSo5ZPjRnH3pHN1DpOCA')

@bot.message_handler(content_types=['text'])

if message.text == 'Привет':
    start_messa

def start_message(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id,"Привет!\n\nНапиши \"Команды\" что бы узнать, что я могу")
    else:

@bot.message_handler(content_types=['text'])

def echo_game(message):
    if message.text == "Игра угадай число":
        bot.send_message(message.chat.id, "Для выхода скажи \"Пока\"")
        while message.text == "Пока":
            n = random.randint(0, 100)
            x = int(message.text)

            if x == n:
                answer = 'Ты отгадал число!'
            elif x < n:
                answer = 'Загаданное число больше!'
            elif x > n:
                answer = 'Загаданное число меньше!'

            bot.send_message(message.chat.id, answer)
    else:

@bot.message_handler(content_types=['text'])
def button_message(message):
    if message.text == 'Команды':
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Игра угадай число")
        markup.add(item1)
        bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)
    else:

bot.polling(none_stop=True)


