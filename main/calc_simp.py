from tkinter import *


class CalcWin(Tk):
    def __init__(self):
        super().__init__()
        self.title('Калькулятор')
        self.minsize(340, 155)
        self.maxsize(340, 155)
        self.config(bg='LightGray')

        XXX = 0
        CCC = 1

        for XX in range(0, 5):
            self.rowconfigure(XX, pad=5)
            self.columnconfigure(XX, pad=5)

        self.font = 'Segoe UI', 12
        btns = ['1', '2', '3', '+', '4', '5', '6', '-',
                '7', '8', '9', '*', 'C', '0', '=', '/']

        self.entry = Entry(self, font=self.font, takefocus=True, width=36)
        self.entry.grid(row=0, column=0, columnspan=4)

        for btn in btns:
            x = Button(self, text=btn, command=lambda z=btn: self.pressed(z), width=10)

            if XXX == 4:
                XXX = 0
                CCC += 1

            x.grid(row=CCC, column=XXX)
            XXX += 1

        self.mainloop()

    def pressed(self, x):
        divs = ['+', '-', '*', '/']

        if x == 'C':
            self.entry.delete(0, END)
        elif x == '=':
            res = eval(self.entry.get())
            self.entry.delete(0, END)
            self.entry.insert(0, res)
        else:
            self.entry.insert(END, x)


if __name__ == '__main__':
    app = CalcWin()
