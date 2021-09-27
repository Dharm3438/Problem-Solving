import operator as op
from collections import defaultdict
import sys

def def_value():
    return 0

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    flag = 0
    sumi = 0

    adict = defaultdict(def_value)
    bdict = defaultdict(def_value)
    sdict = defaultdict(def_value)

    for i in a:
        if i in adict.keys():
            adict[i] = adict[i] + 1
        else:
            adict[i] = 1
            
        if i in sdict.keys():
            sdict[i] = sdict[i] + 1
        else:
            sdict[i] = 1

    for j in b:
        if j in bdict.keys():
            bdict[j] = bdict[j] + 1
        else:
            bdict[j] = 1
            
        if j in sdict.keys():
            sdict[j] = sdict[j] + 1
        else:
            sdict[j] = 1

    print("Initial")
    print(adict)
    print(bdict)
    print(sdict)
    print(sumi)
    print()

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
        #a_min = min(a)
        #b_min = min(b)
        while(not op.eq(adict, bdict)):
            temp = iter(sdict)
            for i in sdict.keys():
                if adict[i] == bdict[i]:
                    #print(f"i: {i}")
                    pass
                else:
                    if(adict[i]>bdict[i]):
                        b_min = min(bdict.keys())
                        if(bdict[b_min]==0):
                            #i = next(temp,0)
                            continue
                        # while(bdict[b_min]==0):
                            # del bdict[b_min]
                            # b_min = min(bdict.keys())
                            
                        #sumi += min(abs(adict[i]), abs(bdict[b_min]))
                        sumi += min(i,b_min)
                        
                        adict[i] = adict[i] - 1
                        bdict[i] = bdict[i] + 1
                        bdict[b_min] = bdict[b_min] - 1
                        adict[b_min] = adict[b_min] + 1
                        print(f"a> sumi {sumi}")
                        print(i,b_min)
                        print(adict[i], bdict[b_min])
                    else:
                        a_min = min(adict.keys())
                        if(adict[a_min]==0):
                            #i = next(temp,0)
                            continue

                        # while(adict[a_min]==0):
                            # del adict[a_min]
                            # a_min = min(adict.keys())

                        #sumi += min(abs(bdict[i]), abs(adict[b_min]))
                        sumi += min(i, a_min)

                        bdict[i] = bdict[i] - 1
                        adict[i] = adict[i] + 1
                        adict[a_min] = adict[a_min] - 1
                        bdict[a_min] = bdict[a_min] + 1
                        print(f"b> sumi {sumi}")
                        print(i,a_min)
                        print(bdict[i], adict[a_min])

                print("for ")

            
            #sys.exit(0)
            print("while ")
            
    print("Final")
    print(adict)
    print(bdict)
    print(sdict)
    print(sumi)