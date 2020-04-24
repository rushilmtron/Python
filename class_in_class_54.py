class student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno


    def show(self):
        print(self.name, self.rollno)

    class laptop:

        def __init__(self):
            self.comp = 'DELL'
            self.cpu = 'i5'
            self.ram = 5


s1 = student('Rushil', 5)
s2 = student('Foram', 20)

# instead of write print every time make its function as show
# print(s1.name, s1.rollno)
# print(s2.name, s2.rollno)

s1.show()

lap1 = student.laptop()
lap2 = student.laptop()