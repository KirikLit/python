import telebot
import random
from telebot import types

bot = telebot.TeleBot('5144155625:AAGSPXWLydSWlZDQSo5ZPjRnH3pHN1DpOCA')

@bot.message_handler(content_types=['text'])

def botyara_logical(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id,"Привет!\n\nНапиши \"Команды\" что бы узнать, что я могу")
    elif message.text == "Игра угадай число":
        #bot.send_message(message.chat.id, 'Игра началась')
        n = random.randint(0, 100)
        win = 0
        while win == 0:
            x = int(message.text)
            if x == n:
                win = 1
                answer = 'Ты отгадал число!'
            elif x < n:
                answer = 'Загаданное число больше!'
            elif x > n:
                answer = 'Загаданное число меньше!'
            bot.send_message(message.chat.id, answer)

    elif message.text == 'Команды':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Игра угадай число")
        markup.add(item1)
        bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)

bot.polling(none_stop=True)