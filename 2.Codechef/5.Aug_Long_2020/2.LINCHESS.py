for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int, input().split()))
    x = []
    for i in range(n):
        if (k%a[i] == 0):
            x.append(a[i])
        else:
            pass
    if (len(x)>0):
        print(max(x))
    else:
        print(-1)