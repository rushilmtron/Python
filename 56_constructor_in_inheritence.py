class a:
    def __init__(self):
        print('in a init')
    def f1(self):
        print('f1')

    def f2(self):
        print('f2')

class b(): # b class is child / sub class of a class

    def __init__(self):
        print('in b init')

    def f3(self):
        print('f3')

    def f4(self):
        print('f4')

class c(a,b): # a's in will be printed in this
    def __init__(self):
        print (' c is in init')
        super().__init__()

    def f5(self):
        print('f5')

a1 = c()
