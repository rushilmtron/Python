class student:
    def __init__(self,m1,m2,):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None): # None is use for if some one not pass any value from the user then n error will be generated.1
        s = 0
        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
             s = a
        return s

x = int(input('Enter 1st value:'))
y = int(input('Enter 2nd value:'))
z = int(input('Enter 3rd value:'))

s1 = student(x,y)

print(s1.sum(x,y,z))