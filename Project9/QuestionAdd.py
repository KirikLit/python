class Question():
    def __init__(self, QText, answ):
        self.QText = QText
        self.answ = answ


#Добавление вопросов
#Пример N-Номер вопроса, QueNT - Текст(\n - Перенос на след. строку)
#QueNA - Номер ответа (А - 1, Б - 2, В - 3, Г - 4)
#Создание вопроса - QueN = Question(QueNT, QueNA)

Que1T = 'Где находится Тунис?\n\nА: В Африке\nБ: На Чёрном море\nВ: В Евразии\nГ: На берегу балтийского моря'
Que1A = 1
Que1 = Question(Que1T, Que1A)

Que2T = "Какой океан не омывает Россию?\n\nА: Атлантический\nБ: Тихий\nВ: Индийский\nГ: Северный Ледовитый"
Que2A = 3
Que2 = Question(Que2T, Que2A)

#Не забудь добавить вопрос в список
Questions = [Que1, Que2]



#Свободные ячейки для автовопросов
newQues = ['Que3', 'Que4', 'Que5', 'Que6', 'Que7', 'Que8', 'Que9', 'Que0', 'Que01', 'Que02', 'Que03', 'Que04', 'Que05',
           'Que06', 'Que07', 'Que08', 'Que09', 'Que00']