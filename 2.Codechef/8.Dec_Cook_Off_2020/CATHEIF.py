import sys 
import math

for _ in range(int(input())):
    x,y,k,n = map(int,input().split()) 
    
    if(x>y):
        gap = x-y
    else:
        gap = y-x

    flag1 = 0
    flag2 = 0
    
    if(gap%2==0):
        #odd may satisfy
        for i in range(1,math.ceil(gap/2)+1,2):
            i=i*2 
            if(gap%i==0):
                flag1 = 1
            else:
                pass
        if(flag1):
            print('YES')
        else:
            print('NO')
    else:
        #even may satisfy
        for i in range(2,math.ceil(gap/2)+1,2):
            i=i*2
            if(gap%i==0):
                flag2 = 1
            else:
                pass
        if(flag2):
            print('YES')
        else:
            print('NO')
