def cansum(t,arr,memo={}):
    if(t in memo.keys()):
        return memo[t]
    if(t==0):
        return True
    if(t<0):
        return False

    for val in arr:
        remainder = t - val
        if(cansum(remainder,arr)):
            memo[t] = True
            return memo[t]

    memo[t] = False
    return memo[t]



print(cansum(3,[1,2,3]))
print(cansum(300,[7,14]))