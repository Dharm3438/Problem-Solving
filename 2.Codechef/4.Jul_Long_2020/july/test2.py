for _ in range(int(input())):
    n,x = map(int,input().split())
    a = list(map(int, input().split()))
    a.sort()
    days = 0
    val = len(a) 
    val2 = 0
    if a[0] < x :
        for j in range(len(a)):
            if a[j] >=x :
                i=0
                break
            else:
                pass
        b = a[0:j]
        a = a[j:]
        print(a)
        val2 = len(b)
        print(b)
        print(val)
        print(val2)
        a = a + b 
        val = len(a)
    else:
        i=0
        
    while(a[i] >= 0):
        days = days + 1
        if x == a[i]:
            a[i] = 0
            x = x*2
            i = i + 1 
            if i == (val-1):
                break
        elif x > a[i] :
            x = a[i] *2
            a[i] = 0
            i = i + 1
            if i == (val-1):
                break
            
        elif a[i] > x:
            x = x * 2
    print(days+val2)