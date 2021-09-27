def remove(n,x,le):
    if(le==-1):
        return 
    
    if(n[0]!=x):
        remove(n[1:],x,le-1)
    else:

        for i in range(1,len(n)-1):
            n[i-1]=n[i]
            
        remove(n,x,le-1)


ans = ['a','b','c','d']
remove(ans,'b',le=len(ans))
print(ans)