mat = []
for i in range(int(input('Col: '))):
    m = list(map(int, input().split()))
    mat.append(m)

for i in range(len(mat)):
    for j in range(len(mat[0])):
        mat[i][j] = mat[j][i]

#mat = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]


print(mat)

for val in mat:
    l=0
    r=len(val)-1
    while(l<r):
        val[l],val[r]=val[r],val[l]
        l+=1
        r-=1

print(mat)