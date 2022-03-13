from .AI import GaMer


class Test:
    def test(self, answer, tries):
        AI = GaMer()
        answ = False
        last = 'start'
        triess = 1

        while not answ:
            if tries > 0:
                inp = AI.get(last)

                if inp > answer:
                    tries -= 1
                    triess += 1
                    last = '<'
                elif inp < answer:
                    tries -= 1
                    triess += 1
                    last = '>'
                elif inp == answer:
                    AI.reset()
                    answ = True
                    return triess
            else:
                AI.reset()
                answ = True
                return 34404
