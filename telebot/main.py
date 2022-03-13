import config
import telebot
import repeats as rep

bot = telebot.TeleBot(config.token)
repeating = False


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, 'Привет')


@bot.message_handler(content_types=['text'])
def send_message(message):
    rep.repeat(message)


if __name__ == '__main__':
    bot.infinity_polling()
