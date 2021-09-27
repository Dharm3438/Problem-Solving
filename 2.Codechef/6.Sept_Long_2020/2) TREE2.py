for _ in range(int(input())):
    n = int(input())
    val = list(map(int,input().split()))

    ct = 0
    
    val.sort(reverse=True)
    max_el = val[0]
    for i in val:
        if(max_el==i):
            ct+=1
        else:
            break
    print(ct)
    res=n-ct + 1
    print(res)