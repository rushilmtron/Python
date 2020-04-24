from threading import  *
from time import *

class Hello(Thread):
    def run(self):
        for i in range(5):
            print('Hello')
            sleep(1)   # it is like delay

class hi(Thread):
    def run(self):
        for i in range(5):
            print('Hi')
            sleep(1)



t1 = Hello()
t2 = hi()

t1.start()
sleep(0.2)
t2.start()


# to print last @ bye
t1.join()
t2.join()

print('Bye')