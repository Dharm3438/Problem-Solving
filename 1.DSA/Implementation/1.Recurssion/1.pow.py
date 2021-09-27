def pow(x,n):
    
    if(x==0):
        return 0
    if(n==0):
        return 1
    
    tmp = pow(x,n//2)
    if(n%2==0):
        return tmp*tmp
    else:
        return tmp*tmp*x
        
print(pow(1,0))
print(pow(1,5))
print(pow(10,0))
print(pow(0,3))