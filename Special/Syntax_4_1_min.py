"""
Синтаксис питона за 1 минуту
В этой программе содержатся почти все
стандартные операторы, методы и прочее,
что есть в стандартном питоне
"""


class ExampleClass:
    def __init__(self):
        print('Инициализация класса ExampleClass')       # При создании класса запускается метод __init__
        self.var1 = 'Переменная 1'                       # Переменные self будут доступны внутри всего класса и снаружи
        self.var2 = True
        self.var3 = 'Переменная "var3"'

        # Вызов метода класса изнутри
        self.example_method()

    def example_method(self):       # У классов есть функции - методы
        print('\nМетод example_method класса ExampleClass')
        if self.var2:
            print('Переменная self.var1 - %s' % self.var1)


def example_if(var, var2, var3):    # Функции можно вызывать много раз и передавать им разные параметры
    if var == 1 or var2 < 2:                    # Если var1 == 1 или var2 меньше 2-х
        return 'var = 1 или var2 меньше 2-х'    # Возвращаем строку
    elif var3 == 2 and var2 == 2:               # Иначе если var3 = 2 и var2 = 2
        return 'var3 = 2 и var2 = 2'            # Возвращаем строку
    else:                                       # Ни одно условие не выполнено
        return 'Ни одно условие не выполнилось'  # Возвращаем строку


def example_while():        # Можно и без параметров
    global x
    while x > 0:            # Выполняем пока x больше чем 0
        x -= 3
        print('x больше чем 0 и равен {}'.format(x))    # Выводим через  .format


def example_list():
    dictionary = {'par1': 'parameter',  # В словаре для каждого параметра есть своё значение
                  'par2': 22,
                  'par3': 'par4'}
    ex = ExampleClass()     # Создаём элемент класса ExampleClass

    # Ниже - список
    list_of_elements = [1, True, 'Hello, World!', 12.5, ex]     # В списке у каждого есть индекс, могут быть разные типы

    tuple_elem = ('Hello,', 'World!')   # Кортежи

    print('Словарь: par2 - {par2},\npar3 - {par3}, par1 - {par1}\n'.format(**dictionary))  # Примеры использования вышеперечисленного

    print(list_of_elements[2])                      # Печатаем элемент с индексом 2 из списка
    list_of_elements[2] = 'Изменение параметра'     # Изменяем элемент с индексом 2 из списка
    print(list_of_elements[2] + '\n')               # Печатаем элемент с индексом 2 из списка
    for elem in list_of_elements:                   # Для каждого элемента из списка выполняем всё что ниже
        print(f'Элемент: {elem!r}, индекс: {list_of_elements.index(elem)}, тип: {type(elem)}')

    # Печатаем кортеж через проценты
    print('\n%s %s' % tuple_elem)


def example_class():
    print('\nПример использования классов')
    clas = ExampleClass()       # Создаём класс, вызывается функция __init__
    classvars = [clas.var1, clas.var2, clas.var3, type(clas.var1), type(clas.var2), type(clas.var3)]    # Список включает в себя переменные и их типы
    print('{0!r}: {3}, {1}: {4}, {2!r}: {5}'.format(*classvars))    # Вывод отформатированного списка на экран

    clas.example_method()   # Вызываем метод класса снаружи


def main():
    # Функция main() вызывает все функции по очереди
    print('\nПример использования if')      # \n переносит на другую строку
    print(example_if(1, 10, 10))            # Вызываем функцию example_if с параметрами 1, 10, 10
    print(example_if(10, 1, 10))
    print(example_if(10, 2, 2))
    print(example_if(10, 10, 10))

    print('\nПример использования while')
    example_while()                         # Если у функции нет параметров, скобки всё равно нужно писать

    print('\nПример использования списков и прочего')
    example_list()

    example_class()


if __name__ == '__main__':                  # Это не обязательно, но программисты так делают
    x = 15
    main()          # Вызываем функцию main(). Можно заменить на любую другую
