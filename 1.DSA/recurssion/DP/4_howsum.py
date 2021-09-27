def howsum(t,arr,memo={}):
    if(t in memo.keys()):
        return memo[t]
    if(t==0):
        return []
    if(t<0):
        return None

    for val in arr:
        remainder = t-val
        res = howsum(remainder,arr)
        if(res!=None):
            memo[t] =  res + [val]
            return memo[t]

    memo[t] = None
    return memo[t]

print(howsum(1000,[7,4])) 