# this is a example for class variable

class car:

# wheels is a class variable
    wheels = 4
    def  __init__(self):
        ## this all are static variable
        self.mil = 10
        self.comp = 'BMW'

# define object with class
c1 = car()
c2 = car()

# mil & comp are instance variable
c1.mil = 17
c1.comp = 'Maruti'

# wheel is a class variable how to change of its value
car.wheels = 5

print(c1.comp , c1.mil , c1.wheels)
print(c2.comp, c2.mil, c2.wheels)
