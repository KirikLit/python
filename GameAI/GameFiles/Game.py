import random
import time
from .AI import GaMer


class Game:

    def __init__(self, include):
        self.AIInclude = include
        self.AI = GaMer()
        self.game()

    def game(self):
        while True:
            answ = False
            tries = 8
            last = 'start'
            rand = random.randint(0, 100)
            print('\nНайдите число от 0 до 100 за %i попыток' % tries)
            time.sleep(1)

            while not answ:
                if tries > 0:
                    print('Осталось попыток: %i' % tries)
                    if not self.AIInclude:
                        inp = int(input('Введите число: '))
                    else:
                        time.sleep(1)
                        inp = self.AI.get(last)
                        print('Введённое число: %i' % inp)

                    if inp > rand:
                        print("Загаданное число меньше\n")
                        tries -= 1
                        last = '<'
                    elif inp < rand:
                        print('Загаданное число больше\n')
                        tries -= 1
                        last = '>'
                    else:
                        print('Вы отгадали число!\n')
                        self.AI.reset()
                        answ = True
                else:
                    print('Попытки закончились\nЗагаданное число - ' + str(rand))
                    self.AI.reset()
                    answ = True


if __name__ == '__main__':
    print('Это модуль для другой программы\nОткрой TestGameAI.py')
