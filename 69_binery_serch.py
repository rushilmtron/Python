
pos = -1
def search(list,n):
    l = 0
    u = len(list)-1
    while l <= u:
        mid = (l+u)//2

        if list[mid] ==n:
            globals() ['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l= mid;
            else:
                u = mid;




list = [1,2,3,4,5,6,7,8,9,10,23,23,32,23,23,43,5,667,7,67,54]
n = 667
if search(list, n):
    print('Found @ Position:', pos+1)
else:
    print('Not found')