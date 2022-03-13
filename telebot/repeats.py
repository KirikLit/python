import config
import telebot

bot = telebot.TeleBot(config.token)
repeating = False


def repeat(message):
    global repeating

    if message.text == 'Повтори':
        bot.send_message(message.chat.id, 'Повторяю за тобой\nСкажи "Стоп" для отключения')
        repeating = True
    elif repeating:
        if message.text == 'Стоп':
            bot.send_message(message.chat.id, 'Я остановился')
            repeating = False
        else:
            bot.send_message(message.chat.id, message.text)
