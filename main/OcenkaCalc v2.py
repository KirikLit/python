from tkinter import *

font = 18
pad = 20
numbers = []


class Btn:
    def __init__(self, frame, text, command, width=10):
        self.frame = frame
        self.text = text
        self.command = command
        self.width = width
        self.Btn = Button(self.frame, text=self.text, command=self.command, width=self.width,
                          font=("Arial Bold", font))


def clicked(clk):
    numbers.append(int(clk))
    calculate()


def calculate():
    global numbers, answ
    if len(numbers) > 0:
        a = sum(numbers)
        b = len(numbers)
        c = round(a / b, 2)
        answ = 'Ваш средний балл: ' + str(c)

        txt2.delete(1.0, END)
        txt2.insert(1.0, 'Ваши оценки: ' + str(numbers) + '\n')
        txt2.insert(3.0, answ)
    else:
        clearAll()


def clearOne():
    numbers.pop()
    calculate()


def clearAll():
    global numbers
    txt2.delete(1.0, END)
    numbers = []


window = Tk()
window.title("Калькулятор среднего балла")
window.geometry('360x515')
window.iconbitmap('icon2.ico')
window.wm_maxsize(360, 515)
window.wm_minsize(360, 515)

fr1 = Frame(window)
fr2 = Frame(window)
fr3 = Frame(window)
fr4 = Frame(window)
fr5 = Frame(window)

txt2 = Text(fr5, font=("Arial Bold", font), height=10, width=24, relief=FLAT, insertontime=0)
lbl = Label(fr1, text='Выбирай оценку', font=("Arial Bold", font))
autorLbl = Label(fr5, text='©Kirill Litvinov 2022')

btn1 = Btn(fr3, '2', (lambda: clicked(2)), 10)
btn2 = Btn(fr3, '3', (lambda: clicked(3)), 10)
btn3 = Btn(fr2, '4', (lambda: clicked(4)), 10)
btn4 = Btn(fr2, '5', (lambda: clicked(5)), 10)
btn5 = Btn(fr4, "Убрать", clearOne, 10)
btn6 = Btn(fr4, 'Очистить', clearAll, 10)

fr1.pack(fill=X)
lbl.pack(expand=False, pady=5)

fr2.pack(fill=X)
btn4.Btn.pack(side=LEFT, padx=pad, pady=5)
btn3.Btn.pack(side=LEFT)

fr3.pack(fill=X)
btn2.Btn.pack(side=LEFT, padx=pad, pady=5)
btn1.Btn.pack(side=LEFT)

fr4.pack(fill=X)
btn5.Btn.pack(side=LEFT, padx=pad, pady=5)
btn6.Btn.pack(side=LEFT)

fr5.pack()
txt2.pack(padx=10, pady=5)
autorLbl.pack(side=LEFT)

window.mainloop()
