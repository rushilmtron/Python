from array import *
arr = array('i',[])
len = int(input('Enter the length of array:'))

for i in range(len):
    arrElements= int(input('Enter the next value:'))
    arr.append(arrElements)

print(arr)