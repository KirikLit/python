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


class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        # Параметры окна
        self.geometry('360x500')
        self.minsize(360, 500)
        self.title('Игра: Викторина!')
        self.iconbitmap('icon.ico')

        # Некоторые переменные
        self.Quest = []
        self.que = None
        self.lastcombo = None
        self.answer = IntVar()
        self.answered = []
        self.score = 0
        self.combo1 = 'Автопроверка'
        self.combo2 = 'Проверка в конце'
        self.combo3 = 'Режим отладки'
        self.answrd = 0
        self.mode = 0  # Режимы: 0 - стартовое меню, 1 - игра, 2 - создание вопроса, 3 - Финальное меню, 4 - редакт.

        # Styles
        st = ttk.Style()
        st.configure('TButton', font=('Segoe UI', 16))
        st.configure('start.TButton', font=('Segoe UI', 20))
        st.map('answ.TButton',
               background=[('active', 'lightgray'), ('!active', 'gray')])
        st.map('start.TButton',
               background=[('active', 'white'), ('!active', 'red')],
               foreground=[('active', 'darkred'), ('!active', 'red')])
        st.map('rest.TButton',
               background=[('!active', 'green')],
               foreground=[('!active', 'green'), ('active', 'darkgreen')])
        st.configure('rest.TButton')
        st.configure('TRadiobutton', font=('Segoe UI', 18))

        # Frames
        self.fr1 = Frame(self)
        self.fr2 = Frame(self)
        self.fr3 = Frame(self)
        self.fr4 = Frame(self)
        self.fr5 = Frame(self)
        self.fr6 = Frame(self)

        # Elements
        self.rad1 = ttk.Radiobutton(self.fr1, text='Вариант А', value=1, variable=self.answer)
        self.rad2 = ttk.Radiobutton(self.fr1, text='Вариант Б', value=2, variable=self.answer)
        self.rad3 = ttk.Radiobutton(self.fr2, text='Вариант В', value=3, variable=self.answer)
        self.rad4 = ttk.Radiobutton(self.fr2, text='Вариант Г', value=4, variable=self.answer)

        self.txt = Text(self.fr3, height=11, font=('Segoe', 16))
        self.btnAnsw = ttk.Button(self.fr4, style='answ.TButton', text='Проверить', command=self.check)
        self.startBut = ttk.Button(self.fr6, style='start.TButton', text='Нажми для начала!', command=self.start)
        self.returnBut = ttk.Button(self, style='rest.TButton', text='Главное меню', command=self.restart, width=24)
        self.answText = Label(self.fr4, font=("Arial Bold", 14), fg='Gray', text='Начинаем!')
        self.FinishLbl = Label(self)
        self.autorLbl = Label(self.fr5, text='©Kirill Litvinov 2022', font=('Segoe UI', 10))

        self.combo = ttk.Combobox(self.fr6, font=('Segoe UI', 12))
        self.combo['values'] = (self.combo1, self.combo2, self.combo3)
        self.combo.current(0)

        # Menu
        menu = Menu(self)
        new_item = Menu(menu, tearoff=0)
        new_item.add_command(label='Новый вопрос', command=self.new_que)
        new_item.add_command(label='Редактировать', command=self.edit)
        new_item.add_command(label='Удалить вопрос', command=self.delete)
        menu.add_cascade(label='Вопросы', menu=new_item)
        menu.add_command(label='Главное меню', command=self.restarti)
        menu.add_command(label='Выход', command=sys.exit)
        self.config(menu=menu)

        # Questions
        self.save('Load')

        self.QueLblTXT = 'Вопросы %i' % len(self.Quest)
        self.QueLbl = Label(self.fr5, text=self.QueLblTXT, font=('Segoe UI', 10))

        self.start_menu()
        self.mainloop()

    def start_menu(self):
        self.mode = 0

        self.fr6.pack(fill=BOTH, pady=100)
        self.startBut.pack(fill=X, ipady=80, pady=5, padx=30)
        self.combo.pack()

        self.fr5.pack(fill=X, side=BOTTOM)
        self.autorLbl.pack(side=LEFT, padx=5)
        self.QueLbl.pack(side=RIGHT, padx=5)

    def start(self):
        self.mode = 1
        com = self.combo.get()

        if com == self.combo3:
            self.answText.config(text='Режим отладки', fg='Gray')
            self.btnAnsw.config(text='Далее')
        else:
            self.answText.config(text='Начинаем!', fg='Gray')
            self.btnAnsw.config(text='Проверить')

        self.fr5.pack_forget()
        self.fr6.pack_forget()

        self.combo.pack_forget()
        self.startBut.pack_forget()
        self.autorLbl.pack_forget()
        self.QueLbl.pack_forget()

        self.main_frame()
        self.que_print()

    def main_frame(self):
        self.fr1.pack(fill=X)
        self.rad1.pack(side=LEFT, pady=5, padx=20)
        self.rad2.pack(side=RIGHT, padx=20)

        self.fr2.pack(fill=X)
        self.rad3.pack(side=LEFT, pady=5, padx=20)
        self.rad4.pack(side=RIGHT, padx=20)

        self.fr3.pack(fill=BOTH, expand=True)
        self.txt.pack(expand=True, padx=20, fill=BOTH)
        
        self.fr4.pack(fill=X)
        self.answText.pack(pady=5)
        self.btnAnsw.pack(fill=X, padx=20, ipady=5)

        self.fr5.pack(fill=X, side=BOTTOM, pady=5)
        self.autorLbl.pack(side=LEFT, padx=5)
        self.QueLbl.pack(side=RIGHT, padx=5)

    def que_print(self):
        if len(self.Quest) == len(self.answered):
            self.Vexit()
            self.mode = 3
        else:
            self.que = random.choice(self.Quest)

            while self.que in self.answered:
                self.que = random.choice(self.Quest)

            self.txt.config(state=NORMAL)
            self.txt.delete(1.0, END)
            self.txt.insert(0.0, self.que.QText)
            self.txt.config(state=DISABLED)
            print(self.que.answ)

    def check(self):
        x = self.answer.get()
        com = self.combo.get()
        self.answer.set(0)

        if com == self.combo1:
            if x == self.que.answ:
                self.answText.config(fg='green', text='Молодец!', font=("Arial Bold", 14))
                self.answered.append(self.que)
                self.score += 20
                self.que_print()
            else:
                self.answText.config(fg='red', text='Неправильный ответ!', font=("Arial Bold", 14))
                self.score -= 10
        elif com == self.combo2:
            if x == self.que.answ:
                self.answrd += 1
                self.answered.append(self.que)
                self.que_print()
            else:
                self.answered.append(self.que)
                self.que_print()
        else:
            self.answered.append(self.que)
            self.que_print()

    def new_que(self):
        if self.mode == 1 or self.mode == 3:
            if self.mode == 3:
                self.FinishLbl.pack_forget()
                self.returnBut.pack_forget()
                self.main_frame()

            self.mode = 2
            self.answText.config(fg='Gray', text='Создание вопроса')
            self.txt.config(insertontime=500, state=NORMAL)
            self.txt.delete(1.0, END)
            self.btnAnsw.config(text='Создать', command=self.create)

    def edit(self):
        if self.mode == 1:
            self.lastcombo = self.combo.get()
            self.mode = 4
            self.answText.config(fg='Gray', text='Редактирование')
            self.btnAnsw.config(text='Сохранить', command=self.create)
            self.txt.config(insertontime=500, state=NORMAL)

    def create(self):
        x = self.answer.get()
        self.answer.set(0)
        xin = [1, 2, 3, 4]
        if self.mode == 2:
            if x in xin:
                nQueT = self.txt.get(1.0, END)
                nQueA = x
                nQue = Question(nQueT, nQueA)

                self.Quest.append(nQue)
                QueLblTXT = 'Вопросы %i' % len(self.Quest)
                self.QueLbl.config(text=QueLblTXT)
                self.save('Save')

                messagebox.showinfo('Adobe Showinfo', 'Вопрос создан!')
            else:
                self.answText.config(text='Выберите ответ!')

        elif self.mode == 4:
            if x in xin:
                self.que.QText = self.txt.get(1.0, END)
                self.que.answ = x
                self.save('Save')
                messagebox.showinfo('Adobe Showinfo', 'Вопрос изменен!')

                if self.lastcombo == self.combo1 or self.lastcombo == self.combo2:
                    self.btnAnsw.config(text='Проверить', command=self.check)
                    self.answText.config(text='Начинаем!', fg='Gray')
                elif self.lastcombo == self.combo3:
                    self.btnAnsw.config(text='Далее', command=self.check)
                    self.answText.config(text='Режим отладки', fg='Gray')
                self.mode = 1
            else:
                self.answText.config(text='Выберите ответ!')

    def delete(self):
        if self.mode == 1:
            self.Quest.remove(self.que)
            QueLblTXT = 'Вопросы %i' % len(self.Quest)
            self.QueLbl.config(text=QueLblTXT)
            self.save('Save')

            self.que_print()

    def Vexit(self):
        self.reset_all()
        com = self.combo.get()

        if len(self.Quest) == 0:
            self.FinishLbl.config(font=("Arial Bold", 20), text='Вопросов нет\nСоздай их!\nВопросы -> Создать')
        elif com == self.combo1:
            self.FinishLbl.config(font=("Arial Bold", 20), text='Ты прошёл викторину!\nТвой счёт: %i' % self.score)
        elif com == self.combo2:
            self.FinishLbl.config(font=("Arial Bold", 20), text='Ты прошёл викторину!\nТы ответил на\n%i'
                                                                ' вопроса(-ов) из %i' % (self.answrd, len(self.Quest)))
        else:
            self.FinishLbl.config(font=("Arial Bold", 20), text='Ты прошёл виктоину\nВ режиме отладки')

        self.FinishLbl.pack(fill=X, pady=100, padx=20)
        self.returnBut.pack(fill=X, padx=30)
        self.fr5.pack(fill=X, side=BOTTOM, pady=5)
        self.autorLbl.pack(side=LEFT, padx=5)
        self.QueLbl.pack(side=RIGHT, padx=5)

    def restart(self):
        self.fr5.pack_forget()
        self.FinishLbl.pack_forget()
        self.returnBut.pack_forget()
        self.autorLbl.pack_forget()
        self.QueLbl.pack_forget()
        self.answText.config(fg='Gray', text='Начинаем!')

        self.answered = []
        self.score = 0
        self.answrd = 0

        self.start_menu()

    def restarti(self):
        if self.mode == 2 or 1:
            if self.mode == 2 or 4:
                self.answText.config(fg='Gray', text='Начинаем!')
                self.btnAnsw.config(text='Проверить', command=self.check)
                self.txt.config(insertontime=0)

            self.answered = []
            self.score = 0
            self.answrd = 0
            self.reset_all()
            self.start_menu()

    def reset_all(self):
        self.fr1.pack_forget()
        self.fr2.pack_forget()
        self.fr3.pack_forget()
        self.fr4.pack_forget()
        self.fr5.pack_forget()

        self.rad1.pack_forget()
        self.rad2.pack_forget()
        self.rad3.pack_forget()
        self.rad4.pack_forget()

        self.txt.pack_forget()
        self.btnAnsw.pack_forget()
        self.answText.pack_forget()
        self.autorLbl.pack_forget()
        self.QueLbl.pack_forget()

    def save(self, method):
        file = None
        if method == 'Save':
            file = open('save.dat', 'wb')
            pickle.dump(self.Quest, file)
        elif method == 'Load':
            file = open('save.dat', 'rb')
            self.Quest = pickle.load(file)
        file.close()


if __name__ == '__main__':
    GG = MainWindow()
