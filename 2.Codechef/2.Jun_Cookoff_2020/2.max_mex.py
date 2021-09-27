for _ in range(int(input())):
    m,n = map(int,input().split())
    val = list(map(int,input().split()))
    flag = 0
    ct = 0
    val.sort()

    pos = val.count(m)
    if(pos>0):
        flag == 1

    for i in range(1,m):
        if(i not in val):
            flag = 1

    if(flag==1):
        print('-1')
    else:
        print(m)

