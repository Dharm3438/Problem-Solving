import math

for _ in range(int(input())):
    n, b, m = map(int, input().split())
    val = list(map(int, input().split()))
    blocks = math.ceil(n/b)
    count = 1

    if(val[0]%b==0):
        first_blk = math.ceil(val[0]/b)
        first_blk = first_blk + 1
    else:
        first_blk = math.ceil(val[0]/b)

    temp = first_blk

    for i in range(1,len(val)):
        if(val[i] % b == 0):
            blk = math.ceil(val[i]/b)
            blk = blk+1
        else:
            blk = math.ceil(val[i]/b)

        if(temp == blk):
            pass
        else:
            temp = blk
            count = count + 1

    print(count)