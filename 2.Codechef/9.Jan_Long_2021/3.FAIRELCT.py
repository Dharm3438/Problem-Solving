for _ in range(int(input())):
    n,m = map(int,input().split())
    arrn = list(map(int, input().split()))
    arrm = list(map(int,input().split()))

    arrn.sort()
    arrm.sort(reverse=True)

    sumn = sum(arrn)
    summ = sum(arrm)

    i=0
    ct=0
    flg=0

    while(i<n and i<m):
        if(sumn>summ):
            flg = 1
            break
        else:
            summ = summ - arrm[i] + arrn[i]
            sumn = sumn - arrn[i] + arrm[i]
            arrn[i],arrm[i] = arrm[i],arrn[i]
            print(arrn[i],sumn,arrm[i],summ)
            ct+=1
            i+=1

    if(sumn>summ):
        print(ct)
    else:
        print(-1)