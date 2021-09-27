import numpy as np

for _ in range(int(input())):
    n = int(input())
    #val = list(map(int,input().split()))
    val = list(range(1,100000000))
    print(val)

    mini = []
    maxi = []
    equal = []

    for i in range(2,n):
        for j in val:
            if(j<i):
                mini.append(j)
            elif(j>i):
                maxi.append(j)
            else:
                equal.append(j)
        print(mini)
        print(maxi)
        print(equal)
        mini = []
        maxi = []
                