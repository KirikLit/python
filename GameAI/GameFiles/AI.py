class GaMer:
    def __init__(self):
        self.state = 1
        self.lastlast = 0
        self.lastcount = 0
        self.used = [50]
        self.states = {1: 20, 2: 10, 3: 5, 4: 2, 5: 1}

    def get(self, last):
        if last == 'start':
            self.lastcount = 50
            return 50
        else:
            if self.lastcount == 50:
                pass
            elif self.lastlast != last and self.state < 6:
                self.state += 1
            elif self.lastcount < self.states[self.state] or self.lastcount > (100 - self.states[self.state]) \
                    and self.state < 6:
                self.state += 1
            elif last == '<' and (self.lastcount - self.states[self.state]) in self.used and self.state < 6:
                self.state += 1
            elif last == '>' and (self.lastcount + self.states[self.state]) in self.used and self.state < 6:
                self.state += 1

            if last == '<':
                self.lastcount -= self.states[self.state]
            elif last == '>':
                self.lastcount += self.states[self.state]

            self.lastlast = last
            self.used.append(self.lastcount)
            return self.lastcount

    def reset(self):
        self.used = [50]
        self.state = 1
        self.lastlast = 0
        self.lastcount = 0


if __name__ == '__main__':
    print('Это модуль для другой программы\nОткрой TestGameAI.py')
