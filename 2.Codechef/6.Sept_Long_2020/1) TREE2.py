for _ in range(int(input())):
    n = int(input())
    val = list(map(int,input().split()))
    
    val.sort(reverse=True)

    ct = 0

    while True:
        max_el = val[0]

        for i in val:
            if(max_el==i):
                pass
            else:
                sec_max = i
                break
        
        if(sec_max==max_el):
            break

        for j in range(len(val)):
            if(val[j]==max_el):
                val[j] = sec_max
            else:
                break 

        ct += 1

        print(max_el,sec_max)
        print(val)

    print(ct+1)