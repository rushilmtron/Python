class a:
    def f1(self):
        print('f1')

    def f2(self):
        print('f2')

class b(a): # b class is child / sub class of a class
    def f3(self):
        print('f3')

    def f4(self):
        print('f4')

class c(b):
    def f5(self):
        print('F5')
class d:
    def f6(self):
        print('f6')

class e:
    def f7(self):
        print('f7')
class f(d,e):
    def f8(self):
        print('f8')

a1 = a()
a2 = a()
a1.f2()
a1.f1()


b1 = b()
b2 = b()
b1.f3()
b2.f4()
b1.f1()

c1 = c()
c1.f3()

f1 = f()
f1.f6()