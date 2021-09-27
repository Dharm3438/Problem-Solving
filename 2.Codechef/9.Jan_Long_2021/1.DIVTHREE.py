for _ in range(int(input())):
    n,k,d = map(int,input().split())
    a = list(map(int, input().split()))
    x = sum(a)
    divide=0
    if x>=k:
        divide = x//k
        if divide < d:
            print(divide)
        else:
            print(d)
        
    else:
        print(0)