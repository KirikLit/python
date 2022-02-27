again = True

while again:
    name = input('Введите название фигуры: ').lower()
    func = input('Введите функцию (1 - Площадь, 2 - Периметер): ')
    funcs = ['1', '2']
    if func not in funcs:
        print('Неверная функция')
        continue
    if name == 'прямоугольник':
        n = float(input('Введите ширину: '))
        c = float(input('Введите длину: '))
        if func == '1':
            res = n * c
        else:
            res = (n + c) * 2
    elif name == 'квадрат':
        n = float(input('Введите длину стороны квадрата: '))
        if func == '1':
            res = n ** 2
        else:
            res = n * 4
    elif name == 'круг':
        n = float(input('Введите радиус круга: '))
        if func == '1':
            res = 3.14 * (n ** 2)
        else:
            res = 2 * 3.14 * n
    elif name == 'параллелограмм':
        n = float(input('Введите основание параллелограмма: '))
        if func == '1':
            c = float(input('Введите высоту параллелограмма: '))
            res = n * c
        else:
            c = float(input('Введите боковую сторону параллелограмма: '))
            res = (n + c) * 2
    else:
        print('Вы ввели неверную фигуру\n')
        continue
    if func == '1':
        print('Площадь фигуры', name, 'равна:', res)
    else:
        print('Периметер фигуры', name, 'равен:', res)
    print('\n')
