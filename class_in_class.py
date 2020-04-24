class student:

    def __init__(self,name, rollno):
        self.name = name
        self.rollno = rollno

        # create object lap inside class
        self.lap = self.laptop()


    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class laptop:

        def __init__(self):
            self.comp = 'DELL'
            self.cpu = 'i5'
            self.ram = 5

        def show(self):
            print(self.comp, self.cpu, self.ram)



s1 = student('Rushil', 5)
s2 = student('Foram', 20)



s1.show()

