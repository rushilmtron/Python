from array import *
arr = array('i',[])

len = int(input('Enter the length of array:'))


for i in range(len):
    arrElement = int(input('Enter the next value:'))
    arr.append(arrElement)
print(arr)

search_val = int(input('Enter the value which user want to find:'))
k=0
for e in arr:
    if e ==search_val:
        print(k)
        break
    k+=1