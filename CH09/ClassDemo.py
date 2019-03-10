class Dog:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def run(self):
        print("Dog", self.name, "[", self.age, "] Run")

dog1 = Dog("Black", 10)
dog1.run()

dog2 = Dog("White", 5)
dog2.run()

print("---------繼承---------")

class HusKy(Dog):
    def __init__(self, n, a, g):
        super(HusKy, self).__init__(n, a)
        self.gender = g

    def run(self):
        print("HusKy", self.name, "[", self.age, "] Run")

dog3 = HusKy("Orange", 3, "M")
dog3.run()