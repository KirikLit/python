import math
import time
from colorama import Back, Fore, init
init()

print(Back.WHITE)
print(Fore.BLACK)
print('SICalc v2.1 ©Kirik_Lit')

print(Fore.RED)
print(Back.RESET)
print('!** - Возведение в степень! \n !*** - Вычисление корня!')

o = "Ваш ответ: "
print(Fore.BLACK)
print(Back.GREEN)
todo = input('Что делаем? (+, -, *, /, **,***, pi ): ')

print(Back.LIGHTYELLOW_EX)

if todo == '***':
    x = float(input('Введите число для извлечения корня: '))
    c = x ** 0.5
    print(o + str(c))
    print('Пока!')
    time.sleep(10)
    exit()
elif todo == 'pi':
    print(o + str(math.pi))
    print('Пока!')
    time.sleep(10)
    exit()
else:
    print(Back.CYAN)

    a = float(input('Ведите первое число: '))
    b = float(input('Введите второе число: '))

    print(Back.LIGHTYELLOW_EX)

    if todo == '+':
        x = a + b
        print(o + str(x))
    elif todo == '-':
        x = a - b
        print(o + str(x))
    elif todo == '*':
        x = a * b
        print(o + str(x))
    elif todo == '/':
        x = a - b
        print(o + str(x))
    elif todo == '**':
        x = a ** b
        print(o + str(x))

    print('Пока!')
    time.sleep(10)



