from tkinter import *
import tkinter.ttk as ttk


class MarkCalc(Tk):
    def __init__(self):
        super().__init__()
        self.title('Калькулятор среднего балла')
        self.geometry('380x570')
        self.iconbitmap('icon2.ico')
        self.marks = []

        # Label
        label = Label(self, font=('Segoe UI', 18), text='Выбирай оценки')
        label.pack(pady=5)

        # buttons
        ttk.Style().configure('TButton', font=('Segoe UI', 16))
        buttons_frame = Frame(self)
        buttons_frame.pack(fill=X, pady=5)
        temp = 2
        buttons = ['5', '4', '3', '2', 'Убрать', 'Очистить']
        for btn in buttons:
            if temp == 2:
                fr = Frame(buttons_frame)
                fr.pack(fill=X)
                temp = 0

            button = ttk.Button(fr, text=btn, width=14, command=lambda b=btn: self.calculate(b))
            if temp == 0:
                button.pack(side=LEFT, fill=X, expand=True, padx=12, pady=6, ipady=3)
            elif temp == 1:
                button.pack(side=RIGHT, fill=X, expand=True, padx=12, pady=6, ipady=3)
            temp += 1

        # define elements
        text_frame = Frame(self)
        self.text = Text(text_frame, font=('Segoe UI', 16), state=DISABLED)

        # pack elements
        text_frame.pack(fill=X, padx=15, pady=10)
        self.text.pack(fill=X)

        self.mainloop()

    def calculate(self, button):
        if button == 'Убрать':
            self.clear(False)
        elif button == 'Очистить':
            self.clear(True)
        else:
            self.marks.append(button)
            self.print_res()

    def clear(self, del_all):
        if del_all:
            self.marks = []
        else:
            self.marks.pop()
        self.print_res()

    def print_res(self):
        self.text.config(state=NORMAL)
        self.text.delete(1.0, END)
        f = lambda: 'Нет' if len(self.marks) == 0 else round(eval('+'.join(self.marks)) / len(self.marks), 2)
        result = f()
        marks = ', '.join(self.marks)
        answer = f'Ваши оценки {marks}\n\nСредний балл: {result}'
        self.text.insert(1.0, answer)
        self.text.config(state=DISABLED)


if __name__ == '__main__':
    GG = MarkCalc()
