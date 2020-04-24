# this is a example of instance variable..

class car:


    def  __init__(self):
        self.mil = 10
        self.comp = 'BMW'
# mil & comp are instance variables

## this all are static variable
c1 = car()
c2 = car()

c1.mil = 17
c1.comp = 'Maruti'

print(c1.comp , c1.mil)
print(c2.comp, c2.mil)
