from tkinter import *


class CalcWin(Tk):
    def __init__(self):
        super().__init__()
        self.title('Калькулятор')
        self.config(bg='LightGray')

        XXX = 0
        CCC = 2
        btns = ['1', '2', '3', '+', '4', '5', '6', '-',
                '7', '8', '9', '*', '0', '.', '/', '=', 'C', '√']

        self.inti = '0'
        self.disp = '0'
        self.oper = False
        self.doubleop = False
        self.lastoper = None
        self.lastdigit = None
        self.font = 'Segoe UI', 12

        for XX in range(0, 7):
            self.rowconfigure(XX, pad=5)
            self.columnconfigure(XX, pad=5)

        self.entry = Entry(self, font=self.font, width=36)
        self.entry2 = Entry(self, font=self.font, takefocus=True, width=36)
        self.entry.grid(row=0, column=0, columnspan=4)
        self.entry2.grid(row=1, column=0, columnspan=4)
        self.entry.insert(0, '0')
        self.entry2.insert(0, '0')

        for btn in btns:
            x = Button(self, text=btn, command=lambda z=btn: self.pressed(z), width=10, height=2)
            extrbtn = ['=', '0']

            if XXX == 4:
                XXX = 0
                CCC += 1

            if btn in extrbtn:
                x.config(width=22)
                x.grid(row=CCC, column=XXX, columnspan=2)
                XXX += 2
            else:
                x.grid(row=CCC, column=XXX)
                XXX += 1

        self.mainloop()

    def pressed(self, x):
        divs = ['+', '-', '*', '/']

        if x == 'C':
            self.inti = '0'
            self.print(self.entry2, '0')
        elif x == '=':
            if self.oper:
                if self.doubleop:
                    self.inti += self.lastoper
                self.inti += self.lastdigit
                self.doubleop = True
            res = eval(self.inti)
            self.print(self.entry2, str(res))
            self.inti = str(res)
            self.oper = True
            self.doubleop = True
        elif x == '√':
            sqrt = float(self.entry2.get()) ** 0.5
            self.print(self.entry2, str(sqrt))
            self.inti = str(sqrt)
        elif x in divs:
            self.doubleop = False
            self.oper = True
            res = eval(self.inti)
            self.print(self.entry2, res)
            self.inti = str(res)
            self.lastoper = x
            self.inti += x
        else:
            if self.oper:
                self.oper = False
                self.entry2.delete(0, END)
                if self.doubleop: self.inti = '0'
            if self.inti == '0':
                self.inti = x
                self.print(self.entry2, x)
            else:
                self.inti += x
                self.entry2.insert(END, x)
            self.lastdigit = self.entry2.get()
        self.print(self.entry, self.inti)
        print(self.inti)

    def print(self, entry, text):
        entry.delete(0, END)
        entry.insert(0, text)


if __name__ == '__main__':
    app = CalcWin()
