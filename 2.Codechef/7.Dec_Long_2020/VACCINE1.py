# cook your dish here
import math

d1,v1,d2,v2,p = map(int,input().split())
if (d1==d2):
    tot = v1+v2
    rem = math.ceil(p/tot)
    print(d1+rem)
elif(d1<d2):
    v2 = v2 + v1
    sub = d2-d1
    prep = v1*sub
    rem = p - prep
    rem2 = math.ceil(rem/v2)
    print(d2+rem2-1)
elif(d1>d2):
    v1 = v1 + v2
    sub = d1-d2
    prep = v2*sub
    rem = p - prep
    rem2 = math.ceil(rem/v1)
    print(d1+rem2-1)