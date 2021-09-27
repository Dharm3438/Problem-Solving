
mat = []
for i in range(int(input('Col: '))):
    m = list(map(int, input().split()))
    mat.append(m)

x=int(input('x: '))

n=len(mat[0])
m=len(mat)
i = 0
j = m-1
fg=0

while(i<n and j>=0 and fg==0):
    if(mat[i][j]==x):
        fg=1
        print(f"val found at {i},{j}")
    elif(mat[i][j]>x):
        j-=1
    else:
        i+=1

if(fg):
    pass
else:
    print('no')
