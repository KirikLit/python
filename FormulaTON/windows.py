from tkinter import *
from PIL import ImageTk, Image
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config


class mainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.geometry('300x300')
        self.title('Органайзер')

        self.font = 'Segoe UI', 15

        btn1 = Button(self, text='Узнать погоду', font=self.font, command=self.weathWind)
        btn2 = Button(self, text='Калькулятор', font=self.font, command=self.calc)

        btn1.pack(padx=15, fill=X, pady=10)
        btn2.pack(padx=15, fill=X)

        self.mainloop()

    def weathWind(self):
        WW = weatherWindow()

    def calc(self):
        CC = calcwin()


class weatherWindow(Toplevel):
    def __init__(self):
        super().__init__()
        self.snwcld = None
        self.suun = None
        self.cl = None
        self.suncl = None
        self.imgLbl = None
        self.entry = None
        self.initUI()

    def initUI(self):
        self.geometry('300x290')
        self.title('Погода')
        self.config(bg='LightBlue')

        suncloud = Image.open('suncloud.ico')
        cloud = Image.open('cloud.ico')
        sun = Image.open('sun.ico')
        snowcloud = Image.open('snowcloud.ico')

        self.suncl = ImageTk.PhotoImage(suncloud)
        self.cl = ImageTk.PhotoImage(cloud)
        self.suun = ImageTk.PhotoImage(sun)
        self.snwcld = ImageTk.PhotoImage(snowcloud)

        fr1 = Frame(self, bg='LightBLue')
        fr2 = Frame(self, bg='LightBLue')

        self.imgLbl = Label(self, image=self.cl, bg='LightBlue')
        self.entry = Entry(fr1, width=20, font=('Segoe UI', 11))
        lbl11 = Label(fr1, text='Введите город:', font=('Segoe UI', 11), bg='LightBlue')
        btnWTH = Button(fr2, text='Узнать погоду', font=('Segoe UI', 11), command=self.wthCalc)
        self.celsLbl = Label(fr1, font=('Segoe UI', 30), bg='LightBlue')
        self.wthLbl = Label(fr1, font=('Segoe UI', 13), bg='LightBlue')

        self.imgLbl.pack()
        fr1.pack(fill=X)
        self.wthLbl.pack()
        self.celsLbl.pack()
        lbl11.pack(side=LEFT, padx=5)
        self.entry.pack(side=LEFT, padx=5)

        fr2.pack(fill=X)
        btnWTH.pack(pady=5, fill=X, padx=10)

        self.mainloop()

    def wthCalc(self):
        config_dict = get_default_config()
        config_dict['language'] = 'ru'
        owm = OWM('85a26eea569d629dc208b2088993880f', config_dict)

        place = self.entry.get()
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(place)
        w = observation.weather

        n = w.detailed_status
        t = w.temperature('celsius')['temp']

        if t < -3:
            self.imgLbl.config(image=self.snwcld)
        elif t < 15:
            self.imgLbl.config(image=self.cl)
        elif t < 25:
            self.imgLbl.config(image=self.suncl)
        elif t > 25:
            self.imgLbl.config(image=self.suun)

        self.celsLbl.config(text=t)
        self.wthLbl.config(text=n)


class calcwin(Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Калькулятор')
        self.minsize(340, 155)
        self.maxsize(340, 155)
        self.config(bg='LightGray')

        XXX = 0
        CCC = 1
        self.inti = '0'
        self.disp = '0'
        self.oper = False

        for XX in range(0, 5):
            self.rowconfigure(XX, pad=5)
            self.columnconfigure(XX, pad=5)

        self.font = 'Segoe UI', 12
        btns = ['1', '2', '3', '+', '4', '5', '6', '-',
                '7', '8', '9', '*', '0', '.', '/', '=', 'C', '√']

        self.entry = Entry(self, font=self.font, takefocus=True, width=36)
        self.entry.grid(row=0, column=0, columnspan=4)
        self.entry.insert(0, '0')

        for btn in btns:
            x = Button(self, text=btn, command=lambda z=btn: self.pressed(z), width=10)

            if XXX == 4:
                XXX = 0
                CCC += 1

            x.grid(row=CCC, column=XXX)
            XXX += 1

    def pressed(self, x):
        divs = ['+', '-', '*', '/']

        if x == '=':
            if self.oper:
                self.inti += self.disp
                self.oper = False
            if self.inti == '0' or '':
                return
            else:
                res = eval(self.inti)
                self.entry.delete(0, END)
                self.entry.insert(0, res)
                self.inti = str(res)
                self.disp = str(res)
        elif x == 'C':
            self.inti = '0'
            self.disp = '0'
            self.entry.delete(0, END)
            self.entry.insert(0, '0')
        else:
            if x not in divs:
                if self.oper:
                    self.disp = x
                    self.oper = False
                elif self.disp == '0':
                    self.disp = x
                else:
                    self.disp += x
                self.entry.delete(0, END)
                self.entry.insert(0, self.disp)
                if self.inti == '0':
                    self.inti = x
                else:
                    self.inti += x
            else:
                if not self.oper:
                    res = eval(self.inti)
                    self.oper = True
                    self.entry.delete(0, END)
                    self.entry.insert(0, res)
                self.inti = str(eval(self.inti))
                self.inti += x

        print(self.inti)


if __name__ == '__main__':
    app = mainWindow()