for _ in range(int(input())):
    
    num=int(input())
    
    arr=list(map(str,input()))
    
    ct,ft,op,cl=0,0,0,0
    
    for i in range(len(arr)):
        if(arr[i]==']'):
            cl+=1
            ft = cl-op
        else:
            op+=1
            if(ft>0):
                ct+=ft
                ft-=1
                
    print(ct)
            
        
    