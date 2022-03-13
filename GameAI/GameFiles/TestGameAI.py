from GameAI.GameFiles.AI import GaMer
import time


class GameTest:

    def __init__(self):
        self.AI = GaMer()
        self.game()

    def game(self):
        while True:

            answ = False
            tries = 8
            tricnt = 1
            last = 'start'
            rand = int(input('Загадайте число: '))
            print('\nПрограмма найдёт число менее чем за 8 попыток')
            time.sleep(1)

            while not answ:
                if tries > 0:
                    print('Осталось попыток: %i' % tries)

                    a = self.AI.get(last)
                    print(a)

                    if a > rand:
                        print("Загаданное число меньше\n")
                        tries -= 1
                        tricnt += 1
                        last = '<'
                    elif a < rand:
                        print('Загаданное число больше\n')
                        tries -= 1
                        tricnt += 1
                        last = '>'
                    else:
                        print('Вы отгадали число!\n')
                        self.AI.reset()
                        answ = True
                else:
                    print('Попытки закончились\nЗагаданное число - ' + str(rand))
                    self.AI.reset()
                    answ = True
            print('Прогрмма нашла число за %i попыток!' % tricnt)


if __name__ == '__main__':
    gg = Game(True)
