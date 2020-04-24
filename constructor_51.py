class computer:
    def __init__(self):
        self.name = 'Rushil'
        self.age = 30
    def update(self):
        self.name = ' Twisha'




c1 = computer()
c2 = computer()


c1.update()

print(c1.name)
c1.name = 'Foram'
c1.age = 29
# this data comes from above lines
print(c1.age)
print(c1.name)
# this dat comes from class part
print(c2.age)
print(c2.name)
