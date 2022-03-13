from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter.ttk as ttk
import random


class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.bombCNT = None
        self.title('Minesweeper')
        self.config(bg='Lightgray')
        self.resizable(False, False)
        self.iconbitmap('minecon.ico')

        # Загрузка изображений
        flagO = Image.open('flag.png')
        self.flag = ImageTk.PhotoImage(flagO.resize((20, 20)))
        
        # Списки
        self.btns = []
        self.bombed = []
        self.frames = []
        self.excl = []
        self.excl2 = []
        self.colors = ['n', 'Blue', 'Green', 'Red', 'Darkgreen', 'Darkred', 'Black', 'Black']       # Цвета кнопок
        
        # Пустые переменные
        self.losegamev = False
        self.bombcount = None
        self.btnscount = None
        self.linelength = None
        
        # Стандартные значения
        self.bombcount2 = 80
        self.btnscount2 = 480
        self.linelength2 = 30
        
        # Меню
        menu = Menu(self)
        newitem = Menu(menu, tearoff=0)
        newitem.add_command(label='Новичок', command=lambda: self.changegrid(81, 9, 10))
        newitem.add_command(label='Любитель', command=lambda: self.changegrid(256, 16, 40))
        newitem.add_command(label='Проффесионал', command=lambda: self.changegrid(480, 30, 80))
        newitem.add_separator()
        newitem.add_command(label='Свой размер', command=self.special)
        menu.add_command(label='Новая игра', command=self.restartgame)
        menu.add_cascade(label='Сложность', menu=newitem)
        self.config(menu=menu)
        
        # Индикатор бомб
        self.bomblbl = Label(self, font=('Segoe UI', 15), bg='lightgray')
        self.bomblbl.pack(pady=5)
        
        # Старт игры
        self.startgame()
        self.mainloop()

    def startgame(self):
        # Создание кнопок
        self.losegamev = False
        self.bombcount = self.bombcount2
        self.btnscount = self.btnscount2
        self.linelength = self.linelength2
        x = self.linelength

        self.excl = []
        self.excl2 = []
        tvar = self.linelength
        tvar2 = self.linelength

        self.frame = Frame(self)
        self.frame.pack(fill=BOTH, padx=20, pady=20)

        for y in range(self.btnscount):
            if x == self.linelength:
                fr = Frame(self.frame)
                fr.pack(fill=X)

                self.frames.append(fr)
                x = 0

            btn = MyButton(self, 0, 0, False, fr, y)
            x += 1

            self.btns.append(btn)

        # Создание бомб
        for bombs in range(self.bombcount):
            bomb = random.choice(self.btns)

            while bomb in self.bombed:
                bomb = random.choice(self.btns)

            bomb.mine = 1
            self.bombed.append(bomb)

        self.bombCNT = len(self.bombed)
        BombText = 'Бомб: ' + str(self.bombCNT)
        self.bomblbl.config(text=BombText)

        # Создание нужных списков
        for x in range(self.linelength - 1, self.btnscount):
            if tvar == self.linelength:
                self.excl.append(x)
                tvar = 0
            tvar += 1

        for x in range(0, self.btnscount):
            if tvar2 == self.linelength:
                self.excl2.append(x)
                tvar2 = 0
            tvar2 += 1

        # Проверка бомб
        for btn in self.btns:
            btn.check(self)

    def wingame(self):
        x = 0

        for btn in self.btns:
            if btn.mine == 1 and btn.flag:
                x += 1

        if x == self.bombcount:
            for btn in self.btns:
                btn.pressed()
            msg = messagebox.askyesno('Победа', 'Вы выиграли!\nХотите сыграть ещё раз?')
            if msg:
                self.restartgame()
            else:
                self.destroy()

    def losegame(self):
        for btn in self.btns:
            btn.pressed()
        msg = messagebox.askyesno('Поражение', 'Вы проиграли!\nХотите сыграть ещё раз?')
        if msg:
            self.restartgame()
        else:
            self.destroy()

    def restartgame(self):
        for btn in self.btns:
            btn.btn.destroy()
        for frames in self.frames:
            frames.destroy()
        self.btns = []
        self.bombed = []
        self.frames = []

        self.frame.destroy()
        self.startgame()

    def changegrid(self, btns, length, mines):
        self.bombcount2 = mines
        self.btnscount2 = btns
        self.linelength2 = length

        self.restartgame()

    def special(self):
        SpecialSize(self)


class MyButton:
    def __init__(self, appb, mine, count, flag, disp, index):
        self.mine = mine
        self.count = count
        self.flag = flag
        self.index = index
        self.app = appb
        self.opened = False

        index = self.index
        self.pos = [index - (self.app.linelength - 1), index - self.app.linelength, index - (self.app.linelength + 1),
                    index + 1, index - 1, index + self.app.linelength, index + (self.app.linelength + 1),
                    index + (self.app.linelength - 1)]

        self.btn = Button(disp, width=2, height=1, bg='Lightgray', command=self.pressed)
        self.btn.bind('<Button-3>', lambda e: self.pressed1(e))
        self.btn.pack(side=LEFT)

    def check(self, appch):
        index = self.index

        if self.mine == 1:
            return
        for posi in self.pos:
            oper = self.pos.index(posi)
            if self.checking(index, oper):
                slf = appch.btns[posi]
                if slf.mine == 1:
                    self.count += 1

    def pressed(self):
        if not self.opened:
            if self.app.losegamev or not self.flag:
                if self.mine == 1:
                    self.btn.config(relief=SUNKEN, text='BB', fg='Darkred', bg='Red', font=('Times Bold', 9))
                    if not self.app.losegamev:
                        self.app.bomblbl.config(text='Вы проиграли!')
                        self.app.losegamev = True
                        self.app.losegame()
                elif self.flag:
                    self.btn.config(relief=SUNKEN, state=DISABLED)
                elif self.count == 0:
                    self.btn.config(relief=SUNKEN, text='', fg='Blue', bg='White', font=('Times Bold', 9),
                                    image='', width=2, height=1)
                    if not self.app.losegamev:
                        self.open()
                else:
                    self.btn.config(relief=SUNKEN, text=self.count, fg=self.app.colors[self.count],  bg='White',
                                    font=('Times Bold', 9), image='', width=2, height=1)
                self.opened = True
        else:
            for pos in self.pos:
                oper = self.pos.index(pos)
                if self.checking(self.index, oper):
                    slf = self.app.btns[pos]
                    if not slf.opened:
                        slf.pressed()
                        if slf.mine == 1 and not slf.flag:
                            break

    def pressed1(self, event):
        if not self.opened:
            if self.flag:
                self.btn.config(image='', width=2, height=1)

                self.app.bombCNT += 1
                BombText = 'Бомб: ' + str(self.app.bombCNT)
                self.app.bomblbl.config(text=BombText)

                self.flag = False
            elif not self.flag and self.app.bombCNT > -1:
                self.btn.config(image=self.app.flag, width=18, height=20)

                self.app.bombCNT -= 1
                BombText = 'Бомб: ' + str(self.app.bombCNT)
                self.app.bomblbl.config(text=BombText)

                self.flag = True
            if self.app.bombCNT == 0:
                self.app.wingame()

    def open(self):
        for posi in self.pos:
            oper = self.pos.index(posi)

            if self.checking(self.index, oper):
                slf = self.app.btns[posi]
                if not slf.opened:
                    if slf.mine == 1:
                        pass
                    elif slf.count == 0:
                        slf.btn.config(relief=SUNKEN, text='', fg='Blue', font=('Times Bold', 9), bg='White')
                        slf.opened = True
                        slf.open()
                    else:
                        slf.btn.config(relief=SUNKEN, text=slf.count, fg=self.app.colors[slf.count],
                                       font=('Times Bold', 9), bg='White')
                        slf.opened = True

    def checking(self, index, oper):
        operation = [index > (self.app.linelength - 1), index > self.app.linelength,
                     index < (self.app.btnscount - self.app.linelength)]

        if oper == 0 and index not in self.app.excl:
            if operation[0]:
                return True
        elif oper == 1 and operation[0]:
            return True
        elif oper == 2 and index not in self.app.excl2:
            if operation[1]:
                return True
        elif oper == 3 and index not in self.app.excl:
            return True
        elif oper == 4 and index not in self.app.excl2:
            return True
        elif oper == 5 and operation[2]:
            return True
        elif oper == 6 and index not in self.app.excl:
            if operation[2]:
                return True
            else:
                return False
        elif oper == 7 and index not in self.app.excl2:
            if operation[2]:
                return True
            else:
                return False
        else:
            return False


class SpecialSize(Toplevel):
    def __init__(self, appm):
        super().__init__()
        self.title('Изменение размера')
        self.resizable(False, False)
        self.app = appm
        self.iconbitmap('minecon.ico')

        fr0 = Frame(self)
        fr0.pack(pady=10, padx=10, expand=True)

        fr1 = Frame(fr0)
        fr2 = Frame(fr0)
        fr3 = Frame(fr0)

        lbl1 = Label(fr1, font=('Segoe UI', 12), text='Ширина:')
        lbl2 = Label(fr2, font=('Segoe UI', 12), text='Высота:')
        lbl3 = Label(fr3, font=('Segoe UI', 12), text='Мины:')
        ttk.Style().configure('TButton')
        self.lblEr = Label(self, font=('Segoe UI', 12), text='', fg='Red')
        entBut = ttk.Button(self, text='OK', command=lambda: self.enter('e'))
        self.bind('<Return>', self.enter)

        self.entry1 = ttk.Entry(fr1, width=15, font=('Segoe UI', 12))
        self.entry2 = ttk.Entry(fr2, width=15, font=('Segoe UI', 12))
        self.entry3 = ttk.Entry(fr3, width=15, font=('Segoe UI', 12))

        fr1.pack(fill=X, expand=True)
        lbl1.pack(side=LEFT)
        self.entry1.pack(side=RIGHT)

        fr2.pack(fill=X, pady=10, expand=True)
        lbl2.pack(side=LEFT)
        self.entry2.pack(side=RIGHT)

        fr3.pack(fill=X, expand=True)
        lbl3.pack(side=LEFT)
        self.entry3.pack(side=RIGHT)
        
        entBut.pack(side=RIGHT, padx=5, pady=5)
        self.lblEr.pack(side=LEFT, padx=5, pady=5)

    def enter(self, event):
        x1 = int(self.entry1.get())
        x2 = int(self.entry2.get())
        x3 = int(self.entry3.get())

        if (x1 * x2) > x3:
            if x1 > 2 and x2 < 40:
                self.app.changegrid((x1 * x2), x1, x3)
                self.destroy()
            else:
                self.lblEr.config(text='Неправильный размер')
        else:
            self.lblEr.config(text='Много бомб')


if __name__ == '__main__':
    app = MainWindow()
