#code
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    m = int(input())
    
    arr.sort()
    
    i = 0
    minimum=9999999999
    
    while(i+m-1<n):
        
        d = arr[i+m-1] - arr[i]
        
        if(d<minimum):
            minimum = d
            
        i +=1
    
    print(minimum)