class computer:
    def __init__(self):
        self.name = 'Rushil'
        self.age = 30
    def update(self):
        self.name = ' Twisha'
    def cmp(self,other):
        if self.age == other.age:
            return  True
        else:
            return False

c1 = computer()
c1.age = int(input('Enter C1 age :'))

c2 = computer()
c2.age = int(input('Enter c2 age :'))

print('age of c1 :',c1.age)
print('age of c2 :',c2.age)

if c1.cmp(c2):
    print('they are same')
else:
    print('They are different')
