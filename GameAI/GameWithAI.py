from GameFiles import *


def main():
    print('Вы хотите использовать ИИ?')
    x = input('Ответ(Да/Нет): ')
    if x == 'Да':
        Game(True)
    elif x == 'Нет':
        Game(False)


if __name__ == '__main__':
    main()
