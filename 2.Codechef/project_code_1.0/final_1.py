T = int(input())
possible = []
impossible = []
for x in range(T):

    values = list(map(int,input().split()))
    s = values[0]
    n = values[1]
    k = values[2]
    r = values[3]

    req = k
    final = req
    for i in range(n-1):
        req = req * r
        final = final +req
    final = s - final
    if(final>0):
        print("POSSIBLE ",final)
        
        possible.insert(i,final)
    else :
        print("IMPOSSIBLE",abs(final))
        impossible.insert(i,abs(final))

print(sum(possible))
print(sum(impossible))