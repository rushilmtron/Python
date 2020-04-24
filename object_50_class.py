class computer:

    def __init__(self, CPU, RAM):
        self.CPU = CPU
        self.RAM = RAM

    def config(self):
        print("Configuration is", self.CPU, self.RAM)

 # class can not be empty
## here we created class now in class we have 2 things 1 is variables & 2. is functions or methodes



com1 = computer('I5', 16)
com2 = computer('I3', 8)

com1.config()
com2.config()
