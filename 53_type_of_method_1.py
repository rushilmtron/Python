class student:
    # here we creat class variable
    school = 'Mechatron'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    # Here we create the method for calculating average of m1,m1 & m3
    # its a instance method
    def avg(self):
        return (self.m1+ self.m2 + self.m3)/3

    # to get m1 value get_1 method is created it is a method
    def get_1(self):
        return self.m1

    # to get m2 value get_2 method is created it is a method
    def get_2(self):
        return self.m2

    # to get m3 value get_3 method is created it is a method
    def get_3(self):
        return self.m3

    # to set value of m1 we createc set_1 method
    def set_m1(self,value1):
        self.m1 = value1
        return (value1)

    # to set value of m1 we createc set_1 method
    def set_m1(self, value2):
        self.m2 = value2
        return (value2)

    # to set value of m1 we createc set_1 method
    def set_m1(self, value3):
        self.m3 = value3
        return (value3)


# create 2 object we can also pass the value in ()
a = int(input('Enter m1 for s1:'))
b = int(input('Enter m2 for s1:'))
c = int(input('Enter m3 for s1:'))


s1 = student(a,b,c)
s2 = student(80,85,95)

# print the avg value
print(s1.avg())
print(s2.avg())

# get value of m1, m2, m3
print(s1.get_1())
print(s1.get_2())
print(s1.get_3())

# set value of m1, m2, m3 we can also give input from assign variable to the while passing values in class ref. line 42
#x = int(input(('Enter the updated marks od s1 in m1 sub:')))
#print(s1.set_m1(x))

#y = int(input(('Enter the updated marks od s1 in m2 sub:')))
#print(s1.set_m1(y))

#z = int(input(('Enter the updated marks od s1 in m3 sub:')))
#print(s1.set_m1(z))

