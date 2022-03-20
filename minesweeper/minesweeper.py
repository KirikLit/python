from tkinter import *
from tkinter import messagebox
from SweepEngine import *
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
        self.bombed = []
        self.frames = []
        self.colors = ['n', 'Blue', 'Green', 'Red', 'Darkgreen', 'Darkred', 'Black', 'Black']       # Цвета кнопок
        
        # Пустые переменные
        self.losegamev = False
        self.bombcount = None
        self.btnscount = None
        self.linelength = None
        self.fl = None
        
        # Стандартные значения
        self.bombcount2 = 10
        self.height2 = 9
        self.linelength2 = 9
        
        # Меню
        menu = Menu(self)
        newitem = Menu(menu, tearoff=0)
        newitem.add_command(label='Новичок', command=lambda: self.changegrid(9, 9, 10))
        newitem.add_command(label='Любитель', command=lambda: self.changegrid(16, 16, 40))
        newitem.add_command(label='Проффесионал', command=lambda: self.changegrid(16, 30, 80))
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
        self.btnscount = self.linelength2 * self.height2
        self.linelength = self.linelength2
        x = self.linelength
        self.fl = Field(self.linelength, self.height2)

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

            self.fl.set_class(y, MyButton, self, fr, y)
            x += 1

        # Создание бомб
        for bombs in range(self.bombcount):
            bomb = random.choice(self.fl.list_field)

            while bomb in self.bombed:
                bomb = random.choice(self.fl.list_field)

            bomb.mine = 1
            self.bombed.append(bomb)

        self.bombCNT = len(self.bombed)
        BombText = 'Бомб: ' + str(self.bombCNT)
        self.bomblbl.config(text=BombText)

        # Проверка бомб
        for btn in self.fl.list_field:
            btn.check()

    def wingame(self):
        x = 0

        for btn in self.fl.list_field:
            if btn.mine == 1 and btn.flag:
                x += 1

        if x == self.bombcount:
            for btn in self.fl.list_field:
                btn.pressed()
            msg = messagebox.askyesno('Победа', 'Вы выиграли!\nХотите сыграть ещё раз?')
            if msg:
                self.restartgame()
            else:
                self.destroy()

    def losegame(self):
        for btn in self.fl.list_field:
            btn.pressed()
        msg = messagebox.askyesno('Поражение', 'Вы проиграли!\nХотите сыграть ещё раз?')
        if msg:
            self.restartgame()
        else:
            self.destroy()

    def restartgame(self):
        for btn in self.fl.list_field:
            btn.btn.destroy()
        for frames in self.frames:
            frames.destroy()
        self.fl.list_field = []
        self.bombed = []
        self.frames = []

        self.frame.destroy()
        self.startgame()

    def changegrid(self, height, length, mines):
        self.bombcount2 = mines
        self.height2 = height
        self.linelength2 = length

        self.restartgame()

    def special(self):
        SpecialSize(self)


class MyButton:
    def __init__(self, appb, disp, index):
        self.mine = 0
        self.count = 0
        self.flag = False
        self.index = index
        self.app = appb
        self.opened = False

        self.btn = Button(disp, width=2, height=1, bg='Lightgray', command=self.pressed)
        self.btn.bind('<Button-3>', lambda e: self.pressed1(e))
        self.btn.pack(side=LEFT)

    def check(self):
        if self.mine == 1:
            return
        for met in self.app.fl.positions:
            slf = self.app.fl.get_near(met, self.index)
            if not slf:
                continue
            elif slf.mine == 1:
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
            for pos in self.app.fl.positions:
                slf = self.app.fl.get_near(pos, self.index)
                if not slf:
                    continue
                else:
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
        for posi in self.app.fl.positions:
            slf = self.app.fl.get_near(posi, self.index)

            if not slf:
                continue
            else:
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
                self.app.changegrid(x2, x1, x3)
                self.destroy()
            else:
                self.lblEr.config(text='Неправильный размер')
        else:
            self.lblEr.config(text='Много бомб')


if __name__ == '__main__':
    app = MainWindow()
