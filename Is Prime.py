number = int(input())
flag = True
for i in range(2, number-1):
    if(number%i==0):
        flag = False

if(flag == False):
    print('No')
else:
    print('Yes')
