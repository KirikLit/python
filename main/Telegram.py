from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
import telebot

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('85a26eea569d629dc208b2088993880f', config_dict)
bot = telebot.TeleBot('5144155625:AAGSPXWLydSWlZDQSo5ZPjRnH3pHN1DpOCA')

@bot.message_handler(content_types=['text'])

def send_echo(message):
    place = message.text
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather
    n = w.detailed_status
    t = w.temperature('celsius')['temp']

    answer = "В городе " + place + " сейчас " + n + '\n'
    answer += 'Температура составляет ' + str(t) + '° по цельсию' + '\n\n'

    if t < 0:
        answer += 'Сейчас очень холодно, одевайся теплее'
    elif t < 10:
        answer += 'Сейчас не очень холодно, но одевайся теплее'
    else:
        answer += "Сейчас нормальная температура"
    bot.send_message(message.chat.id, answer)
bot.polling(none_stop=True)