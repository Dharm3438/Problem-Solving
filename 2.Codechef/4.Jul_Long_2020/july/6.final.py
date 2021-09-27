for _ in range(int(input())):
    n, x = map(int, input().split())
    v = list(map(int, input().split()))

    v.sort()
    ct = 0
    i = 0
    y = 0
    days = 0
    b = []

    if v[0] < x:
        for j in range(n):
            if v[j] < x:
                y = y + 1
            else:
                break
        if y > 0:
            b = v[0:y]
            v = v[y:]
        else:
            pass

    fin = b + v
    print(b,v)
    print(fin)

    # while(i < len(v)):
    #     if(x >= v[i]):
    #         x = 2*v[i]
    #         i += 1
    #         ct += 1
    #     else:
    #         x = 2*x
    #         ct += 1

    # for i in v:
    #     if(x<i):
    #         while(x<i):
    #             x = x*2
    #             days += 1
    #         days+=1
    #     else:
    #         days += 1
    #         x = 2*i

    next_small = len(b)

    for i in range(next_small,n):
        if(x<fin[i]):
            while(x<v[i]):
                x = 2*x
                days += 1
            days+=1
        else:
            days+=1
            x = 2*fin[i]

    val = days + next_small

    if(next_small!=0):
        days = 0
        next_small -= 1
        for j in range(next_small,n):
            if(x<fin[j]):
                while(x<fin[j]):
                    x = x*2
                    days += 1
                days +=1
            else:
                days += 1
                x = 2*fin[j]
        print(min(days+next_small,val),"if")
    else:
        print(val,"else")