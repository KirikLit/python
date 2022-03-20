import pickle
import sys
import time
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
import tkinter.ttk as ttk


class Notes(Frame):
    def __init__(self):
        super().__init__()
        self.note = None
        self.notes = None
        self.menu = None
        self.pageLbl = None
        self.autorLbl = None
        self.txt = None
        self.btnNext = None
        self.btnPrev = None
        self.clock = None
        self.initUI()

    def initUI(self):
        self.pack(fill=BOTH, expand=True)

        self.notes = []
        self.note = 1

        file = open('notes.dat', 'rb')
        self.notes = pickle.load(file)
        file.close()

        fr1 = Frame(self)
        fr2 = Frame(self)

        ttk.Style().configure('TButton', font=('Segoe UI', 16))
        self.clock = Label(fr1, font=('Times New Roman Bold', 40))
        self.btnPrev = ttk.Button(fr1, text='Пред.', width=10, command=self.preNote)
        self.btnNext = ttk.Button(fr1, text='След.', width=10, command=self.nextNote)
        self.txt = Text(fr2)
        self.autorLbl = Label(fr2, text='©Kirill Litvinov 2022')
        self.pageLbl = Label(fr2, anchor=NE)

        fr1.pack(fill=X)
        self.clock.pack(side=LEFT, pady=20, padx=20)
        self.btnNext.pack(side=RIGHT, pady=20, padx=20)
        self.btnPrev.pack(side=RIGHT, pady=20)

        fr2.pack(fill=BOTH, expand=True)
        self.txt.pack(fill=BOTH, pady=0, padx=20, expand=True)
        self.autorLbl.pack(side=LEFT, padx=20)
        self.pageLbl.pack(side=RIGHT)

        self.menu = Menu(self)
        new_item = Menu(self, tearoff=0)
        new_item.add_command(label='Удалить заметку', command=self.delNote)
        new_item.add_separator()
        new_item.add_command(label='Удалить всё', command=self.delAll)
        self.menu.add_cascade(label='Заметки', menu=new_item)

        new_item2 = Menu(self, tearoff=0)
        new_item2.add_command(label='Открыть', command=self.openfile)
        new_item2.add_command(label='Сохранить', command=self.savefile)
        self.menu.add_cascade(label='Файл', menu=new_item2)

        if len(self.notes) == 0:
            x = ''
            self.notes.append(x)

        self.timing()
        self.prNote(1)

        print(self.notes)

    def nextNote(self):
        self.save(self.note)

        if self.note == len(self.notes):
            x = ''
            self.notes.append(x)
        self.note += 1
        self.prNote(self.note)

    def preNote(self):
        self.save(self.note)

        if self.note == 1:
            pass
        else:
            self.note -= 1
            self.prNote(self.note)

    def prNote(self, note):
        self.txt.delete(0.0, END)
        self.txt.insert(0.0, self.notes[note - 1])

        self.pageLbl.config(text='Заметка ' + str(self.note) + '/' + str(len(self.notes)))

    def save(self, note):
        x = self.txt.get(0.0, END)
        self.notes[note - 1] = x

        fileS = open('notes.dat', 'wb')
        pickle.dump(self.notes, fileS)
        fileS.close()

    def exiting(self):
        x = messagebox.askyesno(title='Выход из программы', message='Вы хотите выйти?')
        if x:
            self.save(self.note)
            sys.exit()

    def timing(self):
        current_time = time.strftime("%H : %M : %S")
        self.clock.config(text=current_time)
        self.clock.after(200, self.timing)

    def delNote(self):
        if self.note == 1:
            x = ''
            self.notes[self.note - 1] = x
            self.txt.delete(0.0, END)
            self.pageLbl.config(text='Заметка ' + str(self.note) + '/' + str(len(self.notes)))
        else:
            self.note -= 1
            self.prNote(self.note)
            self.notes.pop(self.note)
            self.pageLbl.config(text='Заметка ' + str(self.note) + '/' + str(len(self.notes)))

    def delAll(self):
        self.txt.delete(0.0, END)
        self.notes = ['']
        self.note = 1
        self.prNote(self.note)

    def openfile(self):
        file = askopenfilename(filetypes=(("Text Files", "*.txt"),))
        file = open(file)
        data = file.read()

        self.notes.append(data)
        self.note = len(self.notes)
        self.prNote(self.note)

        file.close()

    def savefile(self):
        tf = asksaveasfile(mode='w', defaultextension=" .txt")
        data = str(self.txt.get(1.0, END))
        tf.write(data)

        tf.close()


def main():
    window = Tk()
    window.geometry('800x600')
    window.title('Заметки--')
    app = Notes()
    window.protocol('WM_DELETE_WINDOW', app.exiting)
    window.config(menu=app.menu)
    window.mainloop()


if __name__ == '__main__':
    main()
