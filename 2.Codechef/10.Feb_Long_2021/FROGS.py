def find_idx(arr, val):
    res = arr.count(val)

    if(res==0):
        return -1
    else:
        res2 = arr.index(val)
        return res2-arr[0]


for _ in range(int(input())):
    n=int(input())
    weights = list(map(int,input().split()))
    lengths = list(map(int,input().split()))
    weight2 = weights[:]

    count = 0

    position=[]
    for i in range(n):
        position[i]=i

    weight2.sort()

    j=1
    while(j<=n-1):
        idx = find_idx(weights,weight2[j])
        p = position[find_idx(weights),weight2[j-1]]
        c = idx

        while(c<=p):
            c+=lengths[idx]
            position[idx] = c
            count += 1
        j+=1

    print(count)
