import random

class Machine:
    def __init__(self, min, max ):
        self.answer = random.randint(min, max)
        self.mininum = min
        self.maxinum = max
        self.guess_times = 0

    def guess(self, number):
        self.guess_times = self.guess_times + 1
        if number == self.answer:
            return True
        elif number < self.answer:
            self.mininum = number
            return False
        else:
            self.maxinum = number
            return False

    def returnInterval(self):
        return (self.mininum, self.maxinum)