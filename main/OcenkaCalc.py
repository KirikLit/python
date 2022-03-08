from tkinter import *

numbers = []

rightargs = ['1', '2', '3', '4', '5']

font = 18


def clicked():
    if txt.get() in rightargs:
        numbers.append(int(txt.get()))

        txt.delete(first=0, last=10)

        txt2.delete(1.0, END)
        txt2.insert(1.0, 'Ваши оценки: ' + str(numbers))

    else:
        txt.delete(first=0, last=10)
        pass

def solve():
    global numbers

    a = sum(numbers)
    b = len(numbers)
    c = round(a / b, 2)
    answ = 'Ваш средний балл: ' + str(c)

    txt2.delete(1.0, END)
    txt2.insert(1.0, answ)

    numbers = []

window = Tk()
window.title("Калькулятор среднего балла")
window.geometry('400x400')
window.iconbitmap('icon2.ico')

lbl = Label(window, text="Вводи свои оценки:", font=("Arial Bold", font))
lbl.grid(row=0)

txt = Entry(window, width=10, font=("Arial Bold", font))
txt.grid(column=1, row=0)
txt.focus()

btn = Button(window, text="Добавить", command=clicked, font=("Arial Bold", font))
btn.grid(row=2)

btn2 = Button(window,text='Посчитать', command=solve, font=("Arial Bold", font))
btn2.grid(column=1, row=2)

txt2 = Text(window, font=("Arial Bold", font), height= 10, width= 25, relief=FLAT, insertontime= 0)
txt2.place(y= 85, x= 25)

window.mainloop()