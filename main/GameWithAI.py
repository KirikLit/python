import random
from GameAI.GameFiles import GaMer


class Game:

    def __init__(self, include):
        self.AIInclude = include
        self.AI = GaMer()
        self.tricnts = {'min': 0, 'max': 0, 'ers': 0}
        self.game()

    def game(self):
        for x in range(100000000):

            answ = False
            tries = 8
            tricnt = 1
            last = 'start'
            rand = random.randint(0, 100)
            print('\nНайдите число от 0 до 100 за %i попыток' % tries)

            while not answ:
                if tries > 0:
                    print('Осталось попыток: %i' % tries)

                    a = self.AI.get(last)
                    print(a)

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
                        self.triap(tricnt)
                    tricnt += 1
                else:
                    print('Попытки закончились\nЗагаданное число - ' + str(rand))
                    self.tricnts['ers'] += 1
                    self.AI.reset()
                    answ = True

        print(self.tricnts)

    def triap(self, tricnt):
        if tricnt > self.tricnts['max']:
            self.tricnts['max'] = tricnt

        if tricnt < self.tricnts['min']:
            self.tricnts['min'] = tricnt


if __name__ == '__main__':
    gg = Game(True)
