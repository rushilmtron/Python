class computer:
    def config(self):
        print("i5, 16gb, 1tb")

 # class can not be empty
## here we created class now in class we have 2 things 1 is variables & 2. is functions or methodes



com1 = computer()
com2 = computer()

com1.config()
com2.config()
#another method to print
computer.config(com1)
computer.config(com2)