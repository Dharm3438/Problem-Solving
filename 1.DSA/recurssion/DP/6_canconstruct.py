import sys
sys.setrecursionlimit(10**6)

def canconstruct(t,arr,memo={}):
    if(t in memo.keys()): 
        return memo[t] 
    if(t==''):
        return True
    
    for val in arr:
        if(t.find(val)==0):
            t = t[len(val)-1:]
            suffix = t
            if(canconstruct(suffix,arr,memo)):
                memo[t] = True
                return memo[t]

    memo[t] = False
    return memo[t]

print(canconstruct('abcdef',['ab','abc','cd','def','abcd']))