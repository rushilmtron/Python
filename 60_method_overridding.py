from abc import ABC, abstractmethod


class computer:
    @abstractmethod  # for abstrect matod we cant create objects
    def processor(self):
        print('abstract method')
        pass


class laptop(computer):
    def process(self):
        print('Its running')


com1 = laptop()
com1.process()
