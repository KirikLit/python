class Field:
    def __init__(self, width, height, classname=None, *clasargs):
        self.width = width
        self.height = height
        self.count = self.width * self.height
        self.list_field = []
        self.excl = []
        self.excl2 = []
        
        self.positions = ['NW', 'N', 'NE', 'W', 'E', 'SW', 'S', 'SE']
        self.clas = classname
        self.classuse = False
        self.translate = {'NW': 2, 'N': 1, 'NE': 0, 'W': 4, 'E': 3, 'SW': 7, 'S': 5, 'SE': 6}

        temp1 = self.width
        temp2 = self.width
        for x in range(self.width - 1, self.count):
            if temp1 == self.width:
                self.excl.append(x)
                temp1 = 0
            temp1 += 1

        for x in range(0, self.count):
            if temp2 == self.width:
                self.excl2.append(x)
                temp2 = 0
            temp2 += 1

        if self.clas is not None:
            self.classuse = True

        for i in range(self.count):
            if self.classuse:
                temp = self.clas(*clasargs)
                self.list_field.append(temp)
            else:
                self.list_field.append(i)

    def check(self, oper, index):
        operation = [index > (self.width - 1), index > self.width, index < (self.count - self.width)]

        if oper == 0 and index not in self.excl:
            if operation[0]:
                return True
        elif oper == 1 and operation[0]:
            return True
        elif oper == 2 and index not in self.excl2:
            if operation[1]:
                return True
        elif oper == 3 and index not in self.excl:
            return True
        elif oper == 4 and index not in self.excl2:
            return True
        elif oper == 5 and operation[2]:
            return True
        elif oper == 6 and index not in self.excl:
            if operation[2]:
                return True
            else:
                return False
        elif oper == 7 and index not in self.excl2:
            if operation[2]:
                return True
            else:
                return False
        else:
            return False

    def get_near(self, pos, index):
        positions = {'NW': index - (self.width + 1), 'N': index - self.width,
                     'NE': index - (self.width - 1), 'W': index - 1,
                     'E': index + 1, 'SW': index + (self.width - 1),
                     'S': index + self.width, 'SE': index + (self.width + 1)}
        temp = self.translate[pos]
        if self.check(temp, index):
            position = positions[pos]
            return self.list_field[position]
        else:
            return False
    
    def get_near_index(self, pos, x, y):
        index = (x * y) - 1
        positions = {'NW': index - (self.width + 1), 'N': index - self.width,
                     'NE': index - (self.width - 1), 'W': index - 1,
                     'E': index + 1, 'SW': index + (self.width - 1),
                     'S': index + self.width, 'SE': index + (self.width + 1)}
        temp = self.translate[pos]
        if self.check(temp, index):
            position = positions[pos]
            return position
        else:
            return False
    
    @staticmethod
    def get_index(x, y):
        return x * y - 1
    
    def get(self, x, y):
        pos = (x * y) - 1
        return self.list_field[pos]
    
    def print_field(self):
        temp = self.width
        temp1 = []
        temp2 = 1
        temp3 = 1
        for i in range(len(self.list_field)):
            temp1.append(f' |{temp3}:{temp2}| ')
            if temp2 == self.width:
                temp2 = 0
                temp3 += 1
                temp1.append('\n')
            temp2 += 1
        print(''.join(temp1))

    def set_class(self, index, clas, *clasargs):
        self.list_field[index] = clas(*clasargs)
