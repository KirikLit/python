from tkinter import *
from PIL import Image, ImageTk
import random


class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title('Minesweeper')
        self.config(bg='Lightgray')

        # Загрузка изображений
        flagO = Image.open('minesweeper flag.png')
        self.flag = ImageTk.PhotoImage(flagO.resize((20, 20)))

        self.btns = []
        self.bombed = []
        self.frame = Frame(self)
        self.frame.pack(fill=BOTH, padx=20, pady=20)

        x = 20

        # Создание кнопок
        for y in range(400):
            if x == 20:
                fr = Frame(self.frame)
                fr.pack(fill=X)
                x = 0
            btn = MyButton(self, 0, 0, False, fr, 0)
            x += 1
            self.btns.append(btn)
            btn.index = self.btns.index(btn)

        # Создание бомб
        for bombs in range(45):
            bomb = random.choice(self.btns)
            while bomb in self.bombed:
                bomb = random.choice(self.btns)
            bomb.mine = 1
            self.bombed.append(bomb)

        # Проверка бомб
        for btn in self.btns:
            btn.check()

        self.mainloop()

    def pressed(self, event, slf, btn):
        if slf.mine == 1:
            slf.btn.config(relief=SUNKEN, state=DISABLED, text='BB', fg='Red', bg='Red', font=('Times Bold', 9))
        elif slf.count == 0:
            slf.btn.config(relief=SUNKEN, state=DISABLED, text='', fg='Blue', font=('Times Bold', 9), bg='White')
            slf.open(self, slf.btn)
        else:
            slf.btn.config(relief=SUNKEN, state=DISABLED, text=slf.count, fg='Blue', font=('Times Bold', 9), bg='White')
        slf.btn.unbind('<Button-1>')
        slf.btn.unbind('<Button-3>')

    def pressed1(self, event, slf, btnn):
        if slf.flag:
            slf.btn.config(image='', width=2, height=1)
            slf.btn.bind('<Button-1>', lambda e, f=slf, btn=slf.btn: self.pressed(e, f, btn))
            slf.flag = False
        else:
            slf.btn.config(image=self.flag, width=18, height=20)
            slf.btn.unbind('<Button-1>')
            slf.flag = True


class MyButton:
    def __init__(self, app, mine, count, flag, disp, index):
        self.mine = mine
        self.count = count
        self.flag = flag
        self.index = index
        self.app = app
        self.opened = None

        self.excl = []
        self.excl2 = []
        tvar = 20
        tvar2 = 20

        for x in range(19, 400):
            if tvar == 20:
                self.excl.append(x)
                tvar = 0
            tvar += 1

        for x in range(0, 400):
            if tvar2 == 20:
                self.excl2.append(x)
                tvar2 = 0
            tvar2 += 1

        self.btn = Button(disp, width=2, height=1, bg='Lightgray')
        self.btn.bind('<Button-1>', lambda e, f=self, btn=self.btn: self.app.pressed(e, f, self.btn))
        self.btn.bind('<Button-3>', lambda e, obj=self, f=self.btn: self.app.pressed1(e, obj, f))
        self.btn.pack(side=LEFT)

    def check(self):
        if self.mine == 1:
            return

        if self.index > 19:
            if self.app.btns[self.index - 20].mine == 1:
                self.count += 1
        if self.index < 380:
            if self.app.btns[self.index + 20].mine == 1:
                self.count += 1
        if self.index not in self.excl:
            if self.index > 19:
                if self.app.btns[self.index - 19].mine == 1:
                    self.count += 1
            if self.index < 379:
                if self.app.btns[self.index + 21].mine == 1:
                    self.count += 1
            if self.app.btns[self.index + 1].mine == 1:
                self.count += 1
        if self.index not in self.excl2:
            if self.index > 20:
                if self.app.btns[self.index - 21].mine == 1:
                    self.count += 1
            if self.index < 380:
                if self.app.btns[self.index + 19].mine == 1:
                    self.count += 1
            if self.app.btns[self.index - 1].mine == 1:
                self.count += 1

    def open(self, app, btn):
        index = self.index
        pos = [index - 19, index - 20, index - 21, index + 1, index - 1, index + 20, index + 21, index + 19]
        for posi in pos:
            oper = pos.index(posi)

            if self.checking(index, oper):
                slf = app.btns[posi]
                if not slf.opened:
                    if slf.mine == 1:
                        pass
                    elif slf.count == 0:
                        slf.btn.config(relief=SUNKEN, state=DISABLED, text='', fg='Blue', font=('Times Bold', 9),
                                       bg='White')
                        slf.opened = True
                        slf.open(app, btn)
                    else:
                        slf.btn.config(relief=SUNKEN, state=DISABLED, text=slf.count, fg='Blue', font=('Times Bold', 9),
                                       bg='White')
                    slf.btn.unbind('<Button-1>')
                    slf.btn.unbind('<Button-3>')

    def checking(self, index, oper):
        operation = [index > 19, index > 20, index < 380]

        if oper == 0:
            if index not in self.excl:
                if operation[0]:
                    return True
        elif oper == 1:
            if operation[0]:
                return True
        elif oper == 2:
            if operation[1]:
                return True
        elif oper == 3:
            if index not in self.excl:
                return True
        elif oper == 4:
            if index not in self.excl2:
                return True
        elif oper == 5:
            if operation[2]:
                return True
        elif oper == 7:
            if operation[2]:
                return True
        elif oper == 6:
            if index not in self.excl:
                if index < 189:
                    return True
        else:
            return False


if __name__ == '__main__':
    app = MainWindow()
