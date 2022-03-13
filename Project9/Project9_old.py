from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
import random
import pickle
import sys


class Question:
    def __init__(self, qtext, answ):
        self.QText = qtext
        self.answ = answ


def quePrint():
    global que, mode

    if len(Quest) == len(answered):
        Vexit()
        mode = 3
    else:
        que = random.choice(Quest)

        while que in answered:
            que = random.choice(Quest)

        txt.delete(1.0, END)
        txt.insert(0.0, que.QText)
        mainFrame()


def check():
    global score, answrd

    x = answer.get()
    com = combo.get()

    if com == combo1:
        if x == que.answ:
            answText.config(fg='green', text='Молодец!', font=("Arial Bold", 14))
            answered.append(que)
            score += 20
            quePrint()
        else:
            answText.config(fg='red', text='Неправильный ответ!', font=("Arial Bold", 14))
            score -= 10
    elif com == combo2:
        if x == que.answ:
            answrd += 1
            answered.append(que)
            quePrint()
        else:
            answered.append(que)
            quePrint()
    else:
        answered.append(que)
        quePrint()


def mainFrame():
    frame1.pack(fill=X)

    rad1.pack(side=LEFT, pady=5, padx=20)
    rad2.pack(side=LEFT)

    frame2.pack(fill=X)

    rad3.pack(side=LEFT, pady=5, padx=20)
    rad4.pack(side=LEFT)

    frame3.pack(fill=BOTH)

    txt.pack(expand=True, padx=20)
    answText.pack(pady=5)
    btnAnsw.pack()


def start():
    global mode

    mode = 1
    com = combo.get()

    if com == combo3:
        answText.config(text='Режим отладки', fg='Gray')
        btnAnsw.config(text='Далее')
    else:
        answText.config(text='Начинаем!', fg='Gray')
        btnAnsw.config(text='Проверить')

    combo.pack_forget()
    startBut.pack_forget()

    mainFrame()
    quePrint()


def Vexit():
    global answrd

    resetAll()

    com = combo.get()

    if len(Quest) == 0:
        FinishLbl.config(font=("Arial Bold", 20), text='Вопросов нет\nСоздай их!\nВопросы -> Создать')
        FinishLbl.pack(pady=100)
        returnBut.pack()
    elif com == combo1:
        FinishLbl.config(font=("Arial Bold", 20), text='Ты прошёл викторину!\nТвой счёт: ' + str(score))
        FinishLbl.pack(pady=100)
        returnBut.pack()
    elif com == combo2:
        FinishLbl.config(font=("Arial Bold", 20), text='Ты прошёл викторину!\nТы ответил на\n' + str(answrd) +
                         ' вопроса(-ов) из ' + str(len(Quest)))
        FinishLbl.pack(pady=100)
        returnBut.pack()
    else:
        FinishLbl.config(font=("Arial Bold", 20), text='Ты прошёл виктоину\nВ режиме отладки')
        FinishLbl.pack(pady=100)
        returnBut.pack()


def restart():
    global answered, score, answrd

    FinishLbl.pack_forget()
    returnBut.pack_forget()
    answText.config(fg='Gray', text='Начинаем!')

    answered = []
    score = 0
    answrd = 0

    startMenu()


def newQue():
    global mode

    if mode == 1:
        mode = 2
        answText.config(fg='Gray', text='Создание вопроса')
        txt.delete(1.0, END)
        btnAnsw.config(text='Создать', command=create)
        txt.config(insertontime=500)


def edit():
    global mode

    if mode == 1:
        mode = 4
        answText.config(fg='Gray', text='Редактирование')
        btnAnsw.config(text='Сохранить', command=create)
        txt.config(insertontime=500)


def create():
    global newQues

    x = answer.get()
    xin = [1, 2, 3, 4]
    if mode == 2:
        if x in xin:
            nQueT = txt.get(1.0, END)
            nQueA = answer.get()

            nQue = Question(nQueT, nQueA)

            Quest.append(nQue)

            QueLblTXT = 'Вопросы ' + str(len(Quest))
            QueLbl.config(text=QueLblTXT)

            fileS = open('save.dat', 'wb')
            pickle.dump(Quest, fileS)
            fileS.close()

            messagebox.showinfo('Adobe Showinfo', 'Вопрос создан!')

    elif mode == 4:
        if x in xin:
            que.QText = txt.get(1.0, END)
            que.answ = answer.get()

            messagebox.showinfo('Adobe Showinfo', 'Вопрос изменен!')

            fileS = open('save.dat', 'wb')
            pickle.dump(Quest, fileS)
            fileS.close()


def delete():
    if mode == 1:
        Quest.remove(que)

        QueLblTXT = 'Вопросы ' + str(len(Quest))
        QueLbl.config(text=QueLblTXT)

        fileS = open('save.dat', 'wb')
        pickle.dump(Quest, fileS)
        fileS.close()

        quePrint()


def startMenu():
    global mode

    mode = 0

    startBut.pack(pady=20)
    combo.pack()


def restarti():
    global answered, score, answrd

    if mode == 2 or 1:
        if mode == 2 or 4:
            answText.config(fg='Gray', text='Начинаем!')
            btnAnsw.config(text='Проверить', command=check)
            txt.config(insertontime=0)

        answered = []
        score = 0
        answrd = 0
        resetAll()
        startMenu()


def resetAll():
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()

    rad1.pack_forget()
    rad2.pack_forget()
    rad3.pack_forget()
    rad4.pack_forget()

    txt.pack_forget()
    btnAnsw.pack_forget()
    answText.pack_forget()


# Параметры окна
window = Tk()
window.geometry('360x480')
window.title('Игра: Викторина!')
window.iconbitmap('icon.ico')
window.maxsize(360, 480)
window.wm_minsize(360, 480)

# Некоторые переменные
font = 18
answer = IntVar()
answered = []
score = 0
combo1 = 'Автопроверка'
combo2 = 'Проверка в конце'
combo3 = 'Режим отладки'
answrd = 0
mode = 0    # Режим игры. 0 - стартовое меню, 1 - игра, 2 - создание вопроса, 3 - Финальное меню, 4 - редактирование

# Задаём значение элементов
frame1 = Frame(window)
frame2 = Frame(window)
frame3 = Frame(window)

rad1 = Radiobutton(frame1, text='Вариант А', value=1, variable=answer, font=("Arial Bold", font))
rad2 = Radiobutton(frame1, text='Вариант Б', value=2, variable=answer, font=("Arial Bold", font))
rad3 = Radiobutton(frame2, text='Вариант В', value=3, variable=answer, font=("Arial Bold", font))
rad4 = Radiobutton(frame2, text='Вариант Г', value=4, variable=answer, font=("Arial Bold", font))

txt = Text(frame3, height=11, width=28, relief=FLAT, insertontime=0, font=("Arial", 15))

btnAnsw = Button(window, width=22, text='Проверить', font=("Arial Bold", font), bg='Gray', command=check)
startBut = Button(window, text='Нажми для начала!', font=("Arial Bold", font), width=16, height=8, bg='Red',
                  command=start)

returnBut = Button(window, text='Главное меню', bg='Green', fg='white', font=("Arial Bold", font), command=restart)

answText = Label(frame3, font=("Arial Bold", 14), fg='Gray', text='Начинаем!')
FinishLbl = Label(window)

combo = ttk.Combobox(window)
combo['values'] = (combo1, combo2, combo3)
combo.current(0)

menu = Menu(window)
new_item = Menu(menu, tearoff=0)
new_item.add_command(label='Новый вопрос', command=newQue)
new_item.add_command(label='Редактировать', command=edit)
new_item.add_command(label='Удалить вопрос', command=delete)
menu.add_cascade(label='Вопросы', menu=new_item)
menu.add_command(label='Главное меню', command=restarti)
menu.add_command(label='Выход', command=sys.exit)
window.config(menu=menu)

autorLbl = Label(window, text='©Kirill Litvinov 2022', font=("Arial", 10))
autorLbl.place(y=455, x=5)

startMenu()

# Вопросы
file = open('save.dat', 'rb')
Quest = pickle.load(file)
file.close()

QueLblTXT = 'Вопросы: ' + str(len(Quest))
QueLbl = Label(window, text=QueLblTXT, font=("Arial", 10))
QueLbl.place(y=455, x=355, anchor=NE)

window.mainloop()
