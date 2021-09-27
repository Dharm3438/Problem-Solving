from difflib import SequenceMatcher

for _ in range(int(input())):
    n, q = map(int,input().split())
    dictionary = []
    mispelt = []
    ct = list(range(200))
    ct2=[]
    ratios = []
    for i in range(n):
        val = input()
        dictionary.append(val)
    for j in range(q):
        val2 = input()
        mispelt.append(val2) 
    
    # for k in mispelt:
    #     for l in k:
    #         for m in range(len(dictionary)):
    #             if(l in dictionary[m]):
    #                 ct[m] += 1

    #     print(ct)
    #     pos = max(dictionary)
    #     pos2 = dictionary.index(pos)
    #     ct2.append(pos2)
    #     ct = list(range(200))

    # for k in range(len(mispelt)):
    #     if(mispelt[0] in )

    # for n in ct2:
    #     print(dictionary[n])

    for i in dictionary:
        for j in mispelt:
            s = SequenceMatcher(None, i, j)
            ratios.append(s.ratio())
        print(ratios)



    
