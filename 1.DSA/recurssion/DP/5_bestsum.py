def bestsum(t,arr,memo={}):
    if(t in memo.keys()):
        return memo[t]
    if(t==0):
        return []
    if(t<0):
        return None

    shortestsum = None

    for val in arr:
        remainder = t-val
        res = bestsum(remainder,arr,memo)
        if(res!=None):
            combination = res + [val]
            if(shortestsum==None or len(shortestsum)>len(combination)):
                shortestsum =  combination
            
    memo[t] = shortestsum
    return memo[t]

print(bestsum(1000,[7,4,100])) 