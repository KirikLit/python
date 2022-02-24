from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM('85a26eea569d629dc208b2088993880f', config_dict)

place = input('Введите свой город: ')

mgr = owm.weather_manager()
observation = mgr.weather_at_place(place)
w = observation.weather

n = w.detailed_status
t = w.temperature('celsius')['temp']
print("В городе " + place + " сейчас " + n + '\n Температура составляет ' + str(t) + ' градусов по цельсию')