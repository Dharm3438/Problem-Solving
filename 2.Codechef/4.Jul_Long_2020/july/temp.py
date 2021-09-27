n,q = map(int,input().split())
h = list(map(int, input().split()))
a = list(map(int, input().split()))
    
for i in range(q):
    x,y,z = map(int,input().split())
        
    if x == 1 :
        a[y-1] = z
    elif x == 2 :
            
        if y > z :
            z=z-1
            y=y-1
            sumx = a[z]
            temp_sum = sumx
            temp = z+1  #3
            while(z <= y and temp <= y):
                #print(a[temp])
                if h[z] < h[temp]: 
                    sumx = sumx + a[temp]
                    temp = temp + 1 
                    z = z+1  
                    
                else :
                    temp = temp+1
            if sumx > temp_sum:
                print(sumx)
            else:
                print(-1)
        elif y==z :
                
            print(a[y])
                
        elif  y < z:
            pass