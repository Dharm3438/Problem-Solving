import sys

for _ in range(int(input())):
    n = int(input())
    p, q = map(int,input().split())
    res = p/q
    pattern = ''
    ct = 0
    sumi = 0

    if(res==0):
        print(0)
        sys.exit(0)

    res = str(res)
    res = res[:-2]
    dec = res.split('.')[1]

    #print(res)
    #print(dec)
    #print(type(dec))

    for i in dec:
        if(i not in pattern):
            pattern += i

    #print(pattern)
        
    for j in pattern:
        sumi += int(j)

    if(n%len(pattern)==0):
        tot = sumi * n/len(pattern)
    else:
        tot = sumi * n//len(pattern)
        val = n * n//len(pattern)

        for k in range(val,n+1):
            for l in pattern:
                tot += int(l)

    print(int(tot))
    
    