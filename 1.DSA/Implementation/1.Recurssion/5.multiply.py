def multiply(n,m):
    
    if(m==0):
        return m

    return n+multiply(n,m-1)


print(multiply(1,2))
print(multiply(3,2))
print(multiply(3,7))