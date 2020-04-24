f = open('65_MyData','r')

print(f.readline(), end='#')
print(f.readline(), end='#')


# To create file in python
# by continuing this we lost previous data
#f1 = open('rushil','w')
# To write in to file
#f1.write('Hare krishna')


# To create file in python
# & add data to file
f1 = open('rushil','a')
# To write in to file
f1.write(' Hare krishna')