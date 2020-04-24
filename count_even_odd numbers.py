def count(list):
    even = 0
    odd = 0
    for i in lis:
        if i % 2 == 0:
            even+=1
        else:
            odd+=1
    return even,odd
            
lis = [12,23,32,23,43,54,7,5,4,3,2]

even,odd = count(lis)
print("even : {} & Odd : {}".format(even,odd))