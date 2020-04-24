from array import *
vals = array('i', [2,3,4,5,6])
newArray = array(vals.typecode,(a*a for a in vals))

for e in newArray:
    print(e)
