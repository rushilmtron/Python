
pos = -1
def search(list,n):
    i = 0
    while i < len(list):
        if list [i] ==n:
            globals()['pos']=i
            return True
        i = 1 + i


    return False

list = [1,2,3,4,5,6,7,8,9,10]
n = 5
if search(list, n,):
    print('Found @ Position:', pos+1)
else:
    print('Not found')