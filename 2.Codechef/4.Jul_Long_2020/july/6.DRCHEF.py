for _ in range(int(input())):
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    days = 1
    i = 0
    if(a[0]<x):
        for j in range(len(a)):
            if(a[j]>=x):
                i = 0
                break
            else:
                pass

        a = a[j:] + a[0:j]
        print(a)
    else:
        i = 0

    while(a[i]>=0):
        days += 1
        if(x==a[i]):
            a[i] = 0
            x = x*2
            i += 1
            if (i==(len(a)-1)):
                break
            elif(x>a[i]):
                x = a[i] * 2
                a[i] = 0
                i += 1
                if(i==(len(a)-1)):
                    break
            elif(a[i]>x):
                x = x*2

        print(days)