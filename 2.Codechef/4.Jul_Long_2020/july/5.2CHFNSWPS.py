import operator as op
import sys

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    flag = 0
    sumi = 0

    adict = dict()
    bdict = dict()
    sdict = dict()

    for i in a:
        if i in adict.keys():
            adict[i] = adict.get(i, 0) + 1
        else:
            adict[i] = 1
            
        if i in sdict.keys():
            sdict[i] = sdict.get(i,0) + 1
        else:
            sdict[i] = 1

    for j in b:
        if j in bdict.keys():
            bdict[j] = bdict.get(j, 0) + 1
        else:
            bdict[j] = 1
            
        if j in sdict.keys():
            sdict[j] = sdict.get(j, 0) + 1
        else:
            sdict[j] = 1

    # print("Initial")
    # print(adict)
    # print(bdict)
    # print(sdict)
    # print(sumi)
    # print()

    for val in sdict.values():
        if(val%2==0):
            pass
        else:
            flag = 1
            break

    if(flag):
        print(-1)
        sys.exit(0)
    else:
        a_min = min(a)
        b_min = min(b)
        while(not op.eq(adict, bdict)):
            for i in sdict.keys():
                if adict.get(i, 0) == bdict.get(i, 0):
                    #print(f"i: {i}")
                    pass
                else:
                    a_val = adict.get(i, 0) #2
                    b_val = bdict.get(i, 0) #0

                    if(a_val>b_val):
                        adict[i] = adict.get(i, 0) - 1
                        bdict[i] = bdict.get(i, 0) + 1
                        bdict[b_min] = bdict.get(b_min, 0) - 1
                        adict[b_min] = adict.get(b_min, 0) + 1
                        sumi += min(abs(adict.get(i, 0)), abs(bdict.get(b_min, 0)))
                        #print(f"a> sumi {sumi}")
                        #print(adict.get(i, 0), bdict.get(b_min, 0))
                    else:
                        a_min = min(adict.keys())
                        bdict[i] = bdict.get(i, 0) - 1
                        adict[i] = adict.get(i, 0) + 1
                        adict[a_min] = adict.get(a_min, 0) - 1
                        bdict[a_min] = bdict.get(a_min, 0) + 1
                        sumi += min(abs(bdict.get(i, 0)), abs(adict.get(b_min, 0)))
                        #print(f"b> sumi {sumi}")
                        #print(bdict.get(i, 0), adict.get(b_min, 0))

                print("for ")

            
            #sys.exit(0)
            print("while ")
            
    # print("Final")
    # print(adict)
    # print(bdict)
    # print(sdict)
    print(sumi)
