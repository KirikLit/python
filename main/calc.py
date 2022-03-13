from tkinter import *
import tkinter.ttk as ttk


class CalcWin(Tk):
    def __init__(self):
        super().__init__()
        self.title('Калькулятор')
        self.config(bg='LightGray')
        self.iconbitmap('icon2.ico')

        ttk.Style().configure('TButton', width=6, font=('Segoe UI', 18))
        ttk.Style().configure('Extr.TButton', width=13, font=('Segoe UI', 18))
        ttk.Style().configure('TEntry')
        ttk.Style().map('TEntry', foreground=[('disabled', 'black')], background=[('disabled', 'white')])

        XXX = 4
        btns = ['1', '2', '3', '+', '4', '5', '6', '-',
                '7', '8', '9', '*', '0', '.', '/', '=', 'C', '√']

        self.inti = '0'
        self.disp = '0'
        self.oper = False
        self.doubleop = False
        self.lastoper = None
        self.lastdigit = None
        self.font = 'Segoe UI', 12

        fr1 = Frame(self)
        fr2 = Frame(self)

        self.entry = ttk.Entry(fr1, font=('Segoe UI', 20))
        self.entry2 = ttk.Entry(fr2, font=('Segoe UI', 20))

        fr1.pack(fill=X)
        self.entry.pack(fill=X, padx=6, pady=6)
        fr2.pack(fill=X)
        self.entry2.pack(fill=X, padx=6, pady=6)

        self.entry.insert(0, '0')
        self.entry2.insert(0, '0')

        self.entry.config(state=DISABLED)
        self.entry2.config(state=DISABLED)

        for btn in btns:
            extrbtn = ['=', '0']

            if XXX == 4:
                XXX = 0
                fr = Frame(self)
                fr.pack(fill=BOTH, expand=True)

            if btn in extrbtn:
                if btn == '=':
                    self.bind('<Return>', lambda e, z=btn: self.pressed(e, z))
                else:
                    self.bind(str(btn), lambda e, z=btn: self.pressed(e, z))

                x = ttk.Button(fr, text=btn, command=lambda z=btn: self.pressed('e', z), style='Extr.TButton')
                XXX += 2
            else:
                if btn != '√':
                    self.bind(str(btn), lambda e, z=btn: self.pressed(e, z))
                    
                x = ttk.Button(fr, text=btn, command=lambda z=btn: self.pressed('e', z))
                XXX += 1
            x.pack(side=LEFT, pady=3, padx=3, fill=BOTH, expand=TRUE)

        self.mainloop()

    def pressed(self, event, x):
        divs = ['+', '-', '*', '/']

        if x == 'C':
            self.inti = '0'
            self.printi(self.entry2, '0')
            self.lastdigit = '0'
        elif x == '=':
            if self.oper:
                if self.doubleop:
                    self.inti += self.lastoper
                self.inti += self.lastdigit
                self.doubleop = True
            res = eval(self.inti)
            self.printi(self.entry2, str(res))
            self.inti = str(res)
            self.oper = True
            self.doubleop = True
        elif x == '√':
            sqrt = float(self.entry2.get()) ** 0.5
            self.printi(self.entry2, str(sqrt))
            self.inti = str(sqrt)
        elif x in divs:
            self.doubleop = False
            self.oper = True
            res = eval(self.inti)
            self.printi(self.entry2, res)
            self.inti = str(res)
            self.lastoper = x
            self.inti += x
        else:
            if self.oper:
                self.oper = False
                self.entry2.delete(0, END)
                if self.doubleop:
                    self.inti = '0'
                    self.lastdigit = '0'
            if self.inti == '0':
                self.inti = x
                self.printi(self.entry2, x)
            else:
                self.inti += x
                self.entry2.config(state=NORMAL)
                self.entry2.insert(END, x)
                self.entry2.config(state=DISABLED)
            self.lastdigit = self.entry2.get()
        self.printi(self.entry, self.inti)
        print(self.inti)

    def printi(self, entry, text):
        entry.config(state=NORMAL)
        entry.delete(0, END)
        entry.insert(0, text)
        entry.config(state=DISABLED)


if __name__ == '__main__':
    app = CalcWin()
