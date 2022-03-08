import random
import time
from GameAI.GameFiles.AI import GaMer


class Game:

    def __init__(self, include):
        self.AIInclude = include
        self.AI = GaMer()
        self.game()

    def game(self):
        while True:
            answ = False
            tries = 20
            ant = 0
            last = 'start'
            rand = random.randint(0, 100)
            print('\nНайдите число от 0 до 100 за %i попыток' % tries)
            time.sleep(1)

            while not answ:
                if tries > 0:
                    print('Осталось попыток: %i' % tries)
                    if not self.AIInclude:
                        a = input('Введите число: ')
                    else:
                        time.sleep(1)
                        a = self.AI.get(last)
                    print(a)
                    ant = a

                    if a > rand:
                        print("Загаданное число меньше\n")
                        tries -= 1
                        last = '<'
                    elif a < rand:
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