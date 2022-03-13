from GameFiles import *


def main():
    print('Вы хотите использовать ИИ?')
    print('Если вы хотите сами загадать число - выберите "Тест"')
    x = input('Ответ(Да/Нет/Тест): ')
    if x == 'Да':
        Game(True)
    elif x == 'Нет':
        Game(False)
    elif x == 'Тест':
        GameTest()


if __name__ == '__main__':
    main()
