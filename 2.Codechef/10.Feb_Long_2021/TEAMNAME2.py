for _ in range(int(input())):
    num = int(input())
    
    arr = input().split()
    
    main=dict()

    for i in arr:
        pos = i[1:]
        if pos in main:
            main[pos].append(i[0])
        else:
            main[pos]=[i[0]]

    main2 = list(main.keys())

    res = 0
    
    for i in range(len(main)):
        for j in range(i+1,len(main)):

            tmp1 = main[main2[i]]
            tmp2 = main[main2[j]]
            tmp3 = set(tmp1+tmp2)
            tmp4 = len(tmp3)
            tmp5 = len(tmp1)
            tmp6 = len(tmp2)
            res += (tmp4-tmp5)*(tmp4-tmp6)

        
    print(2*res)