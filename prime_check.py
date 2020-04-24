num = int(input('enter the number:'))
#num = 7

for i in range(2, num-1):
    if num % i ==0:
        print('not prime')
        break
else:
    print('Prime')