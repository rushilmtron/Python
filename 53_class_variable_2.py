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

    # class method we here define for SCHOOL class variable
    @classmethod
    def s_info(cls):
        return cls.school




# create 2 object we can also pass the value in ()
a = int(input('Enter m1 for s1:'))
b = int(input('Enter m2 for s1:'))
c = int(input('Enter m3 for s1:'))


s1 = student(a,b,c)
s2 = student(80,85,95)

# print the avg value
print(s1.avg())
print(student.s_info())


