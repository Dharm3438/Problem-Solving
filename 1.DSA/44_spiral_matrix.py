#User function Template for python3

def spirallyTraverse(matrix, r, c): 
    # code here 

    top = 0
    dow = r-1
    lef = 0
    rig = c-1
    arr = []
    side = 0
    
    while(top<=dow and lef<=rig ):
        if(side == 0):
            for i in range(lef,rig+1):
                arr.append(matrix[top][i])
            top+=1
        elif(side == 1):
            for i in range(top,dow+1):
                arr.append(matrix[i][rig])
            rig-=1            
        elif(side == 2):
            i=rig
            while(i>=lef):
                arr.append(matrix[dow][i])
                i=i-1
            #for i in range(lef,rig,-1):
            #    arr.append(matrix[dow][i])
            dow-=1
        elif(side == 3):
            i=dow
            while(i>=top):
                arr.append(matrix[i][lef])
                i=i-1
            #for i in range(top,dow,-1):
            #    arr.append(matrix[i][lef])
            lef+=1
        
        side = (side+1)%4
        
    return arr
            









#{ 
#  Driver Code Starts
#Initial Template for Python 3

if _name_ == '_main_':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(values[k])
                k+=1
            matrix.append(row)
        ans = spirallyTraverse(matrix,r,c)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends