
mat = []
for i in range(int(input('Col: '))):
    m = list(map(int, input().split()))
    mat.append(m)

maxi = -99999
for i in mat:
    ct = i.count(1)
    maxi=max(maxi,ct)

print(maxi)