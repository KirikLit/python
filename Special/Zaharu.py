products = []
products2 = []
ask = True

while ask:
    x = input('Введите название товара: ')
    x1 = int(input('Введите цену товара: '))
    x2 = int(input('Введите кол-во товара: '))
    xSum = x1 * x2

    print('Вы купили ' + str(x2) + ' ' + x + ' стоимостью ' + str(xSum))

    products.append(x)
    products2.append(xSum)

    closeAsk = input('Введите \'Нет\' для выхода или нажмите Enter для продолжения: ')
    if closeAsk == 'Нет':
        ask = False

prSum = ', '.join(products)
print("Вы купили: " + prSum)
print('Стоимость: ' + str(sum(products2)))