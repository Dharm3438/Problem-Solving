
mat = []
for i in range(int(input('Col'))):
    m = list(map(int, input().split()))
    mat.append(m)

l = 0
r = len(mat[0])-1
t = 0
d = len(mat)-1
arr = []
side = 0

while(l<=r and t<=d):

    #first row
    if(side==0):
        for i in range(l,r+1):
            arr.append(mat[t][i])
        t+=1
    elif(side==1):
        for i in range(t,d+1):
            arr.append(mat[i][r])
        r-=1
    elif(side==2):
        i=r
        while(i>=l):
            arr.append(mat[d][i])
            i=i-1
        d-=1
    elif(side==3):
        i=d
        while(i>=t):
            arr.append(mat[i][l])
            i-=1
        l+=1

    side = (side+1)%4

print(arr)
    
