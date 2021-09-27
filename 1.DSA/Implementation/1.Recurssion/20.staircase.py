def staircase(n,store={}):
    
    if(n in store):
        return store[n]
    
    if(n==1 or n==0):
        return 1
    elif(n==2):
        return 2

    store[n] = staircase(n-1,store) + staircase(n-2,store) + staircase(n-3,store)
    return store[n]

print(staircase(4))
print(staircase(5))
print(staircase(1000))

